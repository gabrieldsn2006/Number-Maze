import time
# Inicia o cronômetro assim que o arquivo começa a ser lido pelo Python
startup_start_time = time.perf_counter()

import heapq
import sys
import os

def solve():
    # Caminho relativo para o arquivo de entrada
    file_path = "dados/entrada_do_problema.txt"
    
    try:
        with open(file_path) as f:
            input_data = f.read().split()
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {file_path}")
        return
        
    if not input_data:
        return
    
    num_mazes = int(input_data[0])
    idx = 1
    
    out = []
    
    for _ in range(num_mazes):
        N = int(input_data[idx])
        M = int(input_data[idx+1])
        idx += 2
        
        # Preenchendo a matriz do labirinto
        grid = []
        for _ in range(N):
            row = [int(x) for x in input_data[idx:idx+M]]
            grid.append(row)
            idx += M
            
        
        pq = [(0, 0, 0)]
        dist = [[float('inf')] * M for _ in range(N)]
          
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while pq:
            d, r, c = heapq.heappop(pq)
            
            # Se chegamos ao canto inferior direito, o caminho de menor custo foi encontrado
            if r == N - 1 and c == M - 1:
                out.append(str(d))
                break
                
            # Evitar reprocessamento de caminhos que já não são mais curtos
            if d > dist[r][c]:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M:
                    new_cost = d + grid[nr][nc]
                    # Se encontrarmos um caminho mais barato para a célula vizinha, atualizamos
                    if new_cost < dist[nr][nc]:
                        dist[nr][nc] = new_cost
                        heapq.heappush(pq, (new_cost, nr, nc))
                        
    # Imprimir todos os resultados separados por quebra de linha
    if out:
        print('\n'.join(out))

if __name__ == '__main__':
    startup_end_time = time.perf_counter()
    start_time = time.perf_counter()
    solve()
    end_time = time.perf_counter()
    print(f"Tempo de carregamento (parsing/imports): {startup_end_time - startup_start_time:.6f} segundos", file=sys.stderr)
    print(f"Tempo de execução: {end_time - start_time:.4f} segundos", file=sys.stderr)
