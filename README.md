# 🧑‍💻 API de Busca Textual em CSV 📄

Esta é uma API simples desenvolvida com Flask que permite realizar buscas textuais em um arquivo CSV de cadastros de operadoras. A API recebe um termo de busca e retorna as linhas do arquivo CSV que contêm esse termo em qualquer uma de suas colunas. 🔍

## Funcionalidades ✨

- Carregamento de um arquivo CSV (`cadastros_operadoras.csv`) 📂.
- Busca de um termo fornecido nas colunas do arquivo CSV 🔎.
- Retorno dos resultados em formato JSON 📊.

## Pré-requisitos ⚙️

Antes de rodar o projeto, é necessário ter o Python 3.x e as dependências instaladas. Para instalar as dependências, use o seguinte comando:

```bash
pip install -r requirements.txt
```
Endpoints 🚀
GET /buscar
Esse endpoint permite realizar uma busca no arquivo CSV, procurando por um termo em todas as colunas. 🌐

Parâmetros:

termo (string) – O termo a ser buscado nas colunas do CSV.

Respostas:

200 OK – Retorna os resultados da busca em formato JSON, onde cada item é uma linha que contém o termo pesquisado.

Exemplo de resposta:

```bash
[
  {
    "coluna1": "valor1",
    "coluna2": "valor2",
    ...
  },
  {
    "coluna1": "valor3",
    "coluna2": "valor4",
   ...
  }
]
```
---
400 Bad Request – Se o parâmetro termo não for fornecido.

Exemplo de resposta:

```bash
{
  "erro": "Parâmetro 'termo' é obrigatório"
}
---
404 Not Found – Se não houver resultados para o termo de busca.

Exemplo de resposta:

{
  "mensagem": "Nenhum resultado encontrado"
}
```
---
500 Internal Server Error – Se o arquivo CSV não puder ser carregado ou ocorrer algum erro interno.

Exemplo de resposta:

```bash

{
  "erro": "Não foi possível carregar os dados"
}
```
##Como Rodar 🏃‍♀️
Para rodar a aplicação localmente, basta executar o seguinte comando:

```bash
python app.py
```
Isso iniciará o servidor na porta 5000 por padrão. A API estará disponível em:

```bash
http://127.0.0.1:5000
```
Exemplo de Uso 💻
Para realizar uma busca, você pode fazer uma requisição GET para o endpoint /buscar passando o parâmetro termo. Por exemplo:

```bash
http://127.0.0.1:5000/buscar?termo=termo_de_busca
```
A resposta será um JSON com as linhas do CSV que contêm o termo de busca.

Considerações 🤔
O arquivo CSV utilizado (cadastros_operadoras.csv) deve estar no mesmo diretório que o script app.py 📂.

O parâmetro termo é obrigatório.

A busca é realizada em todas as colunas do CSV, e a busca não diferencia maiúsculas de minúsculas 🔠.

