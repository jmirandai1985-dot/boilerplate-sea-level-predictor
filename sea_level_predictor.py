import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Importar los datos desde el archivo del repositorio
    df = pd.read_csv("epa-sea-level.csv")

    # --- PIPELINE DE LIMPIEZA INCLUIDO ---
    # Rellenar los valores nulos con la media de sus respectivas columnas
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        if df[col].isnull().sum() > 0:
            df[col] = df[col].fillna(df[col].mean())

    # 2. Crear el gráfico de dispersión (Scatter Plot)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], color="blue", label="Datos Históricos", s=15)

    # 3. Primera línea de regresión (1880 - 2050)
    reg_completa = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_proyeccion1 = pd.Series(range(1880, 2051))
    valores_proyeccion1 = reg_completa.slope * years_proyeccion1 + reg_completa.intercept
    ax.plot(years_proyeccion1, valores_proyeccion1, color="red", label="Tendencia (1880-2050)", linewidth=2)

    # 4. Segunda línea de regresión (2000 - 2050)
    df_reciente = df[df["Year"] >= 2000]
    reg_reciente = linregress(df_reciente["Year"], df_reciente["CSIRO Adjusted Sea Level"])
    years_proyeccion2 = pd.Series(range(2000, 2051))
    valores_proyeccion2 = reg_reciente.slope * years_proyeccion2 + reg_reciente.intercept
    ax.plot(years_proyeccion2, valores_proyeccion2, color="green", label="Tendencia Reciente (2000-2050)", linewidth=2)

    # 5. Agregar títulos y etiquetas exactas requeridas
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.5)
    
    # Asegurar el límite visual para que se note la extensión al 2050
    ax.set_xlim(1870, 2060)

    # Guardar la imagen y retornar los ejes para el test (No modificar)
    fig.savefig("sea_level_plot.png")
    return plt.gca()
