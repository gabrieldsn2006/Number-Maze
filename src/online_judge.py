import time
# Inicia o cronômetro assim que o arquivo começa a ser lido pelo Python
startup_start_time = time.perf_counter()

import sys
import heapq

def main():
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
        
        pq = [(grid[0], 0)]
        
        # Armazenar as funções em variáveis locais economiza tempo de busca de namespace
        heappop = heapq.heappop
        heappush = heapq.heappush
        
        dest = size - 1
        
        while pq:
            d, u = heappop(pq)
            
            if u == dest:
                results.append(str(d))
                break
                
            if d > dist[u]:
                continue
                
            # Coordenadas da matriz decodificadas do índice 1D
            r = u // M
            c = u % M
            
            # Loop Unrolling: Verificar as 4 direções manualmente
            if r > 0:           # Cima
                v = u - M
                cost = d + grid[v]
                if cost < dist[v]:
                    dist[v] = cost
                    heappush(pq, (cost, v))
            if r < N - 1:       # Baixo
                v = u + M
                cost = d + grid[v]
                if cost < dist[v]:
                    dist[v] = cost
                    heappush(pq, (cost, v))
            if c > 0:           # Esquerda
                v = u - 1
                cost = d + grid[v]
                if cost < dist[v]:
                    dist[v] = cost
                    heappush(pq, (cost, v))
            if c < M - 1:       # Direita
                v = u + 1
                cost = d + grid[v]
                if cost < dist[v]:
                    dist[v] = cost
                    heappush(pq, (cost, v))
                    
    print('\n'.join(results))

if __name__ == '__main__':
    startup_end_time = time.perf_counter()
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Tempo de carregamento (parsing/imports): {startup_end_time - startup_start_time:.6f} segundos", file=sys.stderr)
    print(f"Tempo de execução: {end_time - start_time:.4f} segundos", file=sys.stderr)
