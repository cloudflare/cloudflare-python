# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["DevicePolicyCertificates"]


class DevicePolicyCertificates(BaseModel):
    enabled: bool
    """
    The current status of the device policy certificate provisioning feature for
    WARP clients.
    """
