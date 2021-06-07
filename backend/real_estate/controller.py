import pandas as pd
from real_estate.dataset import Dataset
from real_estate.housing import Housing

class Controller(object):

    dataset: object = Dataset()
    housing: object = Housing()

    def preprocess(self, KBhousing):
        housing = self.housing
        this = self.dataset



    @staticmethod
    def main():
        c = Controller()
        print(c.print_this())
