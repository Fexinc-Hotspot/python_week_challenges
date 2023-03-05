#Write a program that accepts user input to create a list of integers. 
#Then, compute the sum of all the integers in the list.

print('----------------------------------------------')
print('A program to Display a list & sum of the list ')
print('----------------------------------------------')
input_string=input("Enter the list with different Element :")

#Convet each item into int datatype
user_list  = input_string.split()

#Calculation of Sum by using for loop
sum=0
for i in user_list:
    sum += int (i)
print('List :',user_list,'\n','Sum of the List= :',sum)