# This is a setup file

import os

os.popen("curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar >> ~/wp-cli.phar")
os.popen("chmod +x wp-cli.phar")

print ('importing done')
