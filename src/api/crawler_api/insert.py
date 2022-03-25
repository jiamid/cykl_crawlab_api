# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author   ：jiamid
@Time     ：2022/1/4 18:37
@File     ：insert.py
@Software ：PyCharm
"""
import datetime

from fastapi import APIRouter, Depends
from commons.crud import input_room
from commons.database import get_db
from schemas.api_schema import RoomModel, ResponseMobel
from sqlalchemy.orm import Session

router = APIRouter()


@router.post('/insert', response_model=ResponseMobel)
async def insert_video(insert_data: RoomModel, session: Session = Depends(get_db)):
    one_room = insert_data
    result = ResponseMobel()

    try:
        status = input_room(session, one_room)
    except ValueError as e:
        result.code = e.args[0]
        result.msg = e.args[1]
    except Exception as e:
        result.code = 2004
        result.msg = str(e)
    finally:
        session.close()
        return result
