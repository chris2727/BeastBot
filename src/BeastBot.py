#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   BeastBot.py - A custom, from scratch IRC bot
#   Copyright (C) 2015 Spacecow99
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import ConfigParser
import re
import time
import os
from threading import Thread
import thread


def main():
    irc = mainFunc.CreateSocket()
    conf = mainFunc.getConfig()
    functions = mainFunc.getFunctions()
    serverfunctions = mainFunc.getServerFunctions()
    while True:
        try:
            line = irc.recv(2048)
        except:
            print "IRC Socket Disconnected"
            wait = input('Press enter to continue')
            exit()
        if line:
            print line
        splitline = line.split(" :")
        try:
            message = splitline[1]
            origmessage = message
            messagechars = message
            message = message.split(" ")
            username = line.split("!")[0].replace(':', '')
            msgto = line.split(" ")[2]  # Gives an error into the log
            if msgto == conf['nick']:
                msgto = username
            command = message[0]
            chan = msgto
        except IndexError, e:
            errorhandling.errorlog('information', e, line)
        except Exception, e:
            errorhandling.errorlog('critical', e)
        try:
            if re.match("http", message[0]):
                message[0] = conf['cominit']+"http"
                command = conf['cominit']+"http"
                messagechars = message[0]
        except IndexError, e:
            errorhandling.errorlog('information', e)

        if messagechars[0] == conf['cominit']:
            command = command[1:]
            command = command.strip()
            if command == "reload":
                if username in conf['admins'].split(" "):
                    if (ircFunc.isRegged(username, irc)):
                        mainFunc.reloadImports()
                        conf = mainFunc.getConfig()
                        functions = mainFunc.getFunctions()
                        modules = mainFunc.getModules()
                        ircFunc.ircSay(msgto, "Configuration Reloaded...", irc)
            elif command == "quit":
                if username in conf['admins'].split(" "):
                    if (ircFunc.isRegged(username, irc)):
                        ircFunc.ircSay(msgto, "Shutting Down....", irc)
                        mainFunc.cleanConfig()
                        irc.close()
                        time.sleep(1)
                        exit()
            elif command == "update":
                if username in conf['admins'].split(" "):
                    if (ircFunc.isRegged(username, irc)):
                        msg = "Shutting down for updates..."
                        ircFunc.ircSay(msgto, msg, irc)
                        mainFunc.cleanConfig()
                        try:
                            irc.close()
                        except Exception, e:
                            ircSay(username, 'Forcing Shutdown...', irc)
                            errorhandling.errorlog('critical', e, 'forcing shutdown')
                            exit()
                        time.sleep(3)
                        os.system("python pullupdates.py")
                        # Bot should not go past this line
                        msg = "Error pulling updates..."
                        errorhandling.errorlog('critical', msg)
                        exit()
            else:
                try:
                    if functions[command]:
                        function = functions[command]
                        functionThread = Thread(target=eval(function), args=(line, irc,))
                        functionThread.daemon = True
                        functionThread.start()
                except KeyError:
                    #Command does not exist
                    pass
                except Exception, e:
                    errorhandling.errorlog('critical', e)
        else:
            try:
                init = splitline[0]
                init = init.lower()
                if serverfunctions[init]:
                    function = serverfunctions[init]
                    eval(function)(line, irc)
            except KeyError:
                #command does not exist
                pass
            except Exception, e:
                errorhandling.errorlog('critical', e)
        if re.match("^:[a-zA-Z0-9\-\.]+\.[a-zA-Z0-9\-\.]+\.(com|org|net|mil|edu|COM|ORG|NET|MIL|EDU) 001 "+conf['nick']+" :Welcome", line):
            splitchannels = conf['channels'].split(" ")
            for chan in splitchannels:
                irc.send("JOIN %s\n" % (chan))
        elif re.search(":This nickname is registered and protected.", line):
            ircFunc.ircSay("NICKSERV", "identify "+conf['password'], irc)


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


def loadImports(path):
    files = os.listdir(path)
    imps = []
    for i in range(len(files)):
        name = files[i].split('.')
        if len(name) > 1:
            if name[1] == 'py' and name[0] != '__init__':
                name = name[0]
                imps.append(name)
    file = open(path+'__init__.py', 'w')
    toWrite = '__all__ ='+str(imps)
    file.write(toWrite)
    file.close()
cleanConfig()
loadImports('modules/')
from modules import *

if __name__ == "__main__":
    main()
