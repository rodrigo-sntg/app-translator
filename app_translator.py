from googletrans import Translator

# @author rodrigo-sntg
#declaring google Translator
translator = Translator()

print('starting translation')

#the translated file has the following structure: key=value
#only value is translated


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
                    #translate the label
                    #dest - destination language
                    #src - language on the file
                    translated = translator.translate(label, dest='la', src='pt')
                    #put the translated value in a map
                    arquivoTraduzido[key] = translated.text
                else:
                    #in case of empty value, insert empt string ''
                    arquivoTraduzido[key] = ''

                contador = contador + 1
                print(str(contador) + ' - translated')
            except Exception as e:
                #in case of error, increment the counter and insert the key with empty value
                arquivoTraduzido[key] = ''
                contador = contador + 1
                print('error' + str(contador) + '|' + str(e))
            
    print('End of translation')

print('Starting file writing')
#gera um arquivo à partir do map de dados traduzidos
pathArquivoTraduzido = pathArquivoATraduzir + '_translated.txt'
with open(pathArquivoTraduzido, "w") as outF:
    for item in arquivoTraduzido.items():
        outF.write(item[0]+ '=' + item[1])
        outF.write("\n")
    print('end of writing')