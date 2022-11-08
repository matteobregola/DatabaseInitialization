# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


minyear=1946
maxyear=2022
year=1946


queryfile="3-directorscannesNOMINATED.txt"

with open(queryfile, "w", encoding="utf-8") as txt_file:
    txt_file.write("INSERT INTO directorawards(director,\"year\",award,\"result\")\nSELECT i.*\nFROM (VALUES\n")
    
    while year <= maxyear:
        url=f"https://www.festival-cannes.com/en/75-editions/retrospective/{year}/selection/competition-1"
        r = requests.get(url)
        soup=BeautifulSoup(r.text, 'html.parser')
        
        for k in soup.find_all('div',{'class':'item block-poster'}):
            directortag=k.find(class_="title-12")
            if(directortag!=None):
                director=(directortag.getText())
                director=director.strip()
                director=director.replace("\n"," ")
                director=director.replace("\t"," ")
                director=director.title()
                print(director)
            
            if(year == 1946):
                txt_file.write(f"('{director}',{year},'Cannes','nominated'::\"awardresult\")")
            else:
                 txt_file.write(f",\n('{director}',{year},'Cannes','nominated'::\"awardresult\")")
            year+=1
    
    txt_file.write(")i(director,\"year\",award,\"result\") \n WHERE EXISTS(SELECT FROM directors d  \n WHERE (d.director)=(i.director) \n FOR SHARE);") 
    
    
    txt_file.close()
    print("Operation sucessfull! You can find the result in: ", queryfile)