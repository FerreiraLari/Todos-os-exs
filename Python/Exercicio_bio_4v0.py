import re
import unidecode
from opencage.geocoder import OpenCageGeocode

class ocorrencias:
    
    def __init__(self, path):
        self.path = path
       
    #abre o arquivo e carrega os dados
    def openFile(self):
              
        with open(self.path) as file:
            content = file.read()
            self.data = [[item for item in linha.split(';')] for linha in content.split('\n')]
            return self.data
    
    def checkInformation(self):
## Transformando as variáveis lat e lon para o formato float para usar a função reverse
        locationValidated = 0
        locationUnvalidated = 0
        stateValidated = 0
        for line in self.data[1:]:    
            if(line[29][:1] == '-'):
                latitude = float(line[29][1:])
                latitude = latitude * -1
            else:
                latitude = float(line[29])

            if(line[30][:1] == '-'):
                longitude = float(line[30][1:])
                longitude = longitude * -1
            else:
                longitude = float(line[30])
## Usando a função reverse que trás as infos de localização através da lat e lon
            key = '01257e357ab4413d88d7b75fb715ec78'
            ##'8168293af4ed4813a30652e99d1d9013'
            geocoder = OpenCageGeocode(key) 
            result = geocoder.reverse_geocode(latitude, longitude)
            print(result)
## Comparando os resultados trazidos pela reverse com os já presentes na base 
            if 'state_code' in result[0]['components']:
                if(unidecode.unidecode(result[0]['components']['state_code'].lower()) == unidecode.unidecode(line[26].lower())):
                    stateValidated += 1 # se o estado na base e no resultado da função reverse corresponderem soma-se 1 nesta variável
                    if 'city' in result[0]['components']:
                        if (unidecode.unidecode(result[0]['components']['city'].lower()) == unidecode.unidecode(line[27].lower())):
                            locationValidated += 1
                        else:
                            locationUnvalidated += 1
                    elif 'city_district' in result[0]['components']:
                        if(unidecode.unidecode(result[0]['components']['city_district'].lower()) == unidecode.unidecode(line[27].lower())):
                            locationValidated += 1
                        else:
                            locationUnvalidated += 1
                    else:
                        locationUnvalidated += 1
                else:
                    locationUnvalidated += 1
            else:
                locationUnvalidated += 1
#Para a variável locationValidated soma-se 1 apenas se a cidade e o estado da base e do resultado da função corresponderem
        print('Registros Validados com Estado:',stateValidated,'do total de',len(inst1.openFile()[1:]))
        print('Registros Validados com Estado e Cidade:',locationValidated,'do total de',len(inst1.openFile()[1:]))


#instanscias de teste
inst1 = ocorrencias('/home/logcomex/Todos-os-exs/Python/bio_borboleta.csv')
inst1.openFile()
inst1.checkInformation()