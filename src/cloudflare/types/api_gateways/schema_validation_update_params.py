# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import Optional

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["SchemaValidationUpdateParams"]


class SchemaValidationUpdateParams(TypedDict, total=False):
    validation_default_mitigation_action: Optional[Literal["none", "log", "block"]]
    """
    The default mitigation action used when there is no mitigation action defined on
    the operation Mitigation actions are as follows:

    - `log` - log request when request does not conform to schema
    - `block` - deny access to the site when request does not conform to schema

    A special value of of `none` will skip running schema validation entirely for
    the request when there is no mitigation action defined on the operation

    `null` will have no effect.
    """

    validation_override_mitigation_action: Optional[Literal["none", "disable_override"]]
    """When set, this overrides both zone level and operation level mitigation actions.

    - `none` will skip running schema validation entirely for the request

    To clear any override, use the special value `disable_override`

    `null` will have no effect.
    """
