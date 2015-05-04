import ConfigParser
import ircFunc
import mainFunc
import errorhandling

import sqlite3
import time, os
import datetime
import pytz

db_file = 'db/seen.db'

def init():
    config = ConfigParser.ConfigParser()
    config.read('conf/beastbot.conf')
    config.set('Modules', 'seen', 'loaded')
    config.set('Functions', 'seen', 'seen.seen')
    config.set('Functions', 'seen_record', 'seen.set_seen_values')

    with open('conf/beastbot.conf', 'wb') as configfile:
        config.write(configfile)
    if not os.path.exists(db_file.split('/')[0]):
        os.mkdir('db')
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    try:
        c.execute('SELECT * FROM Karma')
    except StandardError:
        c.execute('CREATE TABLE IF NOT EXISTS seen_values(nick TEXT, channel TEXT, message TEXT, time INTEGER)')
        conn.commit()
    conn.close()


init()

def seen(line, irc):
    message, username, msgto = ircFunc.ircMessage(line)
    try:
        if message[1]:
            nick = message[1]
            values = get_seen_value(nick)
            if values[0] == msgto:
                channel = 'here'
            else:
                channel = 'another channel' #not mentioning channels for privacy

            lastmsg = values[1]
            time_seen = values[2]

            timestamp = format_time(time_seen)
            ircFunc.ircSay(msgto, 'I last saw {0} on {1} in {2} saying {3}'.format(nick, timestamp, channel, lastmsg), irc)
    except TypeError as e:
        ircFunc.ircSay(msgto, 'Sorry, i haven\'t seen {0} around.'.format(nick), irc)
    except IndexError as e:
        ircFunc.ircSay(msgto, '{0}, seen who?'.format(username), irc)

def set_seen_values(nick, channel, message, time):
    nick = nick.lower()
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    with conn:
        c.execute('SELECT * FROM seen_values WHERE nick=?',[nick])
        result=c.fetchone()
        if result is not None:
            c.execute('UPDATE seen_values SET channel=?, message=?, time=? WHERE nick=?', [channel, message, time, nick])
        else:
            c.execute('INSERT INTO seen_values VALUES (?, ?, ?, ?)',[nick, channel, message, time])
        conn.commit()
    
def get_seen_value(nick):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    with conn:
        c.execute('SELECT channel, message, time FROM seen_values WHERE nick=?', [nick])
        result = c.fetchone()
        return result

def format_time(timestamp):
    tformat = '%A %D %T %z'
    return datetime.datetime.fromtimestamp(timestamp).strftime(tformat)
