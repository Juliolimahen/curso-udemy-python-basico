# Nas listas e tuplas acessamos os dados por meio dos índices. Já nos dicionários, o acesso aos dados é feito por meio da chave associada a eles. 
# Para adicionar elementos num dicionário basta associar uma nova chave ao objeto e dar um valor a ser associado a ela.

meu_dicionario = {"A": "AMEIXA", "B": "BOLA", "C": "CACHORO"}
#imprimindo indice dicionario 
print(meu_dicionario["C"])
#imprimindo dicionario 
print(meu_dicionario)
#imprimindo indice dicionario
for chave in meu_dicionario: 
    print(chave+"-"+meu_dicionario[chave])
#funções 
#converte um tupla
for i in meu_dicionario.items():
    print(i)
#retorna só valores
for i in meu_dicionario.values():
    print(i)
#retorna só chave
for i in meu_dicionario.keys():
    print(i)
