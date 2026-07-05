from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field

from api.schemas.interpreter_schema import InterpreterBase
from api.schemas.location_schema import CourtDistanceSchema, LocationSchema
from api.schemas.booking_schema import BookingSearchResponseSchema



class DatesSchema(BaseModel):
    arrivalTime: Optional[str] = None
    date: Optional[datetime] = None
    period: Optional[str] = None


class CrcDateRangeSchema(BaseModel):
    endDate: Optional[str] = None
    startDate: Optional[str] = None

class BaseInterpreterSearchSchema(BaseModel):    
    languageId:  Optional[int] = None
    level: Optional[List[str]] = None
    city: Optional[str] = None
    dates: Optional[List[DatesSchema]] = None
    name: Optional[str] = None
    keywords: Optional[str] = None
    active: Optional[bool] = None
    criminalRecordCheck: Optional[CrcDateRangeSchema] = None
    courtAddr: Optional[str] = None
    distanceLimit: Optional[bool] = None
    location: Optional[LocationSchema] = None

class InterpreterSearchRequestSchema(BaseInterpreterSearchSchema):    
    limit: Optional[int] = None
    page: Optional[int] = None
    # sort: Optional[str]



class InterpreterSearchResponseSchema(InterpreterBase):    
    id: int     
    events: Optional[List] = []
    booking: Optional[List[BookingSearchResponseSchema]] = []
    created_at: Optional[datetime] = None
    court: Optional[CourtDistanceSchema] = None
    court_distance: Optional[int] = Field(None, alias="courtDistance")    


class InterpreterDataInExcelRequestSchema(BaseInterpreterSearchSchema):
    pass

