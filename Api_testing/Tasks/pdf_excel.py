# code to converting pdf to excel

# importing tabula  module for converting

import tabula
import csv

# Read a pdf file

df = tabula.read_pdf("C:\Users\kasthuri.kandavelu\Downloads", pages=3)

# convert pdf into CSV
tabula.convert_into("C:\Users\kasthuri.kandavelu\Downloads", "kasthuri.csv", output_format="csv", pages='all')

print(df)
