# Number-Maze

## Link
https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=submit_problem&problemid=870&category=0

## Análise de Complexidade

Para analisarmos a complexidade de tempo (Big-O) das implementações, vamos primeiro definir as variáveis que compõem o problema:

*   **$T$**: Número de casos de teste.
*   **$V$**: Número total de vértices no labirinto. Como é uma matriz $N \times M$, temos **$V = N \times M$**.
*   **$E$**: Número total de arestas. Em um grid 2D onde andamos para cima, baixo, esquerda e direita, cada vértice tem no máximo 4 vizinhos. Logo, $E \approx 4V$. Portanto, podemos dizer que **$E = O(V)$**.
*   **$W$**: O peso máximo de uma célula (neste problema específico, os números variam de 0 a 9, então **$W = 9$**).

### 1. `main.py` (Dijkstra Tradicional com Fila de Prioridade)
**Big-O Total: $\mathcal{O}(T \times V \log V)$**

*   **Leitura e construção da matriz:** Percorrer os dados de entrada para montar o grid leva $\mathcal{O}(V)$.
*   **Fila de Prioridade (`heapq`):** No pior caso, o algoritmo insere e extrai vértices do `heapq`. A inserção/remoção em um *Binary Heap* custa $\mathcal{O}(\log V)$.
*   Como processamos até $E$ vizinhos e os adicionamos à fila, o custo do laço principal do Dijkstra é $\mathcal{O}(E \log V)$.
*   Sabendo que $E \approx 4V$, o custo de cada caso de teste se simplifica para $\mathcal{O}(V \log V)$.
*   Multiplicando pelo número de casos de teste $T$, chegamos à complexidade final.

### 2. `online_judge_otimizado.py` (Algoritmo de Dial / Fast I/O)
**Big-O Total: $\mathcal{O}(T \times V)$** *(Complexidade Linear)*

*   **Leitura Rápida (Fast I/O):** A leitura usando `sys.stdin.read().split()` processa a entrada inteira de uma só vez. Fazer o parser de todo o texto leva $\mathcal{O}(T \times V)$.
*   **Algoritmo de Dial:** Em vez de usar um `heapq` que custa $\log V$ por operação, o código utiliza 10 listas (buckets) simulando uma fila circular. 
*   Inserir um elemento num bucket (`append`) custa $\mathcal{O}(1)$.
*   Remover um elemento de um bucket (`pop`) custa $\mathcal{O}(1)$.
*   O algoritmo gasta um pequeno tempo extra avançando o cursor de distância `d` para achar o próximo bucket não vazio. No pior dos casos, esse cursor avança até a distância máxima possível, que é limitada por $V \times W$.
*   A complexidade teórica do algoritmo de Dial para um único caso de teste é $\mathcal{O}(E + V \times W)$. Como $E \approx 4V$ e $W = 9$ (uma constante muito pequena), a equação vira $\mathcal{O}(4V + 9V) = \mathcal{O}(13V)$, que na notação Big-O é simplificada para **$\mathcal{O}(V)$**.