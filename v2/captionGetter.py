import pickle

def captionGetter(cID, path):
	for filename in os.listdir(path+'/captions/'+cID):
		try:
			with open(filename, 'rb') as f:
				mynewlist = pickle.load(f)
				#print(mynewlist)
				
		except Exception as e:
			print(e)
			print("No transcipts available")