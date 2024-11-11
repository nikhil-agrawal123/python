import requests 
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class Recipe:
    def __init__(self, recipe_name):
        self.recipe_name = recipe_name

    __app_id = '5a91edbf'
    __app_key = 'a79d75fe4ddab033ee6a7bb30075ecae'

    def search_recipes(self):
        url = 'https://api.edamam.com/search'
        params = {
            'q': self.recipe_name,
            'app_id': self.__app_id,
            'app_key': self.__app_key,
            'from': 0,
            'to': 5 
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            with open('recipes.json', 'w') as f:
                f.write(response.text + '\n')
            for recipe in response.json()['hits']:
                print()
                print(f"Recipe: {recipe['recipe']['label']}") 
                print(f"URL: {recipe['recipe']['url']}")
                print(f"Ingredients: {', '.join(recipe['recipe']['ingredientLines'])}")
        else:
            print("Failed to retrieve recipes")
            return None

class Github:
    def __init__(self, user):
        self.user = user

    def get_user_info(self):
        url = f'https://api.github.com/users/{self.user}'
        response = requests.get(url)
        if response.status_code == 200:
            with open('user.json', 'w') as f:
                f.write(response.text + '\n')
            data = response.json()
            print(f"Username: {data['login']}")
            print(f"Name: {data['name']}")
            print(f"Location: {data['location']}")
            print(f'User Profile: {data["html_url"]}')
            print(f"Bio: {data['bio']}")
        else:
            print("Failed to retrieve user information")
            return None

class Other:
    def __init__(self,query):
        self.query = query

    def other_method(self):
        genai.configure(api_key=f"{os.getenv('API_KEY')}")
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(self.query)
        return response.text


selection = input("Enter 'r' to search for recipes or 'h' to get user GitHub information for any other query enter o: ")

if selection == 'r':
    recipe_name = input("Enter the recipe name: ")
    recipe = Recipe(recipe_name)
    recipe.search_recipes()

elif selection == 'h':
    user = input("Enter the GitHub username: ")
    github = Github(user)
    github.get_user_info()

elif selection == 'o':
    query = input("Enter your query: ")
    other = Other(query)
    print(other.other_method())