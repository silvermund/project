from crime_cctv.models import CrimeDTO
from crime_cctv.services import Crimecctvservices
from common.services import CommonService

class CrimeAPI(object):

    @staticmethod
    def main():
        util = Crimecctvservices
        dto = CrimeDTO()
        serv = CommonService
        while 1:
            m = input('1. print cctv 2.print xlsx')
            if 1 == '0':
                break
            elif m ==  '1':
                dto.dframe = util.new_model('crime')
                CrimeAPI.print_this(dto.dframe)
            elif menu == '2':
                util.
