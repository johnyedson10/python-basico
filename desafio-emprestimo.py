"""
Desafio de Emprestimo calculando
Usando python com condicionais e variaveis
"""

"""
emprestimo de 1000
cliente vip1 = juros de 14% ( sem garantias cliente já foi negativado 3 vez em 5 anos )
cliente vip2 = juros de 7%  ( sem garantias cliente somente atrasa )
cliente vip3 = juros de 3%  ( com garantia cliente só paga adiantado )
"""

"""
j = cit/100
"""

vip1 = 14
vip2 = 7
vip3 = 3
capital = 1000
resultado  = capital * vip1 / 100 + 1000
resultado2 = capital * vip2 / 100 + 1000      
resultado3 = capital * vip3 / 100 + 1000

input("Digite a taxa:")

if(vip1) == 14 :
  print("O valor do empréstimo do cliente vip1 é:", resultado)
if(vip2) == 7 :
  print("O valor do empréstimo do cliente vip2 é:", resultado2)
if(vip3) == 3 : 
  print("O valor do empréstimo do cliente vip3 é:", resultado3)

  
  
