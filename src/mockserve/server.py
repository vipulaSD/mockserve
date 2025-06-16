from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

from mockserve.config import MockConfig
from mockserve.generator import ResponseGenerator


class MockServer:
    def __init__(self, config: MockConfig):
        app = FastAPI()
        self.app = app
        self.generator = ResponseGenerator()
        self._register_routes(config)

    def _add_route(self, path: str, method: str, status: int, content: dict):
        async def handler(request: Request):
            rendered_content = self.generator.render_template(content)
            return JSONResponse(status_code=status, content=rendered_content)

        self.app.add_api_route(path=path, endpoint=handler, methods=[method])

    def _register_routes(self, config: MockConfig):
        for route in config.routes:
            self._add_route(
                path=route.path,
                method=route.method,
                status=route.response.status_code,
                content=route.response.content,
            )

    def get_app(self):
        return self.app
