import numpy as np





focallength = 256

sep = 2

offset = np.array([383.5, 205, 0])


#UR
with open('UR0.txt') as f0:
    UR0 = f0.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
UR0 = [x.strip() for x in UR0]
print('UR')
print('Data size is :' +str(np.shape(UR0)))

with open('UR1.txt') as f1:
    UR1 = f1.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
UR1 = [x.strip() for x in UR1]

print( str(np.shape(UR1)))

#UL
with open('UL0.txt') as f0:
    UL0 = f0.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
UL0 = [x.strip() for x in UL0]
print('UL')
print(np.shape(UL0))

with open('UL1.txt') as f1:
    UL1 = f1.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
UL1 = [x.strip() for x in UL1]

print(np.shape(UL1))



#DL
with open('DL0.txt') as f0:
    DL0 = f0.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
DL0 = [x.strip() for x in DL0]
print('DL')
print(np.shape(DL0))

with open('DL1.txt') as f1:
    DL1 = f1.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
DL1 = [x.strip() for x in DL1]

print(np.shape(DL1))


#DR
with open('DR0.txt') as f0:
    DR0 = f0.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
DR0 = [x.strip() for x in DR0]
print('DR')
print(np.shape(DR0))

with open('DR1.txt') as f1:
    DR1 = f1.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
DR1 = [x.strip() for x in DR1]

print(np.shape(DR1))









#Python code to make value int for x coor
# Python code to convert string to list
def convertx(string):
    li = list(string.split(","))
    a = li[0]
    a = round(float(a[1:]))
    a = int(a)
    return a

#Python code to make value int for x coor
def converty(string):
    li = list(string.split(","))
    a = li[1]
    a = round(float(a))
    a = int(a)
    return a
#obtained the 2d vector
def make2d(x):
    xcoord = convertx(x)
    ycorrd = converty(x)

    position = np. array([xcoord, ycorrd, focallength])
    position = position - offset

    position = position
    return position

datanumber =  0
datasetUR0 = np.array([None, None, None])
datasetUL0 = np.array([None, None, None])
datasetDR0 = np.array([None, None, None])
datasetDL0 = np.array([None, None, None])


datasetUR1 = np.array([None, None, None])
datasetUL1 = np.array([None, None, None])
datasetDR1 = np.array([None, None, None])
datasetDL1 = np.array([None, None, None])


while datanumber <= np.shape(UR0)[0]-1:


    positionUR0 = make2d(UR0[datanumber])
    positionUL0 = make2d(UL0[datanumber])

    positionDR0 = make2d(DR0[datanumber])
    positionDL0 = make2d(DL0[datanumber])


    positionUR1 = make2d(UR1[datanumber])
    positionUL1 = make2d(UL1[datanumber])
    positionDR1 = make2d(DR1[datanumber])
    positionDL1 = make2d(DL1[datanumber])

    ratioUR = sep / (positionUR1[0]- positionUR0[0])
    ratioUL = sep / (positionUL1[0] - positionUL0[0])
    ratioDR = sep / (positionDR1[0] - positionDR0[0])
    ratioDL = sep / (positionDL1[0] - positionDL0[0])

    p3dUR = positionUR0 * -ratioUR

    p3dUL = positionUL0 * -ratioUL


    p3dDL = positionDL0 * -ratioDL

    p3dDR = positionDR0 * -ratioDR


    n1 = p3dUR - p3dDL
    n2 = p3dUL - p3dDR
    ncross = np.cross(n1, n2)
    print(p3dUR, p3dDL)
    print(n1, n2)
    print(ncross)


    datasetUR0 = np.vstack((datasetUR0, p3dUR))
    datasetUL0 = np.vstack((datasetUL0, p3dUL))
    datasetDR0 = np.vstack((datasetDR0, p3dDR))
    datasetDL0 = np.vstack((datasetDR0, p3dDL))
    # datasetUR1 = np.vstack((datasetUR1, positionUR1))
    # datasetUL1 = np.vstack((datasetUL1, positionUL1))
    # datasetDR1 = np.vstack((datasetDR1, positionDR1))
    # datasetDL1 = np.vstack((datasetDL1, positionDL1))



    datanumber+=1

#     print(datanumber, p3dUR)
# #
# #
# # print(datasetUL0)



