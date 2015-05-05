from __future__ import print_function
import sys
import socket
import ConfigParser
import errorhandling
import mainFunc
import ircFunc
import sys


def CreateSocket():
    conf = mainFunc.getConfig()
    try:
        irc = socket.create_connection((conf['server'], int(conf['port'])))
    except socket.error as socketerror:
        print("Connection Error: ", socketerror)
	sys.exit()
    #irc.send('NICK '+conf['nick']+'\r\n')
    ircFunc.ircNick(conf['nick'], irc)
    irc.send('USER ' + conf['user'] + ' ' + conf['nick'] + ' ' + conf['nick'] + ' :' + conf['name'] + '\r\n')
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
    config.set('Main', 'tempchannels', '')
    config.set('Main', 'tempnick', '')
    with open('conf/beastbot.conf', 'wb') as configfile:
        config.write(configfile)


def reloadImports():
    modules = getModules()
    for i in modules:
        print ("reloading: " + i)
        try:
            reload(sys.modules['modules.' + i])
        except KeyError, e:
            print ("Module does not exist: " + i)
            errorhandling.errorlog('warning', e, "Module probably does not exist: " + i)
        except Exception, e:
            errorhandling.errorlog('critical', e, "Trying to load module: " + i)


def confLoad(item):
    config = ConfigParser.RawConfigParser()
    config.read('conf/beastbot.conf')
    items = dict(config.items(item))
    return items


def getModules():
    return confLoad('Modules')


def getConfig():
    return confLoad('Main')


def getFunctions():
    return confLoad('Functions')
