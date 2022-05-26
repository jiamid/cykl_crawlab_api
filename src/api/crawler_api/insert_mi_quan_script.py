# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author   ：jiamid
@Time     ：2022/5/26 21:41
@File     ：insert_mi_quan_script.py
@Software ：PyCharm
"""
import datetime

from fastapi import APIRouter, Depends
from commons.crud import input_mi_quan_script
from commons.database import get_db
from schemas.api_schema import ResponseMobel, MiQuanScriptModel
from sqlalchemy.orm import Session

router = APIRouter()


@router.post('/insert_mi_quan_script', response_model=ResponseMobel)
async def insert_mi_quan_script(insert_data: MiQuanScriptModel, session: Session = Depends(get_db)):
    one = insert_data
    result = ResponseMobel()
    try:
        status = input_mi_quan_script(session, one)
    except Exception as e:
        result.code = 2004
        result.msg = str(e)
    finally:
        session.close()
        return result
