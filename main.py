import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)  # 数据库初始化，如果没有库或者表，会自动创建

app = FastAPI()


# Dependency
def get_db():
    """
    每一个请求处理完毕后会关闭当前连接，不同的请求使用不同的连接
    :return:
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 通过status查询磁盘报修数量信息
@app.get("/disk/byHost")
def read_disk_info(Hostname: str, db: Session = Depends(get_db)):
    db_info = crud.get_host_info(db,Hostname=Hostname)
    if not db_info:
        raise HTTPException(status_code=404, detail="Info not found")
    return {"Msg":"成功","data":db_info}


@app.get("/disk/byProject")
def read_project_info(ProjectName: str, db: Session = Depends(get_db)):
    db_info = crud.get_project_info(db, ProjectName=ProjectName)
    if not db_info:
        raise HTTPException(status_code=404, detail="Info not found")
    return {"Msg":"成功","data": {"name": ProjectName, "value": db_info}}


if __name__ == '__main__':
    uvicorn.run(app=app, host="127.0.0.1", port=8000)
