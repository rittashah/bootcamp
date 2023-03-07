
city = 'Toronto'

# myCity = []

# for letter in city: 
#     upper_letter = letter.upper()
#     if upper_letter == 'O':
#       myCity.append(upper_letter)

myCity = [letter.upper() for letter in city if letter.upper() == 'O']

print(myCity)