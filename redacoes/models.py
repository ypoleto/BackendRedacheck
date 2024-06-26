from pydantic import BaseModel
from typing import Optional, List

class Redacao(BaseModel):
    texto: str
    proposta_id: int
    user_id: int

class RedacaoInDB(Redacao):
    _id: Optional[str] = None
    
