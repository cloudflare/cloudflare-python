# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["UserListResponse"]


class UserListResponse(BaseModel):
    user_emails: Optional[List[str]] = FieldInfo(alias="userEmails", default=None)
    """List of user emails"""
