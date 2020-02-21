import requests
import os
from bs4 import BeautifulSoup

import pandas as pd
import json

# %%


def request_icsd_property(prop, icsd=True):
    '''
    Input
    -----
    prop: str
        property from list of valid aflow properties

    Return
    -----
    df: pandas.DataFrame
        DataFrame containing property information
    '''

    api_url = 'http://aflowlib.duke.edu/search/API/?'

    # paging(0) returns all instances of data in the aflow catalog
    if icsd is True:
        catalog_url = '(),catalog(icsd),paging(0)'
    else:
        catalog_url = '(),paging(0)'

    url = api_url + prop + catalog_url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = json.loads(str(soup))
    df = pd.DataFrame(data).T
    return df


def list_aflow_urls(icsd=True):
    df = request_icsd_property(prop='aurl', icsd=icsd)
    aflow_api_urls = df['aurl'].str.replace(':', '/')
    aflow_entries = df['aurl'].str.split('/').str.get(-1).to_list()
    return aflow_api_urls, aflow_entries


def download_cif_files(icsd=True):
    aflow_api_urls, aflow_entries = list_aflow_urls(icsd)
    for url, entry in zip(aflow_api_urls, aflow_entries):
        cif_url = 'http://' + url + '/' + entry + '.cif'
        response = requests.get(cif_url)
        open('cif_files/'+entry+'.cif', 'wb').write(response.content)


def download_property_files(icsd=True):
    property_files = os.listdir('property_files')
    aflow_api_urls, aflow_entries = list_aflow_urls(icsd)
    for url, entry in zip(aflow_api_urls, aflow_entries):
        if entry+'.json' in property_files:
            pass
        else:
            try:
                cif_url = 'http://' + url + '/' + 'aflowlib.json'
                response = requests.get(cif_url)
                open('property_files/'+entry+'.json',
                     'wb').write(response.content)
            except:
                print('error:', entry)


# get aflow cif files from the icsd
download_cif_files(icsd=True)

# get aflow property files from the icsd
download_property_files(icsd=True)
