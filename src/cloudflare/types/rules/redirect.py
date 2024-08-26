# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Redirect"]

class Redirect(BaseModel):
    source_url: str

    target_url: str

    include_subdomains: Optional[bool] = None

    preserve_path_suffix: Optional[bool] = None

    preserve_query_string: Optional[bool] = None

    status_code: Optional[Literal[301, 302, 307, 308]] = None

    subpath_matching: Optional[bool] = None