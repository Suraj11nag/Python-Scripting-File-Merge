from pandas import ExcelWriter
import pandas as pd
import glob
import os

writer = ExcelWriter("Output.xlsx")

for filename in glob.glob("dataset_1.xlsx"):
    df_excel = pd.read_excel(filename)

    (_, f_name) = os.path.split(filename)
    (f_short_name, _) = os.path.splitext(f_name)

    df_excel.to_excel(writer, f_short_name, index=False)

for filename in glob.glob("dataset_2.xlsx"):
    df_excel = pd.read_excel(filename)

    (_, f_name) = os.path.split(filename)
    (f_short_name, _) = os.path.splitext(f_name)

    df_excel.to_excel(writer, f_short_name, index=False)

for filename in glob.glob("dataset_3.xlsx"):
    df_excel = pd.read_excel(filename)

    (_, f_name) = os.path.split(filename)
    (f_short_name, _) = os.path.splitext(f_name)

    df_excel.to_excel(writer, f_short_name, index=False)

writer.save()