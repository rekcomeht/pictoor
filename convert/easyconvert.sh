#!/bin/bash
# easily convert a file into epaper format
echo 'type the name of the file you want to convert (e.g. the example part of example.png)'
read source
echo 'type the extension of the file you want to convert (e.g. the png part of example.png)'
read ext

convert $source.$ext -dither FloydSteinberg -define dither:diffusion-amount=85% -remap 2c.png BMP3:~/pictoor/RaspberryPi_JetsonNano/python/pic/$source.bmp

