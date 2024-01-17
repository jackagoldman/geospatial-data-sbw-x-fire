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
          data_defoliated.append({'geometry': fire['geometry'].intersection(bw['geometry']), 'defol_year': bw['Year'], 'fire_year': fire['Fire_Year']}) # can i add a column that calculates the difference between bw year and fire year?
          data_non_defoliated.append({'geometry': fire['geometry'].difference(bw['geometry']), 'defol_year': bw['Year'], 'fire_year': fire['Fire_Year']})

df = gp.GeoDataFrame(data_defoliated,columns=['geometry', 'defol_year', 'Fire_Year'])

print(df)




#jpbw.to_file(outfolder / 'jpbw-on-1937-2018.shp') # export it to folder