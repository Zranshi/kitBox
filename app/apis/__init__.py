# -*- coding: UTF-8 -*-
# @Time     : 2022/08/27 13:09
# @Author   : Ranshi
# @File     : __init__.py
# @Doc      : apis包主要根据功能分类归纳一系列路由函数

from app.apis.index import r as index_router
from fastapi import APIRouter

r = APIRouter()

r.include_router(index_router, prefix="", tags=["Index"])
