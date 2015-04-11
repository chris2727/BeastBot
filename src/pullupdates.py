import os
import time


time.sleep(1)
print "Updating..."
os.system('git pull')
time.sleep(2)
print 'Updated...'
time.sleep(1)
print "Relaunching...."
time.sleep(1)
os.system('python BeastBot.py')
exit() #Script should not hit this line
