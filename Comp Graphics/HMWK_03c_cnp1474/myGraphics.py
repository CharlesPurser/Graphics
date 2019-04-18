# Purser, Charles N 
# cnp1474
# 2019-01-24

#----------------------------------------------------------------------
# This code was originally created by Prof. Farhad Kamangar.
# It has been significantly modified and updated by Brian A. Dalio for
# use in CSE 4303 / CSE 5365 in the 2019 Spring semester.

#----------------------------------------------------------------------

from CohenSutherland import clipLine

class cl_world :
  def __init__( self, objects = [], canvases = [] ) :
    self.canvases = canvases

  def add_canvas( self, canvas ) :
    self.canvases.append( canvas )
    canvas.world = self

  def reset( self ) :
    for canvas in self.canvases :
      canvas.delete( 'all' )

  def create_graphic_objects( self, canvas, mesh, doClip, doPerspective ) :

    #Draw object
    faces = mesh.getFaces()
    if( doClip == 0 ) :
      for i in faces :     
        v1 = mesh.getTransformedVertex( i[0], doPerspective )
        v2 = mesh.getTransformedVertex( i[1], doPerspective )
        v3 = mesh.getTransformedVertex( i[2], doPerspective )   
        canvas.create_line( v1[0], v1[1], v2[0], v2[1], fill= "red" )
        canvas.create_line( v2[0], v2[1], v3[0], v3[1], fill= "red" )
        canvas.create_line( v3[0], v3[1], v1[0], v1[1], fill= "red" )
    else : 
      v = mesh.getViewport()
      width  = int( canvas.cget( "width" ) )
      height = int( canvas.cget( "height" ) )
      xMin = v[0] * width
      xMax = v[2] * width
      yMin = v[1] * height
      yMax = v[3] * height
      portal = (xMin, yMin, xMax, yMax)
      for i in faces : 
        v1 = mesh.getTransformedVertex( i[0], doPerspective )
        v2 = mesh.getTransformedVertex( i[1], doPerspective )
        v3 = mesh.getTransformedVertex( i[2], doPerspective )
        doDraw, p1x, p1y, p2x, p2y = clipLine(v1[0], v1[1], v2[0], v2[1], portal )
        if(doDraw == True) : 
          canvas.create_line( p1x, p1y, p2x, p2y, fill= "red" )
        doDraw, p1x, p1y, p2x, p2y = clipLine(v2[0], v2[1], v3[0], v3[1], portal)
        if(doDraw == True) :
          canvas.create_line( p1x, p1y, p2x, p2y, fill= "red" )  
        doDraw, p1x, p1y, p2x, p2y = clipLine(v3[0], v3[1], v1[0], v1[1], portal)            
        if(doDraw == True) :
          canvas.create_line( p1x, p1y, p2x, p2y, fill= "red" )
#----------------------------------------------------------------------
