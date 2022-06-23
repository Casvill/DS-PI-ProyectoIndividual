from contantes import PATHS,DATABASE_LOCATION
from transformar import transformar
from cargar import crear_db,cargar

def main():

    crear_db(DATABASE_LOCATION)

    for path in PATHS:
        df,table_name = transformar(path['path'],path['sep'],path['encoding'])
        cargar(DATABASE_LOCATION,df,table_name)

if __name__ == '__main__':
    main()  