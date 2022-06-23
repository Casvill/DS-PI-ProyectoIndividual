import pandas as pd


def transformar(path:str,sep:str,encoding:str) -> pd.DataFrame:
    """
    Transforma los datos
    """

    
    nombre_archivo = path.split('/')[-1][:-4]
    df = pd.read_csv(path,sep=sep,encoding=encoding)


    if len(nombre_archivo) >= 8 and nombre_archivo[:8] == 'Clientes':
        nombre_archivo = 'Clientes'
        df.drop(columns='col10',inplace=True)

        x = df['X'].replace(to_replace=r',', value='.', regex=True)
        df['X'] = pd.to_numeric(x)
        y = df['Y'].replace(to_replace=r',', value='.', regex=True)
        df['Y'] = pd.to_numeric(y)

        df['X'][df.X > 0] = df['X'][df.X > 0] * -1
        df['Y'][df.Y > 0] = df['Y'][df.Y > 0] * -1

        df['Longitud'] = df['Y']
        df['Latitud'] = df['X']
        df.drop(columns=['X','Y'],inplace=True)

        df['Edad'][df.Edad <= 30] = 30

        df['Rango_Etario'] = '-'
        df['Rango_Etario'][df.Edad <= 30] = '1_Hasta 30 años'
        df['Rango_Etario'][(df.Edad <= 40) & (df.Rango_Etario == '-')] = '2_De 31 a 40 años'
        df['Rango_Etario'][(df.Edad <= 50) & (df.Rango_Etario == '-')] = '3_De 41 a 50 años'
        df['Rango_Etario'][(df.Edad <= 60) & (df.Rango_Etario == '-')] = '4_De 51 a 60 años'
        df['Rango_Etario'][(df.Edad > 60) & (df.Rango_Etario == '-')] = '5_Desde 60 años'
    
    elif nombre_archivo == 'Compra':
        df.drop(columns=['Fecha_Año','Fecha_Mes','Fecha_Periodo'],inplace=True)

        df['Fecha'] = pd.to_datetime(df['Fecha'])


    elif nombre_archivo == 'Gasto':
        df['Fecha'] = pd.to_datetime(df['Fecha'])


    elif nombre_archivo == 'Localidades':
        df.rename(columns={'centroide_lon':'Longitud','centroide_lat':'Latitud'},inplace=True)

    
    elif nombre_archivo == 'Proveedores':
        df.rename(columns={'Address':'Domicilio','City':'Ciudad','State':'Provincia','Country':'Pais','departamen':'Localidad'},inplace=True)

        df.Ciudad = df['Ciudad'].str.capitalize()
        df.Provincia = df['Provincia'].str.capitalize()
        df.Pais = df['Pais'].str.capitalize()
        df.Localidad = df['Localidad'].str.capitalize()

    elif nombre_archivo == 'Sucursales':
        df['Latitud'].replace(',','.',regex=True,inplace=True)
        df['Latitud'] = pd.to_numeric(df['Latitud'])
        df['Longitud'].replace(',','.',regex=True,inplace=True)
        df['Longitud'] = pd.to_numeric(df['Longitud'])

    elif nombre_archivo == 'Venta':
        pass

    return df,nombre_archivo