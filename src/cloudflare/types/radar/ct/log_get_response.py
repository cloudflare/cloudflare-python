# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "LogGetResponse",
    "CertificateLog",
    "CertificateLogPerformance",
    "CertificateLogPerformanceEndpoint",
    "CertificateLogRelated",
]


class CertificateLogPerformanceEndpoint(BaseModel):
    endpoint: Literal[
        "add-chain (new)",
        "add-chain (old)",
        "add-pre-chain (new)",
        "add-pre-chain (old)",
        "get-entries",
        "get-roots",
        "get-sth",
    ]
    """The certificate log endpoint names used in performance metrics."""

    response_time: float = FieldInfo(alias="responseTime")

    uptime: float


class CertificateLogPerformance(BaseModel):
    """Log performance metrics, including averages and per-endpoint details."""

    endpoints: List[CertificateLogPerformanceEndpoint]

    response_time: float = FieldInfo(alias="responseTime")

    uptime: float


class CertificateLogRelated(BaseModel):
    description: str
    """A brief description of the certificate log."""

    end_exclusive: datetime = FieldInfo(alias="endExclusive")
    """The end date and time for when the log will stop accepting certificates."""

    slug: str
    """A URL-friendly, kebab-case identifier for the certificate log."""

    start_inclusive: datetime = FieldInfo(alias="startInclusive")
    """The start date and time for when the log starts accepting certificates."""

    state: Literal["USABLE", "PENDING", "QUALIFIED", "READ_ONLY", "RETIRED", "REJECTED"]
    """The current state of the certificate log.

    More details about log states can be found here:
    https://googlechrome.github.io/CertificateTransparency/log_states.html
    """


class CertificateLog(BaseModel):
    api: Literal["RFC6962", "STATIC"]
    """The API standard that the certificate log follows."""

    avg_throughput: float = FieldInfo(alias="avgThroughput")
    """
    The average throughput of the CT log, measured in certificates per hour
    (certs/hour).
    """

    description: str
    """A brief description of the certificate log."""

    end_exclusive: datetime = FieldInfo(alias="endExclusive")
    """The end date and time for when the log will stop accepting certificates."""

    last_update: datetime = FieldInfo(alias="lastUpdate")
    """Timestamp of the most recent update to the CT log."""

    operator: str
    """The organization responsible for operating the certificate log."""

    performance: Optional[CertificateLogPerformance] = None
    """Log performance metrics, including averages and per-endpoint details."""

    related: List[CertificateLogRelated]
    """Logs from the same operator."""

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

    submittable_cert_count: Optional[str] = FieldInfo(alias="submittableCertCount", default=None)
    """
    Number of certificates that are eligible for inclusion to this log but have not
    been included yet. Based on certificates signed by trusted root CAs within the
    log's accepted date range.
    """

    submitted_cert_count: Optional[str] = FieldInfo(alias="submittedCertCount", default=None)
    """Number of certificates already included in this CT log."""

    url: str
    """The URL for the certificate log."""


class LogGetResponse(BaseModel):
    certificate_log: CertificateLog = FieldInfo(alias="certificateLog")
