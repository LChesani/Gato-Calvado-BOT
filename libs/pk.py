import pickle;
from os.path import exists;

def load_pickle(default, filename):
   filename = 'bd/' + filename;
   if exists(f'{filename}.pickle'):
       with open(f'{filename}.pickle', 'rb') as f:
           return pickle.load(f)
   else:
       with open(f'{filename}.pickle', 'wb') as f:
           pickle.dump(default, f)
           return default


def save_pickle(obj, filename):
    filename = 'bd/' + filename;
    with open(f'{filename}.pickle', 'wb') as f:
        pickle.dump(obj, f)