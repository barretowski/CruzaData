import pandas as pd
import matplotlib.pyplot as plt

class CruzaData:
    def __init__(self, csv_path):
        # Carregar o CSV com a codificação correta
        self.df = pd.read_csv(csv_path, encoding='utf-8-sig', delimiter=';', quotechar='"', on_bad_lines='skip')
        # Remover espaços extras nos nomes das colunas
        self.df.columns = self.df.columns.str.strip()
    
    def save_excel(self, df, path):
        # Salvar o DataFrame em um arquivo Excel
        df.to_excel(path, index=False, engine='openpyxl')
        
    def save_csv(self, df, path):
        df.to_csv(path, index=False)

    def save_json(self, df, path):
        df.to_json(path, orient='records', lines=True)


    def executar_analise_cruzada(self, colunas_agrupamento, caminho, grafico='false', formato='excel', nome_coluna='Quantidade'):
        try:
            # Realiza a análise cruzada
            analise_cruzamento = self.df.groupby(colunas_agrupamento).size().reset_index(name=nome_coluna)
            print(analise_cruzamento)
            
            # Salva os resultados no formato especificado
            if formato == 'excel':
                self.save_excel(analise_cruzamento, caminho)
            elif formato == 'csv':
                self.save_csv(analise_cruzamento, caminho)
            elif formato == 'json':
                self.save_json(analise_cruzamento, caminho)
            else:
                raise ValueError("Formato especificado não é suportado. Use 'excel', 'csv' ou 'json'.")
            
            # Gera plot da análise
            if grafico == 'true':
                self.plot_analise(analise_cruzamento, colunas_agrupamento[0], nome_coluna, title=f'Análise de {colunas_agrupamento}')
        
        except ValueError as ve:
            print(f"Erro de valor: {ve}")
        except FileNotFoundError as fe:
            print(f"Arquivo não encontrado: {fe}")
        except Exception as e:
            print(f"Erro inesperado: {e}")


    def filtrar_dados(self, condicoes):
        self.df = self.df.query(condicoes)

    def plot_analise(self, df, x_col, y_col, kind='bar', title=''):
        df.plot(kind=kind, x=x_col, y=y_col)
        plt.title(title)
        plt.show()