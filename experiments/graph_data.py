#!/usr/bin/python
from cProfile import label
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


import os
import glob

def calculate_error_dataframe(df):
    df['error'] = df['prediction'] - df['actual']
    df['variance'] = df['error'] * df['error']
    # Standard deviation
    df['std'] = df['error'].std()
    return df

def create_plot(df):
    # Make lines thinner   
    ax = sns.regplot(x="prediction", y="actual", data=df)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(axis='both', which='major', labelsize=14)

    return ax

def create_error_plot(df):
    df = calculate_error_dataframe(df)
    # Add error data points
    ax_error = sns.regplot(x="prediction", y="error", data=df, label="Error data points")
    ax_error.set_xlabel("Predicted")
    ax_error.set_ylabel("Error")
    ax_error.grid(True)
    ax_error.set_axisbelow(True)
    ax_error.tick_params(axis='both', which='major', labelsize=14)


    # Variance
    ax_error.axhline(y=df['variance'].mean(), color='r', linestyle='-', label='Variance')

    # Standard deviation
    ax_error.axhline(y=df['std'].mean(), color='g', linestyle='-', label='Standard Deviation')

    # Add legend
    ax_error.legend(loc='upper right')

    return ax_error
    


def export_plot(ax, filename):
    ax.set_title(
        os.path.basename(filename)
        .replace(".png", "")
        .replace("_", " ")
        .replace("-", " ")
        .replace(".", " ")
    )
    ax.figure.savefig(filename, bbox_inches='tight')

def get_csv_files(path):
    return glob.glob(os.path.join(path, '*.csv'))

def main():

    files = get_csv_files("./experiments/data/")
    for file in files:
        df = pd.read_csv(file)
        ax = create_plot(df)
        export_plot(ax, file.replace(".csv", ".png"))
        print("Created plot for file: " + file)

        plt.close()

        ax_error = create_error_plot(df)
        export_plot(ax_error, file.replace(".csv", "_error.png"))

if __name__ == "__main__":
    main()
    