import uvicorn

from mockserve.parser import ConfigLoader
from mockserve.server import MockServer


def serve(config_file: str, port: int = 8000):
    loader = ConfigLoader()
    mock_config = loader.load(filepath=config_file)
    server = MockServer(mock_config)
    uvicorn.run(server.get_app(), host="0.0.0.0", port=port)


if __name__ == "__main__":
    serve(config_file="mock_config.yaml")
