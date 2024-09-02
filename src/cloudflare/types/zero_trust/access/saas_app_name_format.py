# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["SaaSAppNameFormat"]

SaaSAppNameFormat: TypeAlias = Literal[
    "urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified",
    "urn:oasis:names:tc:SAML:2.0:attrname-format:basic",
    "urn:oasis:names:tc:SAML:2.0:attrname-format:uri",
]
