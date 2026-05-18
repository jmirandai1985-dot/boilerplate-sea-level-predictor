import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Import data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # First line of best fit
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    x_pred = pd.Series(range(1880, 2051))
    y_pred = res.slope * x_pred + res.intercept

    ax.plot(x_pred, y_pred, 'r')

    # Second line of best fit
    df_recent = df[df["Year"] >= 2000]

    res_recent = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    x_recent = pd.Series(range(2000, 2051))
    y_recent = res_recent.slope * x_recent + res_recent.intercept

    ax.plot(x_recent, y_recent, 'g')

    # Labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")

    # Save plot and return data
    plt.savefig("sea_level_plot.png")
    return ax
