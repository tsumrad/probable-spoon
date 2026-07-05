import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field
from typing import List

class RoleSchema(BaseModel):
    
    id: int    
    role_name: str
    
    model_config = ConfigDict(from_attributes=True)


class RoleSchemaRequest(BaseModel):
   
    role_name: str


class UserRoleSchemaRequest(BaseModel):
   
    user_id: int
    roles: List[int]    
    

class RoleRequestAccessSchema(BaseModel):   
    message: str
