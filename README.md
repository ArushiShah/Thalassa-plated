# Thalassa-plated
github repo : https://github.com/ArushiShah/Thalassa-plated.git
The requirements.txt contains all the dependencies necessary for running the application.

To run, clone the repo and run $ python app.py

I have used Postman to update/delete/manage the recipes and menus. 
https://www.getpostman.com

The app is deployed at https://obscure-wave-61033.herokuapp.com/ 

Instructions to use postman:

1. Download https://www.getpostman.com
2. Set headers :
    key : Authorization
    Value : Token token="{MyToken}"
3. For POST request -> body -> JSON(application/json)
    Insert the paramters in body eg: for posting a new recipe to a menu
    select POST -> set url to https://plated-coding-challenge.herokuapp.com/v1/menus/334/recipes.json
    set header
    body -> JSON(application/json)
    write in body :{
  "recipe_id": "{recipe_id}"
  }
  
