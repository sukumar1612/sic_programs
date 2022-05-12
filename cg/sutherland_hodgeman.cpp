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
struct windowCoord{
    float x1, y1;
    float x2, y2;
};
struct lineCoord{
    float x1, y1;
    float x2, y2;
};
struct windowCoord wn;
vector<pair<float, float> > polygon_points;
int flag=0;
int cnt=0;


int checkLineSide(struct lineCoord &ln, float x, float y)
{
    float p = 1.0*(ln.x2 - ln.x1)*(y - ln.y1) - 1.0*(ln.y2 - ln.y1)*(x - ln.x1);
    if(p<0)
    {
        return -1;
    }
    if(p==0)
    {
        return 0;
    }
    return 1;

}
void getLine(struct lineCoord &ln, struct windowCoord &w, int mode)
{
    if(mode == 0)
    {
        ln.x1 = w.x1;
        ln.x2 = w.x1;
        ln.y1 = w.y1;
        ln.y2 = w.y2;
    }
    if(mode == 1)
    {
        ln.x1 = w.x1;
        ln.x2 = w.x2;
        ln.y1 = w.y2;
        ln.y2 = w.y2;
    }
    if(mode == 2)
    {
        ln.x1 = w.x2;
        ln.x2 = w.x2;
        ln.y1 = w.y2;
        ln.y2 = w.y1;
    }
    if(mode == 3)
    {
        ln.x1 = w.x2;
        ln.x2 = w.x1;
        ln.y1 = w.y1;
        ln.y2 = w.y1;
    }
}
void getIntersection(pair<float, float> &p1, pair<float, float> &p2, struct lineCoord &ln, int mode, pair<float, float> &inter)
{
    float m = (p2.second - p1.second)/(p2.first - p1.first);
    float c = p1.second - m*p1.first;

    int pt1 = checkLineSide(ln, p1.first, p1.second);
    int pt2 = checkLineSide(ln, p2.first, p2.second);

    if(pt1 != pt2 )
    {
        if(mode == 0)
        {
            inter.first = ln.x1;
            inter.second = m*ln.x1 + c;
        }
        if(mode == 1)
        {
            inter.first = (ln.y1 - c)/m;
            inter.second = ln.y1;
        }
        if(mode == 2)
        {
            inter.first = ln.x1;
            inter.second = m*ln.x1 + c;
        }
        if(mode == 3)
        {
            inter.first = (ln.y1 - c)/m;
            inter.second = ln.y1;
        }

        if(pt1 == -1)
        {
            p2.first = inter.first;
            p2.second = inter.second;
        }
        else
        {
            p1.first = inter.first;
            p1.second = inter.second;
        }
    }
    else
    {
        inter.first = -1;
        inter.second = -1;
        if(pt1 == 1)
        {
            p1.first = inter.first;
            p1.second = inter.second;

            p2.first = inter.first;
            p2.second = inter.second;
        }
    }
}

void clipPolygonToLine(pair<float, float> &p1, pair<float, float> &p2, struct windowCoord &w, int mode)
{
    struct lineCoord ln;
    pair<float, float> intersection;
    getLine(ln, w, mode);
    getIntersection(p1, p2, ln, mode, intersection);

    glPointSize(10);
    glBegin(GL_POINTS);
        if(intersection.first > -1)
        {
            glVertex2f(intersection.first, intersection.second);
        }
    glEnd();
    glFlush();
}

void clipPolygon(vector<pair<float, float> > & points, struct windowCoord &w)
{
    for (int mode = 0; mode<4;mode++)
    {
        vector<pair<float, float> > new_pts;
        for (int i=0;i<points.size()-1;i++)
        {
            pair<float, float> p1, p2;
            p1 = points[i];
            p2 = points[i+1];
            clipPolygonToLine(p1, p2, w, mode);
            if(p1.first!=-1)
            {
                new_pts.push_back(p1);
                new_pts.push_back(p2);
            }
        }
        points.clear();
        for(int i=0;i<new_pts.size();i++)
        {
            points.push_back(new_pts[i]);
        }
    }
}

void drawPolygon(vector<pair<float, float> > & points, struct windowCoord &w)
{
    glBegin(GL_LINE_LOOP);
        for(int i=0;i<points.size();i++)
        {
            glVertex2f(points[i].first, points[i].second);
        }
    glEnd();

    clipPolygon(points, w);

    glColor3f(1,1,0);
    glBegin(GL_LINE_LOOP);
        for(int i=0;i<points.size();i++)
        {
            glVertex2f(points[i].first, points[i].second);
        }
    glEnd();
}

void drawWindow(struct windowCoord &w)
{
    glBegin(GL_LINE_LOOP);
        glVertex2f(w.x1, w.y1);
        glVertex2f(w.x1, w.y2);
        glVertex2f(w.x2, w.y2);
        glVertex2f(w.x2, w.y1);
    glEnd();
}

void keyboardFunct(unsigned char button, int , int y)
{
    if(button == 's')
    {
        flag++;
        flag = flag%3;
        cnt=0;
    }
}

void mouseHandler(int button, int state, int x, int y)
{
    y = SCREEN_HEIGHT - y;
    if(button == GLUT_LEFT_BUTTON && state == GLUT_DOWN)
    {
        if(flag == 1)
        {
            pair<int, int> p;
            p.first = x;
            p.second = y;
            polygon_points.push_back(p);
        }
        else if(flag == 0 && cnt == 0)
        {
            wn.x1=x;
            wn.y1=y;
            cnt=1;
        }
        else if(flag == 0 && cnt == 1)
        {
            wn.x2=x;
            wn.y2=y;
            cnt=0;
        }
        else if(flag == 2)
        {
            struct lineCoord ln1;
            getLine(ln1, wn, 0);
            checkLineSide(ln1, x, y);
        }
    }
    else if(button == GLUT_RIGHT_BUTTON && state == GLUT_DOWN)
    {
        if (flag==1)
        {
            polygon_points.push_back(polygon_points[0]);
            drawPolygon(polygon_points, wn);
            polygon_points.clear();
        }
        else if(flag==0)
        {
            drawWindow(wn);
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
