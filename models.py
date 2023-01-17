from sqlalchemy import BOOLEAN, Column, Integer, String
from database import Base


class Disk(Base):
    __tablename__ = "Disk_alarm"
    Id = Column(Integer, primary_key=True, index=True)
    IssueKey = Column(String(32), unique=True, index=True)
    IssueStatus = Column(String(32))
    ProjectName = Column(String(32))
    Assignee = Column(String(32))
    Hostname = Column(String(32))
    CreatedDate = Column(Integer())
