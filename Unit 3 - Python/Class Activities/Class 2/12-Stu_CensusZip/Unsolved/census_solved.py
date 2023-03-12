import csv
filepathr=r'Unit 3 - Python/Class Activities/Class 2/12-Stu_CensusZip/Resources/census_starter.csv'
filepathw=r'Unit 3 - Python/Class Activities/Class 2/12-Stu_CensusZip/Resources/result.csv'
place=[]
population=[]
income=[]
pcount=[]
with open(filepathr,'r') as csvfile:
    myfile=csv.reader(csvfile,delimiter=",")
    for row in myfile:
        place.append(row[0])
        population.append(row[1])
        income.append(row[4])
        pcount.append(row[5])    

final=zip(place,population,income,pcount)
with open (filepathw,'w',newline='') as ff:
    newl=csv.writer(ff,delimiter=",")
    newl.writerow(["place","population","income","povertycount"]) 
    newl.writerows(final)  



