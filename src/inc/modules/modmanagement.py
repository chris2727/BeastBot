'''
    ModManagement module for BeastBot
'''

from inc import *


modFunc.addCommand('mod', 'modmanagement', 'modmanage')


def modmanage(line, irc):
    message, whole, username, msgto = ircFunc.ircMessage(line.strip(), whl=True)
    usernamel = username.lower()
    if usernamel in configFunc.getBotConf('botadmins').split(" "):
        if (ircFunc.isRegged(usernamel, irc)):
            try:
                if message[1].strip() == 'load':
                    try:                
                        if message[2].strip() != "":
                            result = modFunc.LoadModule(message[2].strip())
                            if result == True:
                                ircFunc.ircSay(msgto, 'Module has been loaded successfully', irc)
                            else:
                                ircFunc.ircSay(msgto, 'Either the module does not exist or something went wrong and it was NOT loaded successfully.', irc)
                    except IndexError:
                        ircFunc.ircSay(msgto, 'You did not enter a module to load')
                    except Exception as e:
                        errorhandling.inputError('critical', e, line)
                elif message[1].strip() == 'unload':
                    try:
                        if message[2].strip() != "":
                            modFunc.UnloadModule(message[2].strip())
                            ircFunc.ircSay(msgto, 'Module (' + message[2].strip() + ') has been unloaded successfully', irc)
                    except IndexError:
                        ircFunc.ircSay(msgto, 'You did not enter a module to unload')
                elif message[1].strip() == 'defaultload':
                    try:
                        if message[2] == 'add':
                            if message[3]:
                                ircFunc.ircSay(msgto, message[3].strip() + ' added to the default load list', irc)
                                modFunc.defaultManage(message[3].strip(), 'add')
                                ircFunc.ircSay(msgto, message[3].strip() + ' added to the default load list', irc)
                        if message[2] == 'del':
                            if message[3]:
                                ircFunc.ircSay(msgto, message[3].strip() + ' removed to the default load list', irc)
                                modFunc.defaultManage(message[3].strip(), 'del')
                                ircFunc.ircSay(msgto, message[3].strip() + ' removed to the default load list', irc)
                        if message[2] == 'list':
                            modlist = modFunc.defaultManage(message[2].strip(), 'list')
                            output = username + ', the default module load list is: ' + modlist
                            ircFunc.ircSay(msgto, output, irc)
                    except IndexError:
                        ircFunc.ircSay(msgto, 'Command parameters are: add, del, list', irc)
                    except Exception as e:
                        errorhandling.inputError('critical', e, line)
                elif message[1].strip() == 'list':
                    try:
                        if message[2].strip is not "":
                            message[2] == 'loaded'
                    except Exception:
                        message[2] == 'loaded'
                    if message[2].strip() == 'all':
                        mods = modFunc.listMods('all')
                        ircFunc.ircSay(msgto, mods, irc)
                    elif message[2].strip() == 'loaded':
                        mods = modFunc.listMods('loaded')
                        ircFunc.ircSay(msgto, mods, irc)
                    elif message[2].strip() == 'unloaded':
                        mods = modFunc.listMods('unloaded')
                        ircFunc.ircSay(msgto, mods, irc)
                    elif message[2].strip() == 'exist':
                        mods = modFunc.listMods('exist')
                        ircFunc.ircSay(msgto, mods, irc)
                    elif message[2].strip() == 'default' or message[2].strip() == 'defaultload':
                        modlist = modFunc.defaultManage(message[3].strip(), 'list')
                        output = username + ', the default module load list is: ' + modlist
                        ircFunc.ircSay(msgto, output, irc)
                else:
                    ircFunc.ircSay(msgto, 'Command parameters are: load, unload, defaultload, list', irc)
            except IndexError:
                ircFunc.ircSay(msgto, 'Command parameters are: load, unload, defaultload, list', irc)
            except Exception as e:
                errorhandling.inputError('critical', e, line)
