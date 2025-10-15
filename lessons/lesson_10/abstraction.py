from abc import ABC, abstractmethod


class DbConnector(ABC):  # абстрактний клас

    @abstractmethod
    def open_connector(self):
        raise AttributeError('connector is Not implemented ... ')

    @abstractmethod
    def close_connection(self):
        raise AttributeError('close_connection is Not implemented ... ')


    def execute_query(self):
        self.connector()
        print('executing .....')
        self.close_connection()


class MsSql(DbConnector):

    DB_TYPE = 'MSSQL'

    def open_connector(self):
        print(f'creating connector for {self.DB_TYPE}')

    pass

my_connector = MsSql()
my_connector.execute_query()

