import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import matplotlib.pyplot as plt

    return mo, pd, plt


@app.cell
def _(pd):
    df = pd.read_csv("data/features/events.csv")
    return (df,)


@app.cell
def _(df, mo, plt):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df['duration_minutes'], bins=30, edgecolor='black', alpha=0.7)
    ax.set_title("Distribution of Event Durations")
    ax.set_xlabel("Duration (Minutes)")
    ax.set_ylabel("Frequency")
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Display the figure in Marimo cleanly
    mo.as_html(fig)
    return


if __name__ == "__main__":
    app.run()
