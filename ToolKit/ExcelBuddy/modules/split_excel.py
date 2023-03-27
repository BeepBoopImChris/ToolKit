import pandas as pd
import os

def split_excel(file_path, num_files, output_folder):
    
    df = pd.read_excel(file_path)

    # split the dataframe 
    file_size = len(df) // num_files
    for i in range(num_files):
        start = i * file_size
        end = (i + 1) * file_size if i != num_files - 1 else len(df)
        split_df = df.iloc[start:end]

        # write to a new excel file
        file_name = os.path.basename(file_path).split(".")[0] + f"_{i+1}.xlsx"
        file_path = os.path.join(output_folder, file_name)
        split_df.to_excel(file_path, index=False)

#TODO -Bug- It is taking the table header in account when splitting the file, need to add a way to handle that