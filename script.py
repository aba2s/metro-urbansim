import pandas as pd
print("--------------------- PROCESS STARTING ------------------------- ")
print("-----------------------------------------------------------------")
print("====================== 1. HOUSEHOLDS ============================")
print("-----------------------------------------------------------------")

"""
Cette matrice contient 5. 199. 198 ménages
"""

households = pd.read_csv('./US_OD_Matrix/households2018.csv')
households.drop('household_id', axis=1, inplace=True)
households.rename(columns={'Unnamed: 0': 'household_id'}, inplace=True)
# households.drop_duplicates(subset=['household_id'], inplace=True)
# print(households.isnull().any())
print(households.isna().sum())
print(households.shape)

print("-----------------------------------------------------------------")
print("======================= 2. WORKERS ==============================")
print("-----------------------------------------------------------------")

"""
Ce fichier contient 5. 344. 481 dont 7 ménagnes manquants (Nan).
"""

workers = pd.read_csv('./US_OD_Matrix/workers2018.csv')
workers.drop('Unnamed: 0', axis=1, inplace=True)
#  print(workers.isnull().sum())
workers.dropna(inplace=True)
# workers.astype({'household_id': 'int32'})
workers['household_id'] = workers['household_id'].astype(int)
print(workers.isna().sum())
print(workers.shape)
print("-----------------------------------------------------------------")
print("===== 2. MATRICE DE CORRESPONDANCES WORKERS <> HOUSEHOLDS =======")
print("-----------------------------------------------------------------")

workers_households = workers.merge(households, on='household_id', how='left')
workers_households.drop('household_id', axis=1, inplace=True)
# Reversing columns orders
# workers_households = workers_households.loc[:, ::-1]
workers_households = workers_households[workers_households.columns[::-1]]


# workers_households.sort_values(by=['zone_id', 'workzone_id'],
#    ignore_index=True, inplace=True)

workers_households['size_from_workers'] = workers_households.groupby(
    ['zone_id', 'workzone_id'])['workzone_id'].transform('count')
xx = workers_households.loc[workers_households['zone_id'] == 1]
print('start')
print(xx[xx['workzone_id'] == 21])
print('fin')
print(workers_households.dtypes)
print('')
print(workers_households.duplicated().value_counts())
print('')
print(workers_households.isna().sum())
print('')
print(workers_households.shape)
print("----------------------------------------------------------------")
print("========================== WEIGHT MATRIX =======================")
print("----------------------------------------------------------------")

cols_to_use = ['origin', 'destination', 'zoneU_O', 'zoneU_D', 'pond_gpe', 'pond_nogpe']
weight_matrix = pd.read_csv('./ODpondUS_METRO.csv', sep=',', usecols=cols_to_use)
weight_matrix.rename(columns={'zoneU_O': 'zone_id',
    'zoneU_D': 'workzone_id'}, inplace=True)

print(weight_matrix.dtypes)
print('')
print(weight_matrix.isna().sum())
print('')
print(weight_matrix.shape)

print("----------------------------------------------------------------")
print("==== MATRICE DE CORRESPONDANCE WEIGHT <> WORKERS_HOUSEHOLS =====")
print("----------------------------------------------------------------")

workers_households.drop_duplicates(subset=['zone_id', 'workzone_id'], inplace=True)
print(workers_households.shape)
od_trips = weight_matrix.merge(workers_households, how='left',
    on=['zone_id', 'workzone_id'])

print(od_trips.isna().sum())
print(od_trips.shape)
#print(od_trips.head())
#print(od_trips.loc[od_trips['size'].isna(), ].head(10))

# certains pairs (zone_id, workzone_id) n'ont pas de size dans le merge final.
# Par exemple le pair (1, 21) n'existait pas dans workers_households. Nous allons
# le calculer maintenant.

od_trips['size_after_merge'] = od_trips.groupby(
    ['zone_id','workzone_id'])['workzone_id'].transform('count')

od_trips['size'] = od_trips.apply(
    lambda x: x['size_from_workers'] if pd.notna(x['size_from_workers'])
        else x['size_after_merge'], axis=1)
# od_trips.drop(['size_from_workers','size_after_merge'], axis=1, inplace=True)
print(od_trips.head())
print(od_trips.loc[od_trips['size_from_workers'].isna(), ].head(10))

print(od_trips.isna().sum())
