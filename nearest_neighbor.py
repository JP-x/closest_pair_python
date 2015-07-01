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
coord_by_x = []
#coord_by_y = []
#open file (arg1)
test_data = open(arg1, 'r')
#go through each line of file
for line in test_data:
    #grab line from file and convert to list of float
    coord_xy = map(float, line.split())
    #add the coordinates to list
    coord_by_x.append(coord_xy)
    #coord_by_y.append(coord_xy)
    #print(coord_xy)
    num_pts += 1

test_data.close()
#################################
#################################

#############################
# SORT LIST BY X COORDINATE #
#############################
coord_by_x.sort(key=lambda elem: elem[0])
#############################
# SORT LIST BY Y COORDINATE #
#############################
#coord_by_y.sort(key=lambda elem: elem[1])

#print(coord_by_x)
#print("\n")
#print(coord_by_y)

#################################
# CALCULATE MIN DISTANCE (BRUTE)#
#################################
def brute_closestneighbor(total_pts):
#initialize closest neighbor to infinity
    min_dis = float("inf")
    
    for i in range(0,total_pts):
        x1 = coord_by_x[i][0]
        y1 = coord_by_x[i][1]
    #print("COORD1:" + str(x1) + " " +  str(y1))
        for j in range(i+1,total_pts):
            x2 = coord_by_x[j][0]
            y2 = coord_by_x[j][1]
       #print("COORD2:" + str(x2) + " " + str(y2))
            cur_dis = calcDistance(x1,y1,x2,y2)
            if cur_dis < min_dis:
                min_dis = cur_dis

    return min_dis

#list passed in is already sorted
#pass in lists sorted by X coord
def get_medianX(sorted_list):
    size = len(sorted_list)
    if size < 1:
            return None
    if size %2 == 1:
            #return x coord of middle coord
            return sorted_list[((size+1)/2)-1][0]
    else:
            #return calculated median
            leftx = sorted_list[(size/2)-1][0]
            rightx = sorted_list[(size/2)][0]
            return float(leftx+rightx)/2.0
            

#pass in lists sorted by Y coord
def get_medianY(sorted_list):
    size = len(sorted_list)
    if size < 1:
            return None
    if size %2 == 1:
            #return x coord of middle coord
            return sorted_list[((size+1)/2)-1][1]
    else:
            #return calculated median
            lefty = sorted_list[(size/2)-1][1]
            righty = sorted_list[(size/2)][1]
            return float(lefty+righty)/2.0



###############################################
# CALCULATE MIN DISTANCE (DIVIDE AND CONQUER) #
###############################################
def closest_neighbor_DaC(sortX):
    #get number of coord in X
    numrows = len(sortX)
    #if data set small enough use brute closestneighbor
    if numrows <= 3:
        return brute_closestneighbor(numrows)
    
    #divide pts in sortX into two subset
    median = get_medianX(sortX)
    
    #split sorted list of x coords in half
    sub_leftx = [] 
    #sortX[:numrows/2]
    sub_rightx = []
    #sortX[numrows/2:]
    for i in range(0,numrows):
        if sortX[i][0] <= median:
            sub_leftx.append(sortX[i])
        else:
            sub_rightx.append(sortX[i])
    
    #recursive call on left and right half 
    closest_left = closest_neighbor_DaC(sub_leftx)
    closest_right = closest_neighbor_DaC(sub_rightx)
    #sortX is the full list of points
    closest_distance = 0
    if closest_left < closest_right:
        smallest_dis = closest_left
    else:
        smallest_dis = closest_right

    #'Remove' coordinates that lie outside of the 2d wide strip
    #initialize array to be sorted by Y coord
    middle_coords = []
    max_left_dis = median - smallest_dis
    max_right_dis = median + smallest_dis
    
    for j in range(0,numrows):
        if sortX[j][0] > max_left_dis and sortX[j][0] < max_right_dis:
            middle_coords.append(sortX[j])
    
    #sort list of coordinates within middle by Y coordinate        
    middle_coords.sort(key=lambda elem: elem[1])
    
    num_in_window = len(middle_coords)
    
    #go through middle 2d wide window
    # and calculate distances
    for x in range(0,num_in_window):
        coord_x1 = middle_coords[x][0]
        coord_y1 = middle_coords[x][1]
        #maximum of 8 points can lie within middle window
        next_y = x+1
        max_y = x+7
        y = next_y
        while y != max_y and y < num_in_window:
            coord_x2 = middle_coords[y][0]
            coord_y2 = middle_coords[y][1]
            current_dis = calcDistance(coord_x1,coord_y1,coord_x2,coord_y2)
            #set new minimum distance if smaller
            if calcDistance(coord_x1,coord_y1,coord_x2,coord_y2) < smallest_dis:
                smallest_dis = current_dis
            y = y+1
                
        
    return smallest_dis


##############################################
##### GET CLOSEST NEIGHBOR ###################
##############################################
#closest_neigh = brute_closestneighbor(num_pts)
closest_neigh = closest_neighbor_DaC(coord_by_x)

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
print("CLOSEST_NEIGHBOR: " + str(closest_neigh))
print("Execution Time: %s \n " % end_time)
