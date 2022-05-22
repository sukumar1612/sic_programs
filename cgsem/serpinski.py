import turtle

turtle.TurtleScreen._RUNNING=True

base_rule = ['F','-','G','-','G']
rule1 = ['F','-','G','+','F','+','G','-','F']
rule2 = ['G','G']

def generategm(depth):
    prev = base_rule
    for i in range(depth):
        ans = []
        for j in range(len(prev)):
            if prev[j] == 'F':
                ans+=rule1
            elif prev[j] == 'G':
                ans+=rule2
            elif (prev[j] == '+') or (prev[j] == '-'):
                ans.append(prev[j])
        print(ans)
        prev = ans
    
    return prev 

def drawShape(gm):
    print(gm)
    for g in gm:
        if g == 'F' or g == 'G':
            t.forward(20)
            print("forward")
        elif g == '-':
            t.left(120)
            print("left")
        elif g == '+':
            t.right(120)
            print("right")


if __name__ == '__main__':
    t = turtle.Turtle()
    gm = generategm(2)
    drawShape(gm)
    turtle.done()

        