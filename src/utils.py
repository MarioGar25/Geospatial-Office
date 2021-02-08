from functools import reduce
import operator


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


def get_school_location_from_dic(dic,x):
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