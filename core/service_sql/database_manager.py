from core.service_sql.sql import SQL
from core.service_sql.select_sql import SelectSQL
from core.service_sql.query import Query
from core.models import Invoice
from datetime import datetime


char_9 = str


class DatabaseManager:
    @staticmethod
    def get_id_bid(db: SQL, number: str) -> str:
        """Получить id заявки по ее номеру"""
        select = SelectSQL()
        select.set_db(db.get_db())
        select.set_query(Query.get_id_bid())
        select.set_params([number,])
        select.execute()
        return select.get_result()[0]['ID']

    @staticmethod
    def get_id_detail_by_name(db: SQL, name: str) -> str:
        """Получить id детали по имени детали"""
        select = SelectSQL()
        select.set_db(db.get_db())
        select.set_query(Query.get_id_detail_by_name())
        select.set_params([name,])
        select.execute()
        return select.get_result()[0]['ID']

    @staticmethod
    def get_invoice(db: SQL, iddoc: char_9) -> Invoice:
        """Получить счет"""
        select = SelectSQL()
        select.set_db(db.get_db())
        select.set_query(Query.get_invoice())
        # select.set_params({'iddoc': ' 9CBPJ   '})
        select.set_params({'iddoc': iddoc})
        select.execute()
        result_query = select.get_result()

        return Invoice(
            id=1,
            up=result_query[0]['UP'],
            kps=result_query[0]['KPS'],
            trtype=result_query[0]['TRTYPE'],
        )
