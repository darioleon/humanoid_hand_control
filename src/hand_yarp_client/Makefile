all: hand_yarp

hand_yarp: hand_yarp.o
	g++ hand_yarp.o -o hand_yarp -lardcom -lrt -lpthread -lYARP_OS -lYARP_init

hand_yarp.o: hand_yarp.cpp
	g++ -c hand_yarp.cpp

clean:
	rm -f *.o hand_yarp
