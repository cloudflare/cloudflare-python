# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from datetime import datetime

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["FallbackOriginUpdateResponse"]


class FallbackOriginUpdateResponse(BaseModel):
    created_at: Optional[datetime] = None
    """This is the time the fallback origin was created."""

    errors: Optional[List[str]] = None
    """
    These are errors that were encountered while trying to activate a fallback
    origin.
    """

    origin: Optional[str] = None
    """Your origin hostname that requests to your custom hostnames will be sent to."""

    status: Optional[
        Literal[
            "initializing",
            "pending_deployment",
            "pending_deletion",
            "active",
            "deployment_timed_out",
            "deletion_timed_out",
        ]
    ] = None
    """Status of the fallback origin's activation."""

    updated_at: Optional[datetime] = None
    """This is the time the fallback origin was updated."""
