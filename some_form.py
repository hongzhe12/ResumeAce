from sqlite3_simple_orm import Model, Column


# 筛选条件
class FilterDefinition(Model):
    __tablename__ = 'filter_mentioned_users'
    id = Column('INTEGER', primary_key=True)
    title = Column('TEXT')
    # 薪水
    salary = Column('TEXT')
    # 任务数量
    number = Column('TEXT')


# 筛选条件
class PhoneInfo(Model):
    __tablename__ = 'phone_info'
    id = Column('INTEGER', primary_key=True)
    ip = Column('TEXT')
