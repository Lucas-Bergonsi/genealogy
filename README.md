# Genealogia: Interesse de busca de sobrenome por regiões do Brasil


## Descrição
Genealogia é um projeto que permite pesquisar o interesse de busca de um sobrenome ou nome em diferentes regiões do Brasil. O programa utiliza o Google Trends para obter dados sobre a popularidade do termo pesquisado em cada localidade. Os resultados são exibidos em um mapa interativo, mostrando a intensidade do interesse em cada região.

## Funcionalidades
- Pesquisar o interesse de busca de um sobrenome ou nome em diferentes regiões do Brasil.
- Exibir os resultados em um mapa interativo, com cores indicando a intensidade do interesse em cada região.
- Mostrar a palavra-chave pesquisada e permitir a realização de novas pesquisas.
- Botão para acessar o Google Trends e obter mais informações sobre os dados apresentados.

## Tecnologias utilizadas
- HTML5 e CSS3 para a estrutura e o estilo da página.
- JavaScript para a interatividade e manipulação dos dados.
- Python para a integração com a API do Google Trends e processamento dos dados.
- Google Trends API para obter os dados de interesse de busca.
- 
## Utilização do Python
O Python desempenha um papel fundamental neste projeto, sendo utilizado para realizar a integração com a API do Google Trends e processar os dados obtidos. Veja como o Python foi utilizado:

1. Integração com a API: Utilizamos a biblioteca `google_trends` em Python para estabelecer a conexão com a API do Google Trends. Isso nos permite fazer consultas e obter dados de interesse de busca relacionados aos sobrenomes e nomes pesquisados.

2. Processamento de dados: Com os dados obtidos da API, utilizamos o Python para processá-los e prepará-los para exibição no site. Isso inclui a formatação dos dados, e a criação de gráficos e visualizações.

3. Lógica de negócio: O Python também é utilizado para implementar a lógica de negócio do aplicativo. Isso inclui a validação dos campos de pesquisa, o controle de eventos e a geração de mensagens de erro ou sucesso, conforme necessário.

O Python é uma linguagem de programação versátil e poderosa, amplamente utilizada no desenvolvimento web e científico. Sua sintaxe clara e legível, juntamente com sua ampla variedade de bibliotecas e frameworks, tornam o Python uma escolha popular para projetos de diferentes naturezas, incluindo este de pesquisa genealógica.


## Imagens

### Página Inicial
![Página Inicial](imagens/genealogia-0.png)

### Resultados da Pesquisa
![Resultados da Pesquisa](imagens/genealogia-1.png)

### Campos de pesquisa não preenchido
![Campos de pesquisa não preenchido](imagens/genealogia-2.png)


### Dados Indisponíveis
![Dados Indisponíveis](imagens/genealogia-3.png)

### Nova Pesquisa
![Nova Pesquisa](imagens/genealogia-4.png)

## Como usar
1. Digite o sobrenome ou nome que deseja pesquisar no campo de pesquisa.
2. Clique no botão "Pesquisar" para ver os resultados.
3. Os resultados serão exibidos no mapa interativo. As regiões com maior intensidade de interesse serão destacadas com cores mais fortes.
4. Você também pode clicar no botão "Acessar Google Trends" para obter mais informações sobre os dados apresentados.

## Contribuição
Contribuições são bem-vindas! Se você tiver alguma sugestão, correção de bugs ou melhorias, sinta-se à vontade para abrir uma nova issue ou enviar um pull request.

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).

