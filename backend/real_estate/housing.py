from real_estate.dataset import Dataset
import pandas as pd
class Housing(object):
    dataset = Dataset()
    def new_model(self, payload):
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        df = pd.read_excel(this.context + this.fname + '.xls', sheet_name='매매종합')
        wb = xw.Book(this.context + this.fname + ',xls')
        sheet = wb.sheets['매매종합']

        return pd.read_excel(this.context + this.fname + '.xlsx', sheet_name='평균전세')

