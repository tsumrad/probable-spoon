
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class LanguageSchemaRequest(BaseModel):
    id: Optional[int] = None
    name: str   


class LanguageSchema(BaseModel):
   
    id: int
    name: str   
    
    model_config = ConfigDict(from_attributes=True)


class InterpreterLanguageSchema(BaseModel):
    id: Optional[int] = None
    language_id: int = Field(alias="languageId")
    level: int
    language: str = Field(alias="languageName")
    comment_on_level: Optional[str] = Field("", alias="commentOnLevel")
       
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
