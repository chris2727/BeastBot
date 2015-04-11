import ConfigParser
import ircFunc
import urllib
import urllib2
import errorhandling
import string
import re

'somestring. with funny characters'
def init():
    config = ConfigParser.ConfigParser()
    config.read('conf/beastbot.conf')
    config.set('Modules', 'urlparsing', 'loaded')
    config.set('Functions', 'http', 'urlparsing.urlparse')

    with open('conf/beastbot.conf', 'wb') as configfile:
        config.write(configfile)

init()

def getConfig():
    config = ConfigParser.RawConfigParser()
    config.read('conf/beastbot.conf')
    conf = dict(config.items('Main'))
    return conf


def urlparse(line, irc):
    splitline = line.split(" :")
    try:
        message = splitline[1]
        message = message.split(" ")
        msgto = line.split(" ")[2]
    except IndexError, e:
        errorhandling.errorlog('information', e, line)
    except Exception, e:
        errorhandling.errorlog('critical', e, line)
    try:
        sock = urllib2.urlopen(message[0], timeout=4)
        html = sock.read()
        sock.close()
        start = html.find('<title>') + 7
        titletest = html.find('<title>')
        titletest2 = html[titletest:]
        titletest2 = titletest2[0:7]
        if titletest2 == '<title>': good = True
        end = html.find('</title>', start)
        title = html[start:end]
        title = title.strip()
        if title != "" and good:
            title = title.strip()
            title = filter(lambda x: x in string.printable, title)
            title = title[0:100]
            output = "Title: ["+title+"]"
            ircFunc.ircSay(msgto, output, irc)
    except IndexError, e:
        errorhandling.errorlog('information', e, line)
    except Exception, e:
        errorhandling.errorlog('critical', e, line)
          