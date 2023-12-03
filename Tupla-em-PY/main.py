tupla =('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')

num = int(input('Digite um número inteiro entre 0 e 20: '))

while(num < 0 or num > 20):
  print('Tente novamente. ', end='')
  num = int(input('Digite um número inteiro entre 0 e 20: '))

print(tupla[num])
  
