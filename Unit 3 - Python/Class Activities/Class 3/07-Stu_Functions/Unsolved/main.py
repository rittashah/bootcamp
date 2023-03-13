# @TODO: Write a function that returns the arithmetic average for a list of numbers


# Test your function with the following:
# print(average([1, 5, 9]))
# print(average(range(11)))
def ave(list):
    l=len(list)
    s=0
    for i in list:
        s=s+i
    return(s/l)

resul=ave([1,2,3,8,5])
print(resul)
# def calculate_average(lst):
#     sum_of_numbers = sum(lst)
#     length_of_list = len(lst)
#     average = sum_of_numbers / length_of_list
#     return average
# my_list = [1, 2, 3, 4, 5]
# result = calculate_average(my_list)
# print(result) 