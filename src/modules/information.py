import ConfigParser
import ircFunc
import mainFunc
import errorhandling


def init():
    config = ConfigParser.ConfigParser()
    config.read('conf/beastbot.conf')
    config.set('Modules', 'information', 'loaded')
    config.set('Functions', 'showip', 'information.showip')
    config.set('Functions', 'about', 'information.about')
    config.set('Functions', 'commands', 'information.commands')
    config.set('Functions', 'help', 'information.commands')
    with open('conf/beastbot.conf', 'wb') as configfile:
        config.write(configfile)

init()


def commands(line, irc):
    message, username, msgto = ircFunc.ircMessage(line)
    try:
        conf = mainFunc.getConfig()
        split = conf['commands'].split('\n')
        for i in split:
            ircFunc.ircSay(username, i, irc)
    except Exception as e:
        errorhandling.errorlog('critical', e, line)


def help(line, irc):
    message, username, msgto = ircFunc.ircMessage(line)
    try:
        ircFunc.ircSay(username, "Still under construction", irc)
    except Exception as e:
        errorhandling.errorlog('critical', e, line)


def about(line, irc):
    message, username, msgto = ircFunc.ircMessage(line)
    try:
        conf = mainFunc.getConfig()
        split = conf['aboutmessage'].split('\n')
        for i in split:
            ircFunc.ircSay(username, i, irc)
    except Exception, e:
        errorhandling.errorlog('critical', e, line)


def showip(line, irc):
    message, username, msgto = ircFunc.ircMessage(line)
    try:
        ircFunc.ircSay(msgto, username + ", my ip address appears to be 127.0.0.1", irc)
    except Exception, e:
        errorhandling.errorlog('critical', e, line)
