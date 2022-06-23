#Rutas archivos csv:
__PATH_CLIENTES = {
                   'path':'Datasets/Clientes.csv',
                   'sep':';',
                   'encoding':'utf-8'
                  }

__PATH_CLIENTES_V2 = {
                      'path':'Datasets/Clientes_v2.csv',
                      'sep':';',
                      'encoding':'utf-8'
                     }

__PATH_COMPRA = {
                 'path':'Datasets/Compra.csv',
                 'sep':',',
                 'encoding':'utf-8'
                }

__PATH_GASTO = {
                'path':'Datasets/Gasto.csv',
                'sep':',',
                'encoding':'utf-8'
               }

__PATH_LOCALIDADES = {
                      'path':'Datasets/Localidades.csv',
                      'sep':',',
                      'encoding':'utf-8'
                     }

__PATH_PROVEEDORES = {
                      'path':'Datasets/Proveedores.csv',
                      'sep':',',
                      'encoding':'latin1'
                     }
                   
__PATH_SUCURSALES = {
                     'path':'Datasets/Sucursales.csv',
                     'sep':';',
                     'encoding':'utf-8'
                    }

__PATH_VENTA = {
                'path':'Datasets/Venta.csv',
                'sep':',',
                'encoding':'utf-8'
               }

PATHS = [__PATH_CLIENTES,__PATH_CLIENTES_V2,__PATH_COMPRA,__PATH_GASTO,__PATH_LOCALIDADES,__PATH_PROVEEDORES,__PATH_SUCURSALES,__PATH_VENTA]


#Información de la Base de Datos:
__DATABASE_INFO = {
                   "host":'localhost',
                   "port":"5432",
                   "user":'postgres',
                   "password":'postgresql',
                   "dbname":'ProyectoIndividual'
                  }

DATABASE_LOCATION = f"postgresql://{__DATABASE_INFO['user']}:{__DATABASE_INFO['password']}@{__DATABASE_INFO['host']}:{__DATABASE_INFO['port']}/{__DATABASE_INFO['dbname']}"

