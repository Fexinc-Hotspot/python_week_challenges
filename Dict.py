
person={}
  
for i in range(1):
    print('-----------------------------------')
    print('The Progam to Store Values in Dict ')
    print('-----------------------------------')
    name=input('Enter the person name :')
    person['Name']=name
    age=int(input('Enter a person age :'))
    person['Age']=age
    color=input('Enter person favorite color :')
    person['Color']=color
  
print(person)
