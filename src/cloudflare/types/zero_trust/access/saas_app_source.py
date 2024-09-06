# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional, Dict

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["SaaSAppSource"]


class SaaSAppSource(BaseModel):
    name: Optional[str] = None
    """The name of the IdP attribute."""

    name_by_idp: Optional[Dict[str, str]] = None
    """A mapping from IdP ID to attribute name."""
