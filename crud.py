from sqlalchemy.orm import Session
import models


# 通过主机名查询
def get_host_info(db:Session,Hostname:str):
    return db.query(models.Disk).filter(models.Disk.Hostname == Hostname).all()


