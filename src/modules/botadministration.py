import ConfigParser
import ircFunc, mainFunc
import errorhandling

def init():
    config = ConfigParser.ConfigParser()
    config.read('conf/beastbot.conf')
    config.set('Modules', 'botadministration', 'loaded')
    config.set('Functions', 'join', 'botadministration.join')
    config.set('Functions', 'part', 'botadministration.part')
    config.set('Functions', 'nick', 'botadministration.changenick')

    with open('conf/beastbot.conf', 'wb') as configfile:
        config.write(configfile)

init()

def changenick(line, irc):
    message, username, msgto = ircFunc.ircMessage(line)
    conf = mainFunc.getConfig()
    if username in conf['admins'].split(" "):
        if (ircFunc.isRegged(username, irc)):
            try:
                if message[1]:
                    ircFunc.ircNick(message[1], irc)
                    print message[1]
            except IndexError:
                ircFunc.ircNick(conf['nick'], irc)
            except Exception as e:
                errorhandling.errorlog('critical', e, line)


def part(line, irc):
    message, username, msgto = ircFunc.ircMessage(line)
    conf = mainFunc.getConfig()
    if username in conf['admins'].split(" "):
        if (ircFunc.isRegged(username, irc)):
            try:
                if message[1]:
                    ircFunc.ircPart(message[1], irc)
                    print message[1]
            except IndexError:
                ircFunc.ircSay(msgto, "No channel specified...", irc)
            except Exception as e:
                errorhandling.errorlog('critical', e, line)


def join(line, irc):
    message, username, msgto = ircFunc.ircMessage(line)
    conf = mainFunc.getConfig()
    if username in conf['admins'].split(" "):
        if (ircFunc.isRegged(username, irc)):
            try:
                if message[1]:
                    ircFunc.ircJoin(message[1], irc)
                    print message[1]
            except IndexError:
                splitchannels = conf['channels'].split(" ")
                for chan in splitchannels:
                    ircFunc.ircJoin(chan, irc)
            except Exception as e:
                errorhandling.errorlog('critical', e, line)
