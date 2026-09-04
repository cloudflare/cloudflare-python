# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["UpstreamTimeseriesResponse", "Meta", "Serie0"]


class Meta(BaseModel):
    data_time: Optional[datetime] = FieldInfo(alias="dataTime", default=None)
    """Timestamp of the underlying RIB data."""

    effective_collector: Optional[str] = FieldInfo(alias="effectiveCollector", default=None)

    query_time: Optional[datetime] = FieldInfo(alias="queryTime", default=None)
    """Timestamp when the query was executed."""

    stale: bool


class Serie0(BaseModel):
    timestamps: List[datetime]

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, List[str]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> List[str]: ...
    else:
        __pydantic_extra__: Dict[str, List[str]]


class UpstreamTimeseriesResponse(BaseModel):
    meta: Meta

    serie_0: Serie0
