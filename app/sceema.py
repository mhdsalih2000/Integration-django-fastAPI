
from fastapi_utils.api_model import APIModel


class KeyValueDTO(APIModel):
    id :int
    key: str
    value: str