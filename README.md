# Database Initialization

Given the ~/DatabaseSchema.sql the file ~/Database_Init.sql initializes the database
with values from the data in the data folder.


## Usage

<u>**Run the query Database_Init.sql in the database or copy the content of Database_Init.txt in the query tool of the editor.**</u>


## Information about the data

All the data in the databse is collected from IMDB.
These data is stored in the data folder with the exception of the directors nominations 
and wins of Cannes Award. This info are collected directly from the cannes website
through a python script that uses bs4 and request module.
There is only one data that is randomized, namely the budget of the films.

(It has been added a final version with more data (see final_version))
