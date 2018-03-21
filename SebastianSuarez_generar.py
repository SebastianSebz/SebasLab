import matplotlib.pyplot as plt
import numpy as np

#Funcion_1 que genera y retorna N numeros aleatorios siguiendo una distribucion discreta de probabilidad, N numeros dado por parametro.

def sample_1(N):

	random = np.random.random_sample(N)
	return random

#print sample_1(10)


#Funcion_2 que genera y retorna Nexp numeros aleatorios siguiendo una distribucion de probabilidad exponencial, N dado por parametro.

def sample_2(beta,Nexp):

	random_Exp = np.random.exponential(beta,Nexp)
	return random_Exp

#print sample_2(0.5,4)

#Funcion que genera y retorna M promedios Sn dada la funcion de sampleo

def get_mean(sampling_fun,N,M):
	prom = []
	for i in range(N):
		promedio=sampling_fun(M)
		prom.append(promedio)
		
	return prom

print get_mean(sample_1,10,10000)
