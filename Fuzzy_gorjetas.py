#                       Antecedentes(entradas)
# Serviço: que nota você daria para o serviço, em uma escala de 0 a 10?
#ruim, aceitavel, ótimo

# Qualidade da Comida: quão boa estava a comida, em uma escala de 0 a 10?
#ruim, boa, saborosa


#                       Consequentes(saidas)
# Gorjetas: quanta gorjeta você daria, entre 0% e 20%?
#media, baixa, alta

#                             Regras
# Se a qualidade da commida for RUIM e o serviço for RUIM então gorjeta será BAIXA
# Se o serviço for ACEITAVEL então a gorjeta será MEDIA
# Se o serviço for OTIMO e a qualidade da comida for SABOROSA então a gorjeta será ALTA

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

qualidade = ctrl.Antecedent(np.arange(0,11,1), 'qualidade')
servico = ctrl.Antecedent(np.arange(0,11,1), 'servico')
gorjeta = ctrl.Consequent(np.arange(0,21,1), 'gorjeta')

print(gorjeta.universe)

#autmof - popula o svalores dentro das faixas
qualidade.automf(number=3, names=['ruim', 'boa','saborosa'])
servico.automf(number=3, names=['ruim', 'aceitavel','ótimo'])

#Definindo o limite das gorjetas
gorjeta['baixa'] = fuzz.trimf(gorjeta.universe, [0,0,10]) # inicio, pico, fim no gráfico
gorjeta['media'] = fuzz.trimf(gorjeta.universe, [0,10,20])
gorjeta['alta'] = fuzz.trimf(gorjeta.universe, [10,20,20])

#Plotando o gráfico
# gorjeta.view()
# plt.show()

# qualidade.view()
# qualidade['boa'].view()
# plt.show()


#Criando as regras para decisão da lógica fuzzi
regra1 = ctrl.Rule(qualidade['ruim'] | servico['ruim'], gorjeta['baixa'])
regra2 = ctrl.Rule(servico['aceitavel'], gorjeta['media'])
regra3 = ctrl.Rule(servico['ótimo'] | qualidade['saborosa'], gorjeta['alta'])

#Criando sistema
sistema_controle = ctrl.ControlSystem([regra1, regra2, regra3])
sistema = ctrl.ControlSystemSimulation(sistema_controle)

#Atribuindo notas do usuario
sistema.input['qualidade']= 20
sistema.input['servico']= 20

#Computar os valores
sistema.compute()

print(sistema.output['gorjeta'])
gorjeta.view(sim=sistema)
plt.show()
