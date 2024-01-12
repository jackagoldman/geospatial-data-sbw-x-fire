# create table for nbr recovery 

import pandas as pd
import numpy as np

### read in files
#fire key
defol_table = pd.read_csv('/Users/jgoldman/Library/CloudStorage/OneDrive-UniversityofToronto/Data/fire-only-sbw-only-perimeters/database_files/defol_table.csv')
#defoliation data
nbr_defol_data = pd.read_csv('/Users/jgoldman/Library/CloudStorage/OneDrive-UniversityofToronto/Data/fire-only-sbw-only-perimeters/cleaned/nbr-recovery/defol/defoliated_fires_nbr.csv')
#non defoliated data
nbr_non_defol_data = pd.read_csv("/Users/jgoldman/Library/CloudStorage/OneDrive-UniversityofToronto/Data/fire-only-sbw-only-perimeters/cleaned/nbr-recovery/non-defol/non_defoliated_fires_nbr.csv")

#rename Fire_ID column to fire_name in severity data
#defoliated
nbr_defol_data = nbr_defol_data[['Fire_ID', 'nbr1', 'nbr2', 
                                 'nbr3', 'nbr4', 'nbr5',
                                 'nbr6','nbr7','nbr8',
                                 'nbr9', 'nbr10']].rename(columns = {'Fire_ID' : 'fire_name'})
#non defolitaed
nbr_non_defol_data = nbr_non_defol_data[['Fire_ID', 'nbr1', 'nbr2', 
                                 'nbr3', 'nbr4', 'nbr5',
                                 'nbr6','nbr7','nbr8',
                                 'nbr9', 'nbr10']].rename(columns = {'Fire_ID' : 'fire_name'})

#merge both severity dataframes to just include the fire names that are in the fire key
#defoliated
nbr_defol = defol_table[defol_table['defol'] == 1].merge(nbr_defol_data, on = 'fire_name', how = "inner")
#non-defoliated
nbr_nondefol = defol_table[defol_table['defol'] == 0].merge(nbr_non_defol_data, on ='fire_name', how='inner')


# keep id and fire_name columns
#defolaited
nbr_defol = nbr_defol[['id', 'fire_name', 'nbr1', 'nbr2', 
                                 'nbr3', 'nbr4', 'nbr5',
                                 'nbr6','nbr7','nbr8',
                                 'nbr9', 'nbr10']]

#non defolaited
nbr_nondefol = nbr_nondefol[['id', 'fire_name', 'nbr1', 'nbr2', 
                                 'nbr3', 'nbr4', 'nbr5',
                                 'nbr6','nbr7','nbr8',
                                 'nbr9', 'nbr10']]

#concatenate dataframe
nbr_table = pd.concat([nbr_defol, nbr_nondefol])

