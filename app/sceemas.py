
from fastapi_utils.api_model import APIModel


class KeyValueDTO(APIModel):
  
    key: str
    value: str