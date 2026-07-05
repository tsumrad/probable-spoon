from fastapi import Query
from pydantic import BaseModel, ConfigDict
from typing import Generic, TypeVar, List

T = TypeVar('T')

class PaginationParams(BaseModel):
    page: int = Query(None)
    limit: int = Query(None)

class PaginatedResponse(BaseModel, Generic[T]):
    items: List[T]
    total: int
    page: int
    limit: int

    model_config = ConfigDict(arbitrary_types_allowed=True)

