# Purser, Charles N.
# cnp1474
# 2019-02-27

import sys

class ModelData() :
  def __init__( self, inputFile = None ) :
    self.m_Vertices = []
    self.m_Faces    = []
    self.m_Window   = None
    self.m_Viewport = None
    self.m_ax = None
    self.m_ay = None
    self.m_sx = None
    self.m_sy = None

    self.m_minX     = float( '+inf' )
    self.m_maxX     = float( '-inf' )
    self.m_minY     = float( '+inf' )
    self.m_maxY     = float( '-inf' )
    self.m_minZ     = float( '+inf' )
    self.m_maxZ     = float( '-inf' )

    if inputFile is not None :
      # File name was given.  Read the data from the file.
      self.loadFile( inputFile )

  def loadFile( self, inputFile ) :
    with open( inputFile, 'r' ) as fp :
      lines = fp.read().replace('\r', '' ).split( '\n' )

    for ( index, line ) in enumerate( lines, start = 1 ) :
      line = line.strip()
      if ( line == '' or line[ 0 ] == '#' ) :
        continue

      if ( line[ 0 ] == 'v' ) :
        try :
          ( _, x, y, z ) = line.split()
          x = float( x )
          y = float( y )
          z = float( z )

          self.m_minX = min( self.m_minX, x )
          self.m_maxX = max( self.m_maxX, x )
          self.m_minY = min( self.m_minY, y )
          self.m_maxY = max( self.m_maxY, y )
          self.m_minZ = min( self.m_minZ, z )
          self.m_maxZ = max( self.m_maxZ, z )

          self.m_Vertices.append( ( x, y, z ) )

        except :
          print( 'Line %d is a malformed vertex spec.' % index )

      elif ( line[ 0 ] == 'f' ) :
        try :
          ( _, v1, v2, v3 ) = line.split()
          v1 = int( v1 )-1
          v2 = int( v2 )-1
          v3 = int( v3 )-1
          self.m_Faces.append( ( v1, v2, v3 ) )

        except :
          print( 'Line %d is a malformed face spec.' % index )

      ##################################################
      # Put your Python code for reading and processing the w and
      # s lines here.
      #
      # The w line has four floats after the w.  Convert the
      # string representation to float and save the four values
      # as a tuple in self.m_Window.  Report any conversion errors
      # or if there are not exactly four floats following the w.

      elif ( line[ 0 ] == 'w' ) :
        try :
          ( _, xmin, ymin, xmax, ymax ) = line.split()
          xmin = float( xmin )
          ymin = float( ymin )
          xmax = float( xmax )
          ymax = float( ymax )

          if self.m_Window != None : 
            print( 'Line %d is a duplicate window spec.' % index )
          self.m_Window = ( ( xmin, ymin, xmax, ymax ) )

        except :
          print( 'Line %d is a malformed window spec.' % index )

      # The s line has four floats after the s.  Convert the
      # string representation to float and save the four values
      # as a tuple in self.m_Viewport.  Report any conversion
      # errors or if there are not exactly four floats following
      # the s.  (It's OK for an int to be given instead of a
      # float.  That is, for example, 1 is OK instead of 1.0.)

      elif ( line[ 0 ] == 's' ) :
        try :
          ( _, xmin, ymin, xmax, ymax ) = line.split()
          xmin = float( xmin )
          ymin = float( ymin )
          xmax = float( xmax )
          ymax = float( ymax )

          if self.m_Viewport != None : 
            print( 'Line %d is a duplicate viewport spec.' % index )
          self.m_Viewport = ( ( xmin, ymin, xmax, ymax ) )

        except :
          print( 'Line %d is a malformed viewport spec.' % index )

      # Finally, there should be no more than one w line and no
      # more than one s line in the model file.  If there is more
      # than one of either kind of line, each such line should be
      # reported as a duplicate.
      #
      # If there are duplicate w and/or s lines, remember the
      # values from the _last_ valid such line.
      ##################################################

      else :
        print( 'Line %d \'%s\' is unrecognized.' % ( index, line ) )
  
  #Get Center

  def getCenter( self ) :
    return (
      ( self.m_minX + self.m_maxX ) / 2.0,
      ( self.m_minY + self.m_maxY ) / 2.0,
      ( self.m_minZ + self.m_maxZ ) / 2.0 )

  def getFaces( self )    : return self.m_Faces
  def getVertices( self ) : return self.m_Vertices
  def getViewport( self ) : return self.m_Viewport
  def getWindow( self )   : return self.m_Window

  #Specify Transform
  def specifyTransform( self, ax, ay, sx, sy ) :
    self.m_ax = ax
    self.m_ay = ay
    self.m_sx = sx
    self.m_sy = sy


  #Get Vertex
  def getTransformedVertex( self, vNum ):
    v = self.m_Vertices[vNum]
    x1 = (self.m_sx*v[0]+self.m_ax)
    y1 = (self.m_sy*v[1]+self.m_ay)
    return (x1, y1, 0.0)

#---------#---------#---------#---------#---------#--------#
def _main() :
  # Get the file name to load.
  fName = sys.argv[1]

  # Create a ModelData object to hold the model data from
  # the supplied file name.
  model = ModelData( fName )

  # Now that it's loaded, print out a few statistics about
  # the model data that we just loaded.
  print( f'{fName}: {len( model.getVertices() )} vert%s, {len( model.getFaces() )} face%s' % (
    'ex' if len( model.getVertices() ) == 1 else 'ices',
    '' if len( model.getFaces() ) == 1 else 's' ))

  print( 'First 3 vertices:' )
  for v in model.getVertices()[0:3] :
    print( f'     {v}' )

  print( 'First 3 faces:' )
  for f in model.getFaces()[0:3] :
    print( f'     {f}' )

  print( f'Window line    : {model.getWindow()}' )
  print( f'Viewport line  : {model.getViewport()}' )

  print( f'Center         : {model.getCenter()}' )

#---------#
if __name__ == '__main__' :
  _main()

#---------#---------#---------#---------#---------#--------#
