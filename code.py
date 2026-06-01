import sys
def solve(input_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        input_data = f.read().split()
    
    data = list(map(int, input_data))
    num_test_cases = data[0]
    idx = 1
    out = []
    
    for _ in range(num_test_cases):
        rows, cols = data[idx], data[idx+1]
        idx += 2
        size = rows * cols
        grid = data[idx : idx + size]
        idx += size
        _dist = [2147483647] * size
        _dist[0] = grid[0]
        buckets = [[] for _ in range(10)]
        buckets[grid[0] % 10].append(0)
        d      = grid[0]
        target = size - 1
        _grid  = grid
        
        while True:
            b = buckets[d % 10]
            while not b:
                d += 1; b = buckets[d % 10]
            u = b.pop()
            
            if _dist[u] < d: continue
                
            if u == target:
                out.append(str(d)); break
        
            if u >= cols: # Cima
                v  = u - cols
                nd = d + _grid[v]
                if nd < _dist[v]:
                    _dist[v] = nd
                    buckets[nd % 10].append(v)
            
            if u < size - cols: # Baixo
                v = u + cols
                nd = d + _grid[v]
                if nd < _dist[v]:
                    _dist[v] = nd
                    buckets[nd % 10].append(v)
            
            if u % cols != 0: # Esquerda
                v = u - 1
                nd = d + _grid[v]
                if nd < _dist[v]:
                    _dist[v] = nd
                    buckets[nd % 10].append(v)
            
            if (u + 1) % cols != 0: # Direita
                v = u + 1
                nd = d + _grid[v]
                if nd < _dist[v]:
                    _dist[v] = nd
                    buckets[nd % 10].append(v)
    sys.stdout.write('\n'.join(out) + '\n')

solve("dados/entrada_do_problema.txt")