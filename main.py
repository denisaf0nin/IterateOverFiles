import os
import pandas as pd
import numpy as np

directory = r"path"


os.chdir(directory)
sub_directories = os.listdir()

for dir in sub_directories:
    dir_path = directory + '\\' + dir
    os.chdir(dir_path)
    files = os.listdir()
    for file in files:
        file_path = dir_path + "\\" + file
        df = pd.read_excel(file_path)
        df['20-25 CAGR'] = np.where(df['col_to_filter'] == 'filter',
                                    ((df['year2025'] / df['year2020']) ** 0.2 - 1) * 100, 0)
        df['20-25 CAGR'].round(2)
        df.to_excel(file)
        print(file, "complete")

