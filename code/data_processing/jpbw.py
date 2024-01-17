# clip JPBW 

import pandas as pd
import geopandas as gp
import geopandas as gpd

# read in file
jpbw = gp.read_file('/Users/jgoldman/Library/CloudStorage/GoogleDrive-jandrewgoldman@gmail.com/My Drive/Projects-Data/shelley-data/data/insect-defoliation/jpbw/raw/jpbw-on-1937-2018.shp')
# Check columns
print(jpbw.info())

# Remove years after 1970 and 2012
jpbw = jpbw[(jpbw['Year'] >= 1970) & (jpbw['Year'] <= 2012)]

jpbw = gp.GeoDataFrame(jpbw)

#read in all fires

fires = gp.GeoDataFrame.from_file('/Users/jgoldman/Library/CloudStorage/GoogleDrive-jandrewgoldman@gmail.com/My Drive/Fire-SBW project/fire-perimeters/ON_FirePerimeters_85to2020_v00.shp')

# for loop to get intersection between two polygons

data_defoliated = []
data_non_defoliated = []

for index, fire in fires.iterrows(): #for each row in fires
    
    fire_year = fire['Fire_Year']
    fire_year15 = (fire_year - 15)
    print(fire_year15)
    jpbw = jpbw[(jpbw['Year'] <= fire_year)] 
    jpbw = jpbw[jpbw['Year'] >= fire_year15]# get bw year to between 15 years 
    print(jpbw)
    for index2, bw in jpbw.iterrows(): # for each row in jpbw
        if fire['geometry'].intersects(bw['geometry']):
          data_defoliated.append({'geometry': fire['geometry'].intersection(bw['geometry']), 'defol_year': bw['Year'], 'fire_year': fire['Fire_Year'], 'fire_name': fire['Fire_ID']}) # can i add a column that calculates the difference between bw year and fire year?
          data_non_defoliated.append({'geometry': fire['geometry'].difference(bw['geometry']), 'defol_year': bw['Year'], 'fire_year': fire['Fire_Year'], 'fire_name': fire['Fire_ID']})

defol_fires = gp.GeoDataFrame(data_defoliated,columns=['geometry', 'defol_year', 'fire_year', 'fire_name']).to_crs(crs=3857)
non_defol_fires = gp.GeoDataFrame(data_non_defoliated,columns=['geometry', 'defol_year', 'fire_year', 'fire_name']).to_crs(crs=3857)

# make sure we take the greatest defoliated area so the greatest perimeter
# for every fire, calculate the area of the perimeter
# function for getting fire area

def fire_area(x):
    """fire area function returns the area of a fire 
       as a new column in hectares (fire_area_ha)
    """
    for index, row in x.iterrows():
        x['fire_area_ha']= x['geometry'].area / 1000
        return x

defol_fires.apply(fire_area, axis = 1)
non_defol_fires.apply(fire_area, axis = 1)

# loop through fires and return the largest area
fire = defol_fires[defol_fires['fire_name']]
data_defoliated2 = []

for fire_name, fire in defol_fires.iteritems():
    maxfire = fire.loc[fire['area'] == fire['area'].max()]
    data_defoliated2.append({'geometry': maxfire['geometry'], 'defol_year': maxfire['defol_year'], 'fire_year': maxfire['fire_year'], 'fire_name': maxfire['fire_name'] })


defol_fires2 = gp.GeoDataFrame(data_defoliated2,columns=['geometry', 'defol_year', 'fire_year', 'fire_name'])
print(defol_fires2)









#jpbw.to_file(outfolder / 'jpbw-on-1937-2018.shp') # export it to folder