from typing import List
from fastapi import APIRouter
from .models import KeyValue
from .sceema import KeyValueDTO





router = APIRouter()

@router.get("/keyValues" ,response_model=List[KeyValueDTO])
def get_keyValues():
    return KeyValue.objects.all()
