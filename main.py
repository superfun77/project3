import uvicorn
from fastapi import FastAPI

from part import app01
from part import app02
from part import app03
from part import app04

app = FastAPI(title='召唤器',
              version='1.0',
              description='召唤铠甲'
              )
app.include_router(app02,prefix='/02',tags=['成为召唤人！'])
app.include_router(app01,prefix='/01',tags=['变身！'])
app.include_router(app03,prefix='/03',tags=['注销'])
app.include_router(app04,prefix='/04',tags=['修改密码'])


if __name__ == '__main__':
    uvicorn.run(app)