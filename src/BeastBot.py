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

import os
import re
import sys
import socket
import os.path
import logging
import argparse
import ConfigParser
import re

def main():
    irc = CreateSocket()
    conf = getConfig()
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
	if splitline[0] == "PING":
		pong = "PONG %s" %splitline[1]
		irc.send(pong)
		print pong
	if re.match(":r2d2.evilzone.org 001 "+conf['nick']+" :Welcome", line):
		splitchannels = conf['channels'].split(" ")
		for chan in splitchannels:
			irc.send("JOIN %s\n" %(chan))

def CreateSocket():
	conf = getConfig()
	irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
	irc.connect((conf['server'], int(conf['port'])))
	irc.send('NICK '+conf['nick']+'\r\n')
	irc.send('USER test test test :test\r\n')
	return irc

def getConfig():
	config = ConfigParser.RawConfigParser()
	config.read('conf/beastbot.conf')
	conf = dict(config.items('Main'))
	return conf

if __name__ == "__main__":
    main()

