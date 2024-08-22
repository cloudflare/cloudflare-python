# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["RequestValidity"]

RequestValidity: TypeAlias = Literal[7, 30, 90, 365, 730, 1095, 5475]