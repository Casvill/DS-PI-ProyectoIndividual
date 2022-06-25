from configuracion import CONFIG_DATASETS,DATABASE_CONFIG,ARCHIVOS,DATASETS,DATASET_DESTINO
import transformar as t
from cargar import crear_db,cargar


def main():

    crear_db(DATABASE_CONFIG)
    
    for archivo in ARCHIVOS:
        if archivo[-3:] != 'csv':
           pass

        elif archivo[:8] == 'Clientes':
            df = t.transformar_clientes(archivo,CONFIG_DATASETS['clientes']['sep'],CONFIG_DATASETS['clientes']['encoding'])
            cargar(DATABASE_CONFIG,df,'Cliente')
            t.exportar_archivo(DATASETS[:-1],DATASET_DESTINO,archivo)
        
        elif archivo[:6] == 'Compra':
            df = t.transformar_compra(archivo,CONFIG_DATASETS['compra']['sep'],CONFIG_DATASETS['compra']['encoding'])
            cargar(DATABASE_CONFIG,df,'Compra')
            t.exportar_archivo(DATASETS[:-1],DATASET_DESTINO,archivo)

        elif archivo[:5] == 'Gasto':
            df = t.transformar_gasto(archivo,CONFIG_DATASETS['gasto']['sep'],CONFIG_DATASETS['gasto']['encoding'])
            cargar(DATABASE_CONFIG,df,'Gasto')
            t.exportar_archivo(DATASETS[:-1],DATASET_DESTINO,archivo)

        elif archivo[:11] == 'Localidades':
            df = t.transformar_localidades(archivo,CONFIG_DATASETS['localidades']['sep'],CONFIG_DATASETS['localidades']['encoding'])
            cargar(DATABASE_CONFIG,df,'Localidades')
            t.exportar_archivo(DATASETS[:-1],DATASET_DESTINO,archivo)
        
        elif archivo[:11] == 'Proveedores':
            df = t.transformar_proveedores(archivo,CONFIG_DATASETS['proveedores']['sep'],CONFIG_DATASETS['proveedores']['encoding'])
            cargar(DATABASE_CONFIG,df,'Proveedores')
            t.exportar_archivo(DATASETS[:-1],DATASET_DESTINO,archivo)
        
        elif archivo[:10] == 'Sucursales':
            df = t.transformar_sucursales(archivo,CONFIG_DATASETS['sucursales']['sep'],CONFIG_DATASETS['sucursales']['encoding'])
            cargar(DATABASE_CONFIG,df,'Sucursales')
            t.exportar_archivo(DATASETS[:-1],DATASET_DESTINO,archivo)
        
        elif archivo[:5] == 'Venta':
            df = t.transformar_venta(archivo,CONFIG_DATASETS['venta']['sep'],CONFIG_DATASETS['venta']['encoding'])
            cargar(DATABASE_CONFIG,df,'Venta')
            t.exportar_archivo(DATASETS[:-1],DATASET_DESTINO,archivo)

if __name__ == '__main__':
    main()  