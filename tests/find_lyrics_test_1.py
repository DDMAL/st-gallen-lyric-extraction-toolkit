from gamera.core import *
from gamera.toolkits.st_gall_lyric_extraction import find_lyrics
import time

init_gamera()

img = load_image("/Users/nickesterer/Desktop/Untitled.png").to_rgb()

onebit = img.to_onebit()

ccs = onebit.cc_analysis()

print "Number of ccs before", len(ccs)

func = find_lyrics.remove_ccs_intersected_by_lines()

lines = [(float(1),float(x * 10)) for x in xrange(20)]

newccs = func(ccs, lines)

print "Number of newccs after", len(newccs)
print "Number of ccs after", len(ccs)

for m, b in lines:
  print m, b
  print onebit.lr.x, m * onebit.lr.x + b
  img.draw_line( FloatPoint(onebit.ul.x, b), FloatPoint(onebit.lr.x, m * onebit.lr.x + b), \
      RGBPixel(0,0,0))

for cc in newccs:
  img.highlight(cc, RGBPixel(255,0,0))

img.save_PNG("/Users/nickesterer/Desktop/find_lyrics_test_1.png")

for x, y in zip(ccs, newccs):
  print "Id's same?", (id(x) == id(y))

del(ccs)
del(newccs)

# print "Sleeping...",
# for i in xrange(10):
#   time.sleep(1)
#   print '.',
# print

#import pdb; pdb.set_trace()
