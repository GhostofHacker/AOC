##There's two lists containing the locations of places. Its unique name is location IDs
##Pair the left and right smallest numbers with each other. Then find the distance between them.
##Then add all the distance in to one to figure out how far all is!
## 3 - 4 = 1; 4 - 7 = 3; || 1 + 3 = 4! 4 is the total of the distance!

cal_doc = open('2024_day_1_input.txt', 'r')
list_1 = []; list_2 = []
totalNum = 0; totalDistance = 0; similarity_score = 0;

def sortedList():
    cordinateID_1 = ''; cordinateID_2 = ''
    global totalNum

    for line in cal_doc:
        for i in range(0, 5):
            cordinateID_1 = cordinateID_1 + line[i]
        for i in range(8, 13):
            cordinateID_2 = cordinateID_2 + line[i]

        list_1.append(int(cordinateID_1))
        list_2.append(int(cordinateID_2))

        cordinateID_1 = ''; cordinateID_2 = ''

        totalNum = totalNum + 1
    
    list_1.sort()
    list_2.sort()

def part_one():
    sortedList()
    global totalDistance

    for x in range(0, totalNum):
        if(list_1[x] - list_2[x] < 0):
            totalDistance = totalDistance + int(-1 * (list_1[x] - list_2[x]))
        if(list_1[x] - list_2[x] >= 0):
            totalDistance = totalDistance + list_1[x] - list_2[x]

    print('Total Distance is:', totalDistance)


##This time well do similarity check! How? Well...
##Check how many time locationID's in the left list appeared in the right list.
##3 appeared 3 times then 3 * 3 = 9 add to the similarity score.
##4 appeared 0 times then 4 * 0 = 0 add to the similarity score.
##Answer is the sum of similarty scores!  

def part_two():
    sortedList()
    global totalNum
    similarity_score = 0; similiar_count = 0 
        
    for l in list_1:
        for r in list_2:
            if(l == r):
                similiar_count = similiar_count + 1

        similarity_score = similarity_score + (l * similiar_count)
        similiar_count = 0     

    print('Similarity Score is: ', similarity_score)

##To get the answer uncomment the function!
## part_one()
part_two()
