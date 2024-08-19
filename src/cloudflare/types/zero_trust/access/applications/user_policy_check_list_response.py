# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel
from .user_policy_check_geo import UserPolicyCheckGeo

__all__ = ["UserPolicyCheckListResponse", "AppState", "UserIdentity"]


class AppState(BaseModel):
    app_uid: Optional[str] = None
    """UUID"""

    aud: Optional[str] = None

    hostname: Optional[str] = None

    name: Optional[str] = None

    policies: Optional[List[object]] = None

    status: Optional[str] = None


class UserIdentity(BaseModel):
    id: Optional[str] = None

    account_id: Optional[str] = None

    device_sessions: Optional[object] = None

    email: Optional[str] = None

    geo: Optional[UserPolicyCheckGeo] = None

    iat: Optional[int] = None

    is_gateway: Optional[bool] = None

    is_warp: Optional[bool] = None

    name: Optional[str] = None

    user_uuid: Optional[str] = None
    """UUID"""

    version: Optional[int] = None


class UserPolicyCheckListResponse(BaseModel):
    app_state: Optional[AppState] = None

    user_identity: Optional[UserIdentity] = None
