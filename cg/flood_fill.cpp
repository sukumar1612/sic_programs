#include<windows.h>
#ifdef __APPLE__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif

#include <stdlib.h>
#include <bits/stdc++.h>

#define SCREEN_WIDTH 640
#define SCREEN_HEIGHT 480


using namespace std;

struct line{
    float x1,y1;
    float x2,y2;
};

vector<pair<int, int> > polygon_points;
map<pair<int, int> , int> visited;
int flag=0;

void drawPoint(int x, int y)
{
    glBegin(GL_POINTS);
     glVertex2f(x, y);
    glEnd();
}

//void fillPolygon(vector<pair<int, int> > )
int checkSideOfLine(struct line &ln, float x, float y)
{
    float p = (ln.x2 - ln.x1)*(y - ln.y1) - (ln.y2 - ln.y1)*(x - ln.x1);
    if(p<0)
    {
        return -1;
    }
    return 1;
}

int checkSideOfPolygon(vector<pair<int, int> > &pp, float x, float y)
{
    for(int i=0;i<pp.size()-1;i++)
    {
        struct line ln;
        ln.x1 = pp[i].first;
        ln.x2 = pp[i+1].first;
        ln.y1 = pp[i].second;
        ln.y2 = pp[i+1].second;

        int p= checkSideOfLine(ln, x, y);
        if(p!=-1)
        {
            return 1;
        }
    }
    return 0;
}

void fillPolygon(int x, int y, map<pair<int, int> , int> &vst, vector<pair<int, int> > &pp)
{
    glFlush();
    if(checkSideOfPolygon(pp, x, y) == 1)
    {
        return;
    }
    if(x>SCREEN_WIDTH || x<0 || y>SCREEN_HEIGHT || y<0)
    {
        return;
    }
    if(vst[make_pair(x, y)] == 5)
    {
        return;
    }

    vst[make_pair(x, y)] = 5;

    drawPoint(x, y);

    fillPolygon(x+1, y, vst, pp);
    drawPoint(x+1, y);

    fillPolygon(x, y+1, vst, pp);
    drawPoint(x, y+1);


    fillPolygon(x-1, y, vst, pp);
    drawPoint(x-1, y);


    fillPolygon(x, y-1, vst, pp);
    drawPoint(x, y-1);

}

void drawPolygon(vector<pair<int, int> > &pp, map<pair<int, int> , int> &vst)
{
    glBegin(GL_LINE_LOOP);
        for(int i=0;i<pp.size();i++)
        {
            glVertex2f(pp[i].first, pp[i].second);
        }
    glEnd();

}

void keyboardFunct(unsigned char button ,int x, int y)
{
    if(button == 's')
    {
        flag++;
        flag=flag%2;
    }
}

void mouseHandler(int button, int state, int x, int y)
{
    y = SCREEN_HEIGHT - y;
    if(button == GLUT_LEFT_BUTTON && state == GLUT_DOWN)
    {
        if(flag==0)
        {
            pair<int, int> p;
            p.first = x;
            p.second = y;

            polygon_points.push_back(p);
        }
        else if(flag==1)
        {
            fillPolygon(x, y, visited, polygon_points);
        }
    }
    else if(button == GLUT_RIGHT_BUTTON && state == GLUT_DOWN)
    {
        polygon_points.push_back(polygon_points[0]);
        drawPolygon(polygon_points, visited);
    }
    glFlush();
}

void display()
{
    glClear(GL_COLOR_BUFFER_BIT);
    drawPoint(10, 10);
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
    glutInitWindowPosition(360, 240);
    glutInitDisplayMode(GLUT_SINGLE);

    glutCreateWindow("GLUT Shapes");
    init();
    glutDisplayFunc(display);
    glutMouseFunc(mouseHandler);
    glutKeyboardFunc(keyboardFunct);
    glutMainLoop();

    return EXIT_SUCCESS;
}
