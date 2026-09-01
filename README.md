# Sistema de Academia (Gerenciamento & IMC)

Sistema em Python desenvolvido para gerenciamento simples de alunos em uma academia, permitindo o cadastro de dados físicos, cálculo automático do IMC (Índice de Massa Corporal) e classificação do status de saúde.

## Funcionalidades

- **Cadastrar Aluno:** Registra nome, altura e peso, calculando automaticamente o IMC e a classificação (Magreza, Normal, Sobrepeso, Obesidade, Obesidade Grave).
- **Listar Alunos:** Exibe todos os alunos cadastrados e suas métricas.
- **Pesquisar Aluno:** Busca rápida de aluno pelo nome.
- **Remover Aluno:** Exclusão de registros do sistema.

## Tecnologias Utilizadas

- **Python 3**
- Módulos nativos (`os`) para navegação e limpeza do terminal.

## Estrutura do Projeto

- `main.py`: Ponto de entrada do programa e fluxo do menu interativo.
- `dados.py`: Armazenamento em memória, funções do CRUD e regras da tabela de IMC.
- `calculos.py`: Módulo responsável pelo cálculo matemático do IMC.

## Como Executar o Projeto

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. Clone este repositório:
   ```bash
   git clone [https://github.com/KonsaWRLD/Sistema-Academia.git](https://github.com/KonsaWRLD/Sistema-Academia.git)

1. Acesse a pasta do projeto:

`cd Sistema-Academia`

2. Execute o arquivo principal:

`python main.py`