#!/usr/bin/env python2
from moviepy.editor import *
import numpy as np
import scipy
import os
import skimage.io as io
from skimage.color import rgb2grey
import matplotlib.pyplot as plt
from multiprocessing import Pool

# TODO: Replace moviepy with pyAV for speed
# TODO: Make this commandline callable

def set_path():
    '''
    Sets correct path specifically on my computer
    '''
    os.chdir("/Users/Teresa/Documents/DTU/Semester2/bigdata/challenge3")

def avg_vid(vid):
    '''
    Converts a MoviePy clip object to an image represented as a numpy array by
    averaging the frames of the clip.
    '''
    # Extract width and height from vid object
    width = vid.w
    heigth = vid.h
    # Create starting matrix of zeros
    img = np.zeros(shape=(heigth, width,3))
    # Frame counter; moviepy does not provide frame information
    n_frames = 0
    # Add up each frame represented as a matrix
    for f in vid.iter_frames():
        img += f
        n_frames += 1
    # Return average of the final cumulative matrix as unsigned int8 (0 to 255)
    return (img/n_frames).astype('uint8')


def main():
    print("Starting video processing...")
    n = 1
    for file in os.listdir("videos/"):
        #if (hash(file.name())==i%8):
        print("... processing (%d/%d)" %( n, len(os.listdir("videos/")) ))
        n += 1

        if file.endswith(".mp4"):
            # Set paths for video import and image export
            path_in = "videos/" + file
            path_out = "images/" + os.path.splitext(file)[0] + ".png"
            # Create directory if necessary
            if not os.path.exists("images/"):
                os.makedirs("images/")
            # Import video and process to obtain averaged image
            vid = VideoFileClip(path_in, audio=False)
            img = avg_vid(vid)
            io.imsave(path_out, img)
        else:
            print("An unsupported file type was detected in the videos folder. Only mp4 is supported.")
            continue

if __name__ == '__main__':
    main()