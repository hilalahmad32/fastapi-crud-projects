from config.db import meta
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String


students=Table(
    'students',meta,
    Column('id',Integer,primary_key=True),
    Column('name',String(255)),
    Column('email',String(255)),
    Column('age',String(255)),
    Column('country',String(255)),
)