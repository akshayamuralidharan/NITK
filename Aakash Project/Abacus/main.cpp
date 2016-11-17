/* L12.c
           OpenGL Framework using GLUT 3.7

           Rob Fletcher  2001

           Draw a Glut object and apply lighting
           and also keep the x,y,z rotations

*/
#include <windows.h>
#include <stdio.h>
#include <stdlib.h>     /* For "exit" prototype */
#include <GL/glut.h>    /* Header File For The GLUT Library */
#include <math.h>

/* ASCII code for the escape key. */
#define ESCAPE 27

GLint window;           /* The number of our GLUT window */
GLint Xsize=400;
GLint Ysize=400;
float sf=0;

GLfloat xangle=0.0,yangle=0.0,zangle=0.0;   /* axis angles */


/* Simple window transformation routine */
GLvoid Transform(GLfloat Width, GLfloat Height)
{
  glViewport(0, 0, Width, Height);              /* Set the viewport */
  glMatrixMode(GL_PROJECTION);                  /* Select the projection matrix */
  glLoadIdentity();				/* Reset The Projection Matrix */
  gluPerspective(45.0,Width/Height,0.1,100.0);  /* Calculate The Aspect Ratio Of The Window */
  glMatrixMode(GL_MODELVIEW);                   /* Switch back to the modelview matrix */
}


/* A general OpenGL initialization function.  Sets all of the initial parameters. */
GLvoid InitGL(GLfloat Width, GLfloat Height)
{

GLfloat LightAmbient[] = { 0.3, 0.3, 0.3, 1.0 };  /* reddish ambient light  */
GLfloat LightDiffuse[] = { 0.7, 0.7, 0.7, 1.0 };  /* bluish  diffuse light. */
GLfloat LightPosition[] = { 0, 0, 10, 1 };    /* position */

  glClearColor(0.0, 0.0, 0.0, 0.0);		/* This Will Clear The Background Color To Black */
  glShadeModel(GL_SMOOTH);

  glLightfv(GL_LIGHT0, GL_AMBIENT, LightAmbient);  /*  add lighting. (ambient) */
  glLightfv(GL_LIGHT0, GL_DIFFUSE, LightDiffuse);  /*  add lighting. (diffuse). */
  glLightfv(GL_LIGHT0, GL_POSITION,LightPosition); /*  set light position. */
  glEnable(GL_LIGHT0);                             /*  turn light 0 on. */

  Transform( Width, Height );                   /* Perform the transformation */
}

/* The function called when our window is resized  */
GLvoid ReSizeGLScene(GLint Width, GLint Height)
{
  if (Height==0)    Height=1;                   /* Sanity checks */
  if (Width==0)     Width=1;
  Transform( Width, Height );                   /* Perform the transformation */
}


/* The main drawing function

   In here we put all the OpenGL and calls to routines which manipulate
   the OpenGL state and environment.

   This is the function which will be called when a "redisplay" is requested.
*/


void cuboid(int x,int y,int z)
{

}


void mat3mul(float a[4][4],float b[4][4])
{
    float c[4][4];

    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            {
            c[i][j]=0;
            for(int k=0;k<4;k++)
                c[i][j]+=a[i][k]*b[k][j];
            }

for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            {
            b[i][j]=c[i][j];
            }


}

void mat1mul(float a[4][4],float b[4][1])
{
    float c[4][1];

    for(int i=0;i<4;i++)
            {
            c[i][0]=0;
            for(int k=0;k<4;k++)
                c[i][0]+=a[i][k]*b[k][0];
            }

for(int i=0;i<4;i++)
            b[i][0]=c[i][0];


}




void make_mat(float xangle,float yangle,float zangle,float a[4][1])
{

float xm[4][4],ym[4][4],zm[4][4];

for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            xm[i][j]=0;

for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            ym[i][j]=0;

for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            zm[i][j]=0;

zm[0][0]=zm[1][1]=cos(zangle);
zm[1][0]=sin(zangle);
zm[0][1]=-zm[1][0];
zm[2][2]=zm[3][3]=1;

ym[0][0]=ym[2][2]=cos(yangle);
ym[0][2]=sin(yangle);
ym[2][0]=-ym[0][2];
ym[1][1]=ym[3][3]=1;


xm[2][2]=xm[1][1]=cos(xangle);
xm[2][1]=sin(xangle);
xm[1][2]=-xm[2][1];
xm[0][0]=xm[3][3]=1;

mat3mul(xm,ym);
mat3mul(ym,zm);
mat1mul(zm,a);


}


GLvoid DrawGLScene()
{
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);	/* Clear The Screen And The Depth Buffer */

        glEnable(GL_DEPTH_TEST);
glEnable(GL_LIGHTING);
//GLfloat mat_specular[] = { 0.7255, 0.2745, 0.0824, 1.0 };

GLfloat mat_specular[] = { 0.596, 0.2274, 0.0706, 1.0 };
   glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular);

     GLUquadricObj *obj[2];// = gluNewQuadric();


for(int i=0;i<5;i++)
    {

      glPushMatrix();
  glLoadIdentity();

float x=-2+(i),y=0,z=-1.5;
float a[4][1];


a[0][0]=x;
a[1][0]=y;
a[2][0]=z;
a[3][0]=1;

make_mat(xangle*3.14/180+1.57,yangle*3.14/180,zangle*3.14/180,a);

glTranslatef(a[0][0],a[1][0],a[2][0]-10+0.5*sf);
if(i)
    printf("%f     %f    %f\n",a[0][0],a[1][0],a[2][0]-10);

  glRotatef(xangle+90,1,0,0);
  glRotatef(yangle,0.0,1.0,0.0);
  glRotatef(zangle,0.0,0.0,1.0);
//  glutSolidCube(0.5);
  //glClear(GL_COLOR_BUFFER_BIT);


obj[i] = gluNewQuadric();
    gluCylinder(obj[i], 0.15, 0.15, 2, 30, 120);

  glPopMatrix();


}


for(int i=0;i<2;i++)
    {

      glPushMatrix();
  glLoadIdentity();

float x=-3+(6*i),y=-1,z=-1.5;
float a[4][1];


a[0][0]=x;
a[1][0]=y;
a[2][0]=z;
a[3][0]=1;

make_mat(xangle*3.14/180+1.57,yangle*3.14/180,zangle*3.14/180,a);

glTranslatef(a[0][0],a[1][0],a[2][0]-10+0.5*sf);
if(i)
    printf("%f     %f    %f\n",a[0][0],a[1][0],a[2][0]-10);

  glRotatef(xangle+90,1,0,0);
  glRotatef(yangle,0.0,1.0,0.0);
  glRotatef(zangle,0.0,0.0,1.0);
//  glutSolidCube(0.5);
  //glClear(GL_COLOR_BUFFER_BIT);


obj[i] = gluNewQuadric();
    gluCylinder(obj[i], 0.25, 0.25, 2.7, 30, 120);

  glPopMatrix();


}




for(int i=0;i<50;i++)
    {
for(int j=0;j<10;j++)
{

      glPushMatrix();
  glLoadIdentity();

float x=-2.5+(0.10*i),y=0.5-(0.1*j),z=-0.5;

float a[4][1];


a[0][0]=x;
a[1][0]=y;
a[2][0]=z;
a[3][0]=1;

make_mat(xangle*3.14/180+1.57,yangle*3.14/180,zangle*3.14/180,a);

glTranslatef(a[0][0],a[1][0],a[2][0]-10+0.5*sf);
if(i)
    printf("%f     %f    %f\n",a[0][0],a[1][0],a[2][0]-10);

  glRotatef(xangle+90,1,0,0);
  glRotatef(yangle,0.0,1.0,0.0);
  glRotatef(zangle,0.0,0.0,1.0);
//  glutSolidCube(0.5);
  //glClear(GL_COLOR_BUFFER_BIT);


//obj[i] = gluNewQuadric();
    glutSolidCube(0.1);

  glPopMatrix();

}
}




for(int i=0;i<29;i++)
    {
for(int j=0;j<9;j++)
{

      glPushMatrix();
  glLoadIdentity();

float x=-3.5+(0.25*i),y=0.5-(0.25*j),z=-1.5;

float a[4][1];


a[0][0]=x;
a[1][0]=y;
a[2][0]=z;
a[3][0]=1;

make_mat(xangle*3.14/180+1.57,yangle*3.14/180,zangle*3.14/180,a);

glTranslatef(a[0][0],a[1][0],a[2][0]-10+0.5*sf);
if(i)
    printf("%f     %f    %f\n",a[0][0],a[1][0],a[2][0]-10);

  glRotatef(xangle+90,1,0,0);
  glRotatef(yangle,0.0,1.0,0.0);
  glRotatef(zangle,0.0,0.0,1.0);
//  glutSolidCube(0.5);
  //glClear(GL_COLOR_BUFFER_BIT);


//obj[i] = gluNewQuadric();
    glutSolidCube(0.25);

  glPopMatrix();

}
}

for(int i=0;i<29;i++)
    {
for(int j=0;j<9;j++)
{

      glPushMatrix();
  glLoadIdentity();

float x=-3.5+(0.25*i),y=0.5-(0.25*j),z=1.2;

float a[4][1];


a[0][0]=x;
a[1][0]=y;
a[2][0]=z;
a[3][0]=1;

make_mat(xangle*3.14/180+1.57,yangle*3.14/180,zangle*3.14/180,a);

glTranslatef(a[0][0],a[1][0],a[2][0]-10+0.5*sf);
if(i)
    printf("%f     %f    %f\n",a[0][0],a[1][0],a[2][0]-10);

  glRotatef(xangle+90,1,0,0);
  glRotatef(yangle,0.0,1.0,0.0);
  glRotatef(zangle,0.0,0.0,1.0);
//  glutSolidCube(0.5);
  //glClear(GL_COLOR_BUFFER_BIT);


//obj[i] = gluNewQuadric();
    glutSolidCube(0.25);

  glPopMatrix();

}
}

for(int i=0;i<5;i++)
    {
for(int j=0;j<5;j++)
{

int kf=j/4;
      glPushMatrix();
  glLoadIdentity();

float x=-2.0+(1*i),y=0,z=1.25-0.3-(j*0.3)-(0.5*kf);

float a[4][1];

a[0][0]=x;
a[1][0]=y;
a[2][0]=z;
a[3][0]=1;

make_mat(xangle*3.14/180+1.57,yangle*3.14/180,zangle*3.14/180,a);
glTranslatef(a[0][0],a[1][0],a[2][0]-10+0.5*sf);
if(i)
    printf("%f     %f    %f\n",a[0][0],a[1][0],a[2][0]-10);

  glRotatef(xangle+90,1,0,0);
  glRotatef(yangle,0.0,1.0,0.0);
  glRotatef(zangle,0.0,0.0,1.0);
//  glutSolidCube(0.5);
  //glClear(GL_COLOR_BUFFER_BIT);
if(j==4)
{

mat_specular[0] = 1;
mat_specular[1] = 0;
mat_specular[2] = 0;
}
else if(j==1) {

mat_specular[0] = 0;
mat_specular[1] = 1;
mat_specular[2] = 0;
}

else if(j==2) {

mat_specular[0] = 1;
mat_specular[1] = 1;
mat_specular[2] = 0;
}

else if(j==3) {

mat_specular[0] = 0;
mat_specular[1] = 1;
mat_specular[2] = 1;
}

else if(j==0) {

mat_specular[0] = 0;
mat_specular[1] = 0;
mat_specular[2] = 1;
}
   glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular);
//obj[i] = gluNewQuadric();
glutSolidTorus(0.15,0.25,5,5);

  glPopMatrix();

}
}


  glFlush();

}


/*  The function called whenever a "normal" key is pressed. */
void NormalKey(GLubyte key, GLint x, GLint y)
{

    switch ( key )    {
     case ESCAPE :
        printf("escape pressed. exit.\n");
	glutDestroyWindow(window);	/* Kill our window */
	exit(0); 			/* Very dirty exit */
        break;				/* Do we need this??? */


     case GLUT_KEY_UP:
        sf++;
        //xangle += 5.0;
        glutPostRedisplay();
        break;
     case GLUT_KEY_DOWN:
         sf--;
        //xangle -= 5.0;
        glutPostRedisplay();
        break;

     case 'y':
        yangle += 5.0;
        glutPostRedisplay();
        break;
     case 'Y':
        yangle -= 5.0;
        glutPostRedisplay();
        break;

     case 'z':
        zangle += 5.0;
        glutPostRedisplay();
        break;
     case 'Z':
        zangle -= 5.0;
        glutPostRedisplay();
        break;

     case 'd':
        glEnable(GL_DEPTH_TEST);
        glutPostRedisplay();
        break;

     case 'D':
        glDisable(GL_DEPTH_TEST);
        glutPostRedisplay();
        break;

     case 'l':
       glEnable(GL_LIGHTING);  /* enable lighting */
       glutPostRedisplay();
        break;

     case 'L':
       glDisable(GL_LIGHTING);  /* enable lighting */
       glutPostRedisplay();
        break;

     default:
	break;
    }

}

void SpecialKey(int key, int x, int y) {

	switch(key) {
		case GLUT_KEY_UP :
				sf++;
				glutPostRedisplay();
				 break;
		case GLUT_KEY_DOWN:
				sf--;
				glutPostRedisplay();
				 break;
        case GLUT_KEY_LEFT:
        zangle += 5.0;
        glutPostRedisplay();
        break;
     case GLUT_KEY_RIGHT:
        zangle -= 5.0;
        glutPostRedisplay();
        break;

	}
}

/*************************** Main ***************************************************************/

int main(int argc, char **argv)
{

/* Initialisation and window creation */

  glutInit(&argc, argv);               /* Initialize GLUT state. */

  glutInitDisplayMode(GLUT_RGBA |      /* RGB and Alpha */
                      GLUT_SINGLE|     /* Single buffer */
                      GLUT_DEPTH);     /* Z buffer (depth) */

  glutInitWindowSize(Xsize,Ysize);         /* set initial window size. */
  glutInitWindowPosition(0,0);         /* upper left corner of the screen. */

  window = glutCreateWindow("L12");     /* Open a window with a title. */
  InitGL(Xsize,Ysize);                     /* Initialize our window. */

/* Now register the various callback functions */

  glutDisplayFunc(DrawGLScene);        /* Function to do all our OpenGL drawing. */
  glutReshapeFunc(ReSizeGLScene);
  glutKeyboardFunc(NormalKey);         /*Normal key is pressed */
  glutSpecialFunc(SpecialKey);
/* Now drop into the event loop from which we never return */

  glutMainLoop();                      /* Start Event Processing Engine. */
  return 1;
}
