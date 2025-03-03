'''
A Library of useful pandas helper functions
'''
import pandas as pd
import os

def get_column_names(df: pd.DataFrame) -> list[str]:
    '''
    Get all column names of a pandas dataframe df
    Returns the names as a list of string
    '''
    return list(df.columns)


def get_columns_of_type(df: pd.DataFrame, numpy_type: any) -> list[str]:
    '''
    Return the column names of a pandas dataframe only when 
    the values in the column match the numpy_type
    '''
    return list(df.select_dtypes(include=[numpy_type]).columns)


def get_unique_values(df: pd.DataFrame, column_name: str) -> list:
    '''
    Get a list of unique values of a column in a pandas dataframe
    '''
    return list(df[column_name].unique())


def get_file_extension(file_path: str) -> str:
    '''
    Return the file extension of a file_path for example:
    '/some/file/data.csv' -> 'csv'
    '/home/important_grades.xlsx' -> 'xlsx'
    'countries.json' -> 'json'
    '''
    return os.path.splitext(file_path)[1][1:]  # Remove the dot


def load_file(file_path: str, ext: str) -> pd.DataFrame:
    '''
    Load a file into a pandas dataframe assumed the file type from the extension
    return a pandas dataframe
    only suppose csv, excel and json file extensions
    - when csv assume first row is header
    - when json assume record-oriented data
    '''
    if ext == 'csv':
        return pd.read_csv(file_path)
    elif ext in ['xlsx', 'xls']:
        return pd.read_excel(file_path)
    elif ext == 'json':
        return pd.read_json(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")


if __name__ == '__main__':
    df = pd.DataFrame({ 
        "name": ["Alice", "Bob", "Chris", "Dee", "Eddie", "Fiona"],
        "age": [25, 30, 35, 40, 45, 50],
        "state": ["NY", "PA", "NY", "NY", "PA", "NJ"],
        "balance": [100.0, 200.0, 250.0, 310.0, 100.0, 60.0]
        })
    cols = get_column_names(df)
    print(f"Columns: {cols}")
    cols = get_columns_of_type(df, 'object')
    print(f"Object Columns: {cols}")
    cols = get_columns_of_type(df, 'int64')
    print(f"Int64 Columns: {cols}")
    cols = get_columns_of_type(df, 'float64')
    print(f"Float64 Columns: {cols}")
    unique = get_unique_values(df, 'state')
    print(f"Unique States: {unique}")
    
    # Test file extension function
    print(f"Extension: {get_file_extension('/some/file/data.csv')}")
    print(f"Extension: {get_file_extension('/home/important_grades.xlsx')}")
    print(f"Extension: {get_file_extension('countries.json')}")