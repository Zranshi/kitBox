# -*- coding: UTF-8 -*-
# @Time     : 2022/08/27 16:25
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 服务入口, 载入所有服务, 并提供Fastapi对象

from fastapi import FastAPI
from libs.conf import conf

from .mids import MIDDLEWARES

app = FastAPI(title="Tool", root_path=conf["prefix_url"], middleware=MIDDLEWARES)


@app.on_event("startup")
async def on_start_up():
    """
    on_start_up 启动app时触发
    """

    # 加载所有的路由
    from .apis import r

    app.include_router(r)


@app.on_event("shutdown")
async def on_shut_down():
    """
    on_shut_down 关闭app时触发
    """
    ...
