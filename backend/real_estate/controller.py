from real_estate.housing import Housing
from real_estate.dataset import Dataset


class Controller(object):

    @staticmethod
    def main():
        while 1:
            menu = input('0-Exit 1-모델생성 2-DF 생성')
        housing = Housing()
        dataset = Dataset()
        dataset.housing = housing.new_model('housing')
        print(dataset.housing)

    @staticmethod
    def print_this(this):
        print('*'*100)
        print(f'1. Housing 의 type \n {type(this)} ')
        print(f'2. Housing 의 Column \n {this.columns} ')
        print(f'3. Housing 의 상위 1개 행\n {this.head()} ')
        print(f'4. Housing 의 상위')


Controller.main()