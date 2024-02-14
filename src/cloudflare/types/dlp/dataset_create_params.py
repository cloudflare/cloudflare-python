# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Optional

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["DatasetCreateParams"]


class DatasetCreateParams(TypedDict, total=False):
    name: Required[str]

    description: Optional[str]

    secret: bool
    """Generate a secret dataset.

    If true, the response will include a secret to use with the EDM encoder. If
    false, the response has no secret and the dataset is uploaded in plaintext.
    """
