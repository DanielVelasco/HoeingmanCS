from random import randint
from geopy.geocoders import Nominatim
from geopy.distance import vincenty

score = 0;

def SuggestCity(city_list):
	random_index = randint(0,len(city_list)-1);
	City = city_list[random_index];
	GenerateList = city_list;
	GenerateList.pop(random_index);
	print ("Your base city is " + City);
	print ("Which city in the list is closest to your base city");
	GenerateRandomCities(GenerateList,City);

def LoadCities():
	City_Array = [];
	input_file = open('CitiesToUse.txt','r');
	read_input_file = input_file.readlines();
	for line in read_input_file:
		split = line.split();
		capital_state = split[1] + ', ' + split[0];
		City_Array.append(capital_state);
	return City_Array;
	
	
def CalculateDistance(generated_array,base_city):
	List_sort = [];
	geolocator = Nominatim();
	main_location = geolocator.geocode(base_city, exactly_one=True, timeout=None);
	main_coordinates = (main_location.latitude,main_location.longitude);
	#print (main_coordinates);
	for x in generated_array:
		other_location = geolocator.geocode(x, exactly_one=True, timeout=None);
		other_coordinates = (other_location.latitude,other_location.longitude);
		result = vincenty(main_coordinates,other_coordinates).miles;
		List_sort.append({'City':x,'Distance_fromBase':result});
	ClosestCity = sorted(List_sort, key=lambda k: k['Distance_fromBase']);
	return ClosestCity[0]['City'];
		
def GenerateRandomCities(generate_list,City):
	global score;
	GenerateSuggested = [];
	for x in range(0,3):
		random_index = randint(0,len(generate_list)-1);
		GenerateSuggested.append(generate_list[random_index]);
		generate_list.pop(random_index);
	print (GenerateSuggested);
	Answer = CalculateDistance(GenerateSuggested,City);
	#print (Answer);
	selected_index = raw_input("Select city by entering index in list (0-3) ");
	selected_value = GenerateSuggested[int(selected_index)];
	if Answer == selected_value:
		print ("Your are correct!");
		
		score +=1
	else:
		print ("You are incorrect");
		print ("Correct answer is " + Answer)
		score -=1
	print ("Your current score is " + str(score));
	keepPlaying = raw_input("Enter q to quit. Enter y to keep playing ");
	if keepPlaying == 'y':
		Main();
	else:
		exit;
		
	
def Main():
	#need to modify to bypass LoadCities other than the first time
	
	Main_List = LoadCities();
		
	value = SuggestCity(Main_List);
	
	
	
Main();
	
