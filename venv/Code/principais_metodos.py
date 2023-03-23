frase = "Python é uma linguagem de programação muito legal - 2023"

#print(frase.count('a'))
'''
import base64

encrypt = base64.b64encode(frase.encode('utf-8'))
decrypt = base64.b64decode(encrypt).decode('utf-8')

print(encrypt)
print(decrypt)
'''
'''
print(frase.find('linguagem'))
print(frase.replace('Python', 'C++'))
print(frase.rfind('linguagem'))
'''
#print(frase.index('linguagem'))

#print("sigmar".join(frase))
'''
print(frase.upper() + "\n" + 
      frase.lower() + "\n" + 
      frase.capitalize() + "\n" + 
      frase.title() + "\n" + 
      frase.swapcase() + "\n" + 
      frase.casefold() + "\n" + 
      frase.strip() + "\n" + 
      frase.rstrip() + "\n" + 
      frase.lstrip())
'''
#print(frase.replace('Python', 'C++'))
print(frase.split("-"))