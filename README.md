# Aplicação web para Dobot Magician

Esse projeto se trata de uma aplicação web que se integra a robôs de braço mecânico da linha "Dobot Magician". Ela possui uma tela principal, na qual é possível controlar o robô por meio da movimentação do braço mecânico a partir de coordenadas definidas pelo usuário. Além disso, há também uma tela de dashboard com logs sobre a movimentação do robô de acordo com as coordenadas e os horários de cada movimentação.

A aplicação web foi feita a partir de Flask, HTMX e TinyDB.

## Pré-requisitos

Para utilizar essa aplicação, você deve ter:

- Git instalado e com chave SSH configurada
- Python e PIP instalados
- Robô Dobot Magician Lite

## Guia de instalação

1. Abra um terminal no diretório no qual você pretende instalar os arquivos do projeto e digite o seguinte comando para clonar este repositório:

```git clone git@github.com:RaiDeOliveira/dobot_magician_web_app.git```

2.  Na mesma janela de terminal, digite os seguintes comandos para adentrar na pasta raiz do projeto, criar um ambiente virtual e ativá-lo:

```cd dobot_magician_web_app```

```python -m venv venv```

```venv\Scripts\activate```

> O comando ```venv\Scripts\activate``` pode variar de acordo com seu sistema operacional. Em caso de dúvidas, cheque a documentação oficial do Python.

3. Na mesma janela de terminal, digite o seguinte comando para instalar as biliotecas necessárias para executar a aplicação web:

```pip install -r requirements.txt```

4. Na mesma janela de terminal, digite o seguinte comando para executar a aplicação web:

```py web-app/app.py```

5. Segure a tecla **ctrl** e clique com o botão esquerdo do mouse na URL exibida na janela de terminal. A aplicação web abrirá no seu navegador padrão.

## Funcionamento

A tela inicial apresenta uma interface de controle de movimentação do braço mecânico. Para utilizá-la, basta digitar os valores das coordenadas de cada eixo do ponto ao qual você deseja que o braço mecânico se direcione. Por fim, aperte o botão de "mover" para iniciar a movimentação. Também há um breve texto na parte inferior da interface que redireciona o usário para a página de dashboard da aplicação.

A página de dashboard exibe logs de movimentação do robô através de uma tabela. Ela registra as coordenadas de cada eixo para cada movimentação do robô feita através da página de controle do braço mecânico, bem como o horário de cada movimentação. Ademais, a parte inferior dessa página contém um breve texto clicável que redireciona o usuário para a página anterior. 

Caso o robô não esteja conectado via USB no seu computador ao iniciar a aplicação web, você será redirecionado para a página de dashboard em vez da página principal de controle do robô. Além disso, também há, em ambas as páginas, uma mensagem que informa o usuário se a conexão com o robô está sendo corretamente feita. Essa mensagem atualiza automaticamente a cada 2 segundos.

> **ATENÇÃO**🚨
> É importante que o robô seja o único dispositivo conectado ao computador via USB.
> Preferencialmente, também não deve haver nenhum dispositivo conectado ao computador via Bluetooth, pois o programa pode identificar o dispositivo conectado via Bluetooth como o robô, o que pode causar problemas de inicialização e/ou utilização.

## Vídeo de demonstração

Para ver um vídeo de demonstração do projeto, [clique aqui](https://www.youtube.com/watch?v=10CvLrI98Bc).