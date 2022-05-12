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

vector<pair<float, float> > polygon_points;
map<int , vector<float> > height_wise_Points;

int sign(float x)
{
    if(x<0)
    {
        return -1;
    }
    return 1;
}
void drawPoint(float x, float y)
{
    glBegin(GL_POINTS);
        glVertex2f(x, y);
    glEnd();
}

void fillMap(map<int , vector<float> > &hwp, pair<float, float> p1, pair<float, float> p2)
{
    float m = (p2.second - p1.second)/(p2.first - p1.first);
    float c = p1.second - m*p1.first;

    float ymax = max(p2.second, p1.second);
    float ymin = min(p2.second, p1.second);

    for(float y = ymin; y<=ymax; y++)
    {
        hwp[y].push_back((y - c)/m);
    }
}

void drawPolygon(vector<pair<float, float> > &points, map<int , vector<float> > &hwp)
{
    glBegin(GL_LINE_LOOP);
        for(int i=0;i<points.size();i++)
        {
            glVertex2f(points[i].first, points[i].second);
        }
    glEnd();
    for(int i=0;i<points.size()-1;i++)
    {
        fillMap(hwp, points[i], points[i+1]);
    }

    map<int , vector<float> >::iterator h= hwp.begin();

    for(h=hwp.begin();h!=hwp.end();h++)
    {
        vector<float> v = h->second;
        for(int j=0;j< v.size()-1; j++)
        {
            if(j%2==0)
            {
                for(int k=v[j];k<=v[j+1];k++)
                {
                    drawPoint(k, h->first);
                }
            }
        }
    }
}

void mouseHandler(int button, int state, int x, int y)
{
    y = SCREEN_HEIGHT - y;
    if(button == GLUT_LEFT_BUTTON && state == GLUT_DOWN)
    {
        pair<float, float> p;
        p.first = x;
        p.second = y;

        polygon_points.push_back(p);
    }
    else if(button == GLUT_RIGHT_BUTTON && state == GLUT_DOWN)
    {
        polygon_points.push_back(polygon_points[0]);
        drawPolygon(polygon_points, height_wise_Points);
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
    gluOrtho2D(0,SCREEN_WIDTH, 0, SCREEN_HEIGHT);
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
