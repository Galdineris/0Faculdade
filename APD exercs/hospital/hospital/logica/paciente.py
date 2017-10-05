pacientes = []


def adicionar_paciente(cpf, nome, telefone):    
    paciente = [cpf, nome, telefone]
    pacientes.append(paciente)
    
def listar_pacientes():
    return pacientes

def buscar_paciente(cpf):
    for p in pacientes:
        if (p[0] == cpf):
            return p
    return None
        
def remover_paciente(cpf):
    for p in pacientes:
        if (p[0] == cpf):
            pacientes.remove(p)
            return True
    return False
        
    
def iniciar_pacientes():
    adicionar_paciente(22222222222, "Charles", 998807766)
    adicionar_paciente(11111111111, "Joao", 98765432112)
    