import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

PETROLE_PRODUCTION = 'https://datos.gob.mx/busca/dataset/produccion-de-petroleo-crudo-por-activos-y-region-estructura-a-partir-del-2004'
METHANE_DERIVATES = 'https://datos.gob.mx/busca/dataset/elaboracion-de-productos-petroquimicos-derivados-del-metano'
PUBLIC_PRICE = 'https://datos.gob.mx/busca/dataset/precio-publico-ponderado-de-productos-petroliferos-seleccionados'

def read_csv(target) :
    ds = pd.read_csv(target, skip_blank_lines=True, header=None, encoding='latin-1')
    ds = ds.drop(ds.columns[0], axis=1)
    ds = ds.dropna(how='all')
    ds = ds.transpose()
    ds = ds.drop(ds.columns[0], axis=1)
    return ds

def get_data_from_site(url) :
    try :
        resp = requests.get(url)
        if resp.status_code == 200 :
            inner_html = resp.content.decode('utf-8')
            soup = bs(inner_html, 'html.parser')
            csv_link = soup.find(class_='btn-primary', text='Descargar').get('href')
            return read_csv(csv_link)
        
        else :
            raise ValueError('Retrieved status code: ' + str(resp.status_code))
    
    except ValueError as e :
        print('An error occurred attempting to get data - ', e)

    return False

def fill_nan_data(df) :
    for col in df.columns :
        df.loc[df[col] == 'N/D', col] = 0

    return df.set_index('fecha')

def run() :
    df_petrole_production = get_data_from_site(PETROLE_PRODUCTION)
    df_petrole_production.columns = ['fecha','totalLb','marinaNoreste','cantarell','kmz','marinaSuroeste','apc','tabasco',
        'regionSur','presidentes','bellota','macuspana','samaria','regionNorte','burgos','pozaRica',
        'atg','veracruz']
    
    df_petrole_production = fill_nan_data(df_petrole_production)
    df_petrole_production.to_csv('csv/petrole_production.csv')

    df_methane_derivates = get_data_from_site(METHANE_DERIVATES)
    df_methane_derivates.columns = ['fecha','carbonico','amoniaco','metanol','etileno','dicloroetano','oxietileno','polietilenoBD',
        'polietilenoLineal','acetaldehido','cloruroVinilo','polietilenoAD','glicoles','percloroetileno','xileno','tolueno',
        'paraxileno','estilbenceno','estireno','aromina100','altoOctano','benceno','aromaPesados','ortoxileno',
        'fluxoil','cumeno','gasAmorfa','gasOctano','propileno','acrilonitrilo','polipropileno','cianhidrico',
        'acetonitrilo','isopropanol','otros','total','largoLigero']
   
    df_methane_derivates = fill_nan_data(df_methane_derivates)
    df_methane_derivates.to_csv('csv/methane_derivates.csv')

    df_public_price = get_data_from_site(PUBLIC_PRICE)
    df_public_price.columns = ['fecha','pemexMagna','pemexPremium','pemexDiesel','combustoleoPesado','dieselMarino']
    
    df_public_price = fill_nan_data(df_public_price)
    df_public_price.to_csv('csv/public_price.csv')

    dfx= pd.concat([df_petrole_production,df_methane_derivates,df_public_price], axis=1, join='inner')
    dfx.to_csv('csv/db_hydrocarbons.csv')
    
    print('Process is complete!')

if __name__ == '__main__' :
    run()