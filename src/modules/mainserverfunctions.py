import ConfigParser
import ircFunc

def init():
    config = ConfigParser.ConfigParser()
    config.read('conf/beastbot.conf')
    config.set('Modules', 'mainserverfunctions', 'loaded')
    config.set('ServerFunctions', 'PING', 'mainserverfunctions.PING')
    
    with open('conf/beastbot.conf', 'wb') as configfile:
        config.write(configfile)

init()

def getConfig():
    config = ConfigParser.RawConfigParser()
    config.read('conf/beastbot.conf')
    conf = dict(config.items('Main'))
    return conf


def PING(line, irc):
    splitline = line.split(" :")
    pong = "PONG %s" % splitline[1]
    irc.send(pong)
    print pong