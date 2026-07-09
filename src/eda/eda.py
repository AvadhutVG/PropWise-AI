import matplotlib.pyplot as plt
import pandas as pd


def dataset_summary(df: pd.DataFrame):

    print("\n========== DATASET SUMMARY ==========\n")

    print(df.describe(include="all"))