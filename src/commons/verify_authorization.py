# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author   ：jiamid
@Time     ：2022/1/13 21:22
@File     ：verify_authorization.py
@Software ：PyCharm
"""
from fastapi import Header, HTTPException
from starlette import status
import hashlib

async def verify_authorization(Authorization: str = Header(...)):
    _str = f'{Authorization}_cykl'
    _str_md5 = hashlib.md5(_str.encode('utf-8')).hexdigest()
    if '6bbd2fef614347d7298582bbb435be0b' != _str_md5:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='用户权限不足')