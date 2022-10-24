import os
from shutil import copy2
import glob


tar = []
for img in glob.iglob('C:/Users/Drew Alderfer/code/flatiron/NYC-DS-091922/Phase_2/**/images/*.jpg', recursive=True):
    tar.append(img)
for img in glob.iglob('C:/Users/Drew Alderfer/code/flatiron/NYC-DS-091922/Phase_2/**/images/*.png', recursive=True):
    tar.append(img)

for x in tar:
    copy2(x, 'C:/Users/Drew Alderfer/code/flatiron/NYC-DS-091922/Phase_2/home/images/')
