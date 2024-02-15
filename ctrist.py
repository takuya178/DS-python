import pandas as pd
from glob import glob

def _get_df(folder='rp_im'):
  data_dict = pd.DataFrame({
    'FilePath': glob(f'dataset/public-covid-data/{folder}/*'),
    'FileName': [p.split('/')[-1] for p in glob(f'dataset/public-covid-data/{folder}/*')]
  })

  return data_dict

def get_df_all():
  rp_im_df = _get_df('rp_im')
  rp_msk_df = _get_df('rp_msk')

  return rp_im_df.merge(rp_msk_df, on='FileName', suffixes=('Image', 'Mask'))
