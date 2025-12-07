# src/core/some_form.py
from typing import Annotated, Optional
from simple_sqlite3_orm import TableSpec, ConstrainRepr


class FilterDefinition(TableSpec):
    """筛选条件表"""
    id: Annotated[int, ConstrainRepr("PRIMARY KEY")]
    title: str
    salary: str          # 薪水
    number: str          # 任务数量


class PhoneInfo(TableSpec):
    """电话信息表"""
    id: Annotated[int, ConstrainRepr("PRIMARY KEY")]
    ip: str