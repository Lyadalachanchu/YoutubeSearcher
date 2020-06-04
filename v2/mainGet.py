from getAllCaptionsFromChannel import get_channel_videos,gacfc
from captionSaver import captionSaver
from captionGetter import captionGetter
import pickle
import os


def mainGet(apikey, cID, path):
	api_key = apikey

	try:
		os.mkdir(path+'/captions/'+cID)
	except:
		print("file exists")


	captions = []


	gacfc(cID, path)
	captionSaver(cID, path)

	for filename in os.listdir(path+'/captions/'+cID):
		try:
			with open(path+'/captions/'+cID+'/'+filename, 'rb') as f:
				mynewlist = pickle.load(f)
				#print(mynewlist)
				captions.append(mynewlist)
				
		except Exception as e:
			#print(e)
			print("No transcipts available")


	return(captions)



