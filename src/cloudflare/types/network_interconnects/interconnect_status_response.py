# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = ["InterconnectStatusResponse", "Pending", "Down", "Unhealthy", "Healthy"]


class Pending(BaseModel):
    state: Literal["Pending"]


class Down(BaseModel):
    state: Literal["Down"]

    reason: Optional[str] = None
    """Diagnostic information, if available"""


class Unhealthy(BaseModel):
    state: Literal["Unhealthy"]

    reason: Optional[str] = None
    """Diagnostic information, if available"""


class Healthy(BaseModel):
    state: Literal["Healthy"]


InterconnectStatusResponse: TypeAlias = Annotated[
    Union[Pending, Down, Unhealthy, Healthy], PropertyInfo(discriminator="state")
]
