# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SettingUpdateResponse"]


class SettingUpdateResponse(BaseModel):
    validation_default_mitigation_action: Literal["none", "log", "block"]
    """The default mitigation action used

    Mitigation actions are as follows:

    - `log` - log request when request does not conform to schema
    - `block` - deny access to the site when request does not conform to schema
    - `none` - skip running schema validation
    """

    validation_override_mitigation_action: Optional[Literal["none"]] = None
    """
    When not null, this overrides global both zone level and operation level
    mitigation actions. This can serve as a quick way to disable schema validation
    for the whole zone.

    - `"none"` will skip running schema validation entirely for the request
    """
