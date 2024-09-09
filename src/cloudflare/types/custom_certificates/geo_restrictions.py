# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["GeoRestrictions"]


class GeoRestrictions(BaseModel):
    label: Optional[Literal["us", "eu", "highest_security"]] = None
