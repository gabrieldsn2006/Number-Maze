"""
Este é o código que executou dentro do limite de tempo de 3 segundos do URI Online Judge.

Site: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=submit_problem&problemid=870&category=0

Caminho para o print das informações da submissão: evidencias/online_judge_otimizado_py.png

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
    print(f"Total de casos de teste a serem processados: {num_test_cases}\n")
    
    for _ in range(num_test_cases):
        rows = data[idx]
        cols = data[idx+1]
        idx += 2
        
        size = rows * cols
        # Grid unidimensional achatado
        grid = data[idx : idx + size]
        idx += size
        
        print("="*60)
        print(f"INICIANDO CASO DE TESTE {_+1}/{num_test_cases} - Labirinto {rows}x{cols}")
        print(f"Grid (1D achatado): {grid}")
        print("="*60)
        
        # Array de distâncias
        _dist = [2147483647] * size
        _dist[0] = grid[0]
        
        # Algoritmo de Dial: Fila circular com apenas 10 buckets
        # Como o peso máximo é 9, o custo de um vizinho é no máximo d + 9
        buckets = [[] for _ in range(10)]
        buckets[grid[0] % 10].append(0)
        
        d = grid[0]
        target = size - 1
        
        print(f"Distância inicial 'd' = {d}. Célula de origem (0) colocada no bucket {d % 10}")
        
        _grid = grid
        
        while True:
            original_d = d
            # Pega o bucket da distância atual 'd'
            b = buckets[d % 10]
            
            # Se o bucket estiver vazio, avança a distância d
            while not b:
                d += 1
                b = buckets[d % 10]
                
            if d > original_d:
                print(f"\n[Avanço de Distância] Sem células nas distâncias anteriores. 'd' avançou para {d}.")
                
            u = b.pop()
            print(f"\n-> [Distância {d}] Retirando célula índice {u} do bucket {d % 10}")
            
            # Verifica se essa entrada na fila já ficou obsoleta (Lazy Deletion)
            if _dist[u] < d:
                print(f"   (Ignorada! A célula {u} já tem um caminho melhor salvo com custo {_dist[u]})")
                continue
                
            # Parada antecipada: chegamos ao final
            if u == target:
                print(f"   *** DESTINO ALCANÇADO! Célula final {u}. Custo mínimo: {d} ***\n")
                out.append(str(d))
                break
                
            print(f"   Analisando vizinhos da célula {u}:")
            # --- Expansão dos Vizinhos (Flat Array) ---
            
            # Cima
            if u >= cols:
                v = u - cols
                nd = d + _grid[v]
                print(f"      - [Cima] Vizinho índice {v} | Novo custo: {nd} (Custo atual salvo: {_dist[v]})", end="")
                if nd < _dist[v]:
                    print(f" -> MELHOR! Atualizou e colocou no bucket {nd % 10}")
                    _dist[v] = nd
                    buckets[nd % 10].append(v)
                else:
                    print(" -> Descartado")
            # Baixo
            if u < size - cols:
                v = u + cols
                nd = d + _grid[v]
                print(f"      - [Baixo] Vizinho índice {v} | Novo custo: {nd} (Custo atual salvo: {_dist[v]})", end="")
                if nd < _dist[v]:
                    print(f" -> MELHOR! Atualizou e colocou no bucket {nd % 10}")
                    _dist[v] = nd
                    buckets[nd % 10].append(v)
                else:
                    print(" -> Descartado")
            # Esquerda
            if u % cols != 0:
                v = u - 1
                nd = d + _grid[v]
                print(f"      - [Esquerda] Vizinho índice {v} | Novo custo: {nd} (Custo atual salvo: {_dist[v]})", end="")
                if nd < _dist[v]:
                    print(f" -> MELHOR! Atualizou e colocou no bucket {nd % 10}")
                    _dist[v] = nd
                    buckets[nd % 10].append(v)
                else:
                    print(" -> Descartado")
            # Direita
            if (u + 1) % cols != 0:
                v = u + 1
                nd = d + _grid[v]
                print(f"      - [Direita] Vizinho índice {v} | Novo custo: {nd} (Custo atual salvo: {_dist[v]})", end="")
                if nd < _dist[v]:
                    print(f" -> MELHOR! Atualizou e colocou no bucket {nd % 10}")
                    _dist[v] = nd
                    buckets[nd % 10].append(v)
                else:
                    print(" -> Descartado")
            
            print(_dist)

    # Imprime todas as respostas de uma vez
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    startup_end_time = time.perf_counter()
    start_time = time.perf_counter()
    solve()
    end_time = time.perf_counter()
    print(f"Tempo de carregamento (parsing/imports): {startup_end_time - startup_start_time:.6f} segundos", file=sys.stderr)
    print(f"Tempo de execução: {end_time - start_time:.4f} segundos", file=sys.stderr)