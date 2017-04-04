import urllib2

file = urllib2.urlopen('https://courses.cs.washington.edu/courses/cse326/02wi/homework/hw5/README-1.txt')
message = file.read()
print message
