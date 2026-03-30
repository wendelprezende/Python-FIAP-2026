idade = int(input('Insira a sua idade: '))

if idade >= 16 and idade < 18 or idade > 70:
    print('Seu voto é opcional')
elif idade < 16:
    print('Você ainda não pode votar')
else: 
    print('Seu voto é obrigatório')