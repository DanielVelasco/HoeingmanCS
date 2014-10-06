#!/usr/bin/env	python
from geopy.geocoders import Nominatim
from geopy.distance import vincenty

#Calculates Distance

def CalculateDistance(place,city_list,Path_to_Take,Distance,length):
	geolocator = Nominatim();
	main_location = geolocator.geocode(place, exactly_one=True, timeout=None);
	main_coordinates = (main_location.latitude,main_location.longitude);
	list_toSort = [];
	for x in city_list:
		place_location = geolocator.geocode(x, exactly_one=True, timeout=None);
		place_coordinates = (place_location.latitude,place_location.longitude);
		print place_coordinates;
		result = vincenty(main_coordinates,place_coordinates).miles
		print result;
		list_toSort.append({'Name':x,'Distance':result});
	newlist = sorted(list_toSort, key=lambda k: k['Distance']) 
	Path_to_Take.append(newlist[1]);
	Distance += newlist[1]['Distance']
	city_list.remove(city_list[0]);
	if len(Path_to_Take) < length:
		CalculateDistance(newlist[1]['Name'],city_list,Path_to_Take,Distance,length);
	if len(Path_to_Take) == length:
		main_location = geolocator.geocode(Path_to_Take[0]['Name'], exactly_one=True, timeout=None);
		main_coordinates = (main_location.latitude,main_location.longitude);
		place_location = geolocator.geocode(Path_to_Take[length-1]['Name'], exactly_one=True, timeout=None);
		place_coordinates = (place_location.latitude,place_location.longitude);
		result = vincenty(main_coordinates,place_coordinates).miles
		Path_to_Take.append({'Name':Path_to_Take[0]['Name'],'Distance':result});
	
	
#Main function which is called in the begining	
def Main():
	input_datafile = open("cityList.txt","r");
	Read_Datafile = input_datafile.readlines();

	geolocator = Nominatim()
	city_list = [];
	Path_to_Take = [];
	Distance = 0;
	for x in Read_Datafile:
	
		if x not in city_list:
	
			city_list.append(x.replace("\n"," ").replace("\t"," "));

	Org_length = len(city_list);
	Path_to_Take.append({'Name':city_list[0],'Distance':0});
	CalculateDistance(city_list[0],city_list,Path_to_Take,Distance,Org_length);
	print Path_to_Take;
	
	for x in Path_to_Take:
		Distance += x['Distance'];
	print Distance;

	
	
Main();
	
