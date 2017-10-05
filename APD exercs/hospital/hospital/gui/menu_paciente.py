from logica import paciente


def imprimir_paciente(paciente):
    print ("CPF: ",  paciente[0])
    print ("Nome: ", paciente[1])
    print ("Telefone: ",  paciente[2])
    print ()

def menu_adicionar():
    print ("\nAdicionar Paciente \n")
    cpf = int(input("CPF: "))
    nome = str (input("Nome: "))
    telefone = int(input("Telefone: "))
    paciente.adicionar_paciente(cpf, nome, telefone)

def menu_listar():
    print ("\nListar Pacientes \n")
    pacientes = paciente.listar_pacientes()
    for p in pacientes:
        imprimir_paciente(p)


def menu_buscar():
    print ("\nBuscar Paciente por CPF \n")
    cpf = int(input("CPF: "))
    p = paciente.buscar_paciente(cpf)
    if (p == None):
        print ("Paciente não encontrado")
    else:
        imprimir_paciente(p)
  
def menu_remover():
    print ("\nRemover Paciente \n")
    cpf = int(input("CPF: "))
    p = paciente.remover_paciente(cpf)
    if (p == False):
        print ("Paciente não encontrado")
    else:
        print ("Paciente removido")
    

def mostrar_menu():
    run_paciente = True
    menu = ("\n----------------\n"+
             "(1) Adicionar novo Paciente \n" +
             "(2) Listar Paciente \n" +
             "(3) Buscar Paciente por CPF \n" +
             "(4) Remover Paciente \n" +
             "(0) Voltar\n"+
            "----------------")
    
    while(run_paciente):
        print (menu)
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            menu_adicionar()
        elif(op == 2):
            menu_listar()
        elif(op == 3):       
            menu_buscar()
        elif (op == 4):
            menu_remover()
        elif (op == 0):
            run_paciente = False
    
