import mainFunc
import ircFunc
import errorhandling
import sqlite3

'''
Configuration Management
'''

def ensureConf():
    import os
    if not os.path.isfile('conf/conf.db'):
        errorhandling.inputInfo('No configuration database found. Creating and setting up.')
        con = sqlite3.connect('conf/conf.db')
        errorhandling.inputInfo('Created conf/conf.db.')
        errorhandling.inputInfo('Setting up tables...')
        while con:
            cur = con.cursor()
            cur.execute('''CREATE TABLE bot
                (var TEXT NOT NULL, 
                content TEXT);''')
            cur.execute('''CREATE TABLE modules
                (location TEXT,
                exist INT,
                name TEXT,
                loaded INT,
                defaultload INT)''')
            cur.execute('''CREATE TABLE commands
                (loaded INT,
                init TEXT,
                module TEXT, 
                function TEXT,
                enabled INT);''')
            con.commit()
            break
        errorhandling.inputInfo('Tables created')
        errorhandling.inputInfo('Inserting default values')
        while con:
            cur = con.cursor()
            cur.execute("INSERT INTO bot (var,content) VALUES ('server', 'irc.evilzone.org')")
            cur.execute("INSERT INTO bot (var,content) VALUES ('port', '6667')")
            cur.execute("INSERT INTO bot (var,content) VALUES ('nickname', 'EZBot')")
            cur.execute("INSERT INTO bot (var,content) VALUES ('tempnickname', 'EZBot')")
            cur.execute("INSERT INTO bot (var,content) VALUES ('username', 'BeastBot')")
            cur.execute("INSERT INTO bot (var,content) VALUES ('realname', 'BeastBot')")
            cur.execute("INSERT INTO bot (var,content) VALUES ('nickservpassword', 'NoPasswordSpecified')")
            cur.execute("INSERT INTO bot (var,content) VALUES ('cominit', '!')")
            cur.execute("INSERT INTO bot (var,content) VALUES ('channels', '#Evilzone')")
            cur.execute("INSERT INTO bot (var,content) VALUES ('tempchannels', '#Evilzone')")
            cur.execute("INSERT INTO bot (var,content) VALUES ('botbanned', '')")
            cur.execute("INSERT INTO bot (var,content) VALUES ('botadmins', 'chris1')")
            con.commit()
            break
        errorhandling.inputInfo('Done inserting default values')
        errorhandling.inputInfo('Done creating configuration database')



def getAllBotConf():
    conf = {}
    con = sqlite3.connect('conf/conf.db')
    while con:
        cur = con.cursor()
        cur.execute("SELECT * FROM bot")
        rows = cur.fetchall()
        break
    for row in rows:
        if row[1] == None:
            row[1] = ''
        conf[row[0]] = row[1]
    return conf


def getBotConf(option):
    con = sqlite3.connect('conf/conf.db')
    while con:
        cur = con.cursor()
        cur.execute("SELECT content FROM bot WHERE var='%s'" % option)
        row = cur.fetchone()
        break
    if row == None:
        errorhandling.inputError('warning', 'botconf option doesnt exist', 'Option: %s' % option)
    else:
        if row[0] == None:
            row[0] = ''
        return str(row[0])


def setBotConf(var, content):
    con = sqlite3.connect('conf/conf.db')
    while con:
        cur = con.cursor()
        cur.execute("UPDATE bot SET content='%s' WHERE var='%s'" % (content, var))
        con.commit()
        break


def CleanModulesDB():
    con = sqlite3.connect('conf/conf.db')
    with con:
        cur = con.cursor()
        cur.execute("UPDATE modules SET exist=0 WHERE exist=1")
        cur.execute("UPDATE modules SET loaded=0 WHERE loaded=1")
        con.commit()
    # Resets module exist to 0
    # Resets module loaded to 0

def CleanCommandsDB():
    con = sqlite3.connect('conf/conf.db')
    with con:
        cur = con.cursor()
        cur.execute("UPDATE commands SET loaded=0 WHERE loaded=1")
        con.commit()
    # Resets commands loaded to 0

def CleanTemps():
    con = sqlite3.connect('conf/conf.db')
    with con:
        cur = con.cursor()
        cur.execute("UPDATE bot SET content='' WHERE var='tempnickname'")
        cur.execute("UPDATE bot SET content='' WHERE var='tempchannels'")
