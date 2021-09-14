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
 
#primechecker
def prime_checker(number):
  flag=0
  r=(int(number/2)+1)
  for i in range(2,r):
    if(number%i==0):
      flag=1
      break
  if(flag==0):
    print("Prime")
  elif(flag==1):
    print("Not Prime")
n = int(input("Check this number: "))
prime_checker(number=n)


#code1
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
  new=""
  for i in range(len(text)):
    for j in range(len(alphabet)):
      if text[i]==alphabet[j]:
       new=new+alphabet[(j+shift)%26]
  print(f"The encoded text is {new}")

encrypt(text,shift)

