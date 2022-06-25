from os import listdir
from os.path import isfile, join

#Ubicación donde se alojan los datasets
DATASETS= 'Datasets/'

#Ubicación donde se reubicaran los datasets una vez cargados a las base de datos
DATASET_DESTINO= 'Datasets_cargados'

#Lista con los nombres de los datasets (no modificar)
ARCHIVOS = [f for f in listdir(DATASETS) if isfile(join(DATASETS, f))]

#Configuración de los datasets:
__CONFIG_CLIENTES = {
                   'sep':',',
                   'encoding':'utf-8'
                  }

__CONFIG_COMPRA = {
                 'sep':',',
                 'encoding':'utf-8'
                }

__CONFIG_GASTO = {
                  'sep':',',
                  'encoding':'utf-8'
                 }

__CONFIG_LOCALIDADES = {
                      'sep':',',
                      'encoding':'utf-8'
                     }

__CONFIG_PROVEEDORES = {
                      'sep':',',
                      'encoding':'latin1'
                     }
                   
__CONFIG_SUCURSALES = {
                     'sep':';',
                     'encoding':'utf-8'
                    }

__CONFIG_VENTA = {
                'sep':',',
                'encoding':'utf-8'
               }

#No modificar
CONFIG_DATASETS = {
                    'clientes':__CONFIG_CLIENTES,
                    'compra':__CONFIG_COMPRA,
                    'gasto':__CONFIG_GASTO,
                    'localidades':__CONFIG_LOCALIDADES,
                    'proveedores':__CONFIG_PROVEEDORES,
                    'sucursales':__CONFIG_SUCURSALES,
                    'venta':__CONFIG_VENTA,
                  }


#Información de la Base de Datos:
__DATABASE_INFO = {
                   "host":'localhost',
                   "port":"5432",
                   "user":'postgres',
                   "password":'postgresql',
                   "dbname":'ProyectoIndividual'
                  }

#Configuración para conectar con la base de datos (No modificar)
DATABASE_CONFIG = f"postgresql://{__DATABASE_INFO['user']}:{__DATABASE_INFO['password']}@{__DATABASE_INFO['host']}:{__DATABASE_INFO['port']}/{__DATABASE_INFO['dbname']}"


