# point = 1,7
# print(point[0])
# print(point[1])

# pointA = (1,7)
# print(pointA[0])


# th =  "thal" ,5 ,60 ,10
# print(th[1] + th[2]+th[3])



def  distance(pointA , pointB):
    return (pointA[0] - pointB[0])**2 + (pointA[1] - pointB[1])**2


def  distance2(x1 ,x2 ,y1 ,y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**.5


pointA = (1,7)
pointB = (1,10)
d = distance(pointA,pointB)
print(d)

d2 = distance2(1 , 2 , 1 , 2)
print(d2)



