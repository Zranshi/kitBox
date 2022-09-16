from app.mids.process_time import ProcessTimeMiddleware
from fastapi.middleware import Middleware, cors, gzip, trustedhost

MIDDLEWARES = [
    # 跨域设置
    Middleware(
        cors.CORSMiddleware,
        # 只允许本地发送请求
        allow_origins=["*"],
        # 只允许这五种请求方法
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTION"],
        allow_headers=["*"],
        allow_credentials=True,
    ),
    # 限制访问host
    Middleware(trustedhost.TrustedHostMiddleware, allowed_hosts=["127.0.0.1"]),
    # GZip压缩
    Middleware(gzip.GZipMiddleware, minimum_size=1000),
    # 处理时间
    Middleware(ProcessTimeMiddleware, header_name="X-Process-Time"),
]

__all__ = [MIDDLEWARES]
