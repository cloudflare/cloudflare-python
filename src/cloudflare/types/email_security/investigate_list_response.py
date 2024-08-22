# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["InvestigateListResponse", "Validation"]

class Validation(BaseModel):
    comment: Optional[str] = None

    dkim: Optional[Literal["pass", "neutral", "fail", "error", "none"]] = None

    dmarc: Optional[Literal["pass", "neutral", "fail", "error", "none"]] = None

    spf: Optional[Literal["pass", "neutral", "fail", "error", "none"]] = None

class InvestigateListResponse(BaseModel):
    id: str

    action_log: object

    client_recipients: List[str]

    detection_reasons: List[str]

    is_phish_submission: bool

    is_quarantined: bool

    message_id: str

    postfix_id: str
    """Message identifier"""

    ts: str

    alert_id: Optional[str] = None

    edf_hash: Optional[str] = None

    final_disposition: Optional[Literal["MALICIOUS", "MALICIOUS-BEC", "SUSPICIOUS", "SPOOF", "SPAM", "BULK", "ENCRYPTED", "EXTERNAL", "UNKNOWN", "NONE"]] = None

    from_: Optional[str] = FieldInfo(alias = "from", default = None)

    from_name: Optional[str] = None

    sent_date: Optional[str] = None

    subject: Optional[str] = None

    threat_categories: Optional[List[str]] = None

    to: Optional[List[str]] = None

    to_name: Optional[List[str]] = None

    validation: Optional[Validation] = None