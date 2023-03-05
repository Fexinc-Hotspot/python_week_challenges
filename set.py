print('-----------------------------------')
print(' A PROGRAM TO STORE VALUES INTO SET')
print('-----------------------------------')
x = input('Enter two different fruits or more  with a comma : ')

x = {a for a in x.split(",")}
print(x)
