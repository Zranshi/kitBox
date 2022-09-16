import time

from starlette.middleware.base import BaseHTTPMiddleware, DispatchFunction
from starlette.types import ASGIApp


class ProcessTimeMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app: ASGIApp,
        dispatch: DispatchFunction = None,
        header_name="X-Process-Time",
    ) -> None:
        super().__init__(app, dispatch)
        self.header_name = header_name

    async def dispatch(self, request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers[self.header_name] = str(process_time)
        return response
