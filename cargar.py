from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine, exc
import sqlalchemy
import pandas as pd


def crear_db(DATABASE_CONFIG:str) -> None:
    """
    Crea la base de datos en caso de que no exista.

    Parameters:
    DATABASE_LOCATION: Una URL del motor SQLAlchemy Ejemplo:('postgresql://user:password@host/databasename')
    """
    if not database_exists(DATABASE_CONFIG):
        create_database(DATABASE_CONFIG)


def __get_engine(DATABASE_CONFIG:str) -> sqlalchemy.engine:
    """
    Crea y retorna un motor de SQLAlchemy.
    
    Parameters:
    DATABASE_LOCATION: Una URL del motor SQLAlchemy Ejemplo:('postgresql://user:password@host/databasename')

    Return:
    sqlalchemy.engine: Un motor de SQLAlchemy
    """
    try:
        engine = create_engine(DATABASE_CONFIG)
        
    except exc.SQLAlchemyError as error:
        print(error)

    return engine


def cargar(DATABASE_CONFIG:str,df:pd.DataFrame,table_name:str) -> None:
    """
    Carga un pd.DataFrame a una base de datos.

    Parameters:
    DATABASE_LOCATION: Una URL del motor SQLAlchemy con la información de la base de datos
                       a la que se cargará el pd.DataFrame. Ejemplo:('postgresql://user:password@host/dbname').
            
    df: El pd.DataFrame que será cargado a la base de datos.
    table_name: El nombre de la tabla donde será cargado el pd.DataFrame en la base de datos
                En caso de que la tabla ya exista, se le añaden los nuevos registros.
    """
    df.to_sql(table_name,__get_engine(DATABASE_CONFIG),index=False,if_exists='append')
    