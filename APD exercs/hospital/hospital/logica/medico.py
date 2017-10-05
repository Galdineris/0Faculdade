medicos = []


def adicionar_medico(crm, nome, endereco):    
    medico = [crm, nome, endereco]
    medicos.append(medico)
    
def listar_medicos():
    return medicos

def buscar_medico(crm):
    for m in medicos:
        if (m[0] == crm):
            return m
    return None
        
def remover_medico(crm):
    for m in medicos:
        if (m[0] == crm):
            medicos.remove(m)
            return True
    return False
        
    
def iniciar_medicos():
    adicionar_medico(22222222222, "Carlos", "Rua Angelica")
    adicionar_medico(11111111111, "Maria", "Rua Consolacao")
    
