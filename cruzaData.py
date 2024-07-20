import pandas as pd

class CruzaData:
    def __init__(self, csv_path):
        # Carregar o CSV com a codificação correta
        self.df = pd.read_csv(csv_path, encoding='utf-8-sig', delimiter=';', quotechar='"', on_bad_lines='skip')
        # Remover espaços extras nos nomes das colunas
        self.df.columns = self.df.columns.str.strip()
    
    def save_excel(self, df, path):
        # Salvar o DataFrame em um arquivo Excel
        df.to_excel(path, index=False, engine='openpyxl')

    def cruzamento_genero_x_idade(self):
        # Agrupar por Gênero e Idade
        analysis = self.df.groupby(['Gênero', 'Idade']).size().reset_index(name='Quantidade')
        print(analysis)
        self.save_excel(analysis, r'C:\\Projetos\\CruzaData\\Util\\Arquivos\\Relatorios\\cruzamento_genero_x_idade.xlsx')

    def cruzamento_cargo_x_escolaridade(self):
        # Agrupar por Escolaridade e Cargo Atual
        education_satisfaction = self.df.groupby(['Escolaridade', 'Qual é o seu cargo atual na empresa?']).size().reset_index(name='Quantidade')
        print(education_satisfaction)
        self.save_excel(education_satisfaction, r'C:\\Projetos\\CruzaData\\Util\\Arquivos\\Relatorios\\cruzamento_cargo_x_escolaridade.xlsx')

    def cruzamento_estilo_lideranca_x_idade(self):
        # Agrupar por Idade e Estilo de Liderança
        leadership_age = self.df.groupby(['Idade', 'Como você descreveria o estilo de liderança do seu superior direto?']).size().reset_index(name='Quantidade')
        print(leadership_age)
        self.save_excel(leadership_age, r'C:\\Projetos\\CruzaData\\Util\\Arquivos\\Relatorios\\cruzamento_estilo_lideranca_x_idade.xlsx')

    def analyze_avg_service_time(self):
        # Limpar e converter o tempo de experiência para numérico
        self.df['Quanto tempo você tem de experiência no seu cargo atual?'] = self.df['Quanto tempo você tem de experiência no seu cargo atual?'].str.replace(' anos', '').str.replace(' mês', '').str.strip()
        self.df['Quanto tempo você tem de experiência no seu cargo atual?'] = pd.to_numeric(self.df['Quanto tempo você tem de experiência no seu cargo atual?'], errors='coerce')
        avg_service_time = self.df.groupby(['Gênero', 'Qual é o seu cargo atual na empresa?'])['Quanto tempo você tem de experiência no seu cargo atual?'].mean().reset_index(name='Average_Service_Time')
        print(avg_service_time)
        self.save_excel(avg_service_time, r'C:\\Projetos\\CruzaData\\Util\\Arquivos\\Relatorios\\avg_service_time.xlsx')

    def cruzamento_estilo_lideranca_x_motivacao_equipe(self):
        # Agrupar por Estilo de Liderança e Nível Geral de Motivação
        analysis = self.df.groupby(['Como você descreveria o estilo de liderança do seu superior direto?', 'Como você classificaria o nível geral de motivação da equipe?']).size().reset_index(name='Quantidade')
        print(analysis)
        self.save_excel(analysis, r'C:\\Projetos\\CruzaData\\Util\\Arquivos\\Relatorios\\cruzamento_estilo_lideranca_x_motivacao_equipe.xlsx')

    def cruzamento_estilo_lideranca_x_desenvolvimento_profissional(self):
        # Agrupar por Estilo de Liderança e Percepção sobre Desenvolvimento Profissional
        analysis = self.df.groupby(['Como você descreveria o estilo de liderança do seu superior direto?', 'Você acredita que o estilo de liderança adotado pelo seu superior direto influencia sua motivação no trabalho?']).size().reset_index(name='Quantidade')
        print(analysis)
        self.save_excel(analysis, r'C:\\Projetos\\CruzaData\\Util\\Arquivos\\Relatorios\\cruzamento_estilo_lideranca_x_desenvolvimento_profissional.xlsx')

    def cruzamento_estilo_lideranca_x_satisfacao_trabalho(self):
        # Agrupar por Estilo de Liderança e Nível de Satisfação no Trabalho
        analysis = self.df.groupby(['Como você descreveria o estilo de liderança do seu superior direto?', 'Você sente que seu superior direto reconhece e valoriza suas contribuições para a equipe?']).size().reset_index(name='Quantidade')
        print(analysis)
        self.save_excel(analysis, r'C:\\Projetos\\CruzaData\\Util\\Arquivos\\Relatorios\\cruzamento_estilo_lideranca_x_satisfacao_trabalho.xlsx')

    def cruzamento_estilo_lideranca_x_feedback(self):
        analysis = self.df.groupby(['Como você descreveria o estilo de liderança do seu superior direto?', 'Você acha que seu superior direto está aberto a sugestões e feedback dos membros da equipe?']).size().reset_index(name='Quantidade')
        print(analysis)
        self.save_excel(analysis, r'C:\\Projetos\\CruzaData\\Util\\Arquivos\\Relatorios\\cruzamento_estilo_lideranca_x_feedback.xlsx')

    def cruzamento_estilo_lideranca_x_motivacao_pessoal(self):
        analysis = self.df.groupby(['Como você descreveria o estilo de liderança do seu superior direto?', 'Você acredita que o estilo de liderança adotado pelo seu superior direto influencia sua motivação no trabalho?']).size().reset_index(name='Quantidade')
        print(analysis)
        self.save_excel(analysis, r'C:\\Projetos\\CruzaData\\Util\\Arquivos\\Relatorios\\cruzamento_estilo_lideranca_x_motivacao_pessoal.xlsx')

    def cruzamento_estilo_lideranca_x_comunicacao_metas(self):
        analysis = self.df.groupby(['Como você descreveria o estilo de liderança do seu superior direto?', 'Com que frequência seu superior direto comunica as metas e objetivos da equipe?']).size().reset_index(name='Quantidade')
        print(analysis)
        self.save_excel(analysis, r'C:\\Projetos\\CruzaData\\Util\\Arquivos\\Relatorios\\cruzamento_estilo_lideranca_x_comunicacao_metas.xlsx')

    def cruzamento_estilo_lideranca_x_empatia_compreensao(self):
        analysis = self.df.groupby(['Como você descreveria o estilo de liderança do seu superior direto?', 'Você sente que seu superior direto demonstra empatia e compreensão em relação às suas necessidades individuais?']).size().reset_index(name='Quantidade')
        print(analysis)
        self.save_excel(analysis, r'C:\\Projetos\\CruzaData\\Util\\Arquivos\\Relatorios\\cruzamento_estilo_lideranca_x_empatia_compreensao.xlsx')

    def cruzamento_estilo_lideranca_x_autonomia_tomada_decisoes(self):
            analysis = self.df.groupby(['Como você descreveria o estilo de liderança do seu superior direto?', 'Você se sente capacitado(a) e autônomo(a) para tomar decisões em seu trabalho?']).size().reset_index(name='Quantidade')
            print(analysis)
            self.save_excel(analysis, r'C:\\Projetos\\CruzaData\\Util\\Arquivos\\Relatorios\\cruzamento_estilo_lideranca_x_autonomia_tomada_decisoes.xlsx')    
