# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .pagerduty import Pagerduty

__all__ = ["PagerdutyGetResponse"]

PagerdutyGetResponse: TypeAlias = List[Pagerduty]
