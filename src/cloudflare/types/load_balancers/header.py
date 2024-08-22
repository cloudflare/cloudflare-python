# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .host import Host
from ..._models import BaseModel

__all__ = ["Header"]


class Header(BaseModel):
    host: Optional[List[Host]] = FieldInfo(alias="Host", default=None)
    """The 'Host' header allows to override the hostname set in the HTTP request.

    Current support is 1 'Host' header override per origin.
    """
