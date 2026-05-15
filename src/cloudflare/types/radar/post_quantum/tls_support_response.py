# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["TLSSupportResponse", "Bugs"]


class Bugs(BaseModel):
    hrr_failure: bool = FieldInfo(alias="hrrFailure")
    """
    Server sends a HelloRetryRequest but fails to complete the handshake after the
    client sends the second ClientHello. Often caused by non-compliant TLS 1.3
    implementations on shared hosting providers.
    """

    split_client_hello: bool = FieldInfo(alias="splitClientHello")
    """
    Server rejects fragmented ClientHello caused by large PQ keyshare, but accepts
    classical (non-PQ) handshakes. Typically caused by middleboxes or firewalls that
    cannot reassemble split TLS ClientHello messages.
    """

    unknown_keyshare: bool = FieldInfo(alias="unknownKeyshare")
    """
    Server cannot handle an unknown key exchange algorithm in the ClientHello
    keyshare extension. Compliant servers should respond with HelloRetryRequest for
    a supported algorithm.
    """


class TLSSupportResponse(BaseModel):
    bugs: Bugs

    host: str
    """The host that was tested"""

    kex: float
    """TLS CurveID of the negotiated key exchange"""

    kex_name: str = FieldInfo(alias="kexName")
    """Human-readable name of the key exchange algorithm"""

    pq: bool
    """
    Whether the negotiated key exchange uses Post-Quantum cryptography (specifically
    X25519MLKEM768)
    """
