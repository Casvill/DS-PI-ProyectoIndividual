import pandas as pd
import logging

def importar_csv(path:str,sep:str) -> pd.DataFrame:
    """
    Importa un archivo csv desde memoria local.

    Parameters:
    path: Ruta donde se aloja el archivo.
    sep: separador que usa el archivo.

    Returns:
    Objeto tipo pd.DataFrame
    """
    try:
        csv_file = pd.read_csv(path,sep=sep,encoding='latin1')
    except(Exception) as error:
        logging.exception(f"extraer.py -> importar_csv(): {error}")

    return csv_file