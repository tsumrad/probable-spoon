from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field
from typing import List

class RateSchema(BaseModel):
    
    id: Optional[int]     = None
    name: Optional[str] = None
    value: Optional[float] = None
    previous_value: Optional[float] = Field(None, alias="previousValue")
    value_changed_date: Optional[datetime] = Field(None, alias="valueChangedDate")
    
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


class RateResponseSchema(RateSchema):
    pass
    # previous_value: Optional[float] = Field(None, alias="previousValue")
    # value_changed_date: Optional[datetime] = Field(None, alias="valueChangedDate")
    
