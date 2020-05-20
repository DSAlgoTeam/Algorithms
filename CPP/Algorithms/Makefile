output: main.o arrays.o linkedlist.o search.o
	g++ main.o arrays.o linkedlist.o search.o -o output

main.o: main.cpp
	g++ -c main.cpp

arrays.o: arrays.cpp
	g++ -c arrays.cpp

search.o: search.cpp
	g++ -c search.cpp

linkedlist.o: linkedlist.cpp
	g++ -c linkedlist.cpp

clean:
	rm *.o output