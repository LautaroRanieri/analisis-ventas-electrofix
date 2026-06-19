import pandas as pd
import matplotlib.pyplot as plt

# Cargar los dos archivos CSV
df_ventas = pd.read_csv("ventas_electrofix.csv")
df_productos = pd.read_csv("productos_electrofix.csv")

print(df_ventas.head())
print(df_productos.head())



# Revisar valores nulos
print("\nValores nulos en ventas:")
print(df_ventas.isnull().sum())

# Convertir la columna Fecha a formato de fecha real
df_ventas["Fecha"] = pd.to_datetime(df_ventas["Fecha"])

print("\nTipo de dato de la columna Fecha:", df_ventas["Fecha"].dtype)

# Revisar valores nulos
print("\nValores nulos en ventas:")
print(df_ventas.isnull().sum())

# Convertir la columna Fecha a formato de fecha real
df_ventas["Fecha"] = pd.to_datetime(df_ventas["Fecha"])

print("\nTipo de dato de la columna Fecha:", df_ventas["Fecha"].dtype)


# Top 5 productos más vendidos (por cantidad de veces vendido)
top_productos = df_ventas["Producto"].value_counts().head(5)
print("\nTop 5 productos más vendidos:")
print(top_productos)

# Ventas totales (en dinero) por categoría
ventas_categoria = df_ventas.groupby("Categoria")["Total"].sum().sort_values(ascending=False)
print("\nVentas totales por categoría:")
print(ventas_categoria)


# Gráfico de ventas por categoría
plt.figure(figsize=(8, 5))
ventas_categoria.plot(kind="bar", color="#4a6fa5")
plt.title("Ventas totales por categoría - ElectroFix")
plt.ylabel("Ventas (ARS)")
plt.xlabel("Categoría")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("grafico_ventas_categoria.png", dpi=150)
plt.show()

# Crear columna de mes y año para agrupar
df_ventas["AnioMes"] = df_ventas["Fecha"].dt.to_period("M")

# Ventas totales por mes
ventas_mensuales = df_ventas.groupby("AnioMes")["Total"].sum()
print("\nVentas por mes:")
print(ventas_mensuales)


# Gráfico de evolución de ventas por mes
plt.figure(figsize=(10, 5))
ventas_mensuales.plot(kind="line", marker="o", color="#4a6fa5")
plt.title("Evolución de ventas mensuales - ElectroFix")
plt.ylabel("Ventas (ARS)")
plt.xlabel("Mes")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("grafico_evolucion_mensual.png", dpi=150)
plt.show()

# Top 10 productos por dinero generado
top_dinero = df_ventas.groupby("Producto")["Total"].sum().sort_values(ascending=False).head(10)
print("\nTop 10 productos por dinero generado:")
print(top_dinero)

plt.figure(figsize=(10, 6))
top_dinero.sort_values().plot(kind="barh", color="#4a6fa5")
plt.title("Top 10 productos por ingresos - ElectroFix")
plt.xlabel("Total vendido (ARS)")
plt.tight_layout()
plt.savefig("grafico_top_productos.png", dpi=150)
plt.show()