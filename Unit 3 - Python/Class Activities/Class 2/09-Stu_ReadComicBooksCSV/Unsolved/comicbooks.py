import csv 

path=("Unit 3 - Python/Class Activities/Class 2/09-Stu_ReadComicBooksCSV/Resources/comic_books.csv")

with open(path,encoding='utf-8') as tempo:
  mydata=csv.reader(tempo, delimiter= ',')
  yy=True
  while yy==True:
    book=input("which book are you looking fo? ")
    for row in mydata:
        if row[0]==book:
            print(f"{row[0]} is published by {row[8]} in {row[9]}")
            break if 
    yy= False
        else:
            print("book could not be found")
            break if
    yy= True
