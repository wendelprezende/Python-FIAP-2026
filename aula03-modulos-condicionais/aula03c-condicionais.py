# -------------------------
# ESTRUTURA CONDICIONAL SIMPLES
# -------------------------

nota = 5.0

if nota < 6:
    print(f'A sua nota é: {nota}')

print('FIM')

# -------------------------
# ESTRUTURA CONDICIONAL COMPOSTA
# -------------------------

nota_final = 5.9
if nota_final < 6:
    print('Reprovado')
else:
    print('Aprovado')

print('FIM')

# -------------------------
# ESTRUTURA CONDICIONAL ENCADEADA
# -------------------------

nota_final = 5.9
if nota_final < 4:
    print('Reprovado')
else:
    if nota_final < 6:
        print('Recuperação')
    else:
        print('Aprovado')

print('FIM')

# -------------------------
# ESTRUTURA CONDICIONAL ENCADEADA
# -------------------------

nota_final = 5.9
if nota_final < 4:
    print('Reprovado')
elif nota_final < 6:
    print('Recuperação')
else:
    print('Aprovado')

print('FIM')