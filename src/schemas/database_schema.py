# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author   ：jiamid
@Time     ：2022/1/5 11:05
@File     ：database_schema.py
@Software ：PyCharm
"""
import datetime

from sqlalchemy import Boolean, Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class WxJuBenShaRoom(Base):
    __tablename__ = 'jbs_xcx'
    id = Column(Integer, primary_key=True)
    app_name = Column(String(50))
    created_time = Column(DateTime)
    room_id = Column(String(255))
    room_qrcode = Column(Text)
    drama_name = Column(String(255))
    drama_male = Column(Integer)
    drama_female = Column(Integer)
    team_creater = Column(String(255))
    team_male = Column(Integer)
    team_female = Column(Integer)
    team_start_time = Column(DateTime)
