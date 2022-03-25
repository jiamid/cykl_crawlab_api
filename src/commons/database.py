# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author   ：jiamid
@Time     ：2022/1/5 10:29
@File     ：database.py
@Software ：PyCharm
"""
from fastapi import Depends
from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from .config import system_conf

SQLALCHEMY_DATABASE_URI: str = system_conf.MYSQL_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    try:
        session = SessionLocal()
        yield session
    finally:
        session.close()

