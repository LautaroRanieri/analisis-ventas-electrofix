# Análisis de Ventas — ElectroFix

Proyecto de análisis de datos sobre las ventas de repuestos de lavarropas de **ElectroFix** (electrofix.online), un negocio propio de venta de repuestos. Incluye análisis exploratorio con Python (pandas, matplotlib) y un dashboard interactivo desarrollado con Streamlit.

## Sobre los datos

- **Catálogo de productos:** datos reales — 44 repuestos con precios reales del negocio.
- **Historial de ventas:** datos sintéticos generados con fines demostrativos, respetando patrones realistas (mayor demanda en meses de invierno por mayor uso de lavarropas, mayor frecuencia de venta en repuestos económicos frente a motores y placas).

Este proyecto fue desarrollado con asistencia de IA como herramienta de aprendizaje para aplicar pandas, matplotlib y Streamlit en un caso de uso real. El análisis, las decisiones de negocio y la comprensión del código son propios.

## Tecnologías utilizadas

- Python
- Pandas
- Matplotlib
- Streamlit

## Estructura del proyecto

- `analisis_electrofix.py` — script de análisis exploratorio: limpieza de datos, métricas generales, ventas por categoría, evolución mensual y top productos.
- `dashboard.py` — dashboard interactivo en Streamlit con filtro por categoría y visualizaciones dinámicas.
- `productos_electrofix.csv` — catálogo de productos.
- `ventas_electrofix.csv` — historial de ventas.

## Análisis realizados

1. Ventas totales por categoría
2. Top 10 productos más vendidos (por cantidad de operaciones)
3. Top 10 productos por ingresos generados
4. Evolución de ventas mensuales
5. Ticket promedio y métricas generales

## Principales hallazgos

- La categoría **Motores** genera más ingresos totales aunque se vende con menor frecuencia, debido a su mayor precio unitario.
- Los repuestos económicos (termoactuadores, blocapuertas, presostatos) son los más vendidos en cantidad de operaciones.
- Se observa un pico de ventas en los meses de invierno, coherente con el mayor uso de lavarropas en esa época del año.

## Cómo ejecutar el dashboard

```bash
pip install streamlit pandas matplotlib
streamlit run dashboard.py
```
