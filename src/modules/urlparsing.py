import ConfigParser
import ircFunc
import urllib
import errorhandling

def init():
    config = ConfigParser.ConfigParser()
    config.read('conf/beastbot.conf')
    config.set('Modules', 'urlparsing', 'loaded')
    config.set('Functions', 'http', 'urlparsing.urlparse')

    with open('conf/beastbot.conf', 'wb') as configfile:
        config.write(configfile)

init()

def getConfig():
    config = ConfigParser.RawConfigParser()
    config.read('conf/beastbot.conf')
    conf = dict(config.items('Main'))
    return conf


def urlparse(line, irc):
    splitline = line.split(" :")
    try:
        message = splitline[1]
        message = message.split(" ")
        msgto = line.split(" ")[2]
    except IndexError, e:
        errorhandling.errorlog('information', e, line)
    except Exception, e:
        errorhandling.errorlog('critical', e, line)
    try:
        sock = urllib.urlopen(message[0])
        html = sock.read()
        sock.close()
        start = html.find('<title>') + 7
        end = html.find('</title>', start)
        title = html[start:end]
        if title != "":
            output = "Title: ["+title+"]"
            ircFunc.ircSay(msgto, output, irc)
    except IndexError, e:
        errorhandling.errorlog('information', e, line)
    except Exception, e:
        errorhandling.errorlog('critical', e, line)
          