def agepass(my,bro,bf):
    print(f"My age: {my}")
    print(f"My brother's age: {bro}")
    print(f"My boyfriend's age: {bf}")
    print("\n")
agepass(20,30,22)
agepass(30,22,20) #wrong 
agepass(bro=30,bf=22,my=20)

#painting wall
def paint_calc(height,width,cover):
  import math
  print(f"You'll need {math.ceil((height*width)/cover)} cans of paint.")
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
 

