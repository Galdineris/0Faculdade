from logica import medico

def imprimir_medico(medico):
    print ("CRM: ",  medico[0])
    print ("Nome: ", medico[1])
    print ("Endereco: ",  medico[2])
    print ()

def menu_adicionar():
    print ("\nAdicionar medico \n")
    crm = int(input("CRM: "))
    nome = str (input("Nome: "))
    endereco = str(input("Endereco: "))
    medico.adicionar_medico(crm, nome, endereco)

def menu_listar():
    print ("\nListar medicos \n")
    medicos = medico.listar_medicos()
    for m in medicos:
        imprimir_medico(m)


def menu_buscar():
    print ("\nBuscar medico por CRM \n")
    crm = int(input("CRM: "))
    m = medico.buscar_medico(crm)
    if (m == None):
        print ("medico não encontrado")
    else:
        imprimir_medico(m)
  
def menu_remover():
    print ("\nRemover medico \n")
    crm = int(input("CRM: "))
    m = medico.remover_medico(crm)
    if (m == False):
        print ("medico não encontrado")
    else:
        print ("medico removido")
    

def mostrar_menu():
    run_medico = True
    menu = ("\n----------------\n"+
             "(1) Adicionar novo medico \n" +
             "(2) Listar medicos \n" +
             "(3) Buscar medico por CRM \n" +
             "(4) Remover medico \n" +
             "(0) Voltar\n"+
            "----------------")
    
    while(run_medico):
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
            run_medico = False

if __name__ == "__main__":
    mostrar_menu()
    
