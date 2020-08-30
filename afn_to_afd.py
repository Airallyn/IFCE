#!/usr/bin/env python
# coding: utf-8

# # imports

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


def afn_to_afd(afn, alfabeto, estados, estado_inicial, estados_finais):
    
    afd = []
    
    estados_afd_criados = [estado_inicial]
    #afd.append(estados_afd_criados)
    
    for j in estados_afd_criados:
        transicao_estados = []
        for i in alfabeto:
        
            print('transição = ',j, i)
            estado_temporario = []
            transicoes = []
            for k in j:
                
                if k != 'z':
                    novo_estado_afd = definir_estado_afd(afn, k, i)
                    estado_temporario.extend(novo_estado_afd)
                    
                    
                    if 'z' in estado_temporario:
                        estado_temporario.remove('z')
                        
                if list(set(estado_temporario)) not in estados_afd_criados:
                    print("###### ", list(set(estado_temporario)))
                    estados_afd_criados.append(list(set(estado_temporario)))
            
            transicao_estados.append(list(set(estado_temporario)))
            
        afd.append(transicao_estados)
        print('***** ',afd)
    return estados_afd_criados, afd


# In[47]:


def definir_estado_afd(afn, estado, transicao):
    
    estado_novo_afd = []
    
    if afn.loc[estado, transicao][0] != '' or afn.columns[-1] == 'e':
        
        if afn.loc[estado, transicao][0] != '':
            estado_temporario = afn.loc[estado, transicao]
            
            for estado_unitario in estado_temporario:
                estado_novo_afd.append(estado_unitario)
                
                if afn.columns[-1] == 'e':
                    
                    if  afn.loc[estado_unitario, 'e'][0] != '':
                        
                        for i in afn.loc[estado_unitario, 'e']:
                            estado_novo_afd.append(i)
        else:
            print('*/*/**/*** ', afn.loc[estado, 'e'][0]) 
            if  afn.loc[estado, 'e'][0] != '':
                print('*/*/**/***')            
                for i in afn.loc[estado, 'e']:
                    estado_novo_afd.append(i)

    if len(estado_novo_afd) != 0:
        
        return sorted(set(estado_novo_afd)) #elimina elementos repetidos
    else:
        return ['z']    


# # Definido AFND

# In[70]:


afn = [[['a'],[''], ['b']],
      [[''],['b'], ['']]]

colunas = ['0','1','e']
alfabeto = ['0','1']
estados = ['a','b']
estado_inicial = ['a']
estados_finais = ['b']

afn = pd.DataFrame(data=afn, index=estados, columns=colunas)
afn


# # outro afnd

# In[165]:


afn1 = [[['a'],['a','b'], ['']],
      [['c'], [''], ['c']],
       [[''], ['d'], ['']],
       [['d'], ['d'], ['']]]

colunas = ['0','1','e']
alfabeto = ['0','1']
estados = ['a','b','c','d']
estado_inicial = ['a']
estados_finais = ['d']

afn = pd.DataFrame(data=afn1, index=estados, columns=colunas)
afn


# # convertendo

# In[71]:


estados_afd_criados, afd = afn_to_afd(afn, alfabeto, estados, estado_inicial, estados_finais)


# # definir estados finais

# In[79]:


estados_finais_afd = []

for n, i in enumerate(estados_afd_criados):
    for j in i:
         for k, m in enumerate(estados_finais):
            if m == j:
                estados_finais_afd.append(n)
                continue


# # Renomeando os estados afd

# In[82]:


y1 = np.zeros((np.array(afd).shape))
x = np.zeros((np.array(estados_afd_criados).shape))

for i in range(len(estados_afd_criados)):
    for j in range(len(alfabeto)):
        for k,m in enumerate(estados_afd_criados):
            if afd[i][j] == m:
                y1[i][j] = str(k)


# In[83]:


for i,j in enumerate(estados_afd_criados):
    x[i] = str(i)


# In[88]:


df = pd.DataFrame(data=y1, index=x, columns=alfabeto)
df


# In[86]:


funcao_transicao = y1
estados = x
estado_inicial = x[0]
alfabeto = alfabeto
estados_finais = estados_finais_afd


# In[87]:


funcao_transicao, estados, estado_inicial, alfabeto, estados_finais


# In[ ]:




