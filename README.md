# Introdução ao Flask

Nesta atividade vamos criar uma aplicação Flask a partir de arquivos html/css de um frontend já pronto, de uma página de placar de jogos esportivos. A aplicação Flask estará separada em controller e view.

## Estrutura do projeto

### Preparação de ambiente virtual

Para o projeto Flask, precisamos instalar pacotes contendo o Flask. Neste projeto, já temos uma estrutura definida para facilitar a instalação. Para não fazer necessário alterar o Python instalado na máquina, podemos fazer as alterações em um ambiente virtual. Para criar um ambiente virtual rodamos o comando:

```
virtualenv venv
```

Não esqueça de verificar se o virtualenv e o python estão instalados.

```
python --version
```

```
virtualenv --version
```

Os dois comandos devem retornar informações sobre a versão instalada. Qualquer mensagem de erro indica que será necessário instalar. Caso não tenha obtido nenhum erro, pule para a próxima sessão.

Para o Python, podemos seguir as instruções no próprio [https://www.python.org/downloads/](site oficial).

Para o Virtualenv, podemos executar o comando

```
python virtualenv
```

### Ativação do ambiente virtual

Com o ambiente preparado, precisamos ativar o ambiente. Para isso usamos o comando

No Windows
```
source venv/Scripts/activate
```

No Linux
```
source venv/bin/activate
```

### Instalação das dependências

Assim que o ambiente estiver ativado, podemos instalar as dependências

```
pip install -r requirements.txt
```

### Executar o servidor Flask

Para executar o servidor, e conseguir acessar as páginas através do Flask, rodamos o comando

```
python server.py
```

### Executar os testes

Esta atividade também possui testes, que podem ser executados com o comando

``` shell
pytest
```

Isso fará com que os testes presentes rodem e indiquem seus acertos.
