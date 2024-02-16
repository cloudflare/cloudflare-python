# File generated from our OpenAPI spec by Stainless.

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["TsigSecondaryDNSTsigListTsiGsResponse", "TsigSecondaryDNSTsigListTsiGsResponseItem"]


class TsigSecondaryDNSTsigListTsiGsResponseItem(BaseModel):
    id: object

    algo: str
    """TSIG algorithm."""

    name: str
    """TSIG key name."""

    secret: str
    """TSIG secret."""


TsigSecondaryDNSTsigListTsiGsResponse = List[TsigSecondaryDNSTsigListTsiGsResponseItem]
