# @TODO: Write a function that returns the arithmetic average for a list of numbers


# Test your function with the following:
# print(average([1, 5, 9]))
# print(average(range(11)))

def average(someList):
    
    sum = 0
    count = len(someList)
    
    for item in someList: 
        #sum = sum + item 
        sum += item
    
    avg = sum / count 
    return avg, sum, count


print(average([19, 20, 21, 22, 23]))