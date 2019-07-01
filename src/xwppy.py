import os

def wpcli(command):
    ''' Sends the command to handle Wordpress using Python'''
	if type(command) != str:
		print ("wpcli accepts only string argument")
	output = os.popen('~/wp-cli.phar '+command)
	print (output)
	return (output) 
