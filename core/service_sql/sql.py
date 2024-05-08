from core.config import DATABASE, HOST, USER, PASSWORD
import pymssql


class SQL:
    def __init__(self) -> None:
        self._database = DATABASE
        self._host = HOST
        self._user = USER
        self._password = PASSWORD
        self._query = ''
        self._params: list or dict = []
        self._db = None
        self._result = []

    def set_query(self, query: str) -> None:
        """Записать запрос"""
        self._query = query

    def set_params(self, params: list or dict) -> None:
        """Установить параметры"""
        self._params = params

    def set_db(self, db) -> None:
        self._db = db

    def get_result(self) -> list:
        """Вернуть результат запрос"""
        return self._result

    def get_db(self):
        """Возвращает подключение к базе"""
        return self._db

    def connect(self) -> None:
        """Подключаемся к базе"""
        self._db = pymssql.connect(
            server=self._host,
            user=self._user,
            password=self._password,
            database=self._database,
        )

    def close(self) -> None:
        """Закрыть подключение"""
        self._db.close()

    def commit(self) -> None:
        """Сохранить изменения"""
        self._db.commit()

    def execute(self) -> None:
        """Выполнить запрос"""
        pass
