# Condição se a pessoa tiver menor de 18 anos, ela nao no sistema.
Idade = 20

if Idade >= 18:
  print('você é maior de idade!')

# Condição IF + ELSE

Idade = int( 15 )

if Idade >= 18:
  print('Você é de maior!')

else:
  print('Você é menor de Idade!!! gugudada')


# Condição IF + ELSE + ELIF

Idade = int( 14 )

if Idade > 18:
  print('Você é de maior!')

elif Idade == 18:
  print('Opa! Welcome the jungle!!! ')

elif Idade < 18 and Idade >= 14:

  if Idade % 2 == 0:
    print('Quase um adulto!!! Aproveita !!!!!!!!!!')

else:
  print('Você é menor de Idade!!! gugudada')
