import pgzrun
WIDTH=1000
HEIGHT=600
question = []
rect = Rect(100,50,800,100)
ans_1 = Rect (61,175,325,175)
ans_2 = Rect (600,175,325,175)
ans_3 = Rect (61,400,325,175)
ans_4 = Rect (600,400,325,175)
timer = Rect (405,175,175,175)
not_a_skip_box = Rect (405,400,175,175)
def draw():
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(rect,"yellow")
    screen.draw.filled_rect(ans_1,"yellow")
    screen.draw.filled_rect(ans_2,"yellow")
    screen.draw.filled_rect(ans_3,"yellow")
    screen.draw.filled_rect(ans_4,"yellow")
    screen.draw.filled_rect(timer,"purple")
    screen.draw.filled_rect(not_a_skip_box,"purple")
    screen.draw.textbox(question[0],rect,color = "blue")
def quedtions():
    file = open("txt_a.txt","r")
    global question
    for i in file:
        question.append(i)
quedtions()
print(question)
pgzrun.go()