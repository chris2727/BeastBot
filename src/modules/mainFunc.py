import sys
import socket
import ConfigParser
import errorhandling

def CreateSocket():
    conf = getConfig()
    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    irc.connect((conf['server'], int(conf['port'])))
    irc.send('NICK '+conf['nick']+'\r\n')
    irc.send('USER test test test :test\r\n')
    return irc

def cleanConfig():
    config = ConfigParser.RawConfigParser()
    config.read('conf/beastbot.conf')
    config.remove_section('Functions')
    config.remove_section('Modules')
    config.remove_section('ServerFunctions')
    config.add_section('ServerFunctions')
    config.add_section('Modules')
    config.add_section('Functions')
    with open('conf/beastbot.conf', 'wb') as configfile:
        config.write(configfile)

def reloadImports():
    modules = getModules()
    for i in modules:
        print "reloading: "+i
        try:
            reload(sys.modules['modules.'+i])
        except KeyError, e:
            print "Module does not exist: "+i
            errorhandling.errorlog('warning', e, "Module probably does not exist: "+i)
        except Exception, e:
            errorhandling.errorlog('critical', e, "Trying to load module: "+i)

def getModules():
    config = ConfigParser.RawConfigParser()
    config.read('conf/beastbot.conf')
    modules = dict(config.items('Modules'))
    return modules

def getConfig():
    config = ConfigParser.RawConfigParser()
    config.read('conf/beastbot.conf')
    conf = dict(config.items('Main'))
    return conf

def getFunctions():
    config = ConfigParser.RawConfigParser()
    config.read('conf/beastbot.conf')
    functions = dict(config.items('Functions'))
    return functions

def getServerFunctions():
    config = ConfigParser.RawConfigParser()
    config.read('conf/beastbot.conf')
    serverfunctions = dict(config.items('ServerFunctions'))
    return serverfunctions
