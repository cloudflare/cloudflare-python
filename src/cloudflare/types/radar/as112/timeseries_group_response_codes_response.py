# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, List

from ...._models import BaseModel

__all__ = ["TimeseriesGroupResponseCodesResponse", "Serie0"]


class Serie0(BaseModel):
    timestamps: List[str]

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> List[str]: ...


class TimeseriesGroupResponseCodesResponse(BaseModel):
    meta: object

    serie_0: Serie0
