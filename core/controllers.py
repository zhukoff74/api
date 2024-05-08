from core import app, Response, HTTPException
from core.service_sql.sql import SQL
from core.service_sql.database_manager import DatabaseManager


@app.post("/test2")
async def test2():
    """Тестовый end point"""
    db = SQL()
    db.connect()
    iddoc = ' 9CBPJ   '
    invoice = DatabaseManager.get_invoice(db=db, iddoc=iddoc)
    return {'status': 200}
