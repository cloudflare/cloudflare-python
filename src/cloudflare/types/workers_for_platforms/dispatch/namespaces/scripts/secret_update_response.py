# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ......_models import BaseModel

__all__ = ["SecretUpdateResponse"]


class SecretUpdateResponse(BaseModel):
    name: Optional[str] = None
    """
    The name of this secret, this is what will be used to access it inside the
    Worker.
    """

    type: Optional[Literal["secret_text"]] = None
    """The type of secret."""
