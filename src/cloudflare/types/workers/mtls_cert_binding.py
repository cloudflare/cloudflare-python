# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing_extensions import Literal

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["MTLSCERTBinding"]


class MTLSCERTBinding(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["mtls_certificate"]
    """The class of resource that the binding provides."""

    certificate_id: Optional[str] = None
    """ID of the certificate to bind to"""
