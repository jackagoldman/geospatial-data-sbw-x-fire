# script to create ID key for fire_key for SQL database

import geopandas as gp
import pandas as pd
import numpy as np

# read in shapefiles 
defol = gp.read_file('/Users/jgoldman/Library/CloudStorage/OneDrive-UniversityofToronto/Data/fire-only-sbw-only-perimeters/cleaned/shapefiles/defoliated-compiled.shp')
non_defol = gp.read_file('/Users/jgoldman/Library/CloudStorage/OneDrive-UniversityofToronto/Data/fire-only-sbw-only-perimeters/cleaned/shapefiles/non-defoliated-compiled.shp')

# get names and years
defol = defol[['Fire_Year', 'Fire_ID']]
non_defol = non_defol[['Fire_Year', 'Fire_ID']]

#convert to pandas df
defol = pd.DataFrame(defol)
non_defol = pd.DataFrame(non_defol)

#filter non_defol dataframe to match the names in defol
#first get return fire IDs from defol as list
defol_ids = defol['Fire_ID'].tolist()

#filter non_defol by ids in list defol ids
fire_key = non_defol[non_defol['Fire_ID'].isin(defol_ids)]

#remove any fires that are later than 2012
fire_key = fire_key[fire_key['Fire_Year'] <= 2012]

#replicate each row to have a row for defoliated and a row for non defoliated
fire_key = pd.concat([fire_key]*2, ignore_index= True)

# create id column
fire_key["id"] = range(1, 69)

#make all column names lowercase
fire_key.columns = fire_key.columns.str.lower()

#rename fire_id column to fire_name
fire_key = fire_key.rename(columns ={'fire_id': 'fire_name'})
