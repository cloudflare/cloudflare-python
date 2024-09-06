# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["OriginSteering"]


class OriginSteering(BaseModel):
    policy: Optional[Literal["random", "hash", "least_outstanding_requests", "least_connections"]] = None
    """The type of origin steering policy to use.

    - `"random"`: Select an origin randomly.
    - `"hash"`: Select an origin by computing a hash over the CF-Connecting-IP
      address.
    - `"least_outstanding_requests"`: Select an origin by taking into consideration
      origin weights, as well as each origin's number of outstanding requests.
      Origins with more pending requests are weighted proportionately less relative
      to others.
    - `"least_connections"`: Select an origin by taking into consideration origin
      weights, as well as each origin's number of open connections. Origins with
      more open connections are weighted proportionately less relative to others.
      Supported for HTTP/1 and HTTP/2 connections.
    """
