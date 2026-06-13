class Chapa:
    def __init__(self, id, tipo, tempo_processamento, setup):
        self.id = id
        self.tipo = tipo

        self.tempo_processamento = tempo_processamento
        self.setup = setup

class Pedido:
    def __init__(self, chapas, tempo_processamento, data_termino, custo_antecipacao, custo_atraso, setup, ):
        self.chapas = chapas # chapas do pedido
        self.tempo_processamento = tempo_processamento 
        self.data_termino = data_termino
        self.custo_antecipacao = custo_antecipacao
        self.custo_atraso = custo_atraso
        self.setup = setup #tupla setup em relacao a outros pedidos
class Job: 
    # informacoes necessarias para cada job
    def __init__(self, tempo_processamento, data_termino, setup, custo_antecipacao, custo_atraso):
        self.tempo_processamento = tempo_processamento
        self.data_termino = data_termino
        self.setup = setup #tupla setup em relacao a outros jobs
        self.custo_antecipacao = custo_antecipacao
        self.custo_atraso = custo_atraso
class Entrada_Modelo:
    def __init__(self, n, P, D, S, a, b):
        self.n = n #numero de jobs
        self.P = P #tupla tempo processamento dos jobs
        self.D = D #tupla data desejada para o termino
        self.S = S #matriz Setup
        self.a = a #tupla custo antecipacao dos jobs
        self.b = b #tupla custo atraso dos jobs
        self.M = 99999

class Saida_Modelo:
    def __init__(self, s, y, e, t, Z):
        self.s = s #tupla tempo inicio do processamento
        self.y = y #matriz antecedencia
        self.e = e #tupla tempo antecipacao
        self.t = t #tupla tempo de atraso
        self.Z = Z #custo
