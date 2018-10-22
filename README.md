# skeleton_particle
A directory to be the framework to hold cropped microglial images, skeleton and particle analyses, and them merged.

# How do I get what I want from this repository? #

Well, I'm glad you asked!!
First is to put all your tif (or tiff) images in the Images folder. Then, install and run Leahsaurus.ijm in Fiji, choosing the Images directory. 

After running Leahsaurus.ijm, open up a terminal. `cd` into this directory (e.g. `cd ~/Desktop/skeleton_particle/`), and then enter `python merge_results.py` This will then merge the most representative sample from the glials and merge them into one spreadsheet which can be found in the base folder (skeleton_particle).