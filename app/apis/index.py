# -*- coding: UTF-8 -*-
# @Time     : 2022/08/27 13:17
# @Author   : Ranshi
# @File     : index.py
# @Doc      : 涉及服务本身的路由接口
from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
from libs import log
from libs.conf import conf

r = APIRouter()


@r.get("/", response_class=RedirectResponse)
async def redirect_2_docs():
    try:
        return RedirectResponse(url=f"{conf['prefix_url']}/docs")
    except Exception as e:
        log.logging.exception(e)
        raise HTTPException(status_code=200, detail=str(e))
