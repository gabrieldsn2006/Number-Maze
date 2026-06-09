"""
Este é o código que NÃO executou dentro do limite de tempo de 3 segundos do URI Online Judge.

Site: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=submit_problem&problemid=870&category=0

Código foi feito utilizando uma implementação do algoritmo de Dijkstra baseada em fila de prioridade indexada 
com apenas algumas otimizações.
"""
import sys

class IndexMinPQ:
    def __init__(self, n):
        self.pq = []
        self.qp = [-1] * n
        self.keys = [None] * n
        
    def insert(self, i, item):
        self.pq.append(i)
        n = len(self.pq) - 1
        self.qp[i] = n
        self.keys[i] = item
        self.swim(n)

    def change(self, i, item):
        self.keys[i] = item
        self.sink(self.qp[i])
        self.swim(self.qp[i])

    def contains(self, index):
        return self.qp[index] != -1

    def delete(self, i):
        index = self.qp[i]
        item = self.keys[i]
        self._swap(index, len(self.pq) - 1)
        self.pq.pop()
        self.swim(index)
        self.sink(index)
        self.keys[i] = None
        self.qp[i] = -1
        return item

    def decrease_key(self, i, key):
        if self.keys[i] <= key:
            raise Exception("calling decrease key with invalid value")
        self.keys[i] = key
        self.swim(self.qp[i])

    def greater(self, i, j):
        return self.keys[self.pq[i]] > self.keys[self.pq[j]]

    def min(self):
        return self.keys[self.pq[0]]

    def del_min(self):
        m = self.pq[0]
        self._swap(0, len(self.pq) - 1)
        self.pq.pop()
        if self.pq:
            self.sink(0)
        self.qp[m] = -1
        self.keys[m] = None
        return m

    def is_empty(self):
        return not self.pq

    def size(self):
        return len(self.pq)

    def _swap(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
        self.qp[self.pq[i]] = i
        self.qp[self.pq[j]] = j

    def swim(self, k):
        while k > 0 and self.greater((k - 1) // 2, k):
            self._swap((k - 1) // 2, k)
            k = (k - 1) // 2

    def sink(self, k):
        N = len(self.pq)
        while 2 * k + 1 <= N - 1:
            j = 2 * k + 1
            if j < N - 1 and self.greater(j, j + 1):
                j += 1
            if not self.greater(k, j):
                break
            self._swap(k, j)
            k = j

def main():
    # Fast I/O: lê o arquivo inteiro de uma vez
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    # Converter tudo para int de uma única vez roda em nível C (MUITO mais rápido)
    data = list(map(int, input_data))
    
    num_mazes = data[0]
    idx = 1
    
    results = []
    
    for _ in range(num_mazes):
        N = data[idx]
        M = data[idx+1]
        idx += 2
        
        size = N * M
        # Utiliza o Labirinto como um array linear 1D (evita lista de listas)
        grid = data[idx : idx + size]
        idx += size
        
        # O maior custo possível seria ~ 9.000.000. 
        # Usar um int(10^9) é mais rápido que float('inf') para as comparações no Python
        dist = [1000000000] * size 
        dist[0] = grid[0]
        
        pq = IndexMinPQ(size)
        pq.insert(0, grid[0])
        
        dest = size - 1
        
        while not pq.is_empty():
            u = pq.del_min()
            d = dist[u]
            
            if u == dest:
                results.append(str(d))
                break
                
            # Coordenadas da matriz decodificadas do índice 1D
            r = u // M
            c = u % M
            
            # Loop Unrolling: Verificar as 4 direções manualmente
            if r > 0:           # Cima
                v = u - M
                cost = d + grid[v]
                if cost < dist[v]:
                    dist[v] = cost
                    if pq.contains(v):
                        pq.decrease_key(v, cost)
                    else:
                        pq.insert(v, cost)
            if r < N - 1:       # Baixo
                v = u + M
                cost = d + grid[v]
                if cost < dist[v]:
                    dist[v] = cost
                    if pq.contains(v):
                        pq.decrease_key(v, cost)
                    else:
                        pq.insert(v, cost)
            if c > 0:           # Esquerda
                v = u - 1
                cost = d + grid[v]
                if cost < dist[v]:
                    dist[v] = cost
                    if pq.contains(v):
                        pq.decrease_key(v, cost)
                    else:
                        pq.insert(v, cost)
            if c < M - 1:       # Direita
                v = u + 1
                cost = d + grid[v]
                if cost < dist[v]:
                    dist[v] = cost
                    if pq.contains(v):
                        pq.decrease_key(v, cost)
                    else:
                        pq.insert(v, cost)
                    
    print('\n'.join(results))

if __name__ == '__main__':
    main()