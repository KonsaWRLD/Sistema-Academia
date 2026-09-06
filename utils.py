import os
import time


def menu():
    horario = time.strftime("%d/%m/%Y %H:%M:%S")
    return f"""Sistema de Academia | {horario}

1. Cadastrar aluno
2. Ver alunos
3. Pesquisar alunos
4. Remover aluno
5. Média de peso dos alunos
0. Sair\n"""


def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def pausar(segundos=1):
    time.sleep(segundos)


def status(imc):
    if imc < 18.5:
        return "Magreza"
    elif 18.5 <= imc <= 24.9:
        return "Normal"
    elif 25 <= imc <= 29.9:
        return "Sobrepeso"
    elif 30 <= imc <= 39.9:
        return "Obesidade"
    else:
        return "Obesidade Grave"


def validar_nome(nome):
    nome = nome.strip()
    if nome == "":
        print("Campo obrigatório!")
        return False
    else:
        return True


def validar_numero(valor):
    try:
        valor = float(valor.strip())
    except (AttributeError, ValueError):
        print("Informe um valor válido!")
        return False

    if valor > 0:
        return True
    else:
        print("Digite um número maior que zero!")
        return False
