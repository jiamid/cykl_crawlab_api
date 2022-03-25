# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author   ：jiamid
@Time     ：2022/1/5 18:13
@File     ：config.py
@Software ：PyCharm
"""

import os
from configparser import ConfigParser
from pydantic import BaseSettings, validator, BaseModel
from typing import List, Union, Dict, Optional


class SystemSettings(BaseSettings):
    PROJECT_DIR: str = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    API_PORT: int = 5555

    MYSQL_HOST: str = 'mysql'
    MYSQL_USERNAME: str = 'root'
    MYSQL_PASSWORD: str = 'cykl+123'
    MYSQL_DB: str = 'crawlab_db'

    MYSQL_PORT: int = 3306
    MYSQL_URI: str = None

    @validator('MYSQL_URI')
    def set_mysql_db_url(cls, _, values: Dict):
        return f'mysql+pymysql://{values["MYSQL_USERNAME"]}:{values["MYSQL_PASSWORD"]}@' \
               f'{values["MYSQL_HOST"]}:{values["MYSQL_PORT"]}/{values["MYSQL_DB"]}'

    # 证书配置
    # SSL_KEYFILE: str = os.path.realpath(os.path.join(PROJECT_DIR, 'src/etc/2_jiamid.club.key'))
    # SSL_CERTFILE: str = os.path.realpath(os.path.join(PROJECT_DIR, 'src/etc/1_jiamid.club_bundle.crt'))

    # 日志配置
    # LOG_DIR: str = os.path.realpath(os.path.join(PROJECT_DIR, 'logs'))
    # @validator('LOG_DIR', pre=True)
    # def create_logs_dir(cls, v: str) -> str:
    #     if v:
    #         if not os.path.exists(v):
    #             os.makedirs(v)
    #     return v
    # LOG_LEVEL: str = 'INFO'
    # LOGURU_FORMAT: str = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | " \
    #                      "<level>{level: <8}</level> | " \
    #                      "<cyan>{process.name: <12}: {process.id: <6}</cyan> | " \
    #                      "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"

    class Config:
        env_file = '.env'


system_conf = SystemSettings()
