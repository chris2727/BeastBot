'''
Hashing module for BeastBot/EZBot

Will return the specified hash for the given string
'''

from inc import *
import hashlib

modFunc.addCommand('md5', 'hash', 'md5', 'user', 'Converts string to md5.. Usage: !md5 <string>')
modFunc.addCommand('sha1', 'hash', 'sha1', 'user', 'Converts string to sha1... Usage: !sha1 <string>')

def md5(line, irc):
    message, username, msgto = ircFunc.ircMessage(line)
    try:
        if (len(message) > 1):
            string = ' '.join(message[1:])
            md5 = hashlib.md5()
            md5.update(string.strip())
            ircFunc.ircSay(msgto, "%s - '%s'" % (username, md5.hexdigest()), irc)
        else:
            ircFunc.ircSay(msgto, "%s, No string given" % username, irc)

    except Exception as e:
        errorhandling.inputError('critical', e, line)

def sha1(line, irc):
    message, username, msgto = ircFunc.ircMessage(line)
    try:
        if (len(message) > 1):
            string = ' '.join(message[1:])
            sha1 = hashlib.sha1()
            sha1.update(string.strip())
            ircFunc.ircSay(msgto, "%s - '%s'" % (username, sha1.hexdigest()), irc)
        else:
            ircFunc.ircSay(msgto, "%s, No string given" % username, irc)

    except Exception as e:
        errorhandling.inputError('critical', e, line)
