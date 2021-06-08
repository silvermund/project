from crime_cctv.models import CrimeDTO
from crime_cctv.services import Crimeservice

class CrimeAPI(object):

    @staticmethod
    def main():

        dto = CrimeDTO()
        serv = Crimeservice()

        while 1:
            m = input('1. print csv 2.print xlsx')
            if 1 == '0':
                break
            elif m == '1':
                dto.dframe = serv.new_model_csv('cctv_in_seoul.csv')
                serv.print_dframe(dto.dframe)
            elif m == '2':
                dto.dframe = serv.new_model_xlsx('pop_in_seoul.xls')
                serv.print_dframe(dto.dframe)
            else:
                continue

CrimeAPI.main()