l = ['10','3','2','6','8']

def getMaxList(list_input):    


	
	list_input.sort(key=int,reverse=True)
	
	MaxValue = list_input[0];
	
	print (MaxValue);
	

getMaxList(l);
