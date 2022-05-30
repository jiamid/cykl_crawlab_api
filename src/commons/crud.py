# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author   ：jiamid
@Time     ：2022/1/5 09:42
@File     ：crud.py
@Software ：PyCharm
"""
import datetime

from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, inspect
from sqlalchemy.dialects.mysql import insert
from schemas.database_schema import WxJuBenShaRoom, HelloabaRankTable, MiQuanScriptTable, OnlineScriptTable
from schemas.api_schema import RoomModel, HelloabaRankModel, MiQuanScriptModel, OnlineScriptModel


def input_online_script(session: Session, insert_script: OnlineScriptModel):
    now = datetime.datetime.now()
    insert_script.updatedAt = now
    rs_dict = insert_script.dict()
    statment = insert(OnlineScriptTable).values(**rs_dict).on_duplicate_key_update(**rs_dict)
    session.execute(statment)
    session.commit()
    return 1


def input_mi_quan_script(session: Session, insert_script: MiQuanScriptModel):
    now = datetime.datetime.now()
    insert_script.updatedAt = now
    rs_dict = insert_script.dict()
    statment = insert(MiQuanScriptTable).values(**rs_dict).on_duplicate_key_update(**rs_dict)
    session.execute(statment)
    session.commit()
    return 1


def input_helloaba_rank(session: Session, insert_rank: HelloabaRankModel):
    new_rank = HelloabaRankTable(**insert_rank.dict())
    session.add(new_rank)
    session.commit()
    session.refresh(new_rank)
    return 1


def input_room(session: Session, insert_room: RoomModel):
    new_room = WxJuBenShaRoom(
        app_name=insert_room.app_name,
        room_id=insert_room.room_id,
        room_qrcode=insert_room.room_qrcode,
        drama_name=insert_room.drama_name,
        drama_male=insert_room.drama_male,
        drama_female=insert_room.drama_female,
        drama_duration=insert_room.drama_duration,
        team_creater=insert_room.team_creater,
        team_male=insert_room.team_male,
        team_female=insert_room.team_female,
        team_start_time=insert_room.team_start_time,
        created_time=datetime.datetime.now()
    )
    session.add(new_room)
    session.commit()
    session.refresh(new_room)
    return 1

# def list_sql(params, key, values):
#     q_str_list = [key == v for v in values]
#     params.append(or_(*q_str_list))
#
#
# def set_assignee_sql(session: Session, req: SetAssigneeRequest):
#     q = session.query(Video)
#     params = []
#     list_sql(params, Video.id, req.ids)
#     video_sql = q.filter(*params)
#     video_sql.update({Video.assignee_id: req.assignee_id})
#     session.commit()
