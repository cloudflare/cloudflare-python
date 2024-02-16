# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["ScriptDeleteParams"]


class ScriptDeleteParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    force: bool
    """
    If set to true, delete will not be stopped by associated service binding,
    durable object, or other binding. Any of these associated bindings/durable
    objects will be deleted along with the script.
    """
