import turtle as t
import random as r
colors  = ["yellow","white"] #태양의 코로나 부분 색 선택을 위한 배열


t.bgcolor("black")#배경색 검정색 지정
t.speed(0)#가장 빠른 속도의 거북이
t.sety(-150)#거북이 위치를 y좌표상에서 -50만큼 이동시켜 화면 정중앙에 위치 시킴니다.
t.st()
def drawcir(n,b):                #태두리 색상에 따라 출력하는 함수 정의
    for i in range(330,340):#for문을 이용하여 반복적으로 다른 크기의 원을 그려 자연스러운 태양 태두리 출력
        t.color(n)
        t.circle(i*b)
        t.up()
        t.lt(90)
        t.fd(330)
        t.down()
        t.lt(90)
        t.color(n)
        t.circle(i*b)

drawcir("white",0.5)#하얀태두리 출력

t.up()#바깥쪽 부분이 더 밝은 빛을 띄는 태양 모습을 고려한 위치이동
t.lt(90)
t.fd(165)
t.lt(90)
t.fd(165)
t.lt(90)


drawcir("yellow",0.49)#노란태두리 출력


t.up()  #태양 내부를 채우기 위한 이동 및 색 지정
t.lt(90)
t.fd(165)
t.down()
t.color("orange")

def fill(a,b,c):# 태양 속 색상 채우는 함수
    for i in range(1,a):#그리기를 원하는 원의 개수,원의 색깔, 간격 새부설정(적은 값으면 넣으면 더 촘촘히 그려진다.)
                        # 등을 이용하여 원의 배열을 만드는 함수 지정
        t.color(b)
        t.circle(80)
        t.left(360/i*c)
fill(160,"red",0.25)#빨간 원의 배열 출력
fill(90,"yellow",0.5)#노란 원의 배열 출력

fill(190,"orange",0.5)#주황색 원의 배열 출력

t.up() #코로나를 그리기 위해 거북이 이동
t.fd(190)
t.lt(90)
t.down()
for i in range(1,100):#코로나를 그리기 위한 for문
    a= r.randint(1,3)# 태양의 코로나 너비를 랜덤으로 설정을 위한 지역변수
    b = r.randint(10,100)# 코로나  생성 위치 랜덤 설정을 위한 지역변수
    c = r.choice(colors)#앞서 정의한 배열을 이용하여 하얀색,노랑색중 코로나의 색상 무작위 선택을 위한 지역변수
    t.color("black")
    t.circle(190, b)#지름이 190 인 보이지 않는 원(배경 검정색 원도 검정색) 위에 코로나 출력할 위치 무작위 지졍

    t.color(c)#코로나 색상 무작위 지정
    t.right(90)

    t.pensize(a)#코로나 너비 무작위 지정
    t.fd(b)#코로나 길이 무작위 지정
    t.back(b)#하나의 for문에서 랜덤 으로 지정된 값은 같음으로 앞으로 갔던만큼 뒤로 돌아와 다시 보이지 않는 원을 그린다.
    t.lt(90)

t.mainloop() #pycharm 환경에서 작업했을때 turtle 그래픽을 띄어놓은 상태로 유지하기 위한 함수