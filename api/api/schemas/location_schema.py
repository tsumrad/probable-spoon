from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional

class LocationSchema(BaseModel):    

    id: int    
    name: str
    location_code: str = Field(alias="locationCode")
    address_line1: Optional[str] = Field(None, alias="addressLine1")
    address_line2: Optional[str] = Field("", alias="addressLine2")
    city: str
    postal_code: Optional[str] = Field(None, alias="postalCode")
    created_at: datetime = Field(alias="createdAt")  
    updated_at: datetime = Field(alias="updatedAt")
    short_description: str = Field(alias="shortDescription")        
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    timezone: Optional[str] = None
    
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

class LocationShortSchema(BaseModel):    

    id: int    
    name: str
    location_code: str = Field(alias="locationCode")    
    short_description: str = Field(alias="shortDescription")
    timezone: Optional[str] = None
    
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


class CourtDistanceSchema(BaseModel):

    # id: int
    court_id: int
    interpreter_id: int
    court_code: str

    # court_address: str
    # interpreter_address: str
    
    
    distance: int
    duration: int
    # court_latitude: Optional[float] = Field("", alias="courtLatitude")
    # court_longitude: Optional[float] = Field("", alias="courtLongitude")
    # interpreter_latitude: Optional[float] = Field("", alias="interpreterLatitude")
    # interpreter_longitude: Optional[float] = Field("", alias="interpreterLongitude")
       
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
