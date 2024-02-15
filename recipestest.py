breads = [{
    "Name":
    "White Bread",
    "Ingredients": [{
        "Name": "Instant Yeast",
        "Amount": "4.5 teaspoons"
    }, {
        "Name": "Water",
        "Amount": "3/4ths cup"
    }, {
        "Name": "Granulated Sugar",
        "Amount": "1/4ths cup"
    }, {
        "Name": "Salt",
        "Amount": "2 tablespoon"
    }, {
        "Name": "Unsalted Butter",
        "Amount": "6 tablespoon"
    }, {
        "Name": "Flour",
        "Amount": "10 cups"
    }]
}, {
    "Name":
    "Wheat Bread",
    "Ingredients": [{
        "Name": "Water",
        "Amount": "1 cup"
    }, {
        "Name": "Milk",
        "Amount": "1/4 cup"
    }, {
        "Name": "Honey",
        "Amount": "3 tablespoons"
    }, {
        "Name": "Dry Yeast",
        "Amount": "2 1/4 teaspoons"
    }, {
        "Name": "Wheat Flour",
        "Amount": "3 cups"
    }, {
        "Name": "Salt",
        "Amount": "1 1/2 teaspoons"
    }, {
        "Name": "Unsalted Butter",
        "Amount": "3 tablespoons"
    }]
}]

cakes = [{
    "Name":
    "Chocolate Cake",
    "Ingredients": [{
        "Name": "flour",
        "Amount": "2 cups"
    }, {
        "Name": "sugar",
        "Amount": "1 cup"
    }, {
        "Name": "cocoa powder",
        "Amount": "1 cup"
    }, {
        "Name": "baking powder",
        "Amount": "1 teaspoon"
    }, {
        "Name": "eggs",
        "Amount": "2 eggs"
    }, {
        "Name": "milk",
        "Amount": "1 cup"
    }, {
        "Name": "oil",
        "Amount": "1 cup"
    }, {
        "Name": "vanilla extract",
        "Amount": "1 teaspoon"
    }]
}, {
    "Name":
    "Velvet Cake",
    "Ingredients": [{
        "Name": "Beetroots",
        "Amount": "3"
    }, {
        "Name": "Vegetable Oil",
        "Amount": "3/4 cup"
    }, {
        "Name": "Muscovado Sugar",
        "Amount": "1/2 cup"
    }, {
        "Name": "Granulated Sugar",
        "Amount": "1/2 cup"
    }, {
        "Name": "Eggs",
        "Amount": "2"
    }, {
        "Name": "Flour",
        "Amount": "1 1/4 cup"
    }, {
        "Name": "Ground Cinnamon",
        "Amount": "1 teaspoon"
    }, {
        "Name": "Baking Powder",
        "Amount": "1 1/2 teaspoons"
    }, {
        "Name": "Salt",
        "Amount": "1 pinch"
    }]
}]

barbeque = [{
    "Name":
    "Barbeque Sauce",
    "Ingredients": [{
        "Name": "Brown Sugar",
        "Amount": "1 1/2 cups"
    }, {
        "Name": "Ketchup",
        "Amount": "1 1/2 cups"
    }, {
        "Name": "Red Wine Vinegar",
        "Amount": "1/2 cup"
    }, {
        "Name": "Water",
        "Amount": "1/2 cup"
    }, {
        "Name": "Dry Mustard",
        "Amount": "2 1/2 tabelspoons"
    }, {
        "Name": "Paprika",
        "Amount": "2 teaspoons"
    }, {
        "Name": "Salt",
        "Amount": "2 teaspoons"
    }, {
        "Name": "Black Pepper",
        "Amount": "1 1/2 teaspoons"
    }, {
        "Name": "Hot Sauce",
        "Amount": "2 dashes"
    }]
}, {
    "Name":
    "Pulled Pork",
    "Ingredients": [{
        "Name": "Pork Shoulder",
        "Amount": "4 lbs"
    }, {
        "Name": "Oil",
        "Amount": "2 tablespoons"
    }, {
        "Name": "Brown Sugar",
        "Amount": "1 tablespoons"
    }, {
        "Name": "Chili Powder",
        "Amount": "1 tablespoons"
    }, {
        "Name": "Onion Powder",
        "Amount": "1 teaspoons"
    }, {
        "Name": "Garlic Powder",
        "Amount": "1 teaspoons"
    }, {
        "Name": "Cumin",
        "Amount": "1 teaspoons"
    }, {
        "Name": "Kosher Salt",
        "Amount": "1 teaspoons"
    }, {
        "Name": "Black Pepper",
        "Amount": "1 teaspoons"
    }, {
        "Name": "Coca-Cola",
        "Amount": "12 ounces"
    }, {
        "Name": "bbq sauce",
        "Amount": "16-32 ounces"
    }]
}]

italian = [{
    "Name":
    "Manicotti",
    "Ingredients": [{
        "Name": "Manicotti Pasta",
        "Amount": "5 1/2 ounces"
    }, {
        "Name": "Ricotta Cheese",
        "Amount": "1 pint"
    }, {
        "Name": "Shredded Mozzarella",
        "Amount": "8 ounces"
    }, {
        "Name": "Grated Parmesan",
        "Amount": "3/4 cup"
    }, {
        "Name": "Eggs",
        "Amount": "2"
    }, {
        "Name": "Dried Parsley",
        "Amount": "1 teaspoom"
    }, {
        "Name": "Salt",
        "Amount": "1 pinch"
    }, {
        "Name": "Pepper",
        "Amount": "1 pinch"
    }, {
        "Name": "Spaghetti Sauce",
        "Amount": "16 ounces"
    }]
}, {
    "Name":
    "Calzone",
    "Ingredients": [{
        "Name": "Yeast",
        "Amount": ".25 ounce"
    }, {
        "Name": "Water",
        "Amount": "1 cup"
    }, {
        "Name": "Olive Oil",
        "Amount": "1 tablespoon"
    }, {
        "Name": "White Sugar",
        "Amount": "1 teaspoon"
    }, {
        "Name": "Salt",
        "Amount": "1 teaspoon"
    }, {
        "Name": "Flour",
        "Amount": "2 1/2 cups"
    }, {
        "Name": "Olive oil",
        "Amount": "1 teaspoon"
    }, {
        "Name": "Egg",
        "Amount": "1"
    }]
}]


def select_subcategory(category):
  for recipe in category:
    print(recipe["Name"])


user_input = input(
    "Which category do you want to load? (breads, cakes, barbeque, italian): ")
if user_input == "breads":
  selected_category = breads
  subcategory_input = input(
      "Which subcategory do you want to load for breads? (white bread, wheat bread) "
  )
  if subcategory_input == "white bread":
    select_subcategory(breads[0]["Ingredients"])
  elif subcategory_input == "wheat bread":
    select_subcategory(breads[1]["Ingredients"])
  else:
    print("Invalid subcategory")
elif user_input == "cakes":
  selected_category = cakes
  subcategory_input = input(
      "Which subcategory do you want to load for cakes? (chocolate cake, velvet cake) "
  )
  if subcategory_input == "chocolate cake":
    select_subcategory(cakes[0]["Ingredients"])
  elif subcategory_input == "velvet cake":
    select_subcategory(cakes[1]["Ingredients"])
  else:
    print("Invalid subcategory")
elif user_input == "barbeque":
  selected_category = barbeque
  subcategory_input = input(
      "Which subcategory do you want to load for barbeque? (barbeque sauce, pulled pork) "
  )
  if subcategory_input == "barbeque sauce":
    select_subcategory(barbeque[0]["Ingredients"])
  elif subcategory_input == "pulled pork":
    select_subcategory(barbeque[1]["Ingredients"])
  else:
    print("Invalid subcategory")
elif user_input == "italian":
  selected_subcategory = italian
  subcategory_input = input(
      "Which subcategory do you want to load for italian? (manicotti, calzone) "
  )
  if subcategory_input == "manicotti":
      select_subcategory(italian[0]["Ingredients"])
  elif subcategory_input == "calzone":
      select_subcategory(italian[1]["Ingredients"])
  else:
    print("Invalid subcategory")
else:
  print("Invalid category")
