# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["TCPConfiguration"]

class TCPConfiguration(BaseModel):
    method: Optional[Literal["connection_established"]] = None
    """The TCP connection method to use for the health check."""

    port: Optional[int] = None
    """Port number to connect to for the health check. Defaults to 80."""