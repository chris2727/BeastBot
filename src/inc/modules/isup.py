'''
IsUp module for BeastBot/EZBot

Will return the online status of a url
'''

from inc import *
import urllib2
import json

modFunc.addCommand('isup', 'isup', 'isup', 'user', 'Checks if a URL is up or down.. Usage: !isup <url>')
modFunc.addCommand('up', 'isup', 'isup', 'user', 'Checks if a URL is up or down.. Usage: !isup <url>')



def isup(line, irc):
    message, username, msgto = ircFunc.ircMessage(line)
    message[1] = message[1].strip()
    try:
        if (len(message) > 1):
            output = ""
            if (len(message[1].split(".")) > 1):
                if ("http://" not in message[1]) and ("https://" not in message[1]):
                    message[1] = "http://"+message[1]
                try:
                    respCode = urllib2.urlopen(message[1]).getcode()
                    if (respCode == 200): # OK
                        output = "It's just you %s! - %s seems to be up from here..." % (username, message[1])
                    
                    elif (respCode == 301) or (respCode == 302): # Moved temporarily or permanetly
                        output = "It's not just you %s! - %s seems to have been moved..." % (username, message[1])
                    
                    else:
                        output = "It's not just you %s! - %s seems to be down from here too!" % (username, message[1])
                except IOError:
                    output = "It's not just you %s! - %s seems to be down from here too!" % (username, message[1])
                ircFunc.ircSay(msgto, output, irc)
            else:
                ircFunc.ircSay(msgto, "%s, that is not a proper web address...." % username, irc)
        else:
            ircFunc.ircSay(msgto, "%s, no URL was given...", irc)
    except Exception as e:
        errorhandling.inputError('critical', e, line)
