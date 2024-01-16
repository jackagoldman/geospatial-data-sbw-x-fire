# script to create defoliation tables to be input into sql database

import pandas as pd
import numpy as np

### read in files
#fire key
fire_key = pd.read_csv('/Users/jgoldman/Library/CloudStorage/OneDrive-UniversityofToronto/Data/fire-only-sbw-only-perimeters/database_files/fire_key.csv')
#defoliation data
defol_data = pd.read_csv('/Users/jgoldman/Work/PhD/sbw-fire-interactions/nbr-recovery/data/clean/sbw-defol-data-v2.csv')

# create defol column 
# in defol column 1 = defoliated 0 = non defoliated
# defoliated from id column 1-34 
# non defoliated from id column 35-68
defol = pd.DataFrame(fire_key[["id", "fire_name"]])
defol['defol'] = np.where(defol['id'].isin(list(range(1,35))), 1, 0)

#join defoliation tsd and number of years defol by fire_name
defol_data = defol_data.rename(columns = {'Fire_ID' : 'fire_name'})
defol_data = defol_data[['fire_name', 'years_defol', 'tsd']]
defol = pd.merge(defol, defol_data, on='fire_name', how='inner')
