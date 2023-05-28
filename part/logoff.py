from fastapi import APIRouter
import pymysql.cursors

app03 = APIRouter()

connection = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123321',
    database='pydb',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)


@app03.get("/logoff/{id}")
def path_params03(id:int,password:str):
    flag = 0
    try:
        cursor = connection.cursor()
        sql = 'select * from 登录注册表 where id = %s'
        cursor.execute(sql,id)
        result = cursor.fetchone()
        print(result)
        if result: flag = 1
        else: flag = 0
    except:
        return {"连接失败"}
    if(flag):
        if(password == result['password']):
            sql = 'delete from 登录注册表 where id = %s'
            cursor.execute(sql,id)
            connection.commit()
            return {result['name']+"已注销!"}
        else: return {"密码错误注销失败"}
    else:return {"查无此人"}