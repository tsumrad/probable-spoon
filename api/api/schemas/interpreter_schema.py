from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, ConfigDict, Field

from api.schemas.language_schema import InterpreterLanguageSchema
from api.schemas.custom_type import JsonBase
from api.schemas.location_schema import CourtDistanceSchema


#__________________________________________
#__________________________________________
class InterpreterBase(BaseModel):

    last_name: Optional[str] = Field(None, alias="lastName")
    first_name: Optional[str] = Field(None, alias="firstName")

    address: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = "BC"
    postal_code: Optional[str] = Field(None, alias="postal")
    
    home_phone: Optional[str] = Field(None, alias="homePhone")
    business_phone: Optional[str] = Field(None, alias="businessPhone")
    cell_phone: Optional[str] = Field(None, alias="phone")
    fax: Optional[str] = None    
    email: Optional[str] =''

    supplier_no: Optional[str] = Field(None, alias="supplier")
    gst_no: Optional[str] = Field(None, alias="gst")
    site_code: Optional[str] = Field(default=None, alias="siteCode")
    
    contract_valid: Optional[bool] = Field(None, alias="contractExtension")
      
    languages: Optional[List[InterpreterLanguageSchema]] = []

    comments: Optional[str] = None
    
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
#__________________________________________
#__________________________________________

class InterpreterCreateModifyRequestSchema(InterpreterBase):
    crc_check_date: Optional[datetime] = Field(None, alias="criminalRecordCheckDate")
    completed_training: Optional[bool] = False
    admin_comment: Optional[str] = Field("", alias="adminComments")
    crc_comment: Optional[str] = Field(None, alias="criminalRecordCheck")
    contract_comment: Optional[str] = None



class InterpreterGetAdminResponseSchema(InterpreterCreateModifyRequestSchema):
    id: int     
    events: Optional[List] = []
    booking: Optional[List] = []
    created_at: Optional[datetime] = None



# payload_in_page_directory = criminalRecordCheck":"2021-12-25T03:39:00.000Z"} "Time is back utc. selected 2021-12-24T19:39Vancouver"




class InterpreterBookingResponseSchema(BaseModel):
    id: Optional[int]  = None
    last_name: Optional[str] = Field(None, alias="lastName")
    first_name: Optional[str] = Field(None, alias="firstName")
    cell_phone: Optional[str] = Field(None, alias="phone")
    email: Optional[str] = None
    languages: Optional[List[InterpreterLanguageSchema]] = []
    language_history: Optional[JsonBase] = Field(None, alias="languageHistory")
    courts: Optional[List[CourtDistanceSchema]] = None
    address: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = "BC"
    postal_code: Optional[str] = Field(None, alias="postal")

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


class InterpreterADMBookingResponseSchema(InterpreterBookingResponseSchema):
    supplier_no: Optional[str] = Field(None, alias="supplier")
    gst_no: Optional[str] = Field(None, alias="gst")
    site_code: Optional[str] = Field(None, alias="siteCode")
    address_longitude : Optional[float] = Field(None, alias="addressLongitude")
    address_latitude : Optional[float] = Field(None, alias="addressLatitude")


class InterpreterGeoStatusSchema(BaseModel):
    id: int
    update_started: bool = False
    last_name: Optional[str] = Field(None, alias="lastName")
    first_name: Optional[str] = Field(None, alias="firstName")

    address: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = "BC"
    postal_code: Optional[str] = Field(None, alias="postal")

    updated_at: Optional[datetime] = None
    contract_valid: Optional[bool] = Field(None, alias="contractExtension")
    geo_service: Optional[str] = None

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

class InterpreterBookingResponseShortSchema(BaseModel):
    id: Optional[int]  = None
    last_name: Optional[str] = Field(None, alias="lastName")
    first_name: Optional[str] = Field(None, alias="firstName")
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
