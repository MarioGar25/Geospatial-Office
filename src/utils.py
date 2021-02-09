from functools import reduce
import operator
import requests
import os
import json
from dotenv import load_dotenv

def extract_city(dic):    
    ''' extracts the city from a dictionary '''
    return dic.get("city")

def extract_latitude(dic):
    ''' extracts the latitude from a dictionary '''
    return dic.get("latitude")

def extract_longitude(dic):
    ''' extracts the longitude from a dictionary '''
    return dic.get("longitude")


def get_coordinates(dic):
        '''extracts the coordinates from the geocode Api'''
        return {
            "type":"Point",
            "coordinates":[float(dic["longt"]),float(dic["latt"])]}


def get_location_from_dic(dic,x):
    ''' get values from dictionaries'''
    return reduce (operator.getitem,x,dic)


'''These functions take the number from establishment 
near the companies, and ponder to take points to choose one of them'''

def get_points_starbucks(lst):
    if lst >=3:
        return  3
    elif lst >=1:
        return 1
    else:
        return 0

def get_points_companies(lst):
    if lst >=7:
        return 6
    elif lst >=5:
        return 3
    elif lst >=3:
        return 1
    else:
        return 0

def get_points_schools(lst):
    if lst >=5:
        return +7
    elif lst >=3:
        return +5
    elif lst >=1:
        return +2
    else:
        return +0

def get_location_from_foursquare_in_SanFrancisco(establishment):
    load_dotenv()
    url = "https://api.foursquare.com/v2/venues/explore"
    tok1 = os.getenv("token1")
    tok2 = os.getenv("token2")
    parameters = {"client_id":tok1,
            "client_secret":tok2,
            "v": "20180323",
            "ll": "37.66881, -122.40443",
              "query":establishment,
              "limit": 100   }
    response = requests.get(url=url, params = parameters).json()
    print("Calling the Api")
    data_json = response.get("response")

    data_groups = data_json.get("groups")[0]

    data_items = data_groups.get("items")
    print("Getting the coordinates")
    final_list = []
    for dic in data_items:
        final_dic = {}
        i = dic.get("venue")
        name = i.get("name")
        location = i.get("location")
        latitude = location.get("lat")
        longitude = location.get("lng")
        final_dic["name"] = name
        final_dic["latitude"] = latitude
        final_dic["longitude"] = longitude
        final_list.append(final_dic)
    print("Finished")
    return final_list

def get_location_from_foursquare_in_SanFrancisco_second_mod(establishment):
    load_dotenv()
    url = "https://api.foursquare.com/v2/venues/explore"
    tok1 = os.getenv("token1")
    tok2 = os.getenv("token2")
    parameters = {"client_id":tok1,
            "client_secret":tok2,
            "v": "20180323",
            "ll": "37.66881, -122.40443",
              "query":establishment,
              "limit": 100   }
    response = requests.get(url=url, params = parameters).json()
    print("Calling the Api")
    data_json = response.get("response")

    data_groups = data_json.get("groups")[0]

    data_items = data_groups.get("items")
    print("Getting the coordinates")
    data_name = ["venue", "name"]
    data_longitude = ["venue", "location", "lng"]
    data_latitude = ["venue", "location", "lat"]
    final_list = []
    for dic in data_items:
        final_dic = {}
        final_dic["name"] = get_location_from_dic(dic, data_name)
        final_dic["latitude"] = get_location_from_dic(dic, data_latitude)
        final_dic["longitude"] = get_location_from_dic(dic, data_longitude)
        final_list.append(final_dic)
    
    return final_list