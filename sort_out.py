#open the file
file = open('words_english.txt', 'r')

#split it into lines
lines = file.readlines()

#sort them
lines.sort()

print lines

thefile = open('test.txt', 'w')

for item in lines:
  thefile.write("%s" % item)

thefile.close()
