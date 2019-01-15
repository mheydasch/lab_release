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
    FRET='/GrowthConeAnalyzer/BiosensorPackage/GCAFeatureExtraction/Descriptor/FRETRatioValues/Movie'
    png_find='.png'
    for root, dirs, files in os.walk(path):
        if FRET in root and 'colorBar' not in root:
            for f in files:
                if png_find in f:
                    graph=os.path.join(root, f)
                    Fovfolders.update({graph:f})   
    return Fovfolders, FRET

def copy_file(path):
    Fovfolders, FRET=get_folders(path)
    newdir=os.path.join(path, 'FRET_Collection')
    createFolder(newdir)
    for i in Fovfolders: 
        strippath=i.replace(FRET, '')
        splitpath=vars()['strippath'].split('/')
        newname= splitpath[-3]+'_'+splitpath[-2]+'_'+splitpath[-1]
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