# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["SpeedHistogramResponse", "Histogram0"]


class Histogram0(BaseModel):
    bandwidth_download: List[str] = FieldInfo(alias="bandwidthDownload")

    bandwidth_upload: List[str] = FieldInfo(alias="bandwidthUpload")

    bucket_min: List[str] = FieldInfo(alias="bucketMin")


class SpeedHistogramResponse(BaseModel):
    histogram_0: Histogram0

    meta: object
