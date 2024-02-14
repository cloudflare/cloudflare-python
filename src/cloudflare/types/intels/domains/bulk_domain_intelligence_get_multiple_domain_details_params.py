# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo
from ....types import shared_params

__all__ = ["BulkDomainIntelligenceGetMultipleDomainDetailsParams"]


class BulkDomainIntelligenceGetMultipleDomainDetailsParams(TypedDict, total=False):
    domain: object
    """Accepts multiple values, i.e. `?domain=cloudflare.com&domain=example.com`."""
