# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["TopLocationsResponse", "Meta", "MetaConfidenceInfo", "Top0"]


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[object]] = None

    level: Optional[int] = None


class Meta(BaseModel):
    date_range: List[object] = FieldInfo(alias="dateRange")

    last_updated: str = FieldInfo(alias="lastUpdated")

    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias="confidenceInfo", default=None)


class Top0(BaseModel):
    bandwidth_download: str = FieldInfo(alias="bandwidthDownload")

    bandwidth_upload: str = FieldInfo(alias="bandwidthUpload")

    client_country_alpha2: str = FieldInfo(alias="clientCountryAlpha2")

    client_country_name: str = FieldInfo(alias="clientCountryName")

    jitter_idle: str = FieldInfo(alias="jitterIdle")

    jitter_loaded: str = FieldInfo(alias="jitterLoaded")

    latency_idle: str = FieldInfo(alias="latencyIdle")

    latency_loaded: str = FieldInfo(alias="latencyLoaded")

    num_tests: float = FieldInfo(alias="numTests")

    rank_power: float = FieldInfo(alias="rankPower")


class TopLocationsResponse(BaseModel):
    meta: Meta

    top_0: List[Top0]
