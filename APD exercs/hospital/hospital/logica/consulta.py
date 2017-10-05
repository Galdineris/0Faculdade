from logica import paciente
from logica import medico

consultas = []
codigo_geral = 0

def _gerar_codigo():
    global codigo_geral
    codigo_geral += 1
    return codigo_geral
    
    

def marcar_consulta(data, cpf_paciente, crm_medico):
    codigo = _gerar_codigo()
    
    p = paciente.buscar_paciente(cpf_paciente)
    m = medico.buscar_medico(crm_medico)
   
    consulta = [codigo, data, p, m]
    consultas.append(consulta)
    
def listar_consultas():
    return consultas    

def buscar_consulta(cod_consulta):
    for c in consultas:
        if (c[0] == cod_consulta):
            return c
    return None

def desmarcar_consulta(codigo_consulta):
    for c in consultas:
        if (c[0] == codigo_consulta):
            consultas.remove(c)
            return True
    return False

    
def iniciar_consultas():
    marcar_consulta("12/02/2017", 22222222222, 22222222222)
    marcar_consulta("12/08/2017", 11111111111, 11111111111)
    marcar_consulta("13/08/2017", 22222222222, 11111111111)
