from googletrans import Translator

# @author 
#declaração da api de tradução do google
translator = Translator()

print('inicio tradução')
#faz a leitura de um arquivo e traduz a chave
#o arquivo traduzido aqui possui a seguinte estrutura: chave=valor
#apenas o valor será traduzido, a chave será mantid ano map
pathArquivoATraduzir = '/home/murah/Documentos/myOutFile2.txt'
with open(pathArquivoATraduzir, 'r') as fileTrad:
    arquivoTraduzido = {}
    contador = 0
    for line in fileTrad.readlines():
            texto = line.split('=')
            key = texto[0]
            try:    
                if len(texto) > 1:
                    label = texto[1]
                    #efetua a tradução da label
                    #dest - lingua para a qual deseja-se traduzir
                    #src - lingua atual da label
                    translated = translator.translate(label, dest='la', src='pt')
                    #insere no map a chave e o valor traduzido
                    arquivoTraduzido[key] = translated.text
                else:
                    #caso o valor seja vazio, insere a chave com o valor vazio
                    arquivoTraduzido[key] = ''

                contador = contador + 1
                print('traduzido ' + str(contador))    
            except Exception as e:
                #em caso de erro na tradução, ele inclui a chave com valor vazio e incrementa o contador
                arquivoTraduzido[key] = ''
                contador = contador + 1
                print('erro' + str(contador) + '|' + str(e))
            
    print('terminou tradução')

print('inicio escrita')
#gera um arquivo à partir do map de dados traduzidos
pathArquivoTraduzido = pathArquivoATraduzir + '_traduzido'
with open(pathArquivoTraduzido, "w") as outF:
    for item in arquivoTraduzido.items():
        outF.write(item[0]+ '=' + item[1])
        outF.write("\n")
    print('terminou escrita')