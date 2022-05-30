# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author   ：jiamid
@Time     ：2022/1/5 11:05
@File     ：database_schema.py
@Software ：PyCharm
"""
import datetime

from sqlalchemy import Boolean, Column, Integer, String, DateTime, Text, FLOAT, VARCHAR
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
    drama_duration = Column(String(50))
    drama_male = Column(Integer)
    drama_female = Column(Integer)
    team_creater = Column(String(255))
    team_male = Column(Integer)
    team_female = Column(Integer)
    team_start_time = Column(DateTime)


class HelloabaRankTable(Base):
    __tablename__ = 'helloaba_rank_data'
    id = Column(Integer, primary_key=True)
    playedStatus = Column(Integer)
    recommendNum = Column(Integer)
    recommendUrl = Column(String)
    scriptCategory = Column(Integer)
    scriptCoverUrl = Column(String)
    scriptFemalePlayerLimit = Column(Integer)
    scriptId = Column(String)
    scriptIntro = Column(String)
    scriptMalePlayerLimit = Column(Integer)
    scriptName = Column(String)
    scriptPlayerLimit = Column(Integer)
    scriptScore = Column(FLOAT)
    scriptTag = Column(String)
    rankType = Column(String)
    rankNum = Column(Integer)
    scriptWantPlayerCount = Column(Integer)


class MiQuanScriptTable(Base):
    __tablename__ = 'mi_quan_script'
    scriptId = Column(VARCHAR, primary_key=True)
    scriptName = Column(VARCHAR)
    scriptScore = Column(FLOAT)
    difficultyLevel = Column(VARCHAR)
    playType = Column(VARCHAR)
    plotType = Column(VARCHAR)
    themeType = Column(VARCHAR)
    updatedAt = Column(DateTime, default=datetime.datetime.now())


class OnlineScriptTable(Base):
    __tablename__ = 'online_drama'
    scriptId = Column(VARCHAR, primary_key=True)
    scriptName = Column(VARCHAR)
    appName = Column(VARCHAR)
    updatedAt = Column(DateTime, default=datetime.datetime.now())
