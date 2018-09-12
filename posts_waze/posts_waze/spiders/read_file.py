 # -*- coding: utf-8 -*-

import csv

#Read the .CSV and put it in a matrix

ds = csv.reader(open('wazecomments.csv'))

lines = [l for l in ds]

#Retrieve the column comment_text

comment_text = []

for i in range(len(lines)):
	comment_text.append(lines[i][0])

print len(comment_text)

unicos = list(set(comment_text))

print len(lines)

for i in range(len(lines)):
	if i < len(unicos):
		lines[i][0] = unicos[i]
	else:	
		lines[i][0] = ''

new_file = open('wazecomments_clear.csv', 'w')
with new_file:
    writer = csv.writer(new_file)
    writer.writerows(lines)

print "Done!"



			
		
