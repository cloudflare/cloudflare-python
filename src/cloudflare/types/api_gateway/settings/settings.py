# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["Settings"]


class Settings(BaseModel):
    validation_default_mitigation_action: Optional[Literal["none", "log", "block"]] = None
    """
    The default mitigation action used when there is no mitigation action defined on
    the operation

    Mitigation actions are as follows:

    - `log` - log request when request does not conform to schema
    - `block` - deny access to the site when request does not conform to schema

    A special value of of `none` will skip running schema validation entirely for
    the request when there is no mitigation action defined on the operation
    """

    validation_override_mitigation_action: Optional[Literal["none"]] = None
    """When set, this overrides both zone level and operation level mitigation actions.

    - `none` will skip running schema validation entirely for the request
    - `null` indicates that no override is in place
    """
