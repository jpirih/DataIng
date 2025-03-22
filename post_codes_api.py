# Iskalnik poštnih številk na osnovi imena kraja in kode države 
# Uporablja dva Api-ja 
# 1 . API Ninjas geocoding  - pridobi podatke o geo lokaciji na osnovi imena kraja in države
# https://www.api-ninjas.com/api/geocoding
# 2. Post Code API pridobi podatke o poštni številki na osnovi geolokacije kraja (lat, long)
# https://apidocs.geoapify.com/playground/postcodes/
# Za oba apija je potrebno dobit Api Key
 
 
# Uporaba: 
# Pridobi oaba Api ključa  da bo koda delovala 
# poženi v terminalu 
# vipši ime Kraja  in  Iso kodo države 
# program vrne rezultat 



import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()


def get_city_geo_data(city:str, country='SI') -> list[dict]:
    """Gets cities geolocation data based on city name and country code"""
    city = city
    country = country
    city_geo_data = []
    api_url = 'https://api.api-ninjas.com/v1/geocoding?city={}&country={}'.format(city, country)
    response = requests.get(api_url + city, headers={'X-Api-Key': os.environ.get('GEO_API_KEY')})
    if response.status_code == requests.codes.ok:
        city_geo_data = response.json()
        print("\nCity geo data")
        print(json.dumps(city_geo_data, indent=4, ensure_ascii=False))
    else:
        city_geo_data.append[{'Error': response.status_code}]
        print("Error:", response.status_code, response.text)

    return city_geo_data


def get_postal_code_info(city_latitude: str, city_longitude: str) -> list[dict]:
    """Gets postal code infrmation about specifice location based on geo location. """
    
    api_key = os.environ.get('POST_CODES_API_KEY')
    url ="https://api.geoapify.com/v1/postcode/search?lat={}&lon={}&geometry=original&apiKey={}".format(str(city_latitude), str(city_longitude), api_key)
    response = requests.get(url)
    data = []
    
    if response.status_code == requests.codes.ok:
        postal_info = response.json()
        features = postal_info['features']
        for feature in features:
            
            data.append(feature['properties']['formatted'])
    else:
        data.append({'Error': response.status_code})
    
    return data
    
    
def get_postal_codes(city: str, country_code='SI') -> list['dict']: 
    """Gets informations about postal code for each city on the list """
    cities = get_city_geo_data(city, country_code)
    my_data = []    
    if len(cities) > 0:
        for city in cities:
            city_name = city['name']
            postal_info = get_postal_code_info(str(city['latitude']), str(city['longitude']))
            my_data.append({'city_name': city_name, 'postal_info': postal_info})
    else:
        my_data.append({'Error': 'Something went wrong try another city'})
        print("Error: No City with given name found.")
    return my_data
            

def search_for_postal_info():
    """Runs search process"""
    city = input('Enter city name: ')
    country_code = input("Enter two digit ISO country code default=SI: ")
    
    search_results = get_postal_codes(city, country_code)
    print("\n Search Results")
    print(json.dumps(search_results, indent=4, ensure_ascii=False))
    
    

if __name__ == '__main__':
    search_for_postal_info()
    