from pydantic import BaseModel, ConfigDict, Field, Json
from datetime import datetime
from typing import Optional, List, Dict
from api.schemas.location_schema import LocationShortSchema

from api.schemas.interpreter_schema import InterpreterBase, InterpreterBookingResponseSchema, InterpreterADMBookingResponseSchema, InterpreterBookingResponseShortSchema
from models.booking_enums import BookingPeriodEnum, BookingStatusEnum, BookingRequestedByEnum, BookingMethodOfAppearanceEnum, BookingInterpretForEnum
from api.schemas.custom_type import TruncatedUserIdBase, JsonBase
from api.schemas.language_schema import InterpreterLanguageSchema


class BookingCasesResponseSchema(BaseModel):    
    id: Optional[int] = None

    file: Optional[str] = None
    case_name: Optional[str] = Field(None, alias="caseName")
    room: Optional[str] = None
    
    case_type: Optional[str] = Field(None, alias="caseType")
    court_level: Optional[str] = Field(None, alias="courtLevel")
    court_class: Optional[str] = Field(None, alias="courtClass")
    court_class_other: Optional[str] = Field(None, alias="courtClassOther")
    reason: Optional[str] = None
    reason_other: Optional[str] = Field(None, alias="reasonOther")
       
    bilingual: Optional[bool] = False
    interpretation_mode: Optional[str] = Field(None, alias="interpretationMode")

    language: Optional[InterpreterLanguageSchema] = None
    interpret_for: Optional[str] = Field(None, alias="interpretFor")

    federal: Optional[bool] = False
    prosecutor: Optional[str] = None

    remote_registry: Optional[str] = Field(None, alias="remoteRegistry")
    remote_location_id: Optional[int] = Field(None, alias="remoteLocationId")
    van_registry: Optional[str] = Field(None, alias="vanRegistry")
    van_location_id: Optional[int] = Field(None, alias="vanLocationId") 
    anticipated_start_time: Optional[str] = Field(None, alias="antcpStartTime")
    justin_no: Optional[str] = Field(None, alias="justinNo")
    physical_file_id: Optional[str] = Field(None, alias="physicalFileId")
    appearance_id: Optional[str] = Field(None, alias="appearanceId")

    requested_by: Optional[BookingRequestedByEnum] = Field(None, alias="requestedBy")
    method_of_appearance: Optional[BookingMethodOfAppearanceEnum] = Field(None, alias="methodOfAppearance")
    
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


class BookingDateSchema(BaseModel):
    id: Optional[int] = None
    date: Optional[datetime] = None

    cases: Optional[List[BookingCasesResponseSchema]] = None

    start_time: Optional[str] = Field(None, alias="startTime")
    finish_time: Optional[str] = Field(None, alias="finishTime")
    
    actual_start_time: Optional[str] = Field(None, alias="actualStartTime")
    actual_finish_time: Optional[str] = Field(None, alias="actualFinishTime")
    approvers_initials: Optional[str] = Field(None, alias="approversInitials")

    cancellation_reason: Optional[str] = Field(None, alias="cancellationReason")
    cancellation_comment: Optional[str] = Field(None, alias="cancellationComment")
    cancellation_date: Optional[datetime] = Field(None, alias="cancellationDate")
    cancellation_time: Optional[str] = Field(None, alias="cancellationTime")
    cancellation_fee: Optional[str] = Field(None, alias="cancellationFee")

    
    comment: Optional[str] = None
   
    method_of_appearance: Optional[BookingMethodOfAppearanceEnum] = Field(None, alias="methodOfAppearance")
    status: Optional[BookingStatusEnum] = None
    
    # location_id: Optional[int] = Field(alias="locationId")
    
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

#_______________________________
#_______Request____(IN)_____
#_______________________________
class BookingDateSchemaIn(BookingDateSchema):
    # languages: Optional[List[Dict]]
    pass

class BookingRequestBase(BaseModel):
      
    # scheduling_clerk: Optional[str] = Field(alias="schedulingClerk")
    clerk_phone: Optional[str] = Field(None, alias="clerkPhone")  

    dates: List[BookingDateSchemaIn]

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

#_______________________________
#______Response____(OUT)____
#_______________________________
class BookingDateSchemaOut(BookingDateSchema):
    languages: Optional[JsonBase] = None

class BookingResponseBase(BaseModel):
      
    scheduling_clerk: Optional[TruncatedUserIdBase] = Field(None, alias="schedulingClerk")
    clerk_phone: Optional[str] = Field(None, alias="clerkPhone") 
    interpreter: InterpreterBookingResponseSchema
    location_id: Optional[int] = None
    location_name: Optional[str] = None
    location: Optional[LocationShortSchema] = None

    dates: List[BookingDateSchemaOut]

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

#_______________________________
#_______Request____(TZ)_____
#_______________________________
class BookingTzSchema(BaseModel):
    id: Optional[int]     = None
    location: Optional[LocationShortSchema]  = None
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
    

class BookingDateTzSchema(BookingDateSchema):
    booking: Optional[BookingTzSchema] = None
#_______________________________
#_______________________________
#_______________________________
#_______________________________

class BookingRequestSchema(BookingRequestBase):
    interpreter_id: Optional[int] = Field(None, alias="interpreterId")
    location_id: Optional[int] = Field(None, alias="locationId")
    location_name: Optional[str] = Field(None, alias="locationName")
    timezone: Optional[str] = Field(None, alias="timezone")



# General Info
class BookingResponseSchema(BookingResponseBase):
    id: Optional[int]            = None
    interpreter: InterpreterBookingResponseSchema
    records_approved: Optional[bool] = Field(None, alias="recordsApproved")
    location: Optional[LocationShortSchema]  = None
    created_at: Optional[datetime] = None
    updated_by: TruncatedUserIdBase



#Specific to ADM (OUT of DB)
class ADMBookingResponseSchema(BookingResponseBase):
    id: Optional[int] = None
    records_approved: Optional[bool] = Field(None, alias="recordsApproved")
    approver_name: Optional[str] = Field(None, alias="approverName")
    interpreter_signed: Optional[bool] = Field(None, alias="interpreterSigned")
    interpreter_signdate: Optional[str] = Field(None, alias="interpreterSigningDate")
    qr_signed: Optional[bool] = Field(None, alias="qualifiedReceiverSigned")
    qr_signdate: Optional[str] = Field(None, alias="qualifiedReceiverSigningDate")
    qr_signed_note: Optional[str] = Field(None, alias="qualifiedReceiverNote")
    fees_gst: Optional[float] = Field(None, alias="feesGST")
    fees_total: Optional[float] = Field(None, alias="feesTotal")
    expense_gst: Optional[float] = Field(None, alias="expenseGST")
    expense_total: Optional[float] = Field(None, alias="expenseTotal")
    invoice_total: Optional[float] = Field(None, alias="invoiceTotal")
    invoice_date: Optional[str] = Field(None, alias="invoiceDate")
    invoice_number: Optional[str] = Field(None, alias="invoiceNumber")
    adm_detail: Optional[JsonBase] = Field(None, alias="admDetail")          
    interpreter: InterpreterADMBookingResponseSchema
    created_at: Optional[datetime] = None
    updated_by: TruncatedUserIdBase
    adm_updated_by: Optional[TruncatedUserIdBase] = None
    updated_at: Optional[datetime] = None

    form_sender: Optional[TruncatedUserIdBase] = Field(None, alias="formSender")
    form_sender_email: Optional[str] = Field(None, alias="formSenderEmail")
    form_recipient_email: Optional[str] = Field(None, alias="formRecipientEmail")
    form_sent_date: Optional[datetime] = Field(None, alias="formSentDate")

    invoice_sender: Optional[TruncatedUserIdBase] = Field(None, alias="invoiceSender")
    invoice_sender_email: Optional[str] = Field(None, alias="invoiceSenderEmail")
    invoice_recipient_email: Optional[str] = Field(None, alias="invoiceRecipientEmail")
    invoice_sent_date: Optional[datetime] = Field(None, alias="invoiceSentDate")

#Specific to ADM (In to DB)
class ADMBookingRequestSchema(BookingRequestBase):
    id: Optional[int] = None
    records_approved: Optional[bool] = Field(None, alias="recordsApproved")
    approver_name: Optional[str] = Field(None, alias="approverName")
    interpreter_signed: Optional[bool] = Field(None, alias="interpreterSigned")
    interpreter_signdate: Optional[str] = Field(None, alias="interpreterSigningDate")
    qr_signed: Optional[bool] = Field(None, alias="qualifiedReceiverSigned")
    qr_signdate: Optional[str] = Field(None, alias="qualifiedReceiverSigningDate")
    qr_signed_note: Optional[str] = Field(None, alias="qualifiedReceiverNote")
    fees_gst: Optional[float] = Field(None, alias="feesGST")
    fees_total: Optional[float] = Field(None, alias="feesTotal")
    expense_gst: Optional[float] = Field(None, alias="expenseGST")
    expense_total: Optional[float] = Field(None, alias="expenseTotal")
    invoice_total: Optional[float] = Field(None, alias="invoiceTotal")
    invoice_date: Optional[str] = Field(None, alias="invoiceDate")
    invoice_number: Optional[str] = Field(None, alias="invoiceNumber")
    adm_detail: Optional[Dict] = Field(None, alias="admDetail")
    
    


class BookingDateRangeSchema(BaseModel):
    endDate: Optional[str] = None
    startDate: Optional[str] = None



class BookingSearchRequestSchema(BaseModel):    

    dates: Optional[List[BookingDateRangeSchema]] = None
    file: Optional[str] = None
    interpreter: Optional[str] = None
    isStartFromToday: Optional[bool] = None
    locationIds: Optional[List[int]] = None
    

    
class BookingSearchResponseSchema(BaseModel):
    
    reason: Optional[str]     = None
    file: Optional[str]     = None
    location_id: Optional[int] = Field(None, alias="locationId")
    location: Optional[LocationShortSchema]     = None
    dates: List[BookingDateSchemaOut]

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


class BookingInvoiceNumberResponseSchema(BaseModel):
    
    id: Optional[int] = None
    invoice_number: Optional[str] = Field(None, alias="invoiceNumber")

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

#_______________________________
#_______________________________
#__________AUDIT________________
#_______________________________
class AuditBookingSchema(BaseModel):    
    interpreter: InterpreterBookingResponseShortSchema
    location_id: Optional[int] = None
    location_name: Optional[str] = None
    location: Optional[LocationShortSchema] = None
    approver_name: Optional[str] = Field(None, alias="approverName")
    interpreter_signed: Optional[bool] = Field(None, alias="interpreterSigned")
    interpreter_signdate: Optional[str] = Field(None, alias="interpreterSigningDate")
    qr_signed: Optional[bool] = Field(None, alias="qualifiedReceiverSigned")
    qr_signdate: Optional[str] = Field(None, alias="qualifiedReceiverSigningDate")
    qr_signed_note: Optional[str] = Field(None, alias="qualifiedReceiverNote")
    fees_gst: Optional[float] = Field(None, alias="feesGST")
    fees_total: Optional[float] = Field(None, alias="feesTotal")
    expense_gst: Optional[float] = Field(None, alias="expenseGST")
    expense_total: Optional[float] = Field(None, alias="expenseTotal")
    invoice_total: Optional[float] = Field(None, alias="invoiceTotal")
    invoice_date: Optional[str] = Field(None, alias="invoiceDate")
    invoice_number: Optional[str] = Field(None, alias="invoiceNumber")
    
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

class AuditBookingDateSchema(BaseModel):
    id: Optional[int] = None
    date: Optional[datetime] = None
    interpreter_id: Optional[int] = Field(None, alias="interpreterId")

    start_time: Optional[str] = Field(None, alias="startTime")
    finish_time: Optional[str] = Field(None, alias="finishTime")    
    actual_start_time: Optional[str] = Field(None, alias="actualStartTime")
    actual_finish_time: Optional[str] = Field(None, alias="actualFinishTime")
    
    approvers_initials: Optional[str] = Field(None, alias="approversInitials")
    
    comment: Optional[str] = None
   
    method_of_appearance: Optional[BookingMethodOfAppearanceEnum] = Field(None, alias="methodOfAppearance")
    status: Optional[BookingStatusEnum] = None

    booking: Optional[AuditBookingSchema] = None

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

class BookingDateSchemaShort(BookingDateSchema):
    cases: Optional[List] = Field(None, exclude=True)
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

class AuditMultipleSessionBooking(AuditBookingSchema):
    adm_detail: Optional[JsonBase] = Field(None, alias="admDetail")
    dates: List[BookingDateSchemaShort]
