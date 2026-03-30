# LÓGICA E (and)
# EMAIL     SENHA       LOGIN
# True      True         True
# True     False       True
# EMAIL     SENHA       LOGIN
# EMAIL     SENHA       LOGIN

verifica_email = True
verifica_senha = True

verifica_login = verifica_email and verifica_senha
print(verifica_login)

if verifica_login:
    print('Entra no programa')

# LÓGICA OU (or)

logica_ou = False or True
print(logica_ou)

# OPERADOR DE NEGAÇÃO

negacao = not False
print(negacao)

if not verifica_login:
    print('Loga certo aí...')
    