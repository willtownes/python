height = 10
width = 5

for j in range(1,height+1):
    for i in range(1,width+1):
        if i == 1:
            cell = "cell_" + str(j) + "_" + str(i)
            print cell,
        elif i == (width):
            cell = "\t" + "cell_" + str(j) + "_" + str(i)
            print cell
        else:
            cell = "\t" + "cell_" + str(j) + "_" + str(i)
            print cell,
