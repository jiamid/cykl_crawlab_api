# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author   ：jiamid
@Time     ：2022/1/5 09:42
@File     ：api_schema.py
@Software ：PyCharm
"""
from pydantic import Field, BaseModel, validator
from datetime import datetime
from typing import Optional, List
from enum import Enum


class RoomModel(BaseModel):
    drama_name: str = Field(default='', description='剧本名')
    drama_male: int = Field(default=0, description='女性角色数')
    drama_female: int = Field(default=0, description='男性角色数')
    drama_duration: Optional[str] = Field(default='', description='时长')
    team_creater: str = Field(default='', description='发车人')
    team_male: int = Field(default=0, description='目前报名男性人数')
    team_female: int = Field(default=0, description='目前报名女性人数')
    team_start_time: Optional[datetime] = Field(default='', description='发车时间')
    room_id: Optional[str] = Field(default='', description='房间id')
    room_qrcode: Optional[str] = Field(default='', description='房间二维码')
    app_name: str = Field(default='', description='爬取应用名')


class HelloabaRankModel(BaseModel):
    playedStatus: Optional[int]
    recommendNum: Optional[int]
    recommendUrl: Optional[str]
    scriptCategory: Optional[int]
    scriptCoverUrl: Optional[str]
    scriptFemalePlayerLimit: Optional[int]
    scriptId: Optional[str]
    scriptIntro: Optional[str]
    scriptMalePlayerLimit: Optional[int]
    scriptName: Optional[str]
    scriptPlayerLimit: Optional[int]
    scriptScore: Optional[float]
    scriptTag: Optional[str]
    rankType: Optional[str] = Field(description='排行榜类型', default='')
    rankNum: Optional[int]
    scriptWantPlayerCount: Optional[int]
    scriptRankScoreValue: Optional[int]
    scriptRankScoreValueType: Optional[int]


class MiQuanScriptModel(BaseModel):
    scriptId: str = Field(default='')
    scriptName: str = Field(default='')
    scriptScore: float = Field(default=0)
    difficultyLevel: str = Field(default='')
    playType: str = Field(default='')
    plotType: str = Field(default='')
    themeType: str = Field(default='')
    updatedAt: datetime = Field(default=datetime.now())


class OnlineScriptModel(BaseModel):
    scriptId: str = Field(default='')
    scriptName: str = Field(default='')
    appName: str = Field(default='')
    updatedAt: datetime = Field(default=datetime.now())


class ResponseMobel(BaseModel):
    code: int = Field(default=200)
    msg: str = Field(default='success')
