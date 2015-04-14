import ConfigParser
import ircFunc, mainFunc
import errorhandling

def init():
    config = ConfigParser.ConfigParser()
    config.read('conf/beastbot.conf')
    config.set('Modules', 'channeladministration', 'loaded')
    config.set('Functions', 'voice', 'channeladministration.voiceuser')
    config.set('Functions', 'devoice', 'channeladministration.devoiceuser')
    config.set('Functions', 'hop', 'channeladministration.hopuser')
    config.set('Functions', 'dehop', 'channeladministration.dehopuser')
    config.set('Functions', 'op', 'channeladministration.opuser')
    config.set('Functions', 'deop', 'channeladministration.deopuser')
    config.set('Functions', 'kick', 'channeladministration.kickuser')
    config.set('Functions', 'unban', 'channeladministration.unbanuser')
    config.set('Functions', 'ban', 'channeladministration.banuser')
    config.set('Functions', 'mode', 'channeladministration.mode')

    with open('conf/beastbot.conf', 'wb') as configfile:
        config.write(configfile)

init()

def mode(line, irc):
    message, whole, username, msgto = ircMessage(line, whl=True)
    conf = mainFunc.getConfig()
    if username in conf['admins'].split(" "):
        if (ircFunc.isRegged(username, irc)):
            try:
                if message[1]:
                    ircFunc.ircMode(msgto, whole, irc)
            except Exception as e:
                errorhandling.errorlog('critical', e, line)

def banuser(line, irc):
    message, username, msgto = ircFunc.ircMessage(line)
    conf = mainFunc.getConfig()
    if username in conf['admins'].split(" "):
        if (ircFunc.isRegged(username, irc)):
            try:
                if message[1]:
                    ircFunc.ircMode(msgto, "+b "+message[1], irc)
                    print message[1]
            except IndexError:
                ircFunc.ircMode(msgto, "+b "+username, irc)
            except Exception as e:
                errorhandling.errorlog('critical', e, line)

def unbanuser(line, irc):
    message, username, msgto = ircFunc.ircMessage(line)
    conf = mainFunc.getConfig()
    if username in conf['admins'].split(" "):
        if (ircFunc.isRegged(username, irc)):
            try:
                if message[1]:
                    ircFunc.ircMode(msgto, "-b "+message[1], irc)
                    print message[1]
            except IndexError:
                ircFunc.ircMode(msgto, "-b "+username, irc)
            except Exception as e:
                errorhandling.errorlog('critical', e, line)

def kickuser(line, irc):
    message, username, msgto = ircFunc.ircMessage(line)
    conf = mainFunc.getConfig()
    if username in conf['admins'].split(" "):
        if (ircFunc.isRegged(username, irc)):
            try:
                irc.send("KICK %s %s\n" % (msgto, message[1]))
            except IndexError as e:
                errorhandling.errorlog('information', e, line)
            except Exception as e:
                errorhandling.errorlog('critical', e, line)

def opuser(line, irc):
    message, username, msgto = ircFunc.ircMessage(line)
    conf = mainFunc.getConfig()
    if username in conf['admins'].split(" "):
        if (ircFunc.isRegged(username, irc)):
            try:
                if message[1]:
                    ircFunc.ircMode(msgto, "+o "+message[1], irc)
                    print message[1]
            except IndexError:
                ircFunc.ircMode(msgto, "+o "+username, irc)
            except Exception as e:
                errorhandling.errorlog('critical', e, line)
def deopuser(line, irc):
    message, username, msgto = ircFunc.ircMessage(line)
    conf = mainFunc.getConfig()
    if username in conf['admins'].split(" "):
        if (ircFunc.isRegged(username, irc)):
            try:
                if message[1]:
                    ircFunc.ircMode(msgto, "-o "+message[1], irc)
                    print message[1]
            except IndexError:
                ircFunc.ircMode(msgto, "-o "+username, irc)
            except Exception as e:
                errorhandling.errorlog('critical', e, line)
def hopuser(line, irc):
    message, username, msgto = ircFunc.ircMessage(line)
    conf = mainFunc.getConfig()
    if username in conf['admins'].split(" "):
        if (ircFunc.isRegged(username, irc)):
            try:
                if message[1]:
                    ircFunc.ircMode(msgto, "+h "+message[1], irc)
                    print message[1]
            except IndexError:
                ircFunc.ircMode(msgto, "+h "+username, irc)
            except Exception as e:
                errorhandling.errorlog('critical', e, line)
def dehopuser(line, irc):
    message, username, msgto = ircFunc.ircMessage(line)
    conf = mainFunc.getConfig()
    if username in conf['admins'].split(" "):
        if (ircFunc.isRegged(username, irc)):
            try:
                if message[1]:
                    ircFunc.ircMode(msgto, "-h "+message[1], irc)
                    print message[1]
            except IndexError:
                ircFunc.ircMode(msgto, "-h "+username, irc)
            except Exception as e:
                errorhandling.errorlog('critical', e, line)


def devoiceuser(line, irc):
    message, username, msgto = ircFunc.ircMessage(line)
    conf = mainFunc.getConfig()
    if username in conf['admins'].split(" "):
        if (ircFunc.isRegged(username, irc)):
            try:
                if message[1]:
                    ircFunc.ircMode(msgto, "-v "+message[1], irc)
                    print message[1]
            except IndexError:
                ircFunc.ircMode(msgto, "-v "+username, irc)
            except Exception as e:
                errorhandling.errorlog('critical', e, line)

def voiceuser(line, irc):
    message, username, msgto = ircFunc.ircMessage(line)
    conf = mainFunc.getConfig()
    if username in conf['admins'].split(" "):
        if (ircFunc.isRegged(username, irc)):
            try:
                if message[1]:
                    ircFunc.ircMode(msgto, "+v "+message[1], irc)
                    print message[1]
            except IndexError:
                ircFunc.ircMode(msgto, "+v "+username, irc)
            except Exception as e:
                errorhandling.errorlog('critical', e, line)
