import json
import pandas as pd
import os
import tqdm


def get_csv(targets):
    file_location = 'property_files/'
    json_files = os.listdir(file_location)
    keys = set()
    # data_dict tracks if the json file has that target value as a key
    data_dict = {}
    for target in targets:
        data_dict[target] = {}
    # this loop reads each json, gets all possible 'keys',
    # and updates data_dict
    for json_data in tqdm.tqdm(json_files):
        with open(file_location + json_data) as json_file:
            data = json.load(json_file)
            for key in data.keys():
                keys.add(key)
        for target in targets:
            if target in data.keys():
                data_dict[target][json_data] = data[target]

    # list all the key values
    all_keys = list(keys)
    df_valid_targets = pd.Series(all_keys)
    df_valid_targets.to_csv('valid_targets.csv',
                            index=False,
                            header=True)

    # convert the dictionary to a pandas series and save as .csv
    os.makedirs('data', exist_ok=True)
    for target in targets:
        df_data = pd.Series(data_dict[target], name=target)
        df_data.to_csv('data/'+target+'.csv',
                       index_label='cif_id',
                       header=True)


def main():
    # here you can put in the target value you want to get properties for
    targets = ['ael_shear_modulus_vrh',
               'ael_bulk_modulus_vrh',
               'ael_debye_temperature',
               'agl_thermal_expansion_300K',
               'agl_thermal_conductivity_300K',
               'Egap',
               'energy_atom']

    get_csv(targets)


main()
