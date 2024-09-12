my_dict={'Anastasiia':2002,'Valentina':2003}
print(my_dict)
print(my_dict['Anastasiia'])
print(my_dict.get('Anton'))
my_dict.update({'Vova':2000,'Max':2010})
print(my_dict)
a = my_dict.pop('Max')
print(my_dict)
print(a)
print(my_dict)

my_set={'Anastasiia',2002,'Valentina',2003,'Vova',2000,'Max',2000,'Anastasiia',2002,'Valentina'}
print(my_set)
a = my_set.add('love')
a = my_set.add('Anton')
a = my_set.discard('Max')
print(my_set)





