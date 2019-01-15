#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 10:44:06 2019

@author: max

Takes the first tif file from the actin channel of all files and copies it into a collection folder.
"""

import os
import re
import argparse
import shutil 

#%%
def parseArguments():
  # Define the parser and read arguments
  parser = argparse.ArgumentParser(description='Get tags from all files in a directory.')
  parser.add_argument('-d', '--dir', type=str, help='The segmented folder', required=True)  
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
    actin='Channels/C1_'
    FoI='C1_001.tif'
    for root, dirs, files in os.walk(path):
        if actin in root:
            for f in files:
                if FoI in f:
                    graph=os.path.join(root, f)
                    Fovfolders.update({graph:f})   
    return Fovfolders

def copy_file(path):
    Fovfolders=get_folders(path)
    newdir=os.path.join(path, 'Actin_Collection')
    createFolder(newdir)
    for i in Fovfolders: 
        splitpath=vars()['i'].split('/')
        newname=splitpath[-5]+'_'+splitpath[-4]+'_'+splitpath[-2]+'_'+splitpath[-1]
        newloc=os.path.join(newdir, newname)
        try:
            shutil.copyfile(i, newloc)
            print(i, 'copied to', newloc)
        except shutil.SameFileError:
            print(Fovfolders[i], 'exists already at this location')
#%%        
if __name__ == '__main__':
    args=parseArguments()
    path=args.dir    
    copy_file(path)
    print(args)
        
        
        
        
        
        
        
        
        
        
        
        
        
#%%        