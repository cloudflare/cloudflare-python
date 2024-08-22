# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from ..._models import BaseModel

__all__ = ["DeviceExperienceMonitor"]


class DeviceExperienceMonitor(BaseModel):
    id: str

    default: bool
    """Whether the policy is the default for the account"""

    name: str
