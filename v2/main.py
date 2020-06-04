from mainGet import mainGet
import pickle



query = "well worth"


path = '/Users/maxdekel/Desktop/stuff/YoutubeSearcher'
key = 'AIzaSyAZjUllFM931vhUM7JdOAl_eysGcTzGZtk'
cID = 'UCr3cBLTYmIK9kY0F_OdFWFQ'

captions = mainGet(apikey=key, cID=cID, path=path)
#print(captions)


for x in captions:
	for a in x[0:len(x)-2]:
		try:
			txt = a['text']
			if query in txt:
				print(a['start'], x[len(x)-1])
		except:
			print("something went wrong")
