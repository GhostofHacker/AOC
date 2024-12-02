##There's two lists containing the locations of places. Its unique name is location IDs
##Pair the left and right smallest numbers with each other. Then find the distance between them.
##Then add all the distance in to one to figure out how far all is!
## 3 - 4 = 1; 4 - 7 = 3; || 1 + 3 = 4! 4 is the total of the distance!

cal_doc = open('2024_day_1_input.txt', 'r')

def part_one():
    cordinateID_1 = ''; cordinateID_2 = ''
    list_1 = []; list_2 = []

    for line in cal_doc:
        for i in range(0, 5):
            cordinateID_1 = cordinateID_1 + line[i]
        for i in range(8, 13):
            cordinateID_2 = cordinateID_2 + line[i]

        list_1.append(int(cordinateID_1))
        list_2.append(int(cordinateID_2))

        cordinateID_1 = ''; cordinateID_2 = ''

    print(list_2)

part_one()
