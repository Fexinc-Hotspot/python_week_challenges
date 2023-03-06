#A PROGRAM THAT USE LIST COMPREHENSION TO CREATE A LIST THAT CONTAIN ODD NUMBER OF CHARACTER

print('------------------------------------------------------------------------------------------------')
print('**A PROGRAM THAT USE LIST COMPREHENSION TO CREATE A LIST THAT CONTAIN ODD NUMBER OF CHARACTER**')
print('-------------------------------------------------------------------------------------------------')
print()
input_words=input('Enter a list of Worlds separeted by a comma  :')
word_list=input_words.split(',')

for word in word_list:

    print('The Word in a List is: :',word)

    print('The Odds of the Character is :',word[1::2])#Character of odd index
    