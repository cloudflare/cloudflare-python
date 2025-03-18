# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["OnRampApplyResponse", "Error", "ErrorMeta", "ErrorSource", "Message", "MessageMeta", "MessageSource"]


class ErrorMeta(BaseModel):
    l10n_key: Optional[str] = None

    loggable_error: Optional[str] = None

    template_data: Optional[object] = None

    trace_id: Optional[str] = None


class ErrorSource(BaseModel):
    parameter: Optional[str] = None

    parameter_value_index: Optional[int] = None

    pointer: Optional[str] = None


class Error(BaseModel):
    code: Literal[
        1001,
        1002,
        1003,
        1004,
        1005,
        1006,
        1007,
        1008,
        1009,
        1010,
        1011,
        1012,
        1013,
        1014,
        1015,
        1016,
        1017,
        2001,
        2002,
        2003,
        2004,
        2005,
        2006,
        2007,
        2008,
        2009,
        2010,
        2011,
        2012,
        2013,
        2014,
        2015,
        2016,
        2017,
        2018,
        2019,
        2020,
        2021,
        2022,
        3001,
        3002,
        3003,
        3004,
        3005,
        3006,
        3007,
        4001,
        4002,
        4003,
        4004,
        4005,
        4006,
        4007,
        4008,
        4009,
        4010,
        4011,
        4012,
        4013,
        4014,
        4015,
        4016,
        4017,
        4018,
        4019,
        4020,
        4021,
        4022,
        4023,
        5001,
        5002,
        5003,
        5004,
        102000,
        102001,
        102002,
        102003,
        102004,
        102005,
        102006,
        102007,
        102008,
        102009,
        102010,
        102011,
        102012,
        102013,
        102014,
        102015,
        102016,
        102017,
        102018,
        102019,
        102020,
        102021,
        102022,
        102023,
        102024,
        102025,
        102026,
        102027,
        102028,
        102029,
        102030,
        102031,
        102032,
        102033,
        102034,
        102035,
        102036,
        102037,
        102038,
        102039,
        102040,
        102041,
        102042,
        102043,
        102044,
        102045,
        102046,
        102047,
        102048,
        102049,
        102050,
        102051,
        102052,
        102053,
        102054,
        102055,
        102056,
        102057,
        102058,
        102059,
        102060,
        102061,
        102062,
        102063,
        102064,
        102065,
        102066,
        103001,
        103002,
        103003,
        103004,
        103005,
        103006,
        103007,
        103008,
    ]

    message: str

    documentation_url: Optional[str] = None

    meta: Optional[ErrorMeta] = None

    source: Optional[ErrorSource] = None


class MessageMeta(BaseModel):
    l10n_key: Optional[str] = None

    loggable_error: Optional[str] = None

    template_data: Optional[object] = None

    trace_id: Optional[str] = None


class MessageSource(BaseModel):
    parameter: Optional[str] = None

    parameter_value_index: Optional[int] = None

    pointer: Optional[str] = None


class Message(BaseModel):
    code: Literal[
        1001,
        1002,
        1003,
        1004,
        1005,
        1006,
        1007,
        1008,
        1009,
        1010,
        1011,
        1012,
        1013,
        1014,
        1015,
        1016,
        1017,
        2001,
        2002,
        2003,
        2004,
        2005,
        2006,
        2007,
        2008,
        2009,
        2010,
        2011,
        2012,
        2013,
        2014,
        2015,
        2016,
        2017,
        2018,
        2019,
        2020,
        2021,
        2022,
        3001,
        3002,
        3003,
        3004,
        3005,
        3006,
        3007,
        4001,
        4002,
        4003,
        4004,
        4005,
        4006,
        4007,
        4008,
        4009,
        4010,
        4011,
        4012,
        4013,
        4014,
        4015,
        4016,
        4017,
        4018,
        4019,
        4020,
        4021,
        4022,
        4023,
        5001,
        5002,
        5003,
        5004,
        102000,
        102001,
        102002,
        102003,
        102004,
        102005,
        102006,
        102007,
        102008,
        102009,
        102010,
        102011,
        102012,
        102013,
        102014,
        102015,
        102016,
        102017,
        102018,
        102019,
        102020,
        102021,
        102022,
        102023,
        102024,
        102025,
        102026,
        102027,
        102028,
        102029,
        102030,
        102031,
        102032,
        102033,
        102034,
        102035,
        102036,
        102037,
        102038,
        102039,
        102040,
        102041,
        102042,
        102043,
        102044,
        102045,
        102046,
        102047,
        102048,
        102049,
        102050,
        102051,
        102052,
        102053,
        102054,
        102055,
        102056,
        102057,
        102058,
        102059,
        102060,
        102061,
        102062,
        102063,
        102064,
        102065,
        102066,
        103001,
        103002,
        103003,
        103004,
        103005,
        103006,
        103007,
        103008,
    ]

    message: str

    documentation_url: Optional[str] = None

    meta: Optional[MessageMeta] = None

    source: Optional[MessageSource] = None


class OnRampApplyResponse(BaseModel):
    errors: List[Error]

    messages: List[Message]

    success: bool
