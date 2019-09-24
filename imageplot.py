import sys, os, math
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

try: # Pillow
  from PIL import Image
except:
  print ('Error: Pillow has not been installed.')
  sys.exit(0)

imgDir      = 'images'
imgFilename = 'mandrill.png'

currentImage = Image.open( os.path.join( imgDir, imgFilename )).convert( 'YCbCr' ).transpose( Image.FLIP_TOP_BOTTOM )

def lights(val,x):
  if x > 1:
    return val ** (.5)
  else:
    return val ** (4)

def darks(val,x):
  if x < 1:
    return val ** (.5)
  else:
    return val ** (4)

def meanbasedstrech(arr):
  mean = np.mean(arr)
  great = arr[arr>mean]
  gpos np.nonzero(arr > mean)
  less = arr[arr<mean]
  lpos np.nonzero(arr < mean)
  print great
  print less
  vfuncl = np.vectorize(lights)
  vfuncd = np.vectorize(darks)
  mapl = vfuncl(great, 1.34)
  mapd = vfuncd(less, 1.34)
  print mapl
  print mapd
  for i in range(gpos.size):
    arr[gpos[i]] = mapl[i]
  for i in range(lpos.size):
    arrp[lpos[i]] = mapd[i]
    
  
  

def strech(li):
  arr = np.asarray(li)
  hist = np.histogram(arr, 256,[0,256])
  print hist
  hist_dist = scipy.stats.rv_histogram(hist)
  c = hist_dist.ppf(0.05)
  d = hist_dist.ppf(0.95)
  print c
  print d
  for i in range(len(li)):
    temp = (255-0)/(d-c)
    pout = (li[i] - c)*temp
    li[i] = pout
  return li

# Plot Bullshit
hello = currentImage.getdata()
k = list()
currentImage = currentImage.convert("YCbCr")
for i in hello:
  temp = (i[0])
  k.append(temp)

r = np.asarray(k)
meanbasedstrech(r)
# e = np.asarray(strech(k))
# 
# plt.hist(r, 256, [0,256], color = 'r')
# plt.hist(e, 256, [0,256], color = 'b')
# plt.show()




