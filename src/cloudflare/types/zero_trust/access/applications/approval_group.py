# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ApprovalGroup"]

class ApprovalGroup(BaseModel):
    approvals_needed: float
    """The number of approvals needed to obtain access."""

    email_addresses: Optional[List[str]] = None
    """A list of emails that can approve the access request."""

    email_list_uuid: Optional[str] = None
    """The UUID of an re-usable email list."""