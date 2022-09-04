
import pandas as pd 
import geopandas as gpd
"""
'zone_id_M': Zone de Metroplis
'zone_id_U': Zone de UrbanSim
"""

print("----------------------------------------------------------------")
print("====================== 1. METROPOLIS (MODUS) ===================")
print("----------------------------------------------------------------")
"""
le fichier contient 1864 observations dont 1289 valeurs uniques 
correspondant aux zones modus (zone_id_M)
"""
metro = pd.read_csv('./130322_ZONE_COMMUNE.txt', sep='\t')
metro.columns = metro.columns.str.lower()
metro.rename(columns={'zone': 'zone_id_M'}, inplace=True)


print("-----------------------------------------------------------------")
print("====================== 2. URBANSIM ==============================")
print("-----------------------------------------------------------------")

"""
Ce fichier contient 1300 observations  dont 725 valeurs uniques correspondant
aux zones urbansim (zone_id_U)
"""
us = pd.read_csv('./zonecdtcom.csv')
us.rename(columns={'com': 'commune', 'zone_id': 'zone_id_U',
    'libgeo': 'name'}, inplace=True)

print("-----------------------------------------------------------------")
print("==== 3. Matrice de correspondance US <> Metropolis (Modus) ======")
print("-----------------------------------------------------------------")

corresp_matrix = metro.merge(us, on="commune", how='left')
corresp_matrix= corresp_matrix.drop_duplicates(subset=['zone_id_M'], inplace=True)
corresp_matrix.to_csv('./merge_us_metro.csv', index=False)

# Ne plus calculer les poids par python


print("----------------------------------------------------------------")
print("========================== 4.OD TRIPS ==========================")
print("----------------------------------------------------------------")
"""
Ce fichier contient 1. 792. 105 observations 
"""
#od_trips = pd.read_csv('./tt30_new.txt', sep='\t')
#od_trips.rename(columns={'O': 'origin', 'D': 'destination'}, inplace=True)
#od_trips.drop_duplicates(subset=['origin','destination'], inplace=True)


""""
print("----------------------------------------------------------------")
print("====================== 4.TRIPS OD MATRIX =======================")
print("----------------------------------------------------------------")

od_matrix_commute = pd.read_csv('./od_matrix_commute.csv')
# Let's remove O-D pair observation for aeroport and train station (>1289)
od_matrix_commute = od_matrix_commute[(od_matrix_commute['origin']<=1289) & 
    (od_matrix_commute['destination']<=1289)]

print("-----------------------------------------------------------------")
print("====== 5. MERGING OD MATRIX WITH US_METRO BY DESTINATION ========")
print("-----------------------------------------------------------------")
columns_to_merge = ['zone_id_M','zone_id_U']
od_matrix_us_metro = od_matrix_commute.merge(
    us_metro[columns_to_merge], left_on='destination',
    right_on='zone_id_M')

# "zone_id_M" correspond to "destination" so we can delete it.
od_matrix_us_metro.drop('zone_id_M', axis=1, inplace=True)

od_matrix_us_metro['size_by_U_d'] = od_matrix_us_metro.groupby('zone_id_U')['size'].transform('sum')
od_matrix_us_metro.sort_values(by=['origin', 'destination'], ignore_index=True, inplace=True)

print(od_matrix_us_metro.head(5))
print(od_matrix_us_metro.shape)
# od_matrix_us_metro.to_csv('./pondOD_us_metro.csv', index=False)

print("-----------------------------------------------------------------")
print("======== 5. MERGING OD MATRIX WITH US_METRO BY ORIGIN ===========")
print("-----------------------------------------------------------------")

columns_to_merge = ['zone_id_M','zone_id_U']
od_matrix_us_metro_o = od_matrix_commute.merge(us_metro[columns_to_merge], 
    left_on='origin', right_on='zone_id_M')

od_matrix_us_metro_o.sort_values(by=['origin', 'destination'], ignore_index=True, inplace=True)
# "zone_id_M" correspond to "origin" so we can delete it.
od_matrix_us_metro_o.drop('zone_id_M', axis=1, inplace=True)

od_matrix_us_metro_o['size_by_U_o'] = od_matrix_us_metro_o.groupby('zone_id_U')['size'].transform('sum')
print(od_matrix_us_metro_o.head(5))
print(od_matrix_us_metro_o.shape)

print("-----------------------------------------------------------------")
print("========================== 5. FINAL OUTPUT ========================")
print("-----------------------------------------------------------------")

df = pd.concat([od_matrix_us_metro_o, od_matrix_us_metro['size_by_U_d']], axis=1)
print(df)
print(df.shape)

"""