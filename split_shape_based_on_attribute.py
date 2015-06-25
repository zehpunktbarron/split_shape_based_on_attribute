# Script created to separate one shapefile in multiple ones by one specific
# attribute. In this script based on the column "ID"

import arcpy

#Set Input Output variables
inputFile = u"D:\SGJ3D_DXF-Export\dxf_lod1_stadtbezirksname.shp"
outDir = u"D:\SGJ3D_DXF-Export\splittet_export\\"

# Reads shapefile for different values in the attribute
rows = arcpy.SearchCursor(inputFile)
row = rows.next()
attribute_types = set([])

while row:
    attribute_types.add(row.ID)
    row = rows.next()

# Output a Shapefile for each different attribute
for each_attribute in attribute_types:
    outSHP = outDir + 'dxf_lod1_' + each_attribute + u".shp"
    print outSHP
    arcpy.Select_analysis (inputFile, outSHP, "\"ID\" = '" + each_attribute + "'")

del rows, row, attribute_types
