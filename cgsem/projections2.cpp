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


void drawObjects()
{
     glColor3f(0.7, 0.0, 0.50);
     glutWireDodecahedron();

     glColor3f(0.0, 1.0, 1.0);
     glTranslatef(-2.0, 1.0, 0.0);

     glutWireCube(2.0);
     glutWireTetrahedron();

     glutWireOctahedron();
}

void display()
{
    glClearColor(0.0, 0.0, 0.0, 0.0);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    drawObjects();
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
