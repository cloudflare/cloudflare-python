# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["SpeedHistogramResponse", "Histogram0"]

class Histogram0(BaseModel):
    bandwidth_download: List[str] = FieldInfo(alias = "bandwidthDownload")

    bandwidth_upload: List[str] = FieldInfo(alias = "bandwidthUpload")

    bucket_min: List[str] = FieldInfo(alias = "bucketMin")

class SpeedHistogramResponse(BaseModel):
    histogram_0: Histogram0

    meta: object