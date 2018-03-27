import random
import time
import matplotlib.pyplot as plt
# Essa funcao define o ultimo elemento como pivor,
# e o coloca em sua posicao ordenada no vetor,
# e posiciona todos os elemento menores que o pivor a esquerda e
# todos os maiores a direita do pivor.

vetorQuickSort = []
vetorTempo = []

###################################################################

def particao(arr,lo,hi):
    i = ( lo-1 )            #indice do menor elemento
    pivor = arr[hi]         #define o pivor
    for j in range(lo,hi):
        #Se o elemento atual for menor ou igual ao pivor
        if arr[j] <= pivor:
            i=i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[hi] = arr[hi],arr[i+1]
    return (i+1)


###################################################################

# Funcao principal que implementa o QuickSort
# arr[]  --> Vetor a ser ordenado
# lo --> indice inicial
# hi --> indice final

def quickSort(arr,lo,hi):
	if lo < hi:
		part = particao(arr,lo,hi)
		quickSort(arr, lo, part-1)
		quickSort(arr, part+1, hi)
	return arr

###################################################################

#Funcao responsavel pela geracao dos vetores

def geraVetor(qtdElementosVetor):
	arr = []
	for x in range(qtdElementosVetor):	# --> Gera os numeros aleatorios para o vetor
		n = random.randint(1,1000)
		arr.append(n)

	return arr

###################################################################

#Funcao responsavel por plotar o grafico
def plotarGrafico(vetorQuickSort, vetorTempo):
	plt.xlabel('Tamanho vetor')
	plt.ylabel('Tempo')
	plt.title('QUICK SORT')
	plt.grid(True)
	plt.plot(vetorQuickSort, vetorTempo)
	plt.show()

###################################################################

for x in range(5):
	n = x*10000			#tamanho do vetor
	arr = geraVetor(n)		#Gera vetor para ordenacao

	inicio = time.time()		#Inicia a contagem de tempo
	arr = quickSort(arr,0,n-1)	#Executa a o algoritmo de ordenacao
	fim = time.time()		#Finaliza a contagem
	duracao = fim - inicio		#Calcula a duracao

	vetorQuickSort.append(n)
	vetorTempo.append(duracao)

plotarGrafico(vetorQuickSort, vetorTempo)
