import pickle
file1 = open('output.txt', 'r') 
Lines = file1.readlines() 
  
count = 0
# Strips the newline character 
for line in Lines: 
    count += 1
    print(count)

for x in range(count):
    try:
        with open('C:\\Users\\lyada\\Desktop\\Python\\Captions\\{}.pkl'.format(str(count-1)), 'rb') as f:
            mynewlist = pickle.load(f)
            print(mynewlist)
    except:
        print("No transcipts available")