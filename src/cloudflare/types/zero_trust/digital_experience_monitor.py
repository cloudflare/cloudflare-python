# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["DigitalExperienceMonitor"]


class DigitalExperienceMonitor(BaseModel):
    id: str

    default: bool
    """Whether the policy is the default for the account"""

    name: str
