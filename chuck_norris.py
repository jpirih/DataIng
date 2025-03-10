# Vici o Chacku Norrisu 
# Naključni vic ne glede na kategorijo 
# En Naključni športni vic 
# En naključni vic za vsako kategorijo 
# Uporablja : https://api.chucknorris.io/

# Uporaba: 
# Poženi  kodo v terminalu 

import requests
import json

def get_chuck_norris_joke() -> str:
    """Returns random Chuck Norris joke"""
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    
    if response.status_code == 200:
        joke_data = response.json()
        return joke_data["value"]
    else:
        return f"Failed to fetch joke. Status code: {response.status_code}"
    
def get_chuck_norris_sport_joke() -> str:
    """Returns random Sports joke about Chuck Norris"""
    url = "https://api.chucknorris.io/jokes/random?category=sport"
    
    response = requests.get(url)
    if response.status_code == 200:
        joke_data = response.json()
        return joke_data['value']
    else:
        print('Something went wrong.')


def get_jokes_categories() -> list:
    """Gets categories of Chuck Norris joeks from Api"""
    categories_url = "https://api.chucknorris.io/jokes/categories"
    cat_resp = requests.get(categories_url)
    if cat_resp.status_code == 200:
        joke_categories = cat_resp.json()
    return joke_categories


def get_joke_by_category(category: str) -> str:
    """Gets random Chuck Norris joke from specified category"""
    url = "https://api.chucknorris.io/jokes/random?category={}".format(category)
    
    response = requests.get(url)
    if response.status_code == 200:
        joke_data = response.json()
        return joke_data['value']
    else:
        print('Something went wrong.')

def get_joke_for_each_category() -> dict:
    """Returns random joke for each category in categories list"""
    categories = get_jokes_categories()
    jokes = {}
    for category in categories:
        jokes[category] = get_joke_by_category(category)
    return jokes

def show_jokes() -> None:
    random_joke = get_chuck_norris_joke()
    sports_joke = get_chuck_norris_sport_joke()
    jokes = get_joke_for_each_category()
    
    print("----- Chuck Norris -----")
    print("\n Random Chuck Norris Joke: {}".format(random_joke))	
    print("\n Chuck Norris Sports Joke: {}".format(sports_joke))	
    print("\n Random Jokes by category")

    print(json.dumps(jokes, indent=4))


if __name__ == "__main__":
    show_jokes()
    
    
    
    