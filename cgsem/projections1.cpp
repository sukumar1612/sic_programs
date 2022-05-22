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

GLfloat ex=0.0, ey=0.0, ez=-3.0;

GLfloat vertices[8][3]={
    {-1.0, -1.0, 1.0},
    {-1.0, 1.0, 1.0},
    {1.0, 1.0, 1.0},
    {1.0, -1.0, 1.0},
    {-1.0, -1.0, -1.0},
    {-1.0, 1.0, -1.0},
    {1.0, 1.0, -1.0},
    {1.0, -1.0, -1.0}
};

GLfloat colors[8][3] = {
    {0.0, 0.0, 1.0},
    {1.0, 0.0, 0.0},
    {1.0, 1.0, 0.0},
    {0.0, 1.0, 0.0},
    {0.75, 0.5, 0.5},
    {1.0, 0.0, 1.0},
    {1.0, 1.0, 1.0},
    {0.0, 1.0, 1.0},
};

void quad(int a, int b, int c, int d)
{
    glBegin(GL_QUADS);
        glVertex3fv(vertices[a]);
        glVertex3fv(vertices[b]);
        glVertex3fv(vertices[c]);
        glVertex3fv(vertices[d]);
    glEnd();
}

void myDraw()
{
    glColor3f(1, 0, 0);
    glColor3fv(colors[0]);
    quad(0, 3, 2, 1);

    glColor3fv(colors[1]);
    quad(2, 3, 7, 6);

    glColor3fv(colors[2]);
    quad(0, 4, 7, 3);

    glColor3fv(colors[3]);
    quad(1, 2, 6, 5);

    glColor3fv(colors[4]);
    quad(4, 5, 6, 7);

    glColor3fv(colors[5]);
    quad(0, 4, 5, 1);

}

static void key(unsigned char key, int x, int y)
{
    switch(key)
    {
        case 27:
        case 'q':
            exit(0);
            break;
        case '+':
            ez+=0.5;
            break;
        case '-':
            ez-=0.5;
            break;
    }
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(ex, ey, ez,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
    glutPostRedisplay();
}

void resize(int width, int height)
{
    double aspect;
    glViewport(0,0,width, height);
    aspect = (double) width / (double) height;
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();

    if(aspect < 1.0)
    {
        glOrtho(-4., -4., -4./aspect, -4./aspect, 1., 100.);
    }
    else
    {
        glOrtho(-4.*aspect, 4.*aspect, -4., 4., 1., 100.);
    }
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
}

static void arrowKey(int key, int x, int y)
{
    if (key == GLUT_KEY_LEFT)
    {
        ex-=0.5;
    }
    if (key == GLUT_KEY_RIGHT)
    {
        ex+=0.5;
    }
    if (key == GLUT_KEY_UP)
    {
        ey-=0.5;
    }
    if (key == GLUT_KEY_DOWN)
    {
        ey+=0.5;
    }
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(ex, ey, ez,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
    glutPostRedisplay();
}

void display()
{
    glClearColor(0.0, 0.0, 0.0, 0.0);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    myDraw();
    glutSwapBuffers();
}

void init()
{
    glEnable(GL_DEPTH_TEST);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();

    glFrustum(-4.0, 4.0, -4.0, 4.0, 1.0, 10.0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    gluLookAt(ex, ey, ez,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
}

int main(int argc, char *argv[])
{
    glutInit(&argc, argv);
    glutInitWindowSize(640,480);
    glutInitWindowPosition(10,10);
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH);

    glutCreateWindow("GLUT Shapes");

    init();
    glutReshapeFunc(resize);
    glutDisplayFunc(display);
    glutKeyboardFunc(key);
    glutSpecialFunc(arrowKey);

    glutMainLoop();

    return EXIT_SUCCESS;
}
