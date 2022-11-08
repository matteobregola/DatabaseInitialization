# -*- coding: utf-8 -*-
import csv
import random
       
def ExtractWrite(filename="example.csv",queryfile="query.txt", tablename="table", indexes=[0,1]):
    '''
    for info see "1-directors.py"
    '''
    
    with open(queryfile, "w") as txt_file:
        
        txt_file.write(f'INSERT INTO {tablename} VALUES\n')
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
        
            for row in csv_reader:
                
                
                if line_count == 0:
                    line_count+=1
                
            
                else :
                    if line_count == 1:
                        #print(f'Column names are {", ".join(row)}')
                        txt_file.write('(')
                        
                        column=0
                        director=""
                        for i in indexes:
                            print(i,row[i])
                            if(i==1):
                                title=row[i]
                                title=title.replace("'","''")
                                txt_file.write(f'\'{title}\',') #title
                                
                                
                            else:
                                if(i==4):
                                    director=row[4] #director
                                   
                            
                                else:
                                    if(i==6):
                                        txt_file.write(row[6]+",") # year
                                        director=director.replace("'","''")
                                        txt_file.write("'"+director+"',") #director
                                        
                                        
    
                                    else:
                                        if(i==10):
                                            txt_file.write(str(random.randrange(1000000,1000000000, 5000000)))
                                            #budget (not real value)
                                            gross=str(round(float(row[i])*1000000))
                                            txt_file.write(f',{gross}')#gross
                                            
                            column+=1
                            
                            
                        line_count += 1
                        txt_file.write(')')
                        
                    else :
                        txt_file.write(',\n(')
                        column=0
                        director=""
                        for i in indexes:
                            if(i==1):
                                title=row[1]
                                title=title.replace("'","''")
                                txt_file.write(f'\'{title}\',') #title
                                column+=1
                                
                            else:
                                if(i==4):
                                    director=row[4] #director
                                    
                            
                                else:
                                    if(i==6):
                                        txt_file.write(row[6]+",") # year
                                        director=director.replace("'","''")
                                        txt_file.write("'"+director+"',") #director
                                        
                                        
    
                                    else:
                                        if(i==10):
                                            txt_file.write(str(random.randrange(1000000,1000000000, 5000000)))
                                            #budget (not real value)
                                            gross=str(round(float(row[i])*1000000))
                                            txt_file.write(f',{gross}')#gross
                                            
                            column+=1
                            
                        txt_file.write(')')
            txt_file.write(';')
          
            
        csv_file.close()
        
    txt_file.close()
    
    print("Operation sucessfull! You can find the result in: ", queryfile)
    


ExtractWrite(queryfile="querymovies.txt",tablename="movies",filename="top1000movies.csv",indexes=[1,4,6,10])
