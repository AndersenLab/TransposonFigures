#!/usr/bin/env python
# repalces _CE
# NOTE: is not specific to TE names and will repalces all occurences in the file, should double check contents that this is wanted

import sys
import re

infile=sys.argv[1]
with open(infile, 'r') as IN:
	for line in IN:
		line=line.rstrip('\n')
		if re.search("_CE$",line):
			line=re.sub("_CE","",line)
		#if re.search("_CE_R$",line):
		line=re.sub("_CE_R","_R",line)
		#if re.search("_CE_NR$",line):
		line=re.sub("_CE_NR","_NR",line)
		print line
