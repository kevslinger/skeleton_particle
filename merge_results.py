#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 17:00:23 2018

@author: kevin

Python script to take all csv result files and merge them into one, removing unneccesary noise.

Example usage:
    python merge_results.py ~/Desktop/Images/
"""


import os
import glob
import pandas as pd
pd.options.mode.chained_assignment = None
def do_stuff(directory):
    # Find directories where the skeelton and particle csvs are hiding.
    skeleton_path = os.path.join(directory, 'Skeleton')
    particle_path = os.path.join(directory, 'Particle')
    # Create DataFrames to hold the max examples of each skeleton/particle csv
    skele_columns = ['Filename', '# Branches', '# Junctions', '# End-point voxels', '# Junction voxels', '# Slab voxels', 'Average Branch Length', '# Triple points', '# Quadruple points', 'Maximum Branch Length']
    skele_df = pd.DataFrame(columns=skele_columns)
    particle_columns = ['Filename', 'Area', 'Mean', 'Min', 'Max']
    particle_df = pd.DataFrame(columns=particle_columns)
    # Make a list for iteration through all csvs in the directories
    skeleton_files = filter(lambda x: '.csv' in x, os.listdir(skeleton_path))
    particle_files = filter(lambda x: '.csv' in x, os.listdir(particle_path))
    # Iterate over all csvs
    for i in range(len(glob.glob(os.path.join(particle_path, '*.csv')))):
        # Read in skeleton csv and add the representative skeleton from image.
        skeleton = pd.read_csv(os.path.join(skeleton_path, skeleton_files[i]))
        skeleton = skeleton[skeleton['# Branches'] == max(skeleton['# Branches'])]
        skeleton.reset_index(drop=True, inplace=True)
        skele_df = pd.concat([skele_df, skeleton.iloc(0)], ignore_index=True, sort=False)
        skele_df['Filename'].iloc[i] = skeleton_files[i]
        # Read in particle csv and add the representative particle from image.
        particle = pd.read_csv(os.path.join(particle_path, particle_files[i]))
        particle.drop(axis=1, columns=[" "], inplace=True)
        particle = particle[particle['Area'] == max(particle['Area'])]
        particle.reset_index(drop=True, inplace=True)
        particle_df = pd.concat([particle_df, particle.iloc(0)], ignore_index=True, sort=False)
        particle_df['Filename'].iloc[i] = particle_files[i]
    # After the loop, sort the dataframes by filename, and then rearrange the columns so filename is the first column, then export.
    skele_df.sort_values(by=['Filename'], inplace=True)
    particle_df.sort_values(by=['Filename'], inplace=True)
    skele_df = skele_df[skele_columns]
    particle_df = particle_df[particle_columns]
    skele_df.to_csv(os.path.join(directory, 'skeleton_results.csv'), index=False)
    particle_df.to_csv(os.path.join(directory, 'particle_results.csv'), index=False)
    print('Merged {} results!'.format(i+1))
    

# Run Script
if __name__ == '__main__':
    '''import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('directory')
    args = parser.parse_args()
    path = args.directory
    '''
    path = os.getcwd()
    do_stuff(path)
    
