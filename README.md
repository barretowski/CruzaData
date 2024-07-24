# Projeto CruzaData

O projeto **CruzaData** é uma ferramenta para análise e cruzamento de dados a partir de arquivos CSV. Utiliza Python e bibliotecas como `pandas` e `matplotlib` para realizar análises cruzadas e gerar relatórios em diferentes formatos (Excel, CSV, JSON) e gráficos.
Inicialmente desenvolvido para o auxilio de uma pós-graduanda para a realização de cruzamento de dados, com amostras obtidas em uma pesquisa realizada pela mesma.

## Funcionalidades

- **Carregamento de Dados**: Carregar dados de arquivos CSV com suporte a codificação UTF-8 e delimitadores personalizados.
- **Análise Cruzada**: Agrupamento e análise de dados com base em colunas especificadas.
- **Exportação**: Salvar resultados das análises em formatos Excel, CSV e JSON.
- **Visualização**: Gerar gráficos de barras para representar visualmente as análises.

## Requisitos

- Python 3.x
- Bibliotecas Python: `pandas`, `matplotlib`, `openpyxl`

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   
2. Instale as dependências:
  bash
  Copiar código
  pip install pandas matplotlib openpyxl

## Uso
  1. Preparação: Certifique-se de que o arquivo CSV está no formato esperado (UTF-8 com delimitador ;).

  2. Instanciar a Classe:
    No seu arquivo main.py, importe e instancie a classe CruzaData com o caminho para o arquivo CSV:
    
    from cruzaData import CruzaData
    # Caminho para o arquivo CSV
    csv_path = 'caminho/para/seu/arquivo.csv'
  
    # Instanciar o módulo de análise
    modulo_analise = CruzaData(csv_path)
  
  3. Executar Análises:
    Utilize o método executar_analise_cruzada para realizar análises cruzadas e gerar relatórios:
    modulo_analise.executar_analise_cruzada(
        ['Gênero', 'Idade'],
        'caminho/para/relatorio.xlsx'
    )
    Gerar Gráficos: 
    A análise cruzada inclui a geração de gráficos de barras automaticamente.

