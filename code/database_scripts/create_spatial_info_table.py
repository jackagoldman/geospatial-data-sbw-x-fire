# script to create spatial information table 
#Author: Jack A. Goldman
#Date: 01/13/2024

import geopandas as gp
import pandas as pd
import pyarrow

# read in defol table
defol_table = pd.read_csv('/Users/jgoldman/Library/CloudStorage/OneDrive-UniversityofToronto/Data/fire-only-sbw-only-perimeters/database_files/defol_table.csv')

# read in compiled fires
#defoliated
defol = gp.read_file('/Users/jgoldman/Library/CloudStorage/OneDrive-UniversityofToronto/Data/fire-only-sbw-only-perimeters/cleaned/shapefiles/defoliated-compiled.shp')
#non defoliated
non_defol = gp.read_file('/Users/jgoldman/Library/CloudStorage/OneDrive-UniversityofToronto/Data/fire-only-sbw-only-perimeters/cleaned/shapefiles/non-defoliated-compiled.shp')

#select columns that are required
# rename id column
# make them lowercase
#defoliated
defol = defol[['Fire_ID', 'Shape_Leng', 'Shape_Area', 'geometry']].rename(columns={'Fire_ID' : 'fire_name', 'Shape_leng' : 'shape_length'})
defol.columns = defol.columns.str.lower()
#nondefoliated
non_defol = non_defol[['Fire_ID', 'Shape_Leng', 'Shape_Area', 'geometry']].rename(columns={'Fire_ID' : 'fire_name',  'Shape_leng' : 'shape_length'})
non_defol.columns = non_defol.columns.str.lower()

##merge both spatial dataframes to just include the fire names that are in the fire key
#defoliated
defol = defol_table[defol_table['defol'] == 1].merge(defol, on = 'fire_name', how = "inner")
#non-defoliated
nondefol = defol_table[defol_table['defol'] == 0].merge(non_defol, on ='fire_name', how='inner')


# keep id and fire_name columns
#defolaited
defol = defol[['id', 'fire_name', 'shape_leng', 'shape_area', 'geometry']]
#non defolaited
nondefol = nondefol[['id', 'fire_name', 'shape_leng', 'shape_area', 'geometry']]

#concatenate dataframe
spatial_table = pd.concat([defol, nondefol])

#make a centroid column
#first, convert to geodataframe and make coordinates in meters 
spatial_table = gp.GeoDataFrame(spatial_table).to_crs(crs=3857)
#now get centroid
spatial_table['fire_centroid'] = spatial_table.centroid

#fire area function
def fire_area(x):
    for index, row in spatial_table.iterrows():
        spatial_table['fire_area_ha']= spatial_table['geometry'].area / 1000
        spatial_table['fire_area_m'] = spatial_table['geometry'].area
    return spatial_table
spatial_table.apply(fire_area, axis = 1)

#fire perimeter function
def fire_perimeter(x):
    for index, row in spatial_table.iterrows():
        spatial_table['fire_perimeter_m']= spatial_table['geometry'].length 
    return spatial_table
spatial_table.apply(fire_perimeter, axis = 1)

#fire shape index function
def fire_shape_index(x):
    for index, row in spatial_table.iterrows():
        eq = '(.25 * fire_perimeter_m)/ sqrt(fire_area_m)'
        spatial_table['fire_shape_index']= spatial_table.eval(eq)
spatial_table.apply(fire_shape_index, axis = 1)


spatial_table = spatial_table[['id', 'fire_name', 'geometry', 
                               'fire_centroid', 'fire_area_ha',
                               'fire_area_m', 'fire_perimeter_m',
                               'fire_shape_index']]



spatial_table.to_wkt()

print(spatial_table)

# save as feather file because it had multiple geometry columns
spatial_table.to_feather('/Users/jgoldman/Library/CloudStorage/OneDrive-UniversityofToronto/Data/fire-only-sbw-only-perimeters/database_files/defol_table.feather')