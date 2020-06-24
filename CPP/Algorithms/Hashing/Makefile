output: main.o hashing.o
	g++ main.o hashing.o -o output

main.o: main.cpp
	g++ -c main.cpp

hashing.o: hashing.cpp
	g++ -c hashing.cpp
	
clean:
	rm *.o output