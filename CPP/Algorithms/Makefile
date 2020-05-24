output: main.o arrays.o linkedlist.o search.o bfs_dfs_topo.cpp tree.cpp 
	g++ main.o arrays.o linkedlist.o search.o bfs_dfs_topo.o tree.o -o output 

main.o: main.cpp
	g++ -c main.cpp

arrays.o: arrays.cpp
	g++ -c arrays.cpp

search.o: search.cpp
	g++ -c search.cpp

linkedlist.o: linkedlist.cpp
	g++ -c linkedlist.cpp

bfs_dfs_topo.o: bfs_dfs_topo.cpp
	g++ -c bfs_dfs_topo.cpp

tree.o: tree.cpp
	g++ -c tree.cpp

clean:
	rm *.o output