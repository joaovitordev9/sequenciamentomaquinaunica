from pulp import *
import dados as dt


# Cria o problema
prob = LpProblem("Sequenciamento Maquina", LpMinimize)

# Variáveis
variaveis = dt.Variaveis_decisao(None, None, None, None, None)

for i,job in enumerate(dt.jobs): 
    x = LpVariable(f"x{i}", lowBound=0)
    y = LpVariable(f"y{i}", lowBound=0)

# Função objetivo
prob += 3*x + 2*y

# Restrições
prob += x + y <= 4
prob += x <= 2
prob += y <= 3

# Resolve
prob.solve()

print("Status:", LpStatus[prob.status])

print("x =", value(x))
print("y =", value(y))
print("Lucro =", value(prob.objective))

#Quando nois pegar pra fazer esse trem junto...
