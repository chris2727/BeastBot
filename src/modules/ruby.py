#
# =================
# === RUBINATOR ===
# =================
#
# A module that makes this bot have ruby modules
#
# Author: Lenoch
#

import ConfigParser
import json
import ircFunc
import errorhandling
import os
from subprocess import Popen, PIPE, STDOUT

def init():
    modulename = "urban"
    config = ConfigParser.ConfigParser()
    config.read('conf/beastbot.conf')
    config.set('Modules', 'ruby', 'loaded')
    
    files = os.listdir('ruby_modules/')
    
    #Add all files in ruby_modules as commands
    for i in range(len(files)):
        config.set('Functions', files[i].split('.')[0], 'ruby.ruby')
    

    with open('conf/beastbot.conf', 'wb') as configfile:
        config.write(configfile)

init()
 
def ruby(line, irc):
    splitline = line.split(" :")
    #define the file to run based on given command
    given_input = splitline[1].split(" ")  
    script_to_execute = given_input[0].rstrip() + ".rb"
    
    #Check for parameters for the ruby script
    parameters = ""
    for i in range(1, len(given_input)):
        parameters = parameters + given_input[i] + ":"
    
    parameters = parameters.rstrip(":").rstrip()

    
    # Open the script associated with the command
    try:
        ruby_script = Popen(['ruby', 'ruby_modules/' + script_to_execute[1:]], stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    except Exception, e:
        errorhandling.errorlog('critical', 'Ruby script could not be executed', line)
        ruby_script.stdout.close()
        
    result = []
    
    #write parameters
    if parameters != "":
        ruby_script.stdin.write(parameters + "\n")
        
    #Some magic that stores the piped data in an array "result"
    try:
        while True:
            ruby_line = ruby_script.stdout.readline().rstrip()
            
            if ruby_script.poll() is not None:
                break
            
            result.append(ruby_line)
                
            if line == '[end]':
                break
            
    except Exception, e:
        errorhandling.errorlog('critical', e, line)
        
    print result
    #output is made ready for sending    
    try:
        for i in range(len(result)):
            output = result[i]
        
        sendinfo = output.split(":")
        msgto = ""
        
        username = line.split("!")[0].replace(':', '')
        #Piped data contains reciptient:data structure so Beastbot knows how to send the command
        if sendinfo[0] == "channel":
            ircFunc.ircSay(line.split(" ")[2], username + ": " + sendinfo[1], irc)
        else:
            ircFunc.ircSay(username, sendinfo[1], irc)

    except Exception, e:
        errorhandling.errorlog('critical', e, line)
        ruby_script.stdout.close()
        
    ruby_script.stdout.close()

