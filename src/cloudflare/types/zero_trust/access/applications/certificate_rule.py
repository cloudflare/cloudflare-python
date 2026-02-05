# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

__all__ = ["CertificateRule", "Certificate"]


class Certificate(BaseModel):
    pass


class CertificateRule(BaseModel):
    """Matches any valid client certificate."""

    certificate: Certificate
