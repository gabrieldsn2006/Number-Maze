"""
Este é o código que executou dentro do limite de tempo de 3 segundos do URI Online Judge.

Site: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=submit_problem&problemid=870&category=0

Caminho para o print das informações da submissão: evidencias\online_judge_otimizado_py.png

Código foi feito utilizando uma implementação otimizada do algoritmo de Dijkstra com fila
de prioridade baseada em buckets (Dial's Algorithm) e outras pequenas otimizações.
"""
import sys
import time
startup_start_time = time.perf_counter()
def solve():
    # Fast I/O: lê o arquivo inteiro de uma vez
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # Converte tudo para inteiros a nível de C (extremamente rápido)
    data = list(map(int, input_data))
    if not data:
        return
        
    num_test_cases = data[0]
    idx = 1
    out = []
    
    for _ in range(num_test_cases):
        rows = data[idx]
        cols = data[idx+1]
        idx += 2
        
        size = rows * cols
        # Grid unidimensional achatado
        grid = data[idx : idx + size]
        idx += size
        
        # Array de distâncias
        _dist = [2147483647] * size
        _dist[0] = grid[0]
        
        # Algoritmo de Dial: Fila circular com apenas 10 buckets
        # Como o peso máximo é 9, o custo de um vizinho é no máximo d + 9
        buckets = [[] for _ in range(10)]
        buckets[grid[0] % 10].append(0)
        
        d = grid[0]
        target = size - 1
        
        _grid = grid
        
        while True:
            # Pega o bucket da distância atual 'd'
            b = buckets[d % 10]
            
            # Se o bucket estiver vazio, avança a distância d
            while not b:
                d += 1
                b = buckets[d % 10]
                
            u = b.pop()
            
            # Verifica se essa entrada na fila já ficou obsoleta (Lazy Deletion)
            if _dist[u] < d:
                continue
                
            # Parada antecipada: chegamos ao final
            if u == target:
                out.append(str(d))
                break
                
            # --- Expansão dos Vizinhos (Flat Array) ---
            
            # Cima
            if u >= cols:
                v = u - cols
                nd = d + _grid[v]
                if nd < _dist[v]:
                    _dist[v] = nd
                    buckets[nd % 10].append(v)
            # Baixo
            if u < size - cols:
                v = u + cols
                nd = d + _grid[v]
                if nd < _dist[v]:
                    _dist[v] = nd
                    buckets[nd % 10].append(v)
            # Esquerda
            if u % cols != 0:
                v = u - 1
                nd = d + _grid[v]
                if nd < _dist[v]:
                    _dist[v] = nd
                    buckets[nd % 10].append(v)
            # Direita
            if (u + 1) % cols != 0:
                v = u + 1
                nd = d + _grid[v]
                if nd < _dist[v]:
                    _dist[v] = nd
                    buckets[nd % 10].append(v)

    # Imprime todas as respostas de uma vez
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    startup_end_time = time.perf_counter()
    start_time = time.perf_counter()
    solve()
    end_time = time.perf_counter()
    print(f"Tempo de carregamento (parsing/imports): {startup_end_time - startup_start_time:.6f} segundos", file=sys.stderr)
    print(f"Tempo de execução: {end_time - start_time:.4f} segundos", file=sys.stderr)