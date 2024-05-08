from core.service_sql.sql import SQL


class SelectSQL(SQL):
    def execute(self) -> None:
        """Выполнить запрос"""
        result = []
        cursor = self._db.cursor(as_dict=True)
        cursor.execute(self._query, self._params)

        for row in cursor:
            result.append(row)

        self._result = result
