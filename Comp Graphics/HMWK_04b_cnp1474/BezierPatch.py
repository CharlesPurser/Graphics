# Purser, Charles N
# cnp1474
# 2019-04-30

import numpy as np

def resolveBezierPatch( res, patch) :
    pointList = []    
    for u in np.linspace( 0.0, 1.0, res ) :
        for v in np.linspace( 0.0, 1.0, res ) :
            pointList.append( calculate_each_point( patch, u, v ) )
    return ( pointList )
                



def calculate_each_point( patch, u, v ) :
    point = ( 0.0, 0.0, 0.0 )
    for i in range( 4 ) :
        for j in range( 4 ) :
            c = calculate_coefficients( u, v, i, j )
            c = (c,c,c)
            point = point + np.multiply(c, patch[i*4+j]) 
    return ( point )

def calculate_coefficients( u, v, i, j ) :
    if( i == 0 and j == 0 ) : return ((((-u+1)**3))*((-v+1)**3))
    if( i == 0 and j == 1 ) : return ((3*v)*((-u+1)**3)*((-v+1)**2))
    if( i == 0 and j == 2 ) : return ((3*(v**2))*((-u+1)**3)*(-v+1))
    if( i == 0 and j == 3 ) : return ((v**3)*((-u+1)**3))
    if( i == 1 and j == 0 ) : return ((3*u)*((-u+1)**2)*((-v+1)**3))
    if( i == 1 and j == 1 ) : return ((9*u*v)*((-u+1)**2)*((-v+1)**2))
    if( i == 1 and j == 2 ) : return ((9*u*(v**2))*((-u+1)**2)*(-v+1))
    if( i == 1 and j == 3 ) : return ((3*u*(v**3))*((-u+1)**2))
    if( i == 2 and j == 0 ) : return ((3*(u**2))*(-u+1)*((-v+1)**3))
    if( i == 2 and j == 1 ) : return ((9*(u**2)*v)*(-u+1)*((-v+1)**2))
    if( i == 2 and j == 2 ) : return ((9*(u**2)*(v**2))*(-u+1)*(-v+1))
    if( i == 2 and j == 3 ) : return ((3*(u**2)*(v**3))*(-u+1))
    if( i == 3 and j == 0 ) : return ((u**3)*((-v+1)**3))
    if( i == 3 and j == 1 ) : return ((3*(u**3)*v)*((-v+1)**2))
    if( i == 3 and j == 2 ) : return ((3*(u**3)*(v**2))*(-v+1))
    if( i == 3 and j == 3 ) : return ((u**3)*(v**3))