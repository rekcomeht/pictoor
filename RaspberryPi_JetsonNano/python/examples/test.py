#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd7in5_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

def picdisplay(fname):
    epd=epd7in5_V2.EPD()
    epd.init()
    Himage = Image.open(os.path.join(picdir,  fname+'.bmp'))
    epd.display(epd.getbuffer(Himage))
    epd.sleep()

try:
    logging.info("epd7in5_V2 Demo")
    epd = epd7in5_V2.EPD()
    
    logging.info("init and Clear")
    epd.init()
  
    logging.info("3.read bmp file")
    Himage = Image.open(os.path.join(picdir, 'pupper.bmp'))
    epd.display(epd.getbuffer(Himage))
    time.sleep(2)

    
    logging.info("Goto Sleep...")
    epd.sleep()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd7in5_V2.epdconfig.module_exit()
    exit()
