from pandas import Series, DataFrame
from numpy import nan as NA
import pandas as pd


data = pd.read_csv('leads_empresa1.csv')    #Importando os dados .CSV


frame = DataFrame(data)                     # Criando DataFrame para alimentar a tabela.



#Retirando colunas que não serão usadas no aprendizado de máquina e criando o DataFrame do ML.
mlFrame = frame.drop(['Email', 'Nome', 'Celular', 'Facebook', 'Twitter', 'Linkedin', 'Site/Blog', 'Telefone', 'Empresa',
                      'Dono do Lead', 'URL pública', 'Área de atuação', 'Comentário Site', 'Data de atualização',
                      'Descrição empresa', 'Função', 'interno - Quantidade de usuários','nomeEmpresa', 'Ramo de atividade',
                      'tributação', 'Cargo', 'UF', 'Cidade', 'Quantidade de Pessoas', 'Data da última conversão', 'Data da primeira conversão'], axis=1)


# Retirando linhas com dados nulos.
mlFrame = mlFrame.dropna()

# print(mlFrame.columns)
mlFrame.columns = ['Classe', 'Tags', 'LeadScoring', 'Interesse', 'Conversoes', 'Origem_Primeira_Conversao', 'Origem_Ultima_Conversao', 'Eventos']

# Quantidade de Clientes e Não Clientes
#print(mlFrame.groupby('Estágio no funil').size())

# print(mlFrame.columns)

format = lambda x: x.split('/')
#
mlFrame['Eventos'] = mlFrame['Eventos'].map(format)

print(mlFrame.groupby)