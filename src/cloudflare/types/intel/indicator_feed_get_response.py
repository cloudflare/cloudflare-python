# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "IndicatorFeedGetResponse",
    "LastUploadSummary",
    "LastUploadSummaryPersisted",
    "LastUploadSummarySkipped",
    "LastUploadSummaryUploaded",
]


class LastUploadSummaryPersisted(BaseModel):
    """Net delta applied to feed indicators by this upload.

    Snapshot
    uploads emit both *_added and *_removed; delta-add emits only
    *_added; delta-remove emits only *_removed.
    """

    domains_added: Optional[int] = None

    domains_removed: Optional[int] = None

    ips_added: Optional[int] = None

    ips_removed: Optional[int] = None

    urls_added: Optional[int] = None

    urls_removed: Optional[int] = None


class LastUploadSummarySkipped(BaseModel):
    """
    Counts of indicators that were uploaded but did not reach
    QuickSilver, broken down by reason.
    """

    allowlisted_domains: Optional[int] = None
    """Domains filtered by the global popularity allowlist at QS provisioning time.

    Popular domains (bing.com, naver.com, etc.) are protected from
    custom-threat-feed enforcement.
    """

    expired_indicators: Optional[int] = None
    """Indicators in the upload whose valid_until is already in the past.

    These are not added to QS; the expiration cron handles cleanup.
    """

    invalid_indicators: Optional[int] = None
    """Reserved for future use.

    Currently always 0 — the unifier aborts the entire upload on a single bad
    indicator.
    """


class LastUploadSummaryUploaded(BaseModel):
    """Indicator counts from the unified file the loader received"""

    domains: Optional[int] = None
    """Number of domain indicators in the upload"""

    ips: Optional[int] = None
    """Number of IP indicators in the upload"""

    urls: Optional[int] = None
    """Number of URL indicators in the upload"""


class LastUploadSummary(BaseModel):
    """Summary of indicator counts from the last successful upload to this
    feed.

    Populated by the custom-threat-feeds loader at the end of each
    successful load. Absent (omitted) when no upload has completed
    successfully or the upload errored before the summary write.
    Surfaces silent-failure paths so operators can see when their
    indicators were dropped (popularity allowlist, expired valid_until,
    etc.) without reading loader logs.
    """

    persisted: Optional[LastUploadSummaryPersisted] = None
    """Net delta applied to feed indicators by this upload.

    Snapshot uploads emit both _\\__added and _\\__removed; delta-add emits only
    _\\__added; delta-remove emits only _\\__removed.
    """

    skipped: Optional[LastUploadSummarySkipped] = None
    """
    Counts of indicators that were uploaded but did not reach QuickSilver, broken
    down by reason.
    """

    uploaded: Optional[LastUploadSummaryUploaded] = None
    """Indicator counts from the unified file the loader received"""


class IndicatorFeedGetResponse(BaseModel):
    id: Optional[int] = None
    """The unique identifier for the indicator feed"""

    created_on: Optional[datetime] = None
    """The date and time when the data entry was created"""

    description: Optional[str] = None
    """The description of the example test"""

    is_attributable: Optional[bool] = None
    """Whether the indicator feed can be attributed to a provider"""

    is_downloadable: Optional[bool] = None
    """Whether the indicator feed can be downloaded"""

    is_public: Optional[bool] = None
    """Whether the indicator feed is exposed to customers"""

    last_upload_summary: Optional[LastUploadSummary] = None
    """Summary of indicator counts from the last successful upload to this feed.

    Populated by the custom-threat-feeds loader at the end of each successful load.
    Absent (omitted) when no upload has completed successfully or the upload errored
    before the summary write. Surfaces silent-failure paths so operators can see
    when their indicators were dropped (popularity allowlist, expired valid_until,
    etc.) without reading loader logs.
    """

    latest_upload_status: Optional[Literal["Mirroring", "Unifying", "Loading", "Provisioning", "Complete", "Error"]] = (
        None
    )
    """Status of the latest snapshot uploaded"""

    modified_on: Optional[datetime] = None
    """The date and time when the data entry was last modified"""

    name: Optional[str] = None
    """The name of the indicator feed"""

    provider_id: Optional[int] = None
    """The unique identifier for the provider"""

    provider_name: Optional[str] = None
    """The provider of the indicator feed"""
