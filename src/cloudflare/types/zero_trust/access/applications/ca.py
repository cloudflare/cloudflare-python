# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["CA"]

class CA(BaseModel):
    id: Optional[str] = None
    """The ID of the CA."""

    aud: Optional[str] = None
    """The Application Audience (AUD) tag.

    Identifies the application associated with the CA.
    """

    public_key: Optional[str] = None
    """The public key to add to your SSH server configuration."""