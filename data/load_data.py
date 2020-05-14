#!/usr/bin/env python
# coding: utf-8

# In[37]:


import pandas as pd
import os

def load_csse_data():
    ## On commence par générer le lien relatif aux données en supposant que le script est lancé d'un dossier externe
    curdir = __file__.strip(os.path.basename(__file__))
    
    ## On charge les données
    df1 = pd.read_csv(curdir+'csse_covid19_time_series/time_series_covid19_confirmed_global.csv', sep=',')
    df2 = pd.read_csv(curdir+'csse_covid19_time_series/time_series_covid19_deaths_global.csv', sep=',')
    df3 = pd.read_csv(curdir+'csse_covid19_time_series/time_series_covid19_recovered_global.csv', sep=',')
    
    ## On filtre sur le sous-ensemble qui nous intéresse (le Canada dans notre cas)
    df_conf = df1.loc[df1['Country/Region'] == 'Canada']
    df_deat = df2.loc[df2['Country/Region'] == 'Canada']
    df_glob = df3.loc[df3['Country/Region'] == 'Canada']
    
    df_conf.drop(['Province/State', 'Country/Region', 'Lat', 'Long'], axis=1, inplace=True)
    df_deat.drop(['Province/State', 'Country/Region', 'Lat', 'Long'], axis=1, inplace=True)
    
    lc = []
    ld = []
    
    for key,value in df_conf.iteritems():
        lc.append(df_conf[key].sum())
        
    for key,value in df_deat.iteritems():
        ld.append(df_deat[key].sum())
        
    ret = pd.DataFrame()
    ret['t'] = list(range(105))
    ret['I'] = lc
    ret['D'] = ld
    
    return ret


# In[ ]:




