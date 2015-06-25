# Script created to separate one shapefile in multiple ones by one specific
# attribute

# Example for a Inputfile called "my_shapefile" and a field called "my_attribute"
import arcpy

#Set Input Output variables
inputFile = u"D:\SGJ3D_DXF-Export\dxf_lod1_stadtbezirksname.shp" #<-- CHANGE
outDir = u"D:\SGJ3D_DXF-Export\splittet_export\\" #<-- CHANGE

# Reads My_shapefile for different values in the attribute
rows = arcpy.SearchCursor(inputFile)
row = rows.next()
attribute_types = set([])

while row:
    attribute_types.add(row.ID) #<-- CHANGE my_attribute to the name of your attribute
    row = rows.next()

# Output a Shapefile for each different attribute
for each_attribute in attribute_types:
    outSHP = outDir + 'dxf_lod1_' + each_attribute + u".shp"
    print outSHP
    arcpy.Select_analysis (inputFile, outSHP, "\"ID\" = '" + each_attribute + "'") #<-- CHANGE my_attribute to the name of your attribute

del rows, row, attribute_types

#END
