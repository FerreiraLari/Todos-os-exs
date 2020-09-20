class ocorrencias:
    
    def __init__(self, path):
        self.path = path
       
    #abre o arquivo e carrega os dados
    def openFile(self):
              
        with open(self.path) as file:
            content = file.read()
            self.data = [[item for item in linha.split(';')] for linha in content.split('\n')]
            return self.data
    
    def meandf(self):
        ncol = len(self.data[0])
        nsinfo = 0
        for linha in self.data:
            for celula in linha:
## A condição abaixo conta cada célula preenchida com "Sem informações"
                if (celula == "Sem Informações"):
                    nsinfo += 1  ## Número de células sem informações
## Para obter a média basta dividir o número de células sem info pelo número de colunas
        print("A média de dados faltantes por coluna é:", nsinfo/ncol)

#instanscias de teste
inst1 = ocorrencias('/home/logcomex/Todos-os-exs/Python/bio_capivara.csv')
inst1.openFile()
inst1.meandf()

