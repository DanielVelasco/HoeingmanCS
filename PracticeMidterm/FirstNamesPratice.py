
names  = ['Superman','Batman','The Joker','Wonder Woman'];

def getHeroLastName(list_input):
	firstNamesArray = [];
	for x in list_input:
		split = x.split();
		firstname = split[0];
		firstNamesArray.append(firstname);
	print (firstNamesArray);

getHeroLastName(names);

def printDictionary(dictionary):
	for a in dictionary.keys():
		print (a + ' : ' + dictionary[a]);
		
printDictionary({'Name':'Nelson','Age':'14'});

def getUserName(firstName,lastName):
	Letter = firstName;
	LastName = lastName;
	firstLetter = Letter[:1];
	print (firstLetter);
	if len(lastName) >= 3:
		lastThreeLetters = lastName[3:];
		print (lastThreeLetters);
	else:
		print (lastName);
		
getUserName('Billbob','Doobie');
		

def updateDictionary(dictionary,key,value):
	dictionary[key] = value;
	print (dictionary)
	
dictionary = {'Name':'Nelson','Age':'14'};
	
	
	
updateDictionary(dictionary,'Name','Bobby');
	









