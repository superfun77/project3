from fastapi import APIRouter
import pymysql.cursors

app02 = APIRouter()

connection = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123321',
    database='pydb',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)


@app02.get("/register/{name}")
def path_params02(name:str,id:int,password:str):
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
        return {"id已被申请"}
    else:
        sql = "insert into 登录注册表(name,id,password,status) values(%s,%s,%s,%s)"
        params = (name,id,password,0)
        cursor.execute(sql,params)
        connection.commit()
        return {"申请成功！"}