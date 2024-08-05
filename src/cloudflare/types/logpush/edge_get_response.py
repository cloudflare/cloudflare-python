# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .instant_logpush_job import InstantLogpushJob

__all__ = ["EdgeGetResponse"]

EdgeGetResponse: TypeAlias = List[Optional[InstantLogpushJob]]
