


#ask for age
age = int(input('How old are you? : '))

if age != '':
    if age<=6:
        #is a child <=6
        print('Child discount')
    elif age >6 and age<11:
        #is a family >6 or <=11
        print('Family discount')
    elif age >11 and age<=13:
        #is a teen  >11 or <=13
        print('Teen discount')
    elif age >13 and age<=18:
        #is a mature >13 or <=18
        print('Mature discount')
    elif age >18 and age<=60:
        #is an adult >18 or >=60
        print('Mature discount')
    elif age >60:
        #is a senior < 60
        print('Senior discount')
else:
    print('a number is needed...')
