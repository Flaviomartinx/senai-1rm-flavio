import math

def calcular_triangulo_retangulo():
    print("Digite as informações conhecidas do triângulo retângulo:")
    print("(1) - Calcular o comprimento da hipotenusa")
    print("(2) - Calcular um dos ângulos agudos")
    print("(3) - Calcular o comprimento de um dos catetos")
    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        cateto1 = float(input("Digite o comprimento do cateto adjacente: "))
        cateto2 = float(input("Digite o comprimento do cateto oposto: "))
        hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
        print("A hipotenusa tem comprimento:", hipotenusa)

    elif opcao == "2":
        cateto1 = float(input("Digite o comprimento do cateto adjacente: "))
        cateto2 = float(input("Digite o comprimento do cateto oposto: "))
        angulo = math.degrees(math.atan(cateto2 / cateto1))
        print("O ângulo agudo é:", angulo, "graus")

    elif opcao == "3":
        hipotenusa = float(input("Digite o comprimento da hipotenusa: "))
        cateto = float(input("Digite o comprimento de um dos catetos conhecidos: "))
        cateto_desconhecido = math.sqrt(hipotenusa**2 - cateto**2)
        print("O comprimento do cateto desconhecido é:", cateto_desconhecido)

    else:
        print("Opção inválida. Por favor, execute o programa novamente e escolha uma opção válida.")

calcular_triangulo_retangulo()


def exibir_menu():
    print("\n===== Lista de Tarefas =====")
    print("Selecione uma opção:")
    print("1 - Exibir lista de tarefas")
    print("2 - Adicionar nova tarefa")
    print("3 - Marcar tarefa como concluída")
    print("4 - Sair")

def exibir_tarefas(tarefas):
    print("\n===== Lista de Tarefas =====")
    if not tarefas:
        print("A lista de tarefas está vazia.")
    else:
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")

def adicionar_tarefa(tarefas):
    nova_tarefa = input("Digite a nova tarefa: ")
    tarefas.append(nova_tarefa)
    print("Tarefa adicionada com sucesso!")

def marcar_tarefa_concluida(tarefas):
    exibir_tarefas(tarefas)
    numero_tarefa = int(input("Digite o número da tarefa concluída: "))
    if 1 <= numero_tarefa <= len(tarefas):
        tarefas.pop(numero_tarefa - 1)
        print("Tarefa marcada como concluída.")
    else:
        print("Número de tarefa inválido.")

def main():
    tarefas = []
    while True:
        exibir_menu()
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            exibir_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefa(tarefas)
        elif opcao == "3":
            marcar_tarefa_concluida(tarefas)
        elif opcao == "4":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")

if __name__ == "__main__":
    main()