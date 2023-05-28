from fastapi import APIRouter
import pymysql.cursors

app04 = APIRouter()

connection = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123321',
    database='pydb',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)


@app04.get("/login/{id}")
def path_params04(id:int,password:str,newpassword:str):
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
            sql = "update 登录注册表 set password = %s where id = %s"
            params = (newpassword,id)
            cursor.execute(sql,params)
            connection.commit()
            return {result['name']+"密码修改成功！"}
        else: return {"密码错误修改失败"}
    else:return {"查无此人"}