# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..redirect import Redirect

from ..hostname import Hostname

from typing_extensions import TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ItemGetResponse"]

ItemGetResponse: TypeAlias = Union[str, Redirect, Hostname, int, None]
