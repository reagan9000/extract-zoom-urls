#!/usr/local/opt/python/libexec/bin/python
#
# extract URLs from Zoom chat logs. Outputs csv-format filename, url, author
#

import sys, os, re

def main(argv):
	script = argv[0]
	USAGE  = str( "Extract URLs from Zoom chat logs. \nUSAGE: " + script + " filename {filename(s)}" )

	if len( argv ) == 1:
		print( USAGE )
		quit()
	elif len( argv ) > 1:
		for path in argv[1:]:
			with open(path) as file:
				filename = os.path.basename( path ) 
				for line in file:
					if "http" in line:
						if re.findall(r'(https?://[^\s]+)', line[15:]) :
							# just the URL
							url = re.findall(r'(https?://[^\s]+)', line[15:])[0]
							# name of the person who provided the URL
							url_author = line[15:].split( ':', 1)[0]
							# original full context of the URL
							url_full_context = str.rstrip(line[15:])
							print( filename + "," + url + "," + str.strip( url_author ) )

# run it
main( sys.argv )

