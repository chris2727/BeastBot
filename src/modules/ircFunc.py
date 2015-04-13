import errorhandling, mainFunc

def ircMode(chan, args, irc):
    irc.send("MODE %s %s\n" % (chan, args))

def ircSay(to, msg, irc):
#to=message to, msg=message to send, irc=socket
    irc.send("PRIVMSG %s :%s\n" % (to, msg))

def ircJoin(channel, irc):
#channel=channel to join, irc=socket
    irc.send("JOIN %s\n" % (channel))

def ircPart(channel, irc):
#channel=channel to part, irc=socket
    irc.send("PART %s\n" % (channel))

def ircNick(newnick, irc):
#newnick=New nickname for the bot, irc=socket
    irc.send("NICK %s\n" % (newnick))

def isRegged(nick, irc):
    """Function to check is user is identified with nickserv.
        true if Nickserv says he's registered."""
    ircSay("NickServ","STATUS %s " % (nick,irc))
    line = ""
    while line is "":
        ircSay("NickServ","STATUS %s " % (nick) ,irc)
        line = irc.recv(512)
        print "REG TEST" + line
        if line.find("STATUS %s 3" % (nick)) != -1:
            return True
        else:
            return False

def getMsgto(line):
    return line.split(" ")[2]

def getUsername(line):
    return line.split("!")[0][1:]


def ircMessage(line, whl=False):
    """Func to process message received from server."""
    conf = mainFunc.getConfig()
    splitline = line.split(" :")
    try:
        message = splitline[1]
        message = message.split(" ")
        username = getUsername(line)
        if getMsgto(line) == conf['nick']: #privmsg
            msgto = username
        else:
            msgto = getMsgto(line)
        if whl:
            whole = message.split(" ", 1)[1]
            return message, whole, username, msgto
        return message, username, msgto
    except IndexError as e:
        errorhandling.errorlog('information', e, line)
    except Exception as e:
        errorhandling.errorlog('critical', e, line)

