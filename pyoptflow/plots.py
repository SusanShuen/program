from matplotlib.pyplot import figure,subplots,draw,pause,gca,show


def plotderiv(fx,fy,ft):
    fg,ax = subplots(1,3,figsize=(18,5))
    for f,a,t in zip((fx,fy,ft),ax,('$f_x$','$f_y$','$f_t$')):
        h=a.imshow(f,cmap='bwr')
        a.set_title(t)
        fg.colorbar(h,ax=a)


def compareGraphs(u,v,Inew,scale=3, quivstep=5):
    """
    makes quiver
    """
    ax = figure().gca()
    ax.imshow(Inew,cmap = 'gray', origin='lower')
    # plt.scatter(POI[:,0,1],POI[:,0,0])
    for i in range(0,u.shape[0], quivstep):
        for j in range(0,u.shape[1], quivstep):
            if u[i,j]>0.3 or v[i,j]>0.3:
                ax.arrow(j,i, v[i,j]*scale, u[i,j]*scale, color='red',
                     head_width=0.5, head_length=1)

    # print "u length: ", len(u)
    # print "quiver step: ", quivstep

	# plt.arrow(POI[:,0,0],POI[:,0,1],0,-5)

    draw(); pause(0.01)


def compareGraphsLK(imgOld, imgNew, POI, V,scale=1.):
    ax = gca()
    ax.imshow(imgNew,cmap = 'gray')
    # plt.scatter(POI[:,0,1],POI[:,0,0])
    for i in range(len(POI)):
        ax.arrow(POI[i,0,1],POI[i,0,0],
                    V[i,1]*scale, V[i,0]*scale,
                    color = 'red')
    # plt.arrow(POI[:,0,0],POI[:,0,1],0,-5)
    show()