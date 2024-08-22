# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CertificateCA"]

CertificateCA: TypeAlias = Literal["digicert", "google", "lets_encrypt", "ssl_com"]