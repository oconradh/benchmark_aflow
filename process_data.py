from sklearn.model_selection import train_test_split
import pandas as pd
import os


def train_val_test_split(data, target):
    train_frac = 0.7
    val_frac = 0.15
    vt_frac = val_frac / (1 - train_frac)
    train_data, vt_data = train_test_split(data,
                                           train_size=train_frac,
                                           shuffle=True,
                                           random_state=1)
    val_data, test_data = train_test_split(vt_data,
                                           train_size=vt_frac,
                                           shuffle=True,
                                           random_state=1)
    os.makedirs('processed_data/'+target, exist_ok=True)
    train_data.to_csv('processed_data/'+target+'/'+'train.csv',
                      index=False,
                      header=True)
    val_data.to_csv('processed_data/'+target+'/'+'val.csv',
                    index=False,
                    header=True)
    test_data.to_csv('processed_data/'+target+'/'+'test.csv',
                     index=False,
                     header=True)


def main(drop_duplicates=True):
    file_location = 'data/'
    data_files = os.listdir(file_location)
    for target in data_files:
        target = target[:-4]
        data = pd.read_csv('data/ael_shear_modulus_vrh.csv')
        data.columns = ['cif_file', 'target']
        formula = data['cif_file'].str.split('_ICSD_').str[0]
        data.insert(1, 'formula', formula)
        if drop_duplicates:
            data = data.drop_duplicates('formula')
        train_val_test_split(data, target)


main()
