from crime_cctv.models import CrimeDTO
import pandas as pd
import xlwings as xw


class CrimeAPI(object):
    dto = CrimeDTO()

    def new_model_csv(self, payload):
        this = self.dto
        this.context = './data/'
        this.fname = payload
        df_csv = pd.read_csv(this.context + this.fname)
        return df_csv

    def new_model_xlsx(self, this):
        this = self.this
        this.context = './data/'
        this.fname = payload
        sheet = xw.Book(this.context + payload + '.xlsl').sheets['crime']
        df_xlsx = pd.read_excel(this.context)
