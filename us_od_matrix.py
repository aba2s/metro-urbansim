import pandas as pd
# import pyreadstat

print("-----------------------------------------------------------------")
print("====================== 1. HOUSEHOLDS ==============================")
print("-----------------------------------------------------------------")

"""
Cette matrice contient 5. 199. 198 ménages 
"""

house_holds = pd.read_csv('./US_OD_Matrix/households2018.csv')
house_holds.drop('household_id', axis=1, inplace=True)
house_holds.rename(columns={'Unnamed: 0': 'household_id'}, inplace=True)
# house_holds.drop_duplicates(subset=['household_id'], inplace=True)
# print(house_holds.isnull().any())

print("-----------------------------------------------------------------")
print("======================= 2. WORKERS ==============================")
print("-----------------------------------------------------------------")

"""
Ce fichier contient 5. 344. 481 dont 7 ménagnes manquants (Nan).
"""

workers = pd.read_csv('./US_OD_Matrix/workers2018.csv')
workers.drop('Unnamed: 0', axis=1, inplace=True)
#print(workers.isnull().sum())
workers.dropna(inplace=True)

workers['id'] = workers.apply(lambda x: int(x['household_id']), axis=1)
workers.drop('household_id', axis=1, inplace=True)
workers.rename(columns={'id': 'household_id'}, inplace=True)
#workers['household_id'] = workers['household_id'].astype(int)
print(workers.head())
print(workers.shape)

print("-----------------------------------------------------------------")
print("============= 2. MATRICE DE CORRESPONDANCES =====================")
print("-----------------------------------------------------------------")

df = workers.merge(house_holds, on='household_id', how='left')
df = df.loc[:, ::-2]

# counter = size =1
df['counter'] = df.apply(lambda x: 1, axis=1)

# Sorting
df.sort_values(by=['zone_id', 'workzone_id'], 
    ignore_index=True, inplace=True)

# calcul of the size of each OD pair
df['size'] = df.groupby(['zone_id','workzone_id'])['counter'].transform('sum')
df.drop_duplicates(subset=['zone_id', 'workzone_id'], inplace=True)
df.reset_index(drop=True, inplace=True)
print(df.head())
print(df.shape)

print("----------------------------------------------------------------")
print("========================== MATRICE DES POIDS ==========================")
print("----------------------------------------------------------------")

weight_matrix = pd.read_csv('./ODpondUS_METRO.csv', sep=',')
weight_matrix.drop(['libgeoD', 'libgeoO'], axis = 1, inplace = True)
print(weight_matrix.head())
print(weight_matrix.shape)


print("----------------------------------------------------------------")
print("========================== MERGING ==========================")
print("----------------------------------------------------------------")

matrix = weight_matrix.merge(df, how='left', left_on=['zoneU_O', 'zoneU_D'],
    right_on=['zone_id', 'workzone_id'])
matrix.drop(['zone_id', 'workzone_id', 'counter', 'zoneU_D', 'pond_tc',
    'pond_tcgpe', 'pond_vp', 'pond_vpgpe', 'fluxtc', 'fluxtcgpe', 'fluxvp', 
    'fluxvpgpe', 'fluxgpetot', 'fluxtot', 'size_tc_by_U', 'size_tcgpe_by_U',
    'size_vp_by_U', 'size_vpgpe_by_U', 'size_gpetot', 'size_nogpetot',], 
    axis=1, inplace=True)
print(matrix.head())
print()
print(matrix.columns.to_list())
matrix['trips'] = matrix.apply(lambda x: x['pond_nogpe']*x['size'], axis=1)
print(matrix.head())
print(matrix.isnull().sum())

"""
si scenario
"""
"""
if scenario =='Ref':
    matrix['trips'] = matrix.apply(lambda x: x['pond_nogpe']*x['size'])
else:
    matrix['trips'] = matrix.apply(lambda x: x['pond_gpe']*x['size'])
"""


