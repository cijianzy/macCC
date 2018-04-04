# -*- coding: UTF-8 -*-
# Title: __init__.py
# Time: 04/04/2018 5:34 PM
# Author: cijian
# Email: cijianzy@gmail.com

from PIL import ImageGrab
im = ImageGrab.grabclipboard()
im.save('somefile.png','PNG')
print('haha')
