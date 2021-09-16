def fun():
    print("This is a function.")
fun()

#hurdle 3
def turn_right():
     turn_left();
     turn_left();
     turn_left();
def jump():
    turn_left();
    move();
    turn_right();
    move();
    turn_right();
    move();
    turn_left();
while(at_goal()!=True):
    if wall_in_front()==True:
        jump();
    else:
        move();

#hurdle 4
def turn_right():
     turn_left();
     turn_left();
     turn_left();
def check():
     while(wall_on_right()==True):
        if not wall_in_front():
            move();
        else:
            turn_left();
def jump():
    turn_left();
    check();
    turn_right();
    move();
    turn_right();
    check();
while(at_goal()!=True):
    if wall_in_front()==True:
        jump();
    else:
        move();
   

    
    
   
   
    
   
