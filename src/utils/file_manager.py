from pathlib import Path
import pandas as pd


class FileManager:

    def __init__(self):

        self.base_path = Path("datasets")

        self.base_path.mkdir(
            parents=True,
            exist_ok=True
        )

    def save_csv(self, dataframe, filename):

        file_path = self.base_path / f"{filename}.csv"

        dataframe.to_csv(
            file_path,
            index=False
        )

        print(f"CSV Saved -> {file_path}")

    def save_parquet(self, dataframe, filename):

        file_path = self.base_path / f"{filename}.parquet"

        dataframe.to_parquet(
            file_path,
            index=False
        )

        print(f"Parquet Saved -> {file_path}")