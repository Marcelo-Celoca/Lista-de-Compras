# 🛒 Lista de Compras Inteligente em Python

Este projeto é uma aplicação de console que permite ao usuário gerenciar uma lista de compras de forma dinâmica, com foco na prática de manipulação de listas e tratamento de erros.

## 📋 Sobre o Projeto
O objetivo foi criar uma ferramenta funcional onde o usuário pudesse não apenas adicionar e visualizar itens, mas também gerenciar erros de entrada e realizar a remoção de itens específicos utilizando índices numéricos.

## 🚀 Funcionalidades
* **Adição de Itens:** Inserção dinâmica de produtos na lista.
* **Exibição Numerada:** Visualização da lista utilizando `enumerate` para facilitar a identificação dos itens.
* **Exclusão por Índice:** Remoção seletiva de itens da lista utilizando o método `.pop()`.
* **Robustez (Tratamento de Erros):** * Captura de `ValueError` para entradas que não são números.
    * Captura de `IndexError` para tentativas de excluir itens em posições inexistentes.
* **Interface Colorida:** Uso de emojis e códigos de escape para melhorar a experiência no terminal.

## 🛠️ Tecnologias Utilizadas
* **Python 3**
* Módulos nativos (sem dependências externas)

## 🔧 Como Executar
1. Certifique-se de ter o Python instalado (v3.6 ou superior).
2. Clone este repositório ou baixe o arquivo `.py`.
3. Execute o comando:
   ```bash
   python nome_do_arquivo.py
