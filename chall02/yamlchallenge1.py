#!/usr/bin/env python3                                                              

import yaml 
import crayons #import crayons package

def main():                                                                         
    with open("farms.yaml", "r") as farmlife:                                       
        farms = yaml.safe_load(farmlife)                                            
        print(farms)                                                                
    #starts a counter to count number of farms                                      
    counter = 0                                                                     
                                                                                    
    # farm will be equal to one of the dict within the list "farms"                 
    for farm in farms:                                                             
        #print name of the farms in bold yellow                                    
        print(crayons.yellow(farm.get('name') + " which is raising: ", bold=True))  
        # from a single "farm" get the list from the key "agriculture"              
        for agri in farm.get('agriculture'):                                       
            #print agriculture in bold blue                                         
            print(crayons.blue(" - "+ agri, bold=True))                             
        #counter increases by 1 until loop is over                                  
        counter = counter + 1                                                       
    #prints number of farms Old Mac has                                            
    print(crayons.green(f"Old Mac has {counter} farms, ee i ee i o", bold=True))   
                                                                                    
main()

