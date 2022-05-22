#include<windows.h>
#ifdef __APPLE__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif

#include <stdlib.h>
#include<bits/stdc++.h>

#define SCREEN_WIDTH 640
#define SCREEN_HEIGHT 480

using namespace std;

vector<pair<float, float> > points;
int cnt=0;

void drawPoint(float x, float y)
{
    glBegin(GL_POINTS);
        glVertex2f(x, y);
    glEnd();
}

float cubicBezierX(vector<pair<float, float> > &p, float t)
{
    return p[0].first*pow((1-t), 3) + p[1].first*3*t*pow((1-t), 2) + p[2].first*3*(1-t)*pow(t, 2) + p[3].first*pow(t, 3);
}

float cubicBezierY(vector<pair<float, float> > &p, float t)
{
    return p[0].second*pow((1-t), 3) + p[1].second*3*t*pow((1-t), 2) + p[2].second*3*(1-t)*pow(t, 2) + p[3].second*pow(t, 3);
}

void drawBezier(vector<pair<float, float> > &p, float step)
{
    for(float i=0;i<1;i+=step)
    {
        drawPoint(cubicBezierX(p, i), cubicBezierY(p, i));
    }
}

void mouseHandler(int button, int state, int x, int y)
{
    y = SCREEN_HEIGHT - y;
    if(button == GLUT_LEFT_BUTTON && state == GLUT_DOWN)
    {
        glColor3f(1,1,1);
        if(cnt!=0)
        {
            glBegin(GL_LINES);
                glVertex2f(points[points.size() - 1].first, points[points.size() - 1].second);
                glVertex2f(x, y);
            glEnd();
        }
        pair<float, float> p;
        p.first = x;
        p.second = y;
        points.push_back(p);
        cnt++;
    }
    else if(button == GLUT_RIGHT_BUTTON && state == GLUT_DOWN)
    {
        glColor3f(1,1,0);
        drawBezier(points, 0.00001);
        cnt=0;
        points.clear();
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
    glutMainLoop();

    return EXIT_SUCCESS;
}
