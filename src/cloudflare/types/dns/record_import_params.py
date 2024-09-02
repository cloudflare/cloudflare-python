# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["RecordImportParams"]


class RecordImportParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    file: Required[str]
    """BIND config to import.

    **Tip:** When using cURL, a file can be uploaded using
    `--form 'file=@bind_config.txt'`.
    """

    proxied: str
    """
    Whether or not proxiable records should receive the performance and security
    benefits of Cloudflare.

    The value should be either `true` or `false`.
    """
