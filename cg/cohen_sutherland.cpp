#include<windows.h>
#ifdef __APPLE__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif
#include<bits/stdc++.h>
#include <stdlib.h>

#define SCREEN_WIDTH 640
#define SCREEN_HEIGHT 480

using namespace std;
struct pointPair{
    float x1, y1;
    float x2, y2;
};
struct pointPair wn, ln;
int flag=0;
int cnt=0;

//tbrl

void getLineCodes(vector<int> &p1, int x, int y, struct pointPair &w)
{
    if(y > w.y2)
    {
        p1[0]=1;
    }
    if(y < w.y1)
    {
        p1[1]=1;
    }
    if(x > w.x2)
    {
        p1[2]=1;
    }
    if(x < w.x1)
    {
        p1[3]=1;
    }
}

int OR(vector<int> &p1, vector<int> &p2)
{
    for(int i=0;i<4;i++)
    {
        if(p1[i]==1 || p2[i]==1)
        {
            return 0;
        }
    }
    return 1;
}

int AND(vector<int> &p1, vector<int> &p2)
{
    for(int i=0;i<4;i++)
    {
        if(p1[i]==1 && p2[i]==1)
        {
            return 1;
        }
    }
    return 0;
}

int clipLine(struct pointPair &l, struct pointPair &w)
{
    vector<int> p1(4, 0);
    vector<int> p2(4, 0);
    getLineCodes(p1, l.x1, l.y1, w);
    getLineCodes(p2, l.x2, l.y2, w);
    if(AND(p1, p2) || OR(p1, p2))
    {
        cout<<"completely inside or outside"<<endl;
        return -1;
    }
    float m = (l.y2 - l.y1)/(l.x2 - l.x1);
    float c = l.y1 - m*l.x1;
    if(p1[0]==1)
    {
        l.x1 = (w.y2 - c)/m;
        l.y1 = w.y2;
    }
    if(p1[1]==1)
    {
        l.x1 = (w.y1 - c)/m;
        l.y1 = w.y1;
    }
    if(p1[2]==1)
    {
        l.x1 = w.x2;
        l.y1 = w.x2*m + c;
    }
    if(p1[3]==1)
    {
        l.x1 = w.x1;
        l.y1 = w.x1*m + c;
    }

    if(p2[0]==1)
    {
        l.x2 = (w.y2 - c)/m;
        l.y2 = w.y2;
    }
    if(p2[1]==1)
    {
        l.x2 = (w.y1 - c)/m;
        l.y2 = w.y1;
    }
    if(p2[2]==1)
    {
        l.x2 = w.x2;
        l.y2 = w.x2*m + c;
    }
    if(p2[3]==1)
    {
        l.x2 = w.x1;
        l.y2 = w.x1*m + c;
    }

    if((l.x1<w.x1 && l.y1<w.y1) || (l.x1>w.x2 && l.y1>w.y2))
    {
        return -1;
    }
    if((l.x2<w.x1 && l.y2<w.y1) || (l.x2>w.x2 && l.y2>w.y2))
    {
        return -1;
    }
    return 0;
}

void drawWindow(struct pointPair &w)
{
    glBegin(GL_LINE_LOOP);
        glVertex2f(w.x1, w.y1);
        glVertex2f(w.x1, w.y2);
        glVertex2f(w.x2, w.y2);
        glVertex2f(w.x2, w.y1);
    glEnd();
}

void drawLine(struct pointPair &l, struct pointPair &w)
{
    glColor3f(1, 1, 1);
    glBegin(GL_LINES);
        glVertex2f(l.x1, l.y1);
        glVertex2f(l.x2, l.y2);
    glEnd();
    if(clipLine(l, w) == -1)
    {
        return;
    }

    glColor3f(1, 1, 0);
    glBegin(GL_LINES);
        glVertex2f(l.x1, l.y1);
        glVertex2f(l.x2, l.y2);
    glEnd();
}

void keyboardFunct(unsigned char button, int , int y)
{
    if(button == 's')
    {
        flag++;
        flag = flag%2;
        cnt=0;
    }
}

void mouseHandler(int button, int state, int x, int y)
{
    y = SCREEN_HEIGHT - y;
    if(button == GLUT_LEFT_BUTTON && state == GLUT_DOWN)
    {
        if(flag == 0)
        {
            if(cnt==0)
            {
                wn.x1=x;
                wn.y1=y;
                cnt=1;
            }
            else if(cnt==1)
            {
                wn.x2=x;
                wn.y2=y;
                cnt=0;
            }
        }
        else if(flag==1)
        {
            if(cnt==0)
            {
                ln.x1=x;
                ln.y1=y;
                cnt=1;
            }
            else if(cnt==1)
            {
                ln.x2=x;
                ln.y2=y;
                cnt=0;
            }
        }
    }
    else if(button == GLUT_RIGHT_BUTTON && state == GLUT_DOWN)
    {
        if(flag==0)
        {
            float x1,x2,y1,y2;
            x1=wn.x1;
            x2=wn.x2;
            y1=wn.y1;
            y2=wn.y2;

            wn.x1 = min(x1, x2);
            wn.x2 = max(x1, x2);
            wn.y1 = min(y1, y2);
            wn.y2 = max(y1, y2);

            drawWindow(wn);
        }
        if(flag==1)
        {
            drawLine(ln, wn);
        }
    }
    glFlush();
}


void display()
{
    glClear(GL_COLOR_BUFFER_BIT);
    glFlush();
}

void init()
{
    glClearColor(0,0,0,1);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT);
}

int main(int argc, char *argv[])
{
    glutInit(&argc, argv);
    glutInitWindowSize(SCREEN_WIDTH,SCREEN_HEIGHT);
    glutInitWindowPosition(10,10);
    glutInitDisplayMode(GLUT_SINGLE);

    glutCreateWindow("GLUT Shapes");
    init();
    glutDisplayFunc(display);
    glutMouseFunc(mouseHandler);
    glutKeyboardFunc(keyboardFunct);
    glutMainLoop();

    return EXIT_SUCCESS;
}
