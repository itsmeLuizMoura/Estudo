n = input('Digite algo: ')
print('Seu tipo primitivo é: ' , type(n))
print('Só tem espaço?: ' , n.isspace())
print('É um numero?: ' , n.isnumeric())
print('É alfabetico? ' , n.isalpha())
print('É alfanumerico? ' , n.isalnum())
print('Está em maiusculas? ' , n.isupper())
print('Está em minusculas? ' , n.islower())
print('Está em capitalisada? ' , n.istitle())