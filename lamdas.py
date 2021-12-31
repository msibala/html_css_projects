# def square(num):
#     x = num ** 2
#     return x

# square(3)
# print(square(3))

#map passes an anonymous function
# def map(list, function):
#     for i in range(len(list)):
#         list[i] = function(list[i])
#     return list

# print (map([1,2,3,4], (lambda num: num*num) ))
# print (map([1,2,3,4], (lambda num: num*3) ))
# print(map([1,2,3,4], (lambda num: num%2) ))


#create a list
# my_arr = [1,2,3,4,5]
# #define a function that squares values
# def square(num):
#     return num**2
# #invoke map function
# print(list(map(square, my_arr)))


my_arr = [1,2,3,4,5]
print(list(map(lambda x: x**2, my_arr)))