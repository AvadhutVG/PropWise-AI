from src.data.load_data import load_dataset


def main():

    df = load_dataset()

    print("\nDataset Loaded Successfully\n")

    print(df.head())

    print("\nShape:", df.shape)


if __name__ == "__main__":
    main()