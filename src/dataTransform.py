import pandas
import numpy


class Data():
    def __init__(self) -> None:
        self.data = None

    def to_CSV(self, file_path):
        self.data = pandas.read_json(file_path).to_numpy()
        
    
