#!/usr/bin/env python

from  __future__ import  print_function
from releaseCommon import Version

v = Version()
v.incrementPatchNumber()
v.updateVersionFile()
v.updateReadmeFile()

print( "Updated Version.hpp and README to v{0}".format( v.getVersionString() ) )