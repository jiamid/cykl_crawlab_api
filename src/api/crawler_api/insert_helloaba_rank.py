# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author   ：jiamid
@Time     ：2022/5/25 21:43
@File     ：insert_helloaba_rank.py
@Software ：PyCharm
"""
import datetime

from fastapi import APIRouter, Depends
from commons.crud import input_helloaba_rank
from commons.database import get_db
from schemas.api_schema import HelloabaRankModel, ResponseMobel
from sqlalchemy.orm import Session

router = APIRouter()


@router.post('/insert_helloaba_rank', response_model=ResponseMobel)
async def insert_video(insert_data: HelloabaRankModel, session: Session = Depends(get_db)):
    one_rank = insert_data
    result = ResponseMobel()
    try:
        status = input_helloaba_rank(session, one_rank)
    except Exception as e:
        result.code = 2004
        result.msg = str(e)
    finally:
        session.close()
        return result