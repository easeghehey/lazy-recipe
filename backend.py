import requests
import os

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/complexSearch"

headers = {
	"X-RapidAPI-Key": os.environ.get("KEY_API"),
	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}

querystring = {"query":"pasta"}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)