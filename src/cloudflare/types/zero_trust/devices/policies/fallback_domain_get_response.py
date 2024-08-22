# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .fallback_domain import FallbackDomain

from typing_extensions import TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["FallbackDomainGetResponse"]

FallbackDomainGetResponse: TypeAlias = List[FallbackDomain]