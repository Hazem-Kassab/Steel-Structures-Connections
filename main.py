import pandas as pd

file = pd.read_csv("HEA.txt", delimiter="\t")
print(file[file["Profile"] == 240])
