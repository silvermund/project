from crime_cctv.models import CrimeDTO
import pandas as pd
from common.services import CommonService


class Crimeservice(CommonService):
    dto = CrimeDTO()

    def new_model_csv(self, payload):
        this = self.dto
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)


    def new_model_xlsx(self, payload):
        this = self.dto
        this.context = './data/'
        this.fname = payload
        return pd.read_excel(this.context + this.fname)