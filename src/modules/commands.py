import mainFunc
import ircFunc
import ConfigParser
import errorhandling

def init():
    config = ConfigParser.ConfigParser()
    config.read('conf/beastbot.conf')
    config.set('Modules', 'commands', 'loaded')
    config.set('Functions', 'commandz', 'commands.commands')

    with open('conf/beastbot.conf', 'wb') as configfile:
        config.write(configfile)

init()

def commands(line, irc):
    message, username, msgto = ircFunc.ircMessage(line)
    conf = mainFunc.getConfig()
    functions = mainFunc.getFunctions()
    commands = functions.keys()
    admin_commands = []
    other_commands = []
    for command in commands:
        if 'administration' in functions[command]:
            admin_commands.append(command)
        else:
            other_commands.append(command)

    ircFunc.ircSay(username, 'Here are the commands i recognise for any user: {0}.'.format(', '.join(other_commands)), irc)
    ircFunc.ircSay(username, 'Admin Commands: {0}.'.format(', '.join(admin_commands)), irc)
    ircFunc.ircSay(username, 'For help, do: \'!help *command*\' for more information on a command.', irc)
