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
    team_start_time: datetime = Field(default='', description='发车时间')

    room_id: str = Field(default='', description='房间id')

    room_qrcode: str = Field(default='', description='房间二维码')
    app_name: str = Field(default='', description='爬取应用名')


class ResponseMobel(BaseModel):
    code: int = Field(default=200)
    msg: str = Field(default='success')
