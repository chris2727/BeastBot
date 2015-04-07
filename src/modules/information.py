import ConfigParser
import ircFunc
import errorhandling

def init():
    config = ConfigParser.ConfigParser()
    config.read('conf/beastbot.conf')
    config.set('Modules', 'information', 'loaded')
    config.set('Functions', 'showip', 'information.showip')
    config.set('Functions', 'about', 'information.about')
    config.set('Functions', 'commands', 'information.commands')
    config.set('Functions', 'help', 'information.help')
    with open('conf/beastbot.conf', 'wb') as configfile:
        config.write(configfile)

init()

def getConfig():
    config = ConfigParser.RawConfigParser()
    config.read('conf/beastbot.conf')
    conf = dict(config.items('Main'))
    return conf

def commands(line, irc):
    splitline = line.split(" :")
    try:
        message = splitline[1]
        message = message.split(" ")
        username = line.split("!")[0].replace(':', '')
        msgto = line.split(" ")[2]
    except IndexError, e:
        errorhandling.errorlog('information', e, line)
    except Exception, e:
        errorhandling.errorlog('critical', e, line)
    try:
        conf = getConfig()
        ircFunc.ircSay(username, "Still under construction", irc)
    except Exception, e:
        errorhandling.errorlog('critical', e, line)

def help(line, irc):
    splitline = line.split(" :")
    try:
        message = splitline[1]
        message = message.split(" ")
        username = line.split("!")[0].replace(':', '')
        msgto = line.split(" ")[2]
    except IndexError, e:
        errorhandling.errorlog('information', e, line)
    except Exception, e:
        errorhandling.errorlog('critical', e, line)
    try:
        conf = getConfig()
        ircFunc.ircSay(username, "Still under construction", irc)
    except Exception, e:
        errorhandling.errorlog('critical', e, line)


def about(line, irc):
    splitline = line.split(" :")
    try:
        message = splitline[1]
        message = message.split(" ")
        username = line.split("!")[0].replace(':', '')
        msgto = line.split(" ")[2]
    except IndexError, e:
        errorhandling.errorlog('information', e, line)
    except Exception, e:
        errorhandling.errorlog('critical', e, line)
    try:
        conf = getConfig()
        ircFunc.ircSay(username, conf['aboutmessage'], irc)
    except Exception, e:
        errorhandling.errorlog('critical', e, line)

def showip(line, irc):
    splitline = line.split(" :")
    try:
        message = splitline[1]
        message = message.split(" ")
        username = line.split("!")[0].replace(':', '')
        msgto = line.split(" ")[2]
    except IndexError, e:
        errorhandling.errorlog('information', e, line)
    except Exception, e:
        errorhandling.errorlog('critical', e, line)
    try:
        ircFunc.ircSay(msgto, username+", my ip address apears to be 127.0.0.1", irc)
    except Exception, e:
        errorhandling.errorlog('critical', e, line)