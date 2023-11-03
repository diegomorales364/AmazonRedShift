# Introducción a Apache HBase

Apache HBase es una base de datos columnar de código abierto, diseñada para ser escalable y distribuida, y se ejecuta sobre el sistema de archivos Hadoop Distributed File System (HDFS). HBase se creó para alojar tablas extremadamente grandes en tiempo real y es una parte integral del ecosistema Hadoop.

## Características Principales de HBase

### Almacenamiento Columnar

- HBase almacena datos en columnas en lugar de filas, lo que permite una lectura y escritura eficientes de datos en grandes conjuntos.
- La naturaleza columnar de HBase es especialmente útil para aplicaciones que necesitan leer y escribir datos en columnas específicas en lugar de filas completas.
- Esta estructura permite a HBase alojar y administrar enormes cantidades de datos de manera eficiente.

### Almacenamiento Distribuido

- HBase está diseñado para operar en clusters distribuidos, lo que le permite escalar horizontalmente al agregar más nodos al cluster.
- Esto permite a HBase manejar petabytes de datos distribuidos entre muchos servidores.

### Modelo de Datos Flexible

- HBase no requiere un esquema fijo, lo que permite a los usuarios agregar columnas sobre la marcha sin necesidad de modificar la estructura de la tabla.
- Puede manejar estructuras de datos complejas y anidadas, lo que lo hace flexible para diferentes aplicaciones.

## Beneficios de Usar HBAse

- **Escalabilidad**: HBase puede escalar horizontalmente al agregar más nodos a su cluster, lo que permite alojar grandes conjuntos de datos.

- **Tiempo real**: HBase es apto para aplicaciones que requieren acceso en tiempo real a grandes conjuntos de datos.

- **Integración con Hadoop**: HBase está estrechamente integrado con el ecosistema Hadoop, permitiendo operaciones MapReduce directamente sobre sus tablas.

## Comparación con otros formatos

### Parquet vs RDBMS

- A diferencia de los sistemas de bases de datos relacionales (RDBMS), HBase es una base de datos NoSQL que no soporta transacciones completas ni un lenguaje de consulta estructurado como SQL.
- Mientras que RDBMS es adecuado para transacciones y operaciones con esquema fijo, HBase brilla en escenarios donde se necesitan grandes volúmenes de datos y estructuras flexibles.

## Ejemplos Prácticos y Casos de Uso

HBase es ideal para situaciones donde:

- Se necesita manejar grandes volúmenes de datos dispersos en tiempo real.
- Se busca una base de datos NoSQL escalable y distribuida.
- Se desea una solución que se integre fácilmente con el ecosistema Hadoop.


## Recursos Adicionales

- [Documentación Oficial de Apache HBase](https://hbase.apache.org/)
- [Qué es HBase - Cloudera](https://es.cloudera.com/products/open-source/apache-hadoop/apache-hbase.html)
- [Introducción a HBase - DataFlair](https://data-flair.training/blogs/hbase-tutorial/)

---

# Implementación

## Guía de Instalación
**Instalación de HBase**:
```bash
# Descargar HBase
wget http://apache.mirrors.tds.net/hbase/stable/hbase-2.3.6-bin.tar.gz
tar xzf hbase-2.3.6-bin.tar.gz

# Configurar HBase
cd hbase-2.3.6
cp conf/hbase-site.xml.template conf/hbase-site.xml
# Editar el archivo conf/hbase-site.xml para configurar HBase

```

## Creación, Inserción y Lectura de Datos en HBase

```bash
# Iniciar HBase
./bin/start-hbase.sh

# Acceder a la shell de HBase
./bin/hbase shell

# Crear una tabla
create 'test', 'cf'

# Insertar datos en la tabla
put 'test', 'row1', 'cf:qual1', 'value1'
put 'test', 'row2', 'cf:qual1', 'value2'

# Leer datos de la tabla
get 'test', 'row1'

# Escanear toda la tabla
scan 'test'
```


## Explicación de los métodos utilizados
- ```create 'nombre_tabla', 'nombre_familia_columnas'```: Crea una nueva tabla en HBase.
- ```put 'nombre_tabla', 'nombre_fila', 'familia_columnas:calificador', 'valor'```: Inserta o actualiza un dato en la tabla.
- ```get 'nombre_tabla', 'nombre_fila'```: Recupera los datos de una fila específica.
- ```scan 'nombre_tabla'```: Escanea y muestra todas las filas de la tabla.