from typing import List

from pydantic import BaseModel


class Response(BaseModel):
    """Strucure of mocked response"""

    status_code: int
    content: dict


class Route(BaseModel):
    """Structure of mocked route"""

    path: str
    method: str
    response: Response


class MockConfig(BaseModel):
    """Structure of mocked config"""

    routes: List[Route]
