#!/usr/bin//env python3

import sys

for line in sys.stdin:
	line = line.lower()

	special_characters = ['!','@','#','$','%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', ',', '.', '<', '>', '/', '?', '~', '`']
	for i in line:
		for j in special_characters:
			if i == j:
				line=line.replace(i,"")

	words = line.split()
	for word in words:
		print('{0}\t{1}'.format(word, 1))
