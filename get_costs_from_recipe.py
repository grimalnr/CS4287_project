from serpapi import GoogleSearch
import spoonacular as sp

# Code to get ingredients from dish
api = sp.API("46a4239a30464cbc8727ab612f8a3558")

def get_id(recipe):
    rps = api.search_recipes_complex(recipe)
    data = rps.json()
    return data

val = input("Enter a recipe: ")
data = get_id(val)
id = data['results'][0]['id']
info = api.get_recipe_information(id)
info_j = info.json()

ingredients = []
for i in range(len(info_j['extendedIngredients'])):
    ingredients.append(info_j['extendedIngredients'][i]['name'])

print(ingredients)

# Gather and print recipe from Walmart
print("Store 1: Walmart")
total_cost_walmart = 0
for item in ingredients:
    params = {
      "engine": "walmart",
      "query": str(item),
      "api_key": "0025420b4b9021ca305353e0bc907bbc650dfde744e6d1eedd5b9165feea8333"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    organic_results = results["organic_results"]
    print("Original Ingredient:", item)
    print("Found:",organic_results[0]['title'])
    print("Cost: $",organic_results[0]['primary_offer']['offer_price'])
    total_cost_walmart += float(organic_results[0]['primary_offer']['offer_price'])

print(" ")

# Gather and print recipe from eBay
print("Store 2: eBay")
total_cost_ebay = 0
for item in ingredients:
    params = {
      "engine": "ebay",
      "_nkw": str(item),
      "ebay_domain": "ebay.com",
      "api_key": "0025420b4b9021ca305353e0bc907bbc650dfde744e6d1eedd5b9165feea8333"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    organic_results = results["organic_results"]
    print("Original Ingredient:", item)
    print("Found:",organic_results[0]['title'])
    price_line = organic_results[0]['price']
    if "from" in price_line:
        print("Cost: $",organic_results[0]['price']['from']['extracted'])
        total_cost_ebay += float(organic_results[0]['price']['from']['extracted'])    
    else:
        print("Cost: $",organic_results[0]['price']['extracted'])
        total_cost_ebay += float(organic_results[0]['price']['extracted'])

print(" ")

# Compare total costs for each store
print("Total costs:")
print("Walmart: $", total_cost_walmart)
print("eBay: $", total_cost_ebay)

