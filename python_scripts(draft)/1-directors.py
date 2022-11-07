# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 08:37:13 2022

@author: matte
"""

import csv




        

def ExtractWrite(filename="example.csv",queryfile="query.txt", tablename="table", indexes=[0,1]):
    '''
       queryfile is where i want to store the query   
       filename is the csv with the data
       tablename is the name of the table i want to create
       indexes are the column of the csv file that i want to include
       in the query
       QUERY FORMAT:
            INSERT INTO tablename, VALUES 
            (data,data,data,...),
            (data,data,data,...),
            ...
            (data,data,data,...);
    '''
    
    with open(queryfile, "w", encoding="utf-8") as txt_file:
        
        txt_file.write(f'INSERT INTO {tablename} VALUES\n')
        with open(filename, encoding="utf-8") as csv_file:
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
                        for i in indexes:
                            if(column==0):
                                director=row[5]
                                director=director.replace("'","''")
                                txt_file.write(f'\'{director}\',')
                                column+=1

                            else:
                                birth=row[7]
                                if(birth=="" ):
                                    birth="1900"
                                txt_file.write(f'{birth[0:4]}')
                            
                        line_count += 1
                        txt_file.write(')')
                        
                    else :
                        txt_file.write(',\n(')
                        column=0
                        for i in indexes:
                            if(column==0):
                                director=row[5]
                                director=director.replace("'","''")
                                txt_file.write(f'\'{director}\',')
                                column+=1
                            else:
                                birth=row[7]
                                if(birth=="" ):
                                    birth="1900"
                                txt_file.write(f'{birth[0:4]}')
                            
                                
                        txt_file.write(')')
            txt_file.write(';')
          
            
        csv_file.close()
        
    txt_file.close()
    
    print("Operation sucessfull! You can find the result in: ", queryfile)
    
ExtractWrite(queryfile="querydirectors2.txt",tablename="directors",filename="top1000directors.csv",indexes=[5,7])







'''



def Extract(filename, tablename, indexes):
    #insert into "tablename" values...
    print(f'\t INSERT INTO {tablename} VALUES')    
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
    
        for row in csv_reader:
            
            if line_count == 1:
                #print(f'Column names are {", ".join(row)}')
                print('\n(',end='')
                for i in indexes:
                    print(f'{row[i]}', end='' )
                line_count += 1
                print('),')
        
            else :
                print(', \n(',end='')
                for i in indexes:
                    print(f'{row[i]}', end='' )
                    if(i!=indexes[-1]):
                        print(',', end='')
                print('),')
                line_count += 1
        print(';')
'''