import os, os.path
import urllib
import urllib.request

url = 'https://www.youtube.com/watch?v=aBTDvlteZcs'

filename = os.path.basename()
r = urllib.request.urlopen(url)
image = np.asarray(bytearray(resp.read()), dtype="uint8")