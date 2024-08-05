# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..logpush_job import LogpushJob

__all__ = ["JobGetResponse"]

JobGetResponse: TypeAlias = List[Optional[LogpushJob]]
