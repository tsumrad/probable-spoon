import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field
from api.schemas.role_schema import RoleSchema
from api.schemas.location_schema import LocationSchema, LocationShortSchema

#___________________________
class UserBase(BaseModel):
    
    first_name: Optional[str]  = None
    last_name: Optional[str] = None
    display_name: Optional[str] = None
    email: str    
    role: List[RoleSchema] = []    

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
#___________________________


class UserSchema(UserBase):
    authorization_id: str = Field(alias="user_id")       
    last_login: datetime.datetime 
    location: Optional[LocationSchema] = None
    
    
class UserSchemaRequest(BaseModel):   
    locationId: Optional[int] = None  


class UserAllSchema(UserBase):
    id: int    
    location: Optional[LocationShortSchema] = None
