# Essa funcao define o ultimo elemento como pivor,
# e o coloca em sua posicao ordenada no vetor,
# e posiciona todos os elemento menores que o pivor a esquerda e
# todos os maiores a direita do pivor.

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

# Funcao principal que implementa o QuickSort
# arr[]  --> Vetor a ser ordenado
# lo --> indice inicial
# hi --> indice final

def quickSort(arr,lo,hi):
    if lo < hi:
        part = particao(arr,lo,hi)
        quickSort(arr, lo, part-1)
        quickSort(arr, part+1, hi)

arr = [10,7,8,9,1,5, 11, 10, 5, 1]
n = len(arr)
quickSort(arr,0,n-1)

print("Sorted array is: ")

for i in range(n):
    print ("%d" %arr[i]),
