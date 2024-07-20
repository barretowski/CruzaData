from cruzaData import CruzaData

# Carregar o arquivo CSV a partir do caminho local
csv_path = r'C:\\Projetos\\CruzaData\\Util\\Arquivos\\csv_utf8.csv'

# Instanciar o DataAnalyzer
analise = CruzaData(csv_path)

# Verificar os nomes das colunas
print("Colunas no DataFrame:", analise.df.columns)

# Realizar análises
# analise.cruzamento_genero_x_idade()
# analise.cruzamento_cargo_x_escolaridade()
# analise.analyze_avg_service_time()
# analise.cruzamento_estilo_lideranca_x_idade()

analise.cruzamento_estilo_lideranca_x_motivacao_equipe() # MOTIVAÇÃO EQUIPE
analise.cruzamento_estilo_lideranca_x_desenvolvimento_profissional() # VALORIZAÇÃO DO SEU DESENVOLVIMENTO
analise.cruzamento_estilo_lideranca_x_satisfacao_trabalho() #VALORIZA CONTRIBUIÇÃO PARA EQUIPE

analise.cruzamento_estilo_lideranca_x_feedback() #LIDERANÇA X FEEDBACK
analise.cruzamento_estilo_lideranca_x_motivacao_pessoal() #LIDERANÇA X MOTIVACAO PESSOAL
analise.cruzamento_estilo_lideranca_x_comunicacao_metas()#LIDERANÇA X COMUNICAÇÃO METAS
analise.cruzamento_estilo_lideranca_x_empatia_compreensao()#LIDERANÇA X EMPATIA COMPREENSAO
analise.cruzamento_estilo_lideranca_x_autonomia_tomada_decisoes()#LIDERANÇA X EMPATIA COMPREENSAO