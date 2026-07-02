# Sistema de Gerenciamento de Tarefas Ágil

tarefas = []

def adicionar_tarefa():
    nome = input("Digite o nome da tarefa: ")
    tarefas.append({
    "nome": nome,
    "concluida": False
})
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("\nLista de Tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            status = "✅" if tarefa["concluida"] else "❌"
            print(f"{i}. {tarefa['nome']} - {status}")
def excluir_tarefa():
    listar_tarefas()

    if tarefas:
        numero = int(input("Digite o número da tarefa que deseja excluir: "))

        if 1 <= numero <= len(tarefas):
            removida = tarefas.pop(numero - 1)
            print(f"Tarefa '{removida}' removida com sucesso!")
        else:
            print("Número inválido.")
while True:
    print("\n===== MENU =====")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Excluir tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa()

    elif opcao == "2":
        listar_tarefas()

    elif opcao == "3":
        excluir_tarefa()

    elif opcao == "4":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")