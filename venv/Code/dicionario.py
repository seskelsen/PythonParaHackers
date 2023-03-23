#construindo e trabalhando com dicionários
dict = {'nome': 'João', 'idade': 25, 'sexo': 'M', 'cursos': ['Python', 'Java']}

print(dict)
print("Nome: %s\nIdade: %d" % (dict['nome'], dict['idade']))

print("Chaves: %s" % dict.keys())
print("Valores: %s" % dict.values())


# a dictionary is a data structure that stores data in an associative way, that is, by key / value pairs

dict = {'nome': 'João', 'idade': 25, 'sexo': 'M', 'cursos': ['Python', 'Java']}

# printing the dictionary
print(dict)

# printing the dictionary's keys
print("Chaves: %s" % dict.keys())

# printing the dictionary's values
print("Valores: %s" % dict.values())

# printing the dictionary's values using a for loop
for key in dict.keys():
    print(key)

# printing the dictionary's values using a for loop
for value in dict.values():
    print(value)

# printing the dictionary's values using a for loop
for key, value in dict.items():
    print(key, value)

# adding a new key / value pair
dict['signo'] = 'Leão'

# printing the dictionary after adding the new key / value pair
print(dict)

# removing a key / value pair
del dict['signo']

# printing the dictionary after removing the new key / value pair
print(dict)


print(dict['nome'])