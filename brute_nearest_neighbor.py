import sys
import time
import math

#calculate distance between two points
def calcDistance(x1,y1,x2,y2):
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return dist

#test for any command line arguments
#remove .txt extension from argument
try:
 arg1 = sys.argv[1]
 print("Now testing: " + arg1 + "\n")
 outputfilename  = arg1
 outputfilename = outputfilename.replace(".txt","")
 #print("parsedname: ")
 #print(outputfilename)
except:
  print("Error: No test file given.\n")
  sys.exit(1)


begin_time = time.time()
num_pts = 0

##################################
#### POPULATE COORDINATE LIST#####
##################################
#initialize list
coord = []
#open file (arg1)
test_data = open(arg1, 'r')
#go through each line of file
for line in test_data:
    #grab line from file and convert to list of float
    coord_xy = map(float, line.split())
    #add the coordinates to list
    coord.append(coord_xy)
    #print(coord_xy)
    num_pts += 1

test_data.close()
#################################
#################################

#############################
# SORT LIST BY X COORDINATE #
#############################
coord.sort(key=lambda elem: elem[0])
print(coord)


#################################
# CALCULATE MIN DISTANCE (BRUTE)#
#################################
def brute_closestneighbor(total_pts):
#initialize closest neighbor to infinity
    min_dis = float("inf")
    
    for i in range(0,total_pts):
        x1 = coord[i][0]
        y1 = coord[i][1]
    #print("COORD1:" + str(x1) + " " +  str(y1))
        for j in range(i+1,total_pts):
            x2 = coord[j][0]
            y2 = coord[j][1]
       #print("COORD2:" + str(x2) + " " + str(y2))
            cur_dis = calcDistance(x1,y1,x2,y2)
            if cur_dis < min_dis:
                min_dis = cur_dis

    return min_dis


##############################################
##### GET CLOSEST NEIGHBOR ###################
##############################################
closest_neigh = brute_closestneighbor(num_pts)

#########################
# WRITE RESULTS TO FILE #
#########################
#getopt.getopt(args,options[,longoptions])
#openfile distance.txt and give permissions to write to file
outputfilename = outputfilename + "_distance.txt"
distance_file = open(outputfilename,'w+');
#write to file distance.txt
#convert distance to string and write to file
distance_file.write(str(closest_neigh))
#close file distance.txt
distance_file.close()

#calculate execution time and print
#end_time = round(time.time() - begin_time, 2)
#use round to not get crazy decimals for time
end_time = time.time() - begin_time
print("Execution Time: %s \n " % end_time)

print("CLOSEST_NEIGHBOR: " + str(closest_neigh) + "\n")
