import os
import time

RESET = "\033[0m"
CYAN = "\033[96m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
WHITE = "\033[97m"
DIM = "\033[2m"


def habilitar_cores():
    if os.name == "nt":
        os.system("")


def titulo(texto):
    return f"{CYAN}>>> {texto.upper()} <<<{RESET}"


def sucesso(texto):
    return f"{GREEN}[OK] {texto}{RESET}"


def aviso(texto):
    return f"{YELLOW}[!] {texto}{RESET}"


def erro(texto):
    return f"{RED}[X] {texto}{RESET}"


def pausar_com_mensagem():
    input(f"\n{DIM}Pressione ENTER para voltar...{RESET}")


def menu():
    horario = time.strftime("%d/%m/%Y %H:%M:%S")
    return f"""{BLUE}+------------------------------------------+
|          SISTEMA DE ACADEMIA             |
+------------------------------------------+{RESET}
{DIM}{horario}{RESET}

{WHITE}[1]{RESET} Cadastrar aluno
{WHITE}[2]{RESET} Ver alunos
{WHITE}[3]{RESET} Pesquisar aluno
{WHITE}[4]{RESET} Remover aluno
{WHITE}[5]{RESET} Media de peso dos alunos
{WHITE}[6]{RESET} Editar aluno
{RED}[0]{RESET} Sair
"""


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
        print(erro("Campo obrigatorio."))
        return False
    else:
        return True


def validar_numero(valor):
    try:
        valor = float(valor.strip())
    except (AttributeError, ValueError):
        print(erro("Informe um valor valido."))
        return False

    if valor > 0:
        return True
    else:
        print(aviso("Digite um numero maior que zero."))
        return False


def menu_edicao(aluno):
    return f"""+------------------------------------------+
|              EDITAR ALUNO                |
+------------------------------------------+
Aluno: {aluno}
{WHITE}[1]{RESET} Nome
{WHITE}[2]{RESET} Altura
{WHITE}[3]{RESET} Peso
"""
