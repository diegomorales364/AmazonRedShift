import happybase

# Conexión con HBase
connection = happybase.Connection('localhost')
table_name = 'ventas'

# Crear tabla en HBase si no existe
if table_name not in connection.tables():
    families = {'detalles': dict()}
    connection.create_table(table_name, families)
    print(f"Tabla '{table_name}' creada con éxito.")
else:
    print(f"La tabla '{table_name}' ya existe.")

# Seleccionar tabla
table = connection.table(table_name)

# Insertar datos de ejemplo en la tabla
data = {
    '2022-01-01': ('Producto A', 10),
    '2022-01-02': ('Producto B', 15),
    '2022-01-03': ('Producto C', 20)
}
for fecha, (producto, precio) in data.items():
    for i in range(1, 5001):
        row_key = f"{fecha}_{producto}_{i}"
        table.put(row_key, {
            'detalles:producto': producto,
            'detalles:cantidad': str(i),
            'detalles:precio_por_unidad': str(precio)
        })
print("Datos insertados con éxito.")

# Mostrar datos de un producto específico
print("\nMostrando algunas filas para 'Producto A':")
rows = table.scan(filter=f"SingleColumnValueFilter('detalles', 'producto', =, 'binary:Producto A')", limit=5)
for key, data in rows:
    print(key, data)

# Cerrar conexión
connection.close()