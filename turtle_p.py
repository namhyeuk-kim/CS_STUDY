import turtle
import random

## 함수 선언 부분 ##

# screenLeftClick 마우스 왼쪽을 누르면 거북이가 클릭한 지점까지 임의의 색상으로 선을 그리면서 따라오도록 하는 함수
# screenRightClick 마우스 오른쪽을 누르면 거북이가 클릭한 지점까지 선을 그리지 않고 이동만 하도록 하는 함수
# screenMidClick 마우스 가운데 버튼을 누르면 거북이가 임의로 크기를 확대 또는 축소하는 함수
# 마우스 가운데 버튼을 누를 때는 선의 색상이 임의로 선택되도록 하고 거북이의 크기도 1~9까지 임의로 설저오디도록 함


# 왼쪽,중앙 통합.

def screenLeftClick(x, y):
    global r, g, b
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x, y)


def screenRightClick(x, y):
    turtle.penup()
    turtle.goto(x, y)


##변수 선언 부분##
pSize = 10
r, g, b = 0.0, 0.0, 0.0

## 메인 코드 부분 ##
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)

turtle.onscreenclick(screenRightClick, 3)

turtle.done()
