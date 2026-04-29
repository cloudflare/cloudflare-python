# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = [
    "DetectionGetResponse",
    "Attachment",
    "Finding",
    "Header",
    "Link",
    "SenderInfo",
    "ThreatCategory",
    "Validation",
]


class Attachment(BaseModel):
    size: int
    """Size of the attachment in bytes"""

    content_type: Optional[str] = None
    """MIME type of the attachment"""

    detection: Optional[
        Literal[
            "MALICIOUS",
            "MALICIOUS-BEC",
            "SUSPICIOUS",
            "SPOOF",
            "SPAM",
            "BULK",
            "ENCRYPTED",
            "EXTERNAL",
            "UNKNOWN",
            "NONE",
        ]
    ] = None
    """Detection result for this attachment"""

    encrypted: Optional[bool] = None
    """Whether the attachment is encrypted"""

    filename: Optional[str] = None
    """Name of the attached file"""

    md5: Optional[str] = None
    """MD5 hash of the attachment"""

    name: Optional[str] = None
    """Attachment name (alternative to filename)"""

    sha1: Optional[str] = None
    """SHA1 hash of the attachment"""

    sha256: Optional[str] = None
    """SHA256 hash of the attachment"""


class Finding(BaseModel):
    attachment: Optional[str] = None

    detail: Optional[str] = None

    detection: Optional[
        Literal[
            "MALICIOUS",
            "MALICIOUS-BEC",
            "SUSPICIOUS",
            "SPOOF",
            "SPAM",
            "BULK",
            "ENCRYPTED",
            "EXTERNAL",
            "UNKNOWN",
            "NONE",
        ]
    ] = None

    field: Optional[str] = None

    name: Optional[str] = None

    portion: Optional[str] = None

    reason: Optional[str] = None

    score: Optional[float] = None

    value: Optional[str] = None


class Header(BaseModel):
    name: str

    value: str


class Link(BaseModel):
    href: str

    text: Optional[str] = None


class SenderInfo(BaseModel):
    as_name: Optional[str] = None
    """The name of the autonomous system."""

    as_number: Optional[int] = None
    """The number of the autonomous system."""

    geo: Optional[str] = None

    ip: Optional[str] = None

    pld: Optional[str] = None


class ThreatCategory(BaseModel):
    id: Optional[int] = None

    description: Optional[str] = None

    name: Optional[str] = None


class Validation(BaseModel):
    comment: Optional[str] = None

    dkim: Optional[Literal["pass", "neutral", "fail", "error", "none"]] = None

    dmarc: Optional[Literal["pass", "neutral", "fail", "error", "none"]] = None

    spf: Optional[Literal["pass", "neutral", "fail", "error", "none"]] = None


class DetectionGetResponse(BaseModel):
    action: str

    attachments: List[Attachment]

    findings: Optional[List[Finding]] = None

    headers: List[Header]

    links: List[Link]

    sender_info: SenderInfo

    threat_categories: List[ThreatCategory]

    validation: Validation

    final_disposition: Optional[
        Literal[
            "MALICIOUS",
            "MALICIOUS-BEC",
            "SUSPICIOUS",
            "SPOOF",
            "SPAM",
            "BULK",
            "ENCRYPTED",
            "EXTERNAL",
            "UNKNOWN",
            "NONE",
        ]
    ] = None
