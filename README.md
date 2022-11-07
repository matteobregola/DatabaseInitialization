# Database Initialization

Given the ~/DatabaseSchema.sql the file ~/Database_Init.sql initializes the database
with values from the data in the data folder.


## Usage

Run the query in the database or copy the content of Database_Init.txt in the query tool
of the editor.


## Information about the data

All the data in the databse is collected from IMDB.
These data is stored in the data folder with the exception of the directors nominations 
and wins of Cannes Award. This info are collected directly from the cannes website
through a python script that uses bs4 and request module.


