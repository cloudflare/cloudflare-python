# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["StatusEditResponse"]


class StatusEditResponse(BaseModel):
    advertised: Optional[bool] = None
    """Enablement of prefix advertisement to the Internet."""

    advertised_modified_at: Optional[datetime] = None
    """Last time the advertisement status was changed.

    This field is only not 'null' if on demand is enabled.
    """
