import matplotlib.pyplot as plt
import numpy as np

plt.axis([-10,140,90,-10])
plt.axis('on')
plt.grid(True, linestyle = ':')

plt.arrow(0,0,40,0,head_length=4,head_width=2,color = 'b')
plt.arrow(0,0,0,40,head_length=4,head_width=2,color='b')

xc=40
yc=10

plt.plot([xc-30,xc+90],[yc,yc],linewidth=1,color='k')
plt.plot([xc,xc],[yc-5,yc+75],linewidth=1,color='k')
plt.text(30,-2,'Xg',color='b')
plt.text(-7,33,'Yg',color='b')
plt.scatter(xc,yc,s=20,color='k')
plt.text(xc+3,yc-2,'(xc,yc)')


def rotz(xp,yp,rz):
    c11=np.cos(rz)
    c12=-np.sin(rz)
    c21=np.sin(rz)
    c22=np.cos(rz)
    xpp=xp*c11+yp*c12
    ypp=xp*c21+yp*c22
    xg=xc+xpp
    yg=yc+ypp
    return[xg,yg]


xp=60
yp=0

# P1
rz=0
rz=rz*np.pi/180
[xg,yg]=rotz(xp,yp,rz)
plt.scatter(xg,yg,s=30,color='k' )
plt.text(xg+1,yg+6,'P1',color='k')

# p2
rz=30
rz=rz*np.pi/180
[xg,yg]=rotz(xp,yp,rz)
plt.scatter(xg,yg,s=30,color='grey')
plt.text(xg+1,yg+6,'P2',color='grey')

# p3
rz=60
rz=rz*np.pi/180
[xg,yg]=rotz(xp,yp,rz)
plt.scatter(xg,yg,s=30,color='r')
plt.text(xg+1,yg+6,'P3',color='r')
xpp3=xg
ypp3=yg

# p4
rz=90
rz=rz*np.pi/180
[xg,yg]=rotz(xp,yp,rz)
plt.scatter(xg,yg,s=30,color='grey')
plt.text(xp-18,yp+74,'P4',color='grey')


plt.arrow(0,0,xc-4,yc-1,head_length=4,head_width=2,color='k')

plt.text(28,6,r'$\mathbf{C}$',color='k')

plt.arrow(0,0,xpp3-3,ypp3-3,head_length=4,head_width=2,color='b')
plt.text(45,50,r'$\mathbf{Pg}$',color='b')

plt.arrow(xc,yc,xpp3-2-xc,ypp3-5-yc,head_length=4,head_width=2,color='r')
plt.text(61,40,r'$\mathbf{P^{\prime}}$',color='r')

plt.arrow(xc,yc,xp-4,yp,head_length=4,head_width=2,color='k')

plt.text(80,yc-2,r'$\mathbf{P}$',color='k')

plt.show()