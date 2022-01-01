# extract-zoom-urls.py
This repo contains a Python script I wrote to extract URLs from Zoom chat logs. 

## Installation

Download the script to any folder in your path, make sure it's executable (`chown 755 extract-zoom-urls.py`) and open a Terminal window to use it.

## Usage

This script takes Zoom chat log filenames as arguments. You can give it any number of filename arguments, but need to provide at least one filename. 

To use this script, open a Terminal window and run it. 

If run with no arguments, you'll get the following usage help:

```
% extract-zoom-urls.py
Extract URLs from Zoom chat logs. 
USAGE: ./extract-zoom-urls.py filename {filename(s)}
```

When run with at least one filename argument, you'll get a comma-separated list, including the filename, found URL, and name of the person who posted the URL
```
% extract-zoom-urls.py my-chat-log.txt *.txt
ERT Thu Wkshp 2 chat.txt,https://www.dickblick.com/products/nature-print-paper/,Kirk (they/them)
ERT Thu Wkshp 2 chat.txt,https://vimeo.com/user495806,John
ERT Thu Wkshp 2 chat.txt,https://www.youtube.com/watch?v=0t-tnN-moSY,Jennifer (she/her)
ERT Thu Wkshp 2 chat.txt,https://open.spotify.com/episode/3X9jFkCmbLN54ELGaU2W5K?si=BkSrXBppSz64XGnIAEetxQ,Tyler (he/him)
...
```

