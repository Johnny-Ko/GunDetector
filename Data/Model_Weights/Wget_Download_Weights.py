# Modified from https://stackoverflow.com/questions/25010369/wget-curl-large-file-from-google-drive

# To download houses weights run
# python Download_Weights.py 1aPCwYXFAOmklmNMLMh81Yduw5UrbHqkN Houses/trained_weights_final.h5

# To download openeings weights run
# python Download_Weights.py 1FbvHzQWCjucXPbTbI4S1MnBLkAi58Mxv Openings/trained_weights_final.h5

import requests
import os
import wget

#create this bar_progress method which is invoked automatically from wget
def bar_progress(current, total, width=80):
  progress_message = "Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total)
  # Don't use print() as it will print in new line every time.
  sys.stdout.write("\r" + progress_message)
  sys.stdout.flush()  

def wget_file(weight_file_name, destination):
    fileURL = 'https://pjreddie.com/media/files/'  + weight_file_name
    fileURL
    filename = wget.download(fileURL, out=destination, bar=bar_progress)


if __name__ == "__main__":
    import sys

    if len(sys.argv) is not 3:
        print("Usage: python wget_download_Weights.py weight_file destination_folder")
    else:
        # TAKE ID FROM SHAREABLE LINK
        weight_file_name = sys.argv[1]
        # DESTINATION FILE ON YOUR DISK
        destination = sys.argv[2]
        wget_file(weight_file_name, destination)
