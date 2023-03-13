
import os
import csv

# Path to collect data from the Resources folder

# Define the function and have it accept the 'state_data' as its sole parameter
def print_percentage(state_data):
    
    headerrow=next(state_data) 
    l= len(list(state_data))
    s=0
    ss=0
    sss=0 
    for row in state_data:
        s=s+float(row[2])
        ss=ss+float(row[4])
        sss=sss+float(row[6])
            
    
    GRP=s/l
    GRR=ss/l
    GRN=sss/l
    print(GRP)
    print(GRR)
    print(GRN)
    return([s,ss,sss])

graduation_path = r"Class Activities/Class 3/08-Par_GraduatingFunctions/Resources/graduation_data.csv"
with open(graduation_path,'r') as ff:
        mydata=csv.reader(ff,delimiter=",")
        print_percentage(mydata)
        # print(f"{s}% and {ss}% and {sss}%")