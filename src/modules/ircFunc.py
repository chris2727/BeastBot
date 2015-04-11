
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
    #true if Nickserv says he's registered
    print "in regged"
    ircSay("NickServ","STATUS %s " % (nick) ,irc)
    print "sent"
    line = ""
    while line is "":
        ircSay("NickServ","STATUS %s " % (nick) ,irc)
        print "in while"
        line = irc.recv(2048)
        print "REG TEST" + line
        if line.find("STATUS %s 3" % (nick)) != -1:
            return True
            print "regged"
        else:
            return False
            print "not regged"