from datetime import datetime
from typing import Union

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import pymysql.cursors
import json

HOST = ''
USER = ''
PASSWORD = ''
NAME = ''

app = FastAPI()

class Item(BaseModel):
    title: str

class Files(BaseModel):
    id: str
    action: str
    result: str
    password: str

class FileCurrent(BaseModel):
    id: str
    action: str
    result: str
    password: str

class RecoverModel(BaseModel):
    id: str
    action: str
    sender: str
    result: str
    password: str

class Equipment(BaseModel):
    """Устройство"""
    id: int
    password: str

@app.get("/action")
def get_action(id:int=0, password:str=''):
    connection = pymysql.connect(host=HOST,
                            user=USER,
                            password=PASSWORD,
                            database=NAME)

    query = """
    SELECT a.`action`
    FROM equipment.equipments as e
    LEFT JOIN actions as a 
    ON e.id = a.id_equipment
    WHERE `e`.`id` = %(id)s AND `e`.`password` = %(password)s
    """

    with connection:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query, {'id': id, "password": password})
        
        result = cursor.fetchone()
        if result is None: return {"status": 400}

    res_json = json.loads(result['action'])

    return {"action": res_json, "status": 200}

@app.post("/delete_action")
def delete_action(data: Equipment):
    """Удаляем действие из базы"""
    print(data)


@app.post("/files")
def set_files(files: Files):
    # TODO: Проверка на id + пароль
    connection = pymysql.connect(host=HOST,
                            user=USER,
                            password=PASSWORD,
                            database=NAME)

    query_delete = f"DELETE FROM equipment.list_files WHERE `id_equipment`=%(id)s"
    with connection:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query_delete, {"id": files.id})
        connection.commit()
    
        files_list = files.result[:-1].rsplit(';')
        
        for f in files_list:
            if len(f) == '': continue
            query_insert = f"INSERT INTO equipment.list_files (id_equipment,file_list) VALUES (%(id)s, %(file)s);"
            cursor.execute(query_insert, {"id": files.id, "file": f})
        connection.commit()
        

    # TODO: Удалить action!
    return {"status": 200}


@app.post("/file")
def set_file(data: RecoverModel):
    # INSERT INTO equipment.valuesofsensors (id_sensors, moment, value) VALUES(0, CURRENT_TIMESTAMP, 0);
    json_request = jsonable_encoder(data) 
    print(json_request)

    # print('id =', id)
    # connection = pymysql.connect(host=HOST,
    #                             user=USER,
    #                             password=PASSWORD,
    #                             database=NAME)
    #
    # with connection:
    #     with connection.cursor() as cursor:
    #         sql = "INSERT INTO equipment.valuesofsensors (id_sensors, moment, value) VALUES(%s, %s, %s);"
    #         cursor.execute(sql, (id, sender, result))
    #
    #     connection.commit()

    return {"status": 200}

@app.get("/dump_finish")
def dump_finish(id, password):
    print('id', id)
    print('password', password)
    return 200

@app.post("/test")
def test(data: FileCurrent):
    j = jsonable_encoder(data)
    print(j)

    return {"test": j['result']}


@app.get("/file_delete")
def file_delete(data: FileCurrent):
    print(123123123)
    return {"test": 200}

