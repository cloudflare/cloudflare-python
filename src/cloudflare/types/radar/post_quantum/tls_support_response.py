# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["TLSSupportResponse"]


class TLSSupportResponse(BaseModel):
    host: str
    """The host that was tested"""

    kex: float
    """TLS CurveID of the negotiated key exchange"""

    kex_name: str = FieldInfo(alias="kexName")
    """Human-readable name of the key exchange algorithm"""

    pq: bool
    """Whether the negotiated key exchange uses Post-Quantum cryptography"""
