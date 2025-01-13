# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .certificate_asssociation import CertificateAsssociation

__all__ = ["AssociationGetResponse"]

AssociationGetResponse: TypeAlias = List[CertificateAsssociation]
