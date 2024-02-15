import json

chocolate_cake = {
  "name": "Chocolate Cake",
  "ingredients": [
    {
      "name": "flour",
      "amount": "2 cups"
    }, {
      "name": "sugar",
      "amount": "1 cup"
    }, {
      "name": "cocoa powder",
      "amount": "1 cup"
    }, {
      "name": "baking powder",
      "amount": "1 teaspoon"
    }, {
      "name": "eggs",
      "amount": "2 eggs"
    }, {
      "name": "milk",
      "amount": "1 cup"
    }, {
      "name": "oil",
      "amount": "1 cup"
    }, {
      "name": "vanilla extract",
      "amount": "1 teaspoon"
    }
  ]
}

with open("chocolate_cake.json", "w") as f:
  json.dump(chocolate_cake, f, indent=2)

with open("chocolate_cake.json") as f:
  chocolate_cake = json.load(f)
print(chocolate_cake)