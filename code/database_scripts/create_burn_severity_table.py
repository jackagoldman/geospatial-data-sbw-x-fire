# script to create burn severity table for the database

import pandas as pd
import numpy as np

### read in files
#fire key
defol_table = pd.read_csv('/Users/jgoldman/Library/CloudStorage/OneDrive-UniversityofToronto/Data/fire-only-sbw-only-perimeters/database_files/defol_table.csv')
#defoliation data
severity_defol_data = pd.read_csv('/Users/jgoldman/Library/CloudStorage/OneDrive-UniversityofToronto/Data/fire-only-sbw-only-perimeters/cleaned/rbr/non-defol/non-defol-fire-perims-rbr.csv')
#non defoliated data
severity_non_defol_data = pd.read_csv("/Users/jgoldman/Library/CloudStorage/OneDrive-UniversityofToronto/Data/fire-only-sbw-only-perimeters/cleaned/rbr/defol/defoliated-perims-rbr-v2.csv")

#rename Fire_ID column to fire_name in severity data
#defoliated
severity_defol_data = severity_defol_data[['Fire_ID', 'rbrCV', 'rbrExtreme', 'rbrMedian']].rename(columns = {'Fire_ID' : 'fire_name'})
#non defolitaed
severity_non_defol_data = severity_non_defol_data[['Fire_ID', 'rbrCV', 'rbrExtreme', 'rbrMedian']].rename(columns = {'Fire_ID' : 'fire_name'})

#merge both severity dataframes to just include the fire names that are in the fire key
#defoliated
sev_defol = defol_table[defol_table['defol'] == 1].merge(severity_defol_data, on = 'fire_name', how = "inner")
#non-defoliated
sev_nondefol = defol_table[defol_table['defol'] == 0].merge(severity_non_defol_data, on ='fire_name', how='inner')


# keep id and fire_name columns
#defolaited
sev_defol = sev_defol[['id', 'fire_name', 'rbrCV', 'rbrExtreme', 'rbrMedian']]
#non defolaited
sev_nondefol = sev_nondefol[['id', 'fire_name', 'rbrCV', 'rbrExtreme', 'rbrMedian']]

#concatenate dataframe
severity_table = pd.concat([sev_defol, sev_nondefol])


