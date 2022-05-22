import turtle

turtle.TurtleScreen._RUNNING=True

base_rule = ["+", 'F', '-', '-', "F", "+"]

def generateGm(depth):
    prev = base_rule
    for i in range(depth):
        ans = []
        for j in range(len(prev)):
            if prev[j] == 'F':
                ans+=base_rule
            else:
                ans.append(prev[j])
        print(ans)
        prev = ans
    
    return prev 

def drawShape(gm):
    print(gm)
    for g in gm:
        if g == 'F':
            t.forward(20)
            print("forward")
        elif g == '-':
            t.left(45)
            print("left")
        elif g == '+':
            t.right(45)
            print("right")


if __name__ == '__main__':
    t = turtle.Turtle()
    gm = generategm(2)
    drawShape(gm)
    turtle.done()