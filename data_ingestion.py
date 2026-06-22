import pandas as pd
import os

folder = "data/raw/datasets"

for file in sorted(os.listdir(folder)):
    if file.endswith(".csv"):
        path = os.path.join(folder, file)

        df = pd.read_csv(path)

        print(file, "->", df.shape)