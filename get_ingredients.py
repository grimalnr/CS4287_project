import spoonacular as sp
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
# Use "get_recipe_information"

