# Design of the API 

## Concept 

Recipe diary: save your favourite recipes and your tricks 

Properties: 
    name
    ingredients
    how-to
    fun fact (str)
    other
    macros (dict)
    date added 
    date modified 

## Functionalities 

CREATE NEW RECIPE
required: 
    name (str)
    ingredients (dict)

READ 
- read all recipes 
- get recipe by ID
- recipe of the day (random recipe) -- sweet or savoury 

UPDATE
- update: name, ingredients, how-to, other, fun fact, macro

## Database 

- generate data synthetically and import to relational database (mySQL)
https://chatgpt.com/share/69d28cd5-cfc8-8332-9e35-fc9446fe3917 

## Hosting 

... 