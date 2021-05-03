#função open 
#variavel = open (nome, modo)

""" 
    r: somente leitura 
    w: escrita(caso o arquivo já exista, ele será apagado e um novo arquivo vazio será criado)
    a: leitura e escrita (adiciona o novo conteúdo ao fim do arquivo)
    r+: leitura e escrita 
    w+ escrita(o modo w+, assim como o w, também apaga o conteúdo anterior do arquivo)
    a+ leitura e escrita (abre o arquivo para atualização)
"""
arquivo = open ("arquivo.txt")

linhas = arquivo.readlines()

for linha in linhas:
    print(linha)