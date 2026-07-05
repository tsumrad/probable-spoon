from typing import Optional
from pydantic import BaseModel, ConfigDict


    
class PdfSchema(BaseModel):
    
    html: Optional[str] = None
    booking_id: Optional[int] = None
    body: Optional[str] = None
    to: Optional[str] = None
    title: Optional[str] = None
    
    model_config = ConfigDict(from_attributes=True)
