# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from ..shared.permission import Permission

from ..accounts.status import Status

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Organization"]


class Organization(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    name: Optional[str] = None
    """Organization name."""

    permissions: Optional[List[Permission]] = None
    """Access permissions for this User."""

    roles: Optional[List[str]] = None
    """List of roles that a user has within an organization."""

    status: Optional[Status] = None
    """Whether the user is a member of the organization or has an invitation pending."""
