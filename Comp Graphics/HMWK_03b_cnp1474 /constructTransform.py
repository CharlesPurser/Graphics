# Purser, Charles N.
# cnp1474
# 2019-02-28

#---------#---------#---------#---------#---------#--------#
def constructTransform( w, v, width, height ) :
    ##################################################
    # Put your Python code for computing fx, fy, gx, gy, sx, sy,
    # ax, and ay here.
    
    #Find mins and maxs
    wxmin = min( w[0], w[2] )
    wymin = min( w[1], w[3] )
    wxmax = max( w[0], w[2] )
    wymax = max( w[1], w[3] )  

    vxmin = min( v[0], v[2] )
    vymin = min( v[1], v[3] )
    vxmax = max( v[0], v[2] )
    vymax = max( v[1], v[3] )

    #compute values
    fx = ( -1*wxmin )
    fy = ( -1*wymin ) 
    gx = ( width*vxmin )
    gy = ( height*vymin )
    sx = ( (width*(vxmax-vxmin))/(wxmax-wxmin) )
    sy = ( (height*(vymax-vymin))/(wymax-wymin) )
    ax = ( (fx*sx)+gx )
    ay = ( (fy*sy)+gy )

    return( (ax, ay, sx, sy) )

    # Return ax, ay, sx, and sy as a tuple.
    ##################################################

#---------#---------#---------#---------#---------#--------#
def _main() :
  w      = ( -1.0, -2.0, 4.0, 5.0 )
  v      = ( 0.15, 0.15, 0.85, 0.85 )
  width  = 500
  height = 400

  values = constructTransform( w, v, width, height )
  ax, ay, sx, sy = values

  print( f'Values          : {values}' )
  print( f'Test transform  : ax {ax}, ay {ay}, sx {sx}, sy {sy}' )

#---------#
if __name__ == '__main__' :
  _main()

#---------#---------#---------#---------#---------#--------#
