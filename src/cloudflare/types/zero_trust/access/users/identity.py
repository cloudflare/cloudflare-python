# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel
from ..applications.user_policy_check_geo import UserPolicyCheckGeo

__all__ = ["Identity", "DeviceSessions", "DevicePosture", "DevicePostureCheck", "IdP", "MTLSAuth"]


class DeviceSessions(BaseModel):
    last_authenticated: Optional[float] = None


class DevicePostureCheck(BaseModel):
    exists: Optional[bool] = None

    path: Optional[str] = None


class DevicePosture(BaseModel):
    id: Optional[str] = None

    check: Optional[DevicePostureCheck] = None

    data: Optional[object] = None

    description: Optional[str] = None

    error: Optional[str] = None

    rule_name: Optional[str] = None

    success: Optional[bool] = None

    timestamp: Optional[str] = None

    type: Optional[str] = None


class IdP(BaseModel):
    id: Optional[str] = None

    type: Optional[str] = None


class MTLSAuth(BaseModel):
    auth_status: Optional[str] = None

    cert_issuer_dn: Optional[str] = None

    cert_issuer_ski: Optional[str] = None

    cert_presented: Optional[bool] = None

    cert_serial: Optional[str] = None


class Identity(BaseModel):
    account_id: Optional[str] = None

    auth_status: Optional[str] = None

    common_name: Optional[str] = None

    device_id: Optional[str] = None

    device_sessions: Optional[Dict[str, DeviceSessions]] = None

    device_posture: Optional[Dict[str, DevicePosture]] = FieldInfo(alias="devicePosture", default=None)

    email: Optional[str] = None

    geo: Optional[UserPolicyCheckGeo] = None

    iat: Optional[float] = None

    idp: Optional[IdP] = None

    ip: Optional[str] = None

    is_gateway: Optional[bool] = None

    is_warp: Optional[bool] = None

    mtls_auth: Optional[MTLSAuth] = None

    service_token_id: Optional[str] = None

    service_token_status: Optional[bool] = None

    user_uuid: Optional[str] = None

    version: Optional[float] = None
