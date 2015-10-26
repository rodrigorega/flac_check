#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
Script Website: https://github.com/rodrigorega/flac_check 
Author: Rodrigo Rega <contacto@rodrigorega.es>
License: CC-BY-SA 3.0 license (http://creativecommons.org/licenses/by/3.0/
'''

import os
import sys

flac_exe = '/usr/bin/flac'

def main():
    script_argument = sys.argv[1]

    if os.path.isfile(script_argument):
        print '- Starting flac file check. Displaying only files with errors:'
        check_flac(script_argument)
    elif os.path.isdir(script_argument):
        print '- Starting flac directory check. Displaying only files with errors:'        
        check_flac_dir(script_argument)
    else:
        print script_argument + ': Invalid file or directory.'

    print '\n- Done.'

def check_flac(flac_file):
    flac_command = flac_exe + ' -wst ' + '"' + flac_file + '"'
    os.system(flac_command)

def check_flac_dir(flac_dir):
    for root, dirs, files in os.walk(flac_dir):
        for file in files:
            nameNoExtension, extension = os.path.splitext(file)
            if extension == '.flac':
                check_flac(os.path.join(root, file))

main()
