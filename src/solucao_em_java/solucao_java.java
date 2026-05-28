package solucao_em_java;
import java.io.InputStream;
import java.io.IOException;
import java.util.PriorityQueue;
import java.util.Arrays;

class Main {

    // Classe para representar os nós na Fila de Prioridade
    static class Node implements Comparable<Node> {
        int u, cost;

        public Node(int u, int cost) {
            this.u = u;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node other) {
            return Integer.compare(this.cost, other.cost);
        }
    }

    public static void main(String[] args) throws IOException {
        // long startTime = System.nanoTime();

        FastScanner sc = new FastScanner(System.in);
        StringBuilder out = new StringBuilder();

        int t = sc.nextInt();
        if (t == -1) return;

        while (t-- > 0) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int size = n * m;

            int[] grid = new int[size];
            for (int i = 0; i < size; i++) {
                grid[i] = sc.nextInt();
            }

            int[] dist = new int[size];
            Arrays.fill(dist, Integer.MAX_VALUE);
            dist[0] = grid[0];

            PriorityQueue<Node> pq = new PriorityQueue<>();
            pq.add(new Node(0, grid[0]));

            int dest = size - 1;

            while (!pq.isEmpty()) {
                Node curr = pq.poll();
                int u = curr.u;
                int d = curr.cost;

                if (u == dest) {
                    out.append(d).append("\n");
                    break;
                }

                if (d > dist[u]) continue;

                int r = u / m;
                int c = u % m;

                // Cima
                if (r > 0) {
                    int v = u - m;
                    int newCost = d + grid[v];
                    if (newCost < dist[v]) {
                        dist[v] = newCost;
                        pq.add(new Node(v, newCost));
                    }
                }
                // Baixo
                if (r < n - 1) {
                    int v = u + m;
                    int newCost = d + grid[v];
                    if (newCost < dist[v]) {
                        dist[v] = newCost;
                        pq.add(new Node(v, newCost));
                    }
                }
                // Esquerda
                if (c > 0) {
                    int v = u - 1;
                    int newCost = d + grid[v];
                    if (newCost < dist[v]) {
                        dist[v] = newCost;
                        pq.add(new Node(v, newCost));
                    }
                }
                // Direita
                if (c < m - 1) {
                    int v = u + 1;
                    int newCost = d + grid[v];
                    if (newCost < dist[v]) {
                        dist[v] = newCost;
                        pq.add(new Node(v, newCost));
                    }
                }
            }
        }
        System.out.print(out);

        // long endTime = System.nanoTime();
        // System.out.printf("Tempo de execução: %.4f segundos\n", (endTime - startTime) / 1e9);
    }

    // Classe para I/O Rápido em Java (evita o Time Limit Exceeded)
    static class FastScanner {
        private InputStream in;
        private byte[] buffer = new byte[1 << 16];
        private int head, tail;

        public FastScanner(InputStream in) {
            this.in = in;
        }

        public int nextInt() throws IOException {
            int c = read();
            while (c <= 32) {
                if (c == -1) return -1;
                c = read();
            }
            int res = 0;
            while (c > 32) {
                if (c < '0' || c > '9') throw new RuntimeException();
                res = res * 10 + c - '0';
                c = read();
            }
            return res;
        }

        private int read() throws IOException {
            if (head >= tail) {
                head = 0;
                tail = in.read(buffer, 0, buffer.length);
                if (tail <= 0) return -1;
            }
            return buffer[head++];
        }
    }
}
