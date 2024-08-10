# Projeto de Interpolação e Fractal de Mandelbrot

Este é um projeto que consiste em desenvolver uma interface em Python utilizando a biblioteca QT. Através da interpolação com C, o objetivo é gerar uma imagem do famoso fractal de Mandelbrot.

## Funcionalidades

- Interface gráfica em Python utilizando QT.
- Utilização de interpolação com C para gerar o fractal de Mandelbrot.
- Opções de personalização da imagem, como zoom e cores.

## Requisitos

- Python 3.x
- Biblioteca PyQt5 e PyInstaller.
- Compilador C

## Como executar

1. Clone o repositório para o seu ambiente local.
2. Garanta ter o Python 3.x instalado em sua máquina.
3. Instale as dependências do projeto utilizando o comando `pip install PyQt5` e `pip install --upgrade pyinstaller`.
4. Compile a parte em C do projeto utilizando o comando `make all`.
5. O comando anterior gerou um arquivo executável chamado `./dist/main`, basta executa-lo através do comando `./dist/main`.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
