# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, List, Union

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RankingTimeseriesGroupsResponse", "Meta", "Serie0"]


class Meta(BaseModel):
    date_range: List[object] = FieldInfo(alias="dateRange")


class Serie0(BaseModel):
    timestamps: List[str]

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> List[Union[str, float]]: ...


class RankingTimeseriesGroupsResponse(BaseModel):
    meta: Meta

    serie_0: Serie0
