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
from api.crawler_api import insert_helloaba_rank
from api.crawler_api import insert_mi_quan_script
from api.crawler_api import insert_online_script

PREFIX = '/crawler'
insert_router = APIRouter()  # prefix='/crawler' windows下不能在这里加

insert_router.include_router(insert.router, prefix=PREFIX)
insert_router.include_router(insert_helloaba_rank.router, prefix=PREFIX)
insert_router.include_router(insert_mi_quan_script.router, prefix=PREFIX)
insert_router.include_router(insert_online_script.router, prefix=PREFIX)
