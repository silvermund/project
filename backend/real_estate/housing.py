import pandas as pd

from real_estate.dataset import Dataset

class Housing(object):

    dataset = Dataset()

    def modeling(self, housing) -> object:
         this = self.dataset
         this.context = './data/'
         this.fname = payload
         return pd.read_excel(this.context + this.fname)



