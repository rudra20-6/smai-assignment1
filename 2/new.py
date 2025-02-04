import pandas as pd
import sys

def compute_frequencies(csv_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Compute frequency counts for each column
    print("Column Value Frequencies:")
    for col in df.columns:
        print(f"\nColumn: {col}")
        print(df[col].value_counts().to_string())
        
def checkingNumberOfEmptyValuesInEachColumn(csv_file):
    df = pd.read_csv(csv_file)
    print("Number of empty values in each column:")
    print(df.isnull().sum())

def checkingRowsAndHowManyEmptyCellsTheyHave(csv_file):
    df = pd.read_csv(csv_file)
    # print("Number of empty values in each row:")
    # print(df.isnull().sum(axis=1))
    # Filter rows with at least one empty cell and print their empty cell count
    empty_rows = df.isnull().sum(axis=1)
    rows_with_empties = empty_rows[empty_rows > 0]
    if not rows_with_empties.empty:
        print("\nRows with empty cells:")
        print(rows_with_empties.to_string())
    else:
        print("\nNo rows contain empty cells")
        

def functionToCheckIfThereIsAnyRelationShipBetween2Columns(csv_file):
    df = pd.read_csv(csv_file)
    sns.pairplot(df)
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <csv_file>")
    else:
        with open('output.txt', 'w') as f:
            sys.stdout = f
            compute_frequencies(sys.argv[1])
            # checkingNumberOfEmptyValuesInEachColumn(sys.argv[1])
            # checkingRowsAndHowManyEmptyCellsTheyHave(sys.argv[1])
            sys.stdout = sys.__stdout__