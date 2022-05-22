import turtle

turtle.TurtleScreen._RUNNING=True

base_rule = ['F', 'X']
ruleX = ['X', '+', 'Y', 'F', '+']
ruleY = ['-', 'F', 'X', '-', 'Y']


def generategm(depth):
    prev = base_rule
    for i in range(depth):
        ans = []
        for j in range(len(prev)):
            if prev[j] == 'X':
                ans+=ruleX
            elif prev[j] == 'Y':
                ans+=ruleY
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
            t.left(90)
            print("left")
        elif g == '+':
            t.right(90)
            print("right")


if __name__ == '__main__':
    t = turtle.Turtle()
    gm = generategm(5)
    drawShape(gm)
    turtle.done()

        