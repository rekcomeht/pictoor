#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)
import socket
    
import logging
from waveshare_epd import epd7in5_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

def boot():
    epd = epd7in5_V2.EPD()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect (("8.8.8.8",80))
    ipadd = s.getsockname()[0]
    epd.init()
    epd.Clear()

    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    Limage = Image.open(os.path.join(picdir, 'pupper.bmp'))
    draw = ImageDraw.Draw(Limage)
    draw.text((20, 25), 'my ip address is', font = font18, fill = 0)
    draw.text((20, 50), str(ipadd)+':8080     use /change/[filename] to change my picture', font = font18, fill = 0)
    epd.display(epd.getbuffer(Limage))
    epd.sleep()
try:
    logging.info("epd7in5_V2 Demo")
    epd = epd7in5_V2.EPD()
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect (("8.8.8.8",80))
    ipadd = s.getsockname()[0]
    
    logging.info("init and Clear")
    epd.init()
    epd.Clear()

    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)

    
    # Drawing on the Vertical image
    logging.info("2.Drawing on the Vertical image...")
    Limage = Image.open(os.path.join(picdir, 'pupper.bmp'))
    draw = ImageDraw.Draw(Limage)
    draw.text((20, 25), 'my ip address is', font = font18, fill = 0)
    draw.text((20, 50), str(ipadd), font = font18, fill = 0)
    epd.display(epd.getbuffer(Limage))
 

    logging.info("Goto Sleep...")
    epd.sleep()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd7in5_V2.epdconfig.module_exit()
    exit()
