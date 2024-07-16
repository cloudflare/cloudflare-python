# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ...._models import BaseModel

__all__ = ["ClientCertificateInput"]


class ClientCertificateInput(BaseModel):
    certificate_id: str
    """UUID of Cloudflare managed certificate."""

    cn: str
    """Common Name that is protected by the certificate"""
