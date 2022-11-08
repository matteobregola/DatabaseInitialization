import csv


def ExtractWrite(filename,queryfile, tablename, indexes):
    '''
     for info see "1-directors.py"
    '''
    with open(queryfile, "w", encoding="utf-8") as txt_file:
        
        
        with open(filename, encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            txt_file.write("INSERT INTO movieawards(title,\"year\",award,\"result\")\nSELECT i.*\nFROM (VALUES\n")
            for row in csv_reader:
                if line_count == 0:
                    line_count+=1
                else:
                    if line_count == 1:
                        print(row)
                        #print(f'Column names are {", ".join(row)}')
                        txt_file.write('(')
                        
                        column=0
                        year=""
                        for i in indexes:
                            if(column==0):
                                year=row[10] #gettin year
                                column+=1
    
                            else:
                                title=row[5]
                                title=title.replace("'","''")
                                txt_file.write(f'\'{title}\',') #1 director
                                txt_file.write(f'{year[0:4]},') #2 birth year
                                txt_file.write("'Oscar, best cinematography','nominated'::\"awardresult\"")
                                
                            
                        line_count += 1
                        txt_file.write(')')
                        
                    else :
                        txt_file.write(',\n(')
                        column=0
                        year=""
                        for i in indexes:
                            if(column==0):
                                year=row[10] #gettin year
                                column+=1
    
                            else:
                                title=row[5]
                                title=title.replace("'","''")
                                txt_file.write(f'\'{title}\',') #1 director
                                txt_file.write(f'{year[0:4]},') #2 birth year
                                txt_file.write("'Oscar, best cinematography','nominated'::\"awardresult\"")
                                
                            
                        line_count += 1
                        txt_file.write(')')
            txt_file.write('')
            txt_file.write(")i(title,\"year\",award,\"result\") \n WHERE EXISTS(SELECT FROM movies m  \n WHERE (m.title)=(i.title) AND (m.year)=(i.year)  \n FOR SHARE\N  ON CONFLICT DO NOTHING);")  
    csv_file.close()
        
    txt_file.close()
    
    print("Operation sucessfull! You can find the result in: ", queryfile)
    
    
    
ExtractWrite(queryfile="4-movieawardsOscarBestcinematographyNominated.txt",tablename="movieawards",filename="bestcinematographyNominated.csv",indexes=[5,7])




