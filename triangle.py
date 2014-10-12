import json

def point_in_triangle(testPoint,triangle):
  
  for x in [1,2,3]:
    index = x - 1 
    coor1 = triangle[index]
    if index == 2:
      index = 0
    else:
      index = index + 1
    coor2 = triangle[index]
    if index == 2:
      index = 0
    else:
      index = index + 1  
    coor3 = triangle[index]

    a = coor1[1] - coor2[1]
    b = coor2[0] - coor1[0]
    c = coor1[0] * coor2[1] - coor2[0] * coor1[1]

    if (a * coor3[0] + b * coor3[1] + c) * (a * testPoint[0] + b * testPoint[1] + c) < 0:
      print "false"
      return
      
  print "true"
  return

triangle = raw_input("Enter the coordinates of the triangle:")
#print triangle
tri = json.loads(triangle)

testPoint = raw_input("Enter the coordinate you wanna test:")
test = json.loads(testPoint)

point_in_triangle(test, tri)