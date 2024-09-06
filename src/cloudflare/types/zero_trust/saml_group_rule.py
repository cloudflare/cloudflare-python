# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["SAMLGroupRule", "SAML"]


class SAML(BaseModel):
    attribute_name: str
    """The name of the SAML attribute."""

    attribute_value: str
    """The SAML attribute value to look for."""


class SAMLGroupRule(BaseModel):
    saml: SAML
