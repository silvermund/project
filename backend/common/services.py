class CommonService(object):

    def print_dframe(self, this):
        print('*' * 100)
        print(f'1. Housing 의 type \n {type(this)} ')
        print(f'2. Housing 의 column \n {this.columns} ')
        print(f'3. Housing 의 상위 1개 행\n {this.head()} ')
        print(f'4. Housing 의 null 의 갯수\n {this.isnull().sum()}개')
        print('*' * 100)