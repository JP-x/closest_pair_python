all: main


#target    #components  #nextline is the comand
#main is the name of the target
#next instruction is how to compile
#link and produce the executable main
main:
	python nearest_neighbor.py input_10.txt

btest1:
	python brute_nearest_neighbor.py input_10.txt

btest2:
	python brute_nearest_neighbor.py input_100.txt

btest3:
	python brute_nearest_neighbor.py input_10e5.txt
 
btest4:
	python brute_nearest_neighbor.py input_10e6.txt


test1:
	python nearest_neighbor.py input_10.txt

test2:
	python nearest_neighbor.py input_100.txt

test3:
	python nearest_neighbor.py input_10e5.txt
 
test4:
	python nearest_neighbor.py input_10e6.txt


clean:
	rm -rf *_distance.txt
#rm == remove file
#-r = remove the contents of directories recursively
#-f = force   ignore nonexistent files, never prompt
# *.out - any .out file
#*.o any object file
