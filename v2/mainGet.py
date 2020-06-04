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


	#gacfc(cID, path)
	#captionSaver(cID, path)

	for filename in os.listdir(path+'/captions/'+cID):
		try:
			with open(path+'/captions/'+cID+'/'+filename, 'rb') as f:
				mynewlist = pickle.load(f)
				#print(mynewlist)
				captions.append(mynewlist)
				#print(mynewlist)
				
		except Exception as e:
			#print(e)
			print("No transcipts available")

	#Searching Part
	wsdv = []
	for x, caption in enumerate(captions):
		counter = 0
		for z, line in enumerate(caption):
			for a, word in enumerate(line['text'].split()):
				wsdv.append([word, counter])
				counter += 1
		

	query = "or ski"
	query = query.split()
	store = []
	location = []
	for i in range(len(wsdv)):
		if (wsdv[i][0] == query[0]):
			for n in range(len(query)):
				if(query[n] == wsdv[i+n][0]):
					pass
				else:
					store = []
					break
				if(n == len(query)-1):
					print('Found query at {}'.format(i))
					store.append(i)
					location = [i, i+len(query)-1]

	print(location)
