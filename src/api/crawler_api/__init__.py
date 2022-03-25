# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author   ：jiamid
@Time     ：2022/1/12 23:07
@File     ：__init__.py.py
@Software ：PyCharm
"""
from fastapi import APIRouter
from api.crawler_api import insert

PREFIX = '/crawler'
insert_router = APIRouter()  # prefix='/crawler' windows下不能在这里加

insert_router.include_router(insert.router, prefix=PREFIX)
