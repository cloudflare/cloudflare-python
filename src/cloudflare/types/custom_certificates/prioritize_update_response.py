# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .custom_certificate import CustomCertificate

__all__ = ["PrioritizeUpdateResponse"]

PrioritizeUpdateResponse: TypeAlias = List[CustomCertificate]
