# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ....._models import BaseModel
from .....types import shared

__all__ = ["StatusIPAddressManagementDynamicAdvertisementGetAdvertisementStatusResponse"]


class StatusIPAddressManagementDynamicAdvertisementGetAdvertisementStatusResponse(BaseModel):
    advertised: Optional[bool] = None
    """Enablement of prefix advertisement to the Internet."""

    advertised_modified_at: Optional[datetime] = None
    """Last time the advertisement status was changed.

    This field is only not 'null' if on demand is enabled.
    """
