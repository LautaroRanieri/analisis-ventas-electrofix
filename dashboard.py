import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="ElectroFix - Dashboard de Ventas", layout="wide")

# Cargar datos
df_ventas = pd.read_csv("ventas_electrofix.csv")
df_ventas["Fecha"] = pd.to_datetime(df_ventas["Fecha"])

# Título principal
st.title("📊 ElectroFix - Dashboard de Ventas")
st.markdown("Análisis de ventas de repuestos para lavarropas")

# Métricas generales arriba
col1, col2, col3 = st.columns(3)
col1.metric("Ventas totales", f"${df_ventas['Total'].sum():,.0f}")
col2.metric("Cantidad de operaciones", len(df_ventas))
col3.metric("Ticket promedio", f"${df_ventas['Total'].mean():,.0f}")

st.markdown("---")

# Filtro interactivo por categoría
categorias = ["Todas"] + sorted(df_ventas["Categoria"].unique().tolist())
categoria_seleccionada = st.selectbox("Filtrar por categoría:", categorias)

if categoria_seleccionada != "Todas":
    df_filtrado = df_ventas[df_ventas["Categoria"] == categoria_seleccionada]
else:
    df_filtrado = df_ventas

# Dos columnas para los gráficos
col_izq, col_der = st.columns(2)

with col_izq:
    st.subheader("Ventas por categoría")
    ventas_cat = df_filtrado.groupby("Categoria")["Total"].sum().sort_values(ascending=False)
    fig1, ax1 = plt.subplots()
    ventas_cat.plot(kind="bar", ax=ax1, color="#4a6fa5")
    plt.xticks(rotation=30)
    st.pyplot(fig1)

with col_der:
    st.subheader("Top 10 productos por ingresos")
    top10 = df_filtrado.groupby("Producto")["Total"].sum().sort_values(ascending=False).head(10)
    fig2, ax2 = plt.subplots()
    top10.sort_values().plot(kind="barh", ax=ax2, color="#4a6fa5")
    st.pyplot(fig2)