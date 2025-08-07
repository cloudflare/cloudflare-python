# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["LogListResponse", "CertificateLog"]


class CertificateLog(BaseModel):
    api: Literal["RFC6962", "STATIC"]
    """The API standard that the certificate log follows."""

    description: str
    """A brief description of the certificate log."""

    end_exclusive: datetime = FieldInfo(alias="endExclusive")
    """The end date and time for when the log will stop accepting certificates."""

    operator: str
    """The organization responsible for operating the certificate log."""

    slug: str
    """A URL-friendly, kebab-case identifier for the certificate log."""

    start_inclusive: datetime = FieldInfo(alias="startInclusive")
    """The start date and time for when the log starts accepting certificates."""

    state: Literal["USABLE", "PENDING", "QUALIFIED", "READ_ONLY", "RETIRED", "REJECTED"]
    """The current state of the certificate log.

    More details about log states can be found here:
    https://googlechrome.github.io/CertificateTransparency/log_states.html
    """

    state_timestamp: datetime = FieldInfo(alias="stateTimestamp")
    """Timestamp of when the log state was last updated."""

    url: str
    """The URL for the certificate log."""


class LogListResponse(BaseModel):
    certificate_logs: List[CertificateLog] = FieldInfo(alias="certificateLogs")
