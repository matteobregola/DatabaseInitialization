
# -*- coding: utf-8 -*-

import csv




        

def ExtractWrite(filename="example.csv",queryfile="query.txt", tablename="table", indexes=[0,1]):
    '''
     for info see "1-directors.py"
    '''
    
    with open(queryfile, "w", encoding="utf-8") as txt_file:
        
        
        with open(filename, encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            txt_file.write("INSERT INTO directorawards(director,\"year\",award,\"result\")\nSELECT i.*\nFROM (VALUES\n")
            for row in csv_reader:
                if line_count == 0:
                    line_count+=1
                else:
                    if line_count == 1:
                        print(row)
                        #print(f'Column names are {", ".join(row)}')
                        txt_file.write('(')
                        
                        column=0
                        birth=""
                        for i in indexes:
                            if(column==0):
                                birth=row[10] #gettin year
                                column+=1
    
                            else:
                                director=row[15]
                                director=director.replace("'","''")
                                txt_file.write(f'\'{director}\',') #1 director
                                txt_file.write(f'{birth[0:4]},') #2 birth year
                                txt_file.write("'Oscar','nominated'::\"awardresult\"")
                                
                            
                        line_count += 1
                        txt_file.write(')')
                        
                    else :
                        txt_file.write(',\n(')
                        column=0
                        birth=""
                        for i in indexes:
                            if(column==0):
                                birth=row[10] #gettin year
                                column+=1
    
                            else:
                                director=row[15]
                                director=director.replace("'","''")
                                txt_file.write(f'\'{director}\',') #1 director
                                txt_file.write(f'{birth[0:4]},') #2 birth year
                                txt_file.write("'Oscar','nominated'::\"awardresult\"")
                                
                            
                        line_count += 1
                        txt_file.write(')')
            txt_file.write('')
            txt_file.write(")i(director,\"year\",award,\"result\") \n WHERE EXISTS(SELECT FROM directors d  \n WHERE (d.director)=(i.director) \n FOR SHARE);")  
    csv_file.close()
        
    txt_file.close()
    
    print("Operation sucessfull! You can find the result in: ", queryfile)
    
ExtractWrite(queryfile="3-directorsoscarNOMINATED.txt",tablename="directorawards",filename="directorsoscarswon.csv",indexes=[5,7])




