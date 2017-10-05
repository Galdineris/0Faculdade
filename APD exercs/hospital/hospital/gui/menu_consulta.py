from logica import consulta
from gui import menu_medico
from gui import menu_paciente


def imprimir_consulta(consulta):
    codigo = consulta[0]
    data = consulta[1]
    paciente = consulta[2]
    medico = consulta[3]
    
    print ("Codigo da Consulta: ", codigo)
    print ("Data: ",  data)
    print ("Paciente - CPF: ", paciente[0])
    print ("Paciente - Nome: ", paciente[1])
    print ("Medico - CRM: ", medico[0])
    print ("Medico - Nome: ", medico[1])        
        
    print()
    
        

def menu_marcar():
    print ("\nMarcar consulta  \n")
    cpf = int(input("CPF do paciente: "))
    crm = int (input("CRM do medico: "))
    data = str(input("Data: "))
    marcou = consulta.marcar_consulta(data, cpf, crm)
    print ("Consulta Marcada")
    
        

def menu_listar():
    print ("\nListar consultas \n")
    consultas = consulta.listar_consultas()
    for c in consultas:
        imprimir_consulta(c)


def menu_buscar():
    print ("\nBuscar consulta \n")
    cod = int(input("Código: "))
    c = consulta.buscar_consulta(cod)
    if (c == None):
        print ("consulta não encontrado")
    else:
        imprimir_consulta(c)

def menu_desmarcar():
    print ("\nDesmarcar consulta \n")
    codigo = int(input("Codigo Consulta: "))
    c = consulta.desmarcar_consulta(codigo)
    if (c == False):
        print ("consulta não encontrada")
    else:
        print ("consulta removido")
    

def mostrar_menu():
    run_consulta = True
    menu = ("\n----------------\n"+
             "(1) Marcar nova consulta \n" +
             "(2) Listar consulta \n" +
             "(3) Buscar consulta por Código \n" +
             "(4) Cancelar consulta \n" +
             "(0) Voltar\n"+
            "----------------")
    
    while(run_consulta):
        print (menu)
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            menu_marcar()
        elif(op == 2):
            menu_listar()
        elif(op == 3):       
            menu_buscar()
        elif (op == 4):
            menu_desmarcar()
        elif (op == 0):
            run_consulta = False
            
    
