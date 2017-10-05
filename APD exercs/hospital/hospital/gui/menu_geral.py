from logica import paciente
from gui import  menu_paciente

from logica import medico
from gui import  menu_medico

from logica import consulta
from gui import  menu_consulta

def inicializar_dados():
    paciente.iniciar_pacientes()
    medico.iniciar_medicos()
    consulta.iniciar_consultas()
    
def mostrar_menu():
    run_menu = True
   
    inicializar_dados()

    
    menu = ("\n----------------\n"+
             "(1) Menu Paciente \n" +
             "(2) Menu Medico \n" +
             "(3) Menu Consulta \n" +
             "(0) Sair\n"+
            "----------------")
    
    while(run_menu):
        print (menu)
        
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            menu_paciente.mostrar_menu()
        elif(op == 2):
            menu_medico.mostrar_menu()
        elif(op == 3):
            menu_consulta.mostrar_menu()
        elif (op == 0):
            print ("Saindo do programa...")
            run_menu = False
        else:
            print ("Valor invalido")
