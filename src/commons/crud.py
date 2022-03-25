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
from schemas.database_schema import WxJuBenShaRoom
from schemas.api_schema import RoomModel


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
