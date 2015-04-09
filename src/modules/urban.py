import ConfigParser
import urllib
import json
import ircFunc
import errorhandling

def init():
    modulename = "urban"
    config = ConfigParser.ConfigParser()
    config.read('conf/beastbot.conf')
    config.set('Modules', 'urban', 'loaded')
    config.set('Functions', 'ud', 'urban.urban')
    config.set('Functions', 'urban', 'urban.urban')

    with open('conf/beastbot.conf', 'wb') as configfile:
        config.write(configfile)

init()
def getConfig():
    config = ConfigParser.RawConfigParser()
    config.read('conf/beastbot.conf')
    conf = dict(config.items('Main'))
    return conf

def urban(line, irc):
    conf = getConfig()
    splitline = line.split(" :")
    try:
        username = line.split("!")[0].replace(':', '')
        message = splitline[1]
        msgto = line.split(" ")[2]
        whole = message.split(" ", 1)[1]
        message = message.split(" ")
    except IndexError, e:
        errorhandling.errorlog('information', e, line)
    except Exception, e:
        errorhandling.errorlog('Critical', e, line)
    try:
        if message[1]:
            if msgto == conf['nick']:
                msgto = username
            msg2 = message[1].lower()
            if msg2.strip() in conf['admins'].lower().split(" "):
                msg = message[1].strip()
                definition = "The coolest god damn person you will ever fucking know...."
                thumbsup = "99999999999"
                thumbsdown = "0"
                output = msg+": "+definition+" Up:"+thumbsup+" Down: "+thumbsdown
                ircFunc.ircSay(msgto, output, irc)
            else:
                url = 'http://api.urbandictionary.com/v0/define?term='+whole
                info = urllib.urlopen(url)
                data = json.loads(info.read())
                try:
                    definition = data['list'][0]['definition']
                    thumbsup = data['list'][0]['thumbs_up']
                    thumbsdown = data['list'][0]['thumbs_down']
                    thumbsdown = str(thumbsdown)
                    thumbsup = str(thumbsup)
                    msg = whole.strip()
                    output = msg+": "+definition+" Up:"+thumbsup+" Down: "+thumbsdown
                    ircFunc.ircSay(msgto, output, irc)
                except IndexError:
                    ircFunc.ircSay(msgto, 'No definition for: '+whole, irc)
                except Exception, e:
                    errorhandling.errorlog('critical', e, line)
    except NameError:
        output = username+" is a dumbass and didn't enter a term to search for...."
        print output
        ircFunc.ircSay(msgto, output, irc)
    except Exception, e:
        errorhandling.errorlog('critical', e, line)
