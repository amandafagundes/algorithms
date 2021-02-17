# MinimumOddPath

The goal is to find the minimum path between the source and destination nodes of a weighted undirected graph. 

The entry must contain in the first line two integers `V` and `E`, where V is the number of nodes and M, the number of edges. The following E lines are composed by three values `u v w`, indicating the weight `w` of the edge `(u,v)`.

This implementation is based on the Dijkstra algorithm with `O(E log E)` complexity.

#### Test case (1):

- Input
7 12
1 2 5
1 3 1
1 4 2
3 2 3
4 3 1
3 6 1
2 7 5
6 2 12
7 6 2
4 5 2
6 5 1
5 7 16

- Output:
4

#### Test case (2):

- Input
7 8
1 2 5
1 3 1
2 4 2
3 4 1
4 5 2
5 6 1
6 2 12
7 5 16

- Output:
:( (Indicating that doesn't exists odd path)