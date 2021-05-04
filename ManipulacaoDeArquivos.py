# -*- coding: utf-8 -*-
# função open
#variavel = open (nome, modo)

""" 
abrir arquivo: funcao open 
lendo arquivos: 
função read() - Lê arquivo inteiro 
função readline() - Lê uma linha 
funcao readlines () - Lê arquivo e o armazena em uma lista 
    r: somente leitura 
    w: escrita(caso o arquivo já exista, ele será apagado e um novo arquivo vazio será criado)
    a: leitura e escrita (adiciona o novo conteúdo ao fim do arquivo)
    r+: leitura e escrita 
    w+ escrita(o modo w+, assim como o w, também apaga o conteúdo anterior do arquivo)
    a+ leitura e escrita (abre o arquivo para atualização)
"""
# arquivo
arquivo = open("arquivo.txt")

# ler  ar quivo por linhas
linhas = arquivo.readlines()
print(linhas)
for linha in linhas:
    print(linha)
texto_completo = arquivo.read()

print(texto_completo)

lista = arquivo.readlines()

print(lista)

# criar arquivos
w = open("arquivo2.txt", "a")

w.write("Esse é o meu arquivo\n")
# fecha arquivo, todo vez que se abre um arquivo é importante fechar
w.close()
