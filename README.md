# BuildJS
builds javascript files into one file

##Usage
It takes one commandline parameter which contains the root file to be built.

Then inside that file and others there are two kinds of special things that are not normal javascript:
 - $include filename$ includes that file into the output file before this file.
 - $insert filename$ writes a file right into where this part is written, with newlines replaced by _.

Oh yeah and all filenames are relative to the original file.
