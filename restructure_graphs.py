#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 15:52:16 2019

@author: max
"""

import os
import re
import argparse
import shutil 

#%%
def parseArguments():
  # Define the parser and read arguments
  parser = argparse.ArgumentParser(description='Get tags from all files in a directory.')
  parser.add_argument('-d', '--dir', type=str, help='The hierarchical cluster folder', required=True)  
  args = parser.parse_args()
  return(args)
  
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' + directory)  

def get_folders(path):
    Fovfolders={}
    for root, dirs, files in os.walk(path):
        for i in files:
            if i.endswith('.png'):
                graph=os.path.join(root, i)
                Fovfolders.update({graph:i})
    return Fovfolders

def copy_file(path):
    Fovfolders=get_folders(path)
    newdir=os.path.join(path, 'Collection')
    createFolder(newdir)
    for i in Fovfolders: 
        newloc=os.path.join(newdir, Fovfolders[i])
        try:
            shutil.copyfile(i, newloc)
            print(i, 'copied to', newloc)
        except shutil.SameFileError:
            print(Fovfolders[i], 'exists already at this location')
        
if __name__ == '__main__':
    args=parseArguments()
    path=args.dir    
    copy_file(path)
    print(args)
        
        
        
        
        
        
        
        
        
        
        
        
        
#%%        