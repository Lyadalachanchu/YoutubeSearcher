from youtube_transcript_api import YouTubeTranscriptApi
import pickle
ids = []
file1 = open('output.txt', 'r') 
Lines = file1.readlines() 
  
count = 0
# Strips the newline character 
for line in Lines: 
    print(line)
    ids.append(line)
print(ids) 



for i, s in enumerate(ids):
	#print(type(s))
	try:
		transcript = YouTubeTranscriptApi.get_transcript(s)
		#print(type(transcript))
		with open('C:\\Users\\lyada\\Desktop\\Python\\Captions\\{}.pkl'.format(str(i)), 'wb') as f:
			pickle.dump(transcript, f)
			print(i)
	except:
		print("No transcipts available")
	''''json = json.dumps(transcript)
					f = open("{}.json".format(str(i)),"w")
					f.write(json)
					f.close()'''