import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

def transformar_clientes(path:str,sep:str,encoding:str) -> pd.DataFrame:

    try:
        df = pd.read_csv(f'Datasets/{path}',sep=sep,encoding=encoding)
    except(ValueError):
        df = pd.read_csv(f'Datasets/{path}',sep=';',encoding=encoding)

    #Dropeo columnas innecesarias:
    df.drop(columns='col10',inplace=True)

    #Normalizo los campos 'X' e 'Y':
    
    x = df['X'].replace(to_replace=r',', value='.', regex=True)
    df['X'] = pd.to_numeric(x, errors='coerce')
    y = df['Y'].replace(to_replace=r',', value='.', regex=True)
    df['Y'] = pd.to_numeric(y, errors='coerce')

    df['X'][df.X > 0] = df['X'][df.X > 0] * -1
    df['Y'][df.Y > 0] = df['Y'][df.Y > 0] * -1
  

    #Cambio nombre el nombre de los campos 'X' e 'Y' por 'Latitud' y 'Longitud':
    df['Longitud'] = df['Y']
    df['Latitud'] = df['X']
    df.drop(columns=['X','Y'],inplace=True)

    #Discretizo la edad con un campo llamado 'Rango_Etario':
    df['Rango_Etario'] = '-'
    df['Rango_Etario'][df.Edad <= 30] = '1_Hasta 30 años'
    df['Rango_Etario'][(df.Edad <= 40) & (df.Rango_Etario == '-')] = '2_De 31 a 40 años'
    df['Rango_Etario'][(df.Edad <= 50) & (df.Rango_Etario == '-')] = '3_De 41 a 50 años'
    df['Rango_Etario'][(df.Edad <= 60) & (df.Rango_Etario == '-')] = '4_De 51 a 60 años'
    df['Rango_Etario'][(df.Edad > 60) & (df.Rango_Etario == '-')] = '5_Desde 60 años'

    return df


def transformar_compra(path:str,sep:str,encoding:str) -> pd.DataFrame:

    df = pd.read_csv(f'Datasets/{path}',sep=sep,encoding=encoding)

    df.drop(columns=['Fecha_Año','Fecha_Mes','Fecha_Periodo'],inplace=True)

    df['Fecha'] = pd.to_datetime(df['Fecha'])

    df= detectar_outliers(df,'Precio')
    df =detectar_outliers(df,'Cantidad')

    return df

def transformar_gasto(path:str,sep:str,encoding:str) -> pd.DataFrame:

    df = pd.read_csv(f'Datasets/{path}',sep=sep,encoding=encoding)

    df['Fecha'] = pd.to_datetime(df['Fecha'])


    df= detectar_outliers(df,'Monto')

    return df


def transformar_localidades(path:str,sep:str,encoding:str) -> pd.DataFrame:

    df = pd.read_csv(f'Datasets/{path}',sep=sep,encoding=encoding)

    df.rename(columns={'centroide_lon':'longitud',
                       'centroide_lat':'latitud'},
                       inplace=True)

    return df


def transformar_proveedores(path:str,sep:str,encoding:str) -> pd.DataFrame:

    df = pd.read_csv(f'Datasets/{path}',sep=sep,encoding=encoding)

    df.rename(columns={'Address':'domicilio',
                        'City':'ciudad',
                        'State':'provincia',
                        'Country':'pais',
                        'departamen':'localidad'},
                        inplace=True)

    df.Ciudad = df['ciudad'].str.capitalize()
    df.Provincia = df['provincia'].str.capitalize()
    df.Pais = df['pais'].str.capitalize()
    df.Localidad = df['localidad'].str.capitalize()

    return df


def transformar_sucursales(path:str,sep:str,encoding:str) -> pd.DataFrame:

    df = pd.read_csv(f'Datasets/{path}',sep=sep,encoding=encoding)

    df['Latitud'].replace(',','.',regex=True,inplace=True)
    df['Latitud'] = pd.to_numeric(df['Latitud'], errors='coerce')
    df['Longitud'].replace(',','.',regex=True,inplace=True)
    df['Longitud'] = pd.to_numeric(df['Longitud'], errors='coerce')

    return df


def transformar_venta(path:str,sep:str,encoding:str) -> pd.DataFrame:

    df = pd.read_csv(f'Datasets/{path}',sep=sep,encoding=encoding)

    df= detectar_outliers(df,'Precio')
    df =detectar_outliers(df,'Cantidad')
    
    new_names = {'IdVenta':'id_venta',
                'Fecha':'fecha',
                'Fecha_Entrega':'fecha_entrega',
                'IdCanal':'id_canal',
                'IdCliente':'id_cliente',
                'IdSucursal':'id_sucursal',
                'IdEmpleado':'id_empleado',
                'IdProducto':'id_producto',
                'Cantidad':'cantidad',
                'Precio':'precio'}

    df.rename(columns=new_names,inplace=True)
    
    return df

def detectar_outliers(df:pd.DataFrame,columna:str,tecnica='cajas') -> pd.DataFrame:

    """
    Función que detecta outliers en un dataframe usando una tecnica determinada.
    Parámetros:
        df: DataFrame sobre el que se realizará la detección de outliers.
        columna: columna sobre la que se realizará la detección de outliers.
        tecnica: tecnica de detección de outliers ('cajas' o 'sigmas').
    Retorna:
        DataFrame: DataFrame con los outliers detectados en una nueva columna llamada 'outlier'.
        
        (0 = outlier, 1 = no outlier)
    """

    if not 'outlier' in df.columns:
        df['outlier'] = 1

    #Detección por medio de Diagrama de Cajas:
    if tecnica == 'cajas':
        q1 = df[columna].describe().loc['25%']
        q3 = df[columna].describe().loc['75%']
        rango_IC = q3 - q1
        minimo = q1 - ((1.5) * (rango_IC))
        maximo = q3 + ((1.5) * (rango_IC))


    #Detección de outliers por medio de las 3 sigmas:
    elif tecnica == 'sigmas':
        promedio = df[columna].mean()
        stddev = df[columna].std()
        maximo = promedio + (3 * stddev)
        minimo = promedio - (3 * stddev)


    df['outlier'][(df[columna] > maximo) | (df[columna] < minimo)] = 0
    
    return df

def exportar_archivo(carpeta_actual:str,carpeta_destino:str,name:str) -> None:
    """
    Cambia la ubicación de un archivo.

    Parameters:
    carpeta_actual: Nombre de la carpeta donde se encuentra el archivo actualmente. Ejemplo: 'archivos'
    carpeta_destino: Nombre de la carpeta donde será reubicado el archivo. En caso de que la carpeta no exista, 
                     será creada. Ejemplo: 'archivos_reubicados'
    name: Nombre del archivo que será reubicado. Ejemplo: 'archivo.txt'
    """
  
    directory = os.getcwd()
    os.makedirs(os.path.dirname(f"{directory}\{carpeta_destino}\{name}"), exist_ok=True)
    try:
        os.rename(f"{directory}\{carpeta_actual}\{name}",f"{directory}\{carpeta_destino}\{name}")
    except(FileNotFoundError) as error:
        print(error)