# Purser, Charles N.
# cnp1474
# 2019-01-31

import sys

class ModelData() :
  def __init__( self, inputFile = None ) :
    self.m_Vertices = []
    self.m_Faces    = []

    if inputFile is not None :
      # File name was given.  Read the data from the file.
      self.loadFile( inputFile )

  def loadFile( self, inputFile ) :
    ##################################################
    # Put your Python code for reading and processing the lines
    # from the source file in the place of the comments below.
    # (The comments give all the direction you should need to
    #  write the code.  It's not all that difficult.)
    ##################################################
    
    # Read each line of the file.
    with open( inputFile, 'r' ) as fp :
      lines = fp.read().replace('\r', '' ).split( '\n' )
    
    # Ignore any blank line (or line that's only whitespace characters).
    for ( index, line ) in enumerate( lines, start = 1 ) :
      if(line.strip()) :
        line = line.strip()
      # Ignore any line that starts with a #.
        if not line.startswith( '#' ) :

        # For the remaining lines, if the line starts with:

        #  f -- Append the three integers as a tuple to self.m_Faces.
          if line.startswith( 'f' ) :
            line = line.strip('f')
            stringVar = line.split()
            temp = [] 
            count = 0
            check = 0
            for i in stringVar :
              count += 1
              try :            
                intVar = int( i )
              #  Subtract 1 to match EXACTLY
                intVar -= 1
                temp.append( intVar )    
              except :
                print("Line " + str( index ) +" is a malformed face spec.")
                count += 4
                check = 1
            if ( count == 3 ) :      
              self.m_Faces.append( tuple( temp ) ) 
            else :
              if ( check != 1 ) :
                print("Line " + str( index ) +" is a malformed face spec.")

        #  v -- Append the three floats as a tuple to self.m_Vertices.
          elif line.startswith( 'v' ) :
            line = line.strip( 'v' )
            stringVar = line.split()
            temp = []
            count = 0
            check = 0
            for i in stringVar :
              count += 1
              try :            
                floatVar = float( i )
                temp.append( floatVar )    
              except :
                print( "Line " + str( index ) +" is a malformed vertex spec." )
                count += 4
                check = 1
            if ( count == 3 ) :
              self.m_Vertices.append( tuple( temp ) )
            else :
              if (check != 1 ) :
                print( "Line " + str( index ) +" is a malformed vertex spec." )
          else :  
            print( "Line " + str( index ) + " '" + line + "' is unrecognized." )

  def getCenter( self ) :
    #initialize
    minX = self.m_Vertices[0][0]
    maxX = minX
    minY = self.m_Vertices[0][1]
    maxY = minY
    minZ = self.m_Vertices[0][2]
    maxZ = minZ
      
    for i in self.m_Vertices :              
      if( i[0] < minX ) :
        minX = i[0]
      elif( i[0] > maxX ) : 
        maxX = i[0]
      if( i[1] < minY ) :
        minY = i[1]
      elif( i[1] > maxY ) : 
        maxY = i[1]
      if( i[2] < minZ ) :
        minZ = i[2]
      elif( i[2] > maxZ ) : 
        maxZ = i[2]

    Xcent = ((minX + maxX)/2)
    Ycent = ((minY + maxY)/2)
    Zcent = ((minZ + maxZ)/2)
    Center = [Xcent, Ycent, Zcent]
    return ( tuple( Center ) )

      # Note that the above comments mention integers and floats.
    # You must convert the string representation of the integers
    # and floats into actual numbers.  There may be formatting
    # errors in the file, so ensure you catch (and report)
    # conversion errors.

    # It is an error if a line starts with any other character.
    # Print an error message for that line, but keep going and look
    # at the rest of the lines.

    # A model file may have any number of f and v lines.  In fact,
    # some model files we will use will have thousands of v and f
    # lines.

    ##################################################
    # All the code you have to write should go above here in the
    # body of the loadFile() routine.
    ##################################################

  def getFaces( self )    : return self.m_Faces
  def getVertices( self ) : return self.m_Vertices

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

#---------#
if __name__ == '__main__' :
  _main()

#---------#---------#---------#---------#---------#--------#
