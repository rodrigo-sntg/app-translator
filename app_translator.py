from googletrans import Translator

# @author rodrigo-sntg
#declaring google Translator
translator = Translator()

print('starting translation')

#the translated file has the following structure: key=value
#only value is translated


pathFileToTranslate = '/home/murah/Documentos/myOutFile2.txt'
with open(pathFileToTranslate, 'r') as fileTrad:
    translatedFile = {}
    counter = 0
    for line in fileTrad.readlines():
            text = line.split('=')
            key = text[0]
            try:    
                if len(text) > 1:
                    label = text[1]
                    #translate the label
                    #dest - destination language
                    #src - language on the file
                    translated = translator.translate(label, dest='la', src='pt')
                    #put the translated value in a map
                    translatedFile[key] = translated.text
                else:
                    #in case of empty value, insert empt string ''
                    translatedFile[key] = ''

                counter = counter + 1
                print(str(counter) + ' - translated')
            except Exception as e:
                #in case of error, increment the counter and insert the key with empty value
                translatedFile[key] = ''
                counter = counter + 1
                print('error' + str(counter) + '|' + str(e))
            
    print('End of translation')

print('Starting file writing')
#creates a file from the map values
pathtranslatedFile = pathFileToTranslate + '_translated.txt'
with open(pathtranslatedFile, "w") as outF:
    for item in translatedFile.items():
        outF.write(item[0]+ '=' + item[1])
        outF.write("\n")
    print('end of writing')