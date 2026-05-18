import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Datos Históricos', s=10)

    res_completo = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    años_extendidos = np.arange(df['Year'].min(), 2051)
    linea_completa = res_completo.slope * años_extendidos + res_completo.intercept
    ax.plot(años_extendidos, linea_completa, color='red', label='Ajuste Histórico (1880-2050)', linewidth=2)

    df_reciente = df[df['Year'] >= 2000]
    res_reciente = linregress(df_reciente['Year'], df_reciente['CSIRO Adjusted Sea Level'])
    años_recientes = np.arange(2000, 2051)
    linea_reciente = res_reciente.slope * años_recientes + res_reciente.intercept
    ax.plot(años_recientes, linea_reciente, color='green', label='Tendencia Reciente (2000-2050)', linewidth=2)

    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_xlim(1870, 2060)
    
    plt.savefig('sea_level_plot.png')
    return ax.get_figure()
