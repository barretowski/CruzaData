from cruzaData import CruzaData

# Carregar o arquivo CSV a partir do caminho local
csv_path = r'C:\\Projetos\\CruzaData\\Util\\Arquivos\\csv_utf8.csv'

# Instanciar o DataAnalyzer
modulo_analise = CruzaData(csv_path)

# Verificar os nomes das colunas
print("Colunas no DataFrame:", modulo_analise.df.columns)

# Realizar análises usando o método genérico
modulo_analise.executar_analise_cruzada(
    ['Gênero', 'Idade'],
    r'C:\\Projetos\\CruzaData\\Util\\Arquivos\\Relatorios\\cruzamento_genero_x_idade.xlsx'
)

modulo_analise.executar_analise_cruzada(
    ['Escolaridade', 'Qual é o seu cargo atual na empresa?'],
    r'C:\\Projetos\\CruzaData\\Util\\Arquivos\\Relatorios\\cruzamento_cargo_x_escolaridade.xlsx'
)

modulo_analise.executar_analise_cruzada(
    ['Idade', 'Como você descreveria o estilo de liderança do seu superior direto?'],
    r'C:\\Projetos\\CruzaData\\Util\\Arquivos\\Relatorios\\cruzamento_estilo_lideranca_x_idade.xlsx'
)

modulo_analise.executar_analise_cruzada(
    ['Como você descreveria o estilo de liderança do seu superior direto?', 'Como você classificaria o nível geral de motivação da equipe?'],
    r'C:\\Projetos\\CruzaData\\Util\\Arquivos\\Relatorios\\cruzamento_estilo_lideranca_x_motivacao_equipe.xlsx'
)

modulo_analise.executar_analise_cruzada(
    ['Como você descreveria o estilo de liderança do seu superior direto?', 'Você acredita que o estilo de liderança adotado pelo seu superior direto influencia sua motivação no trabalho?'],
    r'C:\\Projetos\\CruzaData\\Util\\Arquivos\\Relatorios\\cruzamento_estilo_lideranca_x_desenvolvimento_profissional.xlsx'
)

modulo_analise.executar_analise_cruzada(
    ['Como você descreveria o estilo de liderança do seu superior direto?', 'Você sente que seu superior direto reconhece e valoriza suas contribuições para a equipe?'],
    r'C:\\Projetos\\CruzaData\\Util\\Arquivos\\Relatorios\\cruzamento_estilo_lideranca_x_satisfacao_trabalho.xlsx'
)

modulo_analise.executar_analise_cruzada(
    ['Como você descreveria o estilo de liderança do seu superior direto?', 'Você acha que seu superior direto está aberto a sugestões e feedback dos membros da equipe?'],
    r'C:\\Projetos\\CruzaData\\Util\\Arquivos\\Relatorios\\cruzamento_estilo_lideranca_x_feedback.xlsx'
)

modulo_analise.executar_analise_cruzada(
    ['Como você descreveria o estilo de liderança do seu superior direto?', 'Você acredita que o estilo de liderança adotado pelo seu superior direto influencia sua motivação no trabalho?'],
    r'C:\\Projetos\\CruzaData\\Util\\Arquivos\\Relatorios\\cruzamento_estilo_lideranca_x_motivacao_pessoal.xlsx'
)

modulo_analise.executar_analise_cruzada(
    ['Como você descreveria o estilo de liderança do seu superior direto?', 'Com que frequência seu superior direto comunica as metas e objetivos da equipe?'],
    r'C:\\Projetos\\CruzaData\\Util\\Arquivos\\Relatorios\\cruzamento_estilo_lideranca_x_comunicacao_metas.xlsx'
)

modulo_analise.executar_analise_cruzada(
    ['Como você descreveria o estilo de liderança do seu superior direto?', 'Você sente que seu superior direto demonstra empatia e compreensão em relação às suas necessidades individuais?'],
    r'C:\\Projetos\\CruzaData\\Util\\Arquivos\\Relatorios\\cruzamento_estilo_lideranca_x_empatia_compreensao.xlsx'
)

modulo_analise.executar_analise_cruzada(
    ['Como você descreveria o estilo de liderança do seu superior direto?', 'Você se sente capacitado(a) e autônomo(a) para tomar decisões em seu trabalho?'],
    r'C:\\Projetos\\CruzaData\\Util\\Arquivos\\Relatorios\\cruzamento_estilo_lideranca_x_autonomia_tomada_decisoes.xlsx'
)
