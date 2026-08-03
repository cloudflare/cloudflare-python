# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ZskListResponse", "DNSKEY", "DNSKEYHdr", "SigningKey"]


class DNSKEYHdr(BaseModel):
    class_: Optional[int] = FieldInfo(alias="Class", default=None)

    name: Optional[str] = FieldInfo(alias="Name", default=None)

    rdlength: Optional[int] = FieldInfo(alias="Rdlength", default=None)

    rrtype: Optional[int] = FieldInfo(alias="Rrtype", default=None)

    ttl: Optional[int] = FieldInfo(alias="Ttl", default=None)


class DNSKEY(BaseModel):
    algorithm: Optional[int] = FieldInfo(alias="Algorithm", default=None)

    flags: Optional[int] = FieldInfo(alias="Flags", default=None)

    hdr: Optional[DNSKEYHdr] = FieldInfo(alias="Hdr", default=None)

    protocol: Optional[int] = FieldInfo(alias="Protocol", default=None)

    public_key: Optional[str] = FieldInfo(alias="PublicKey", default=None)


class SigningKey(BaseModel):
    kek: Optional[str] = None
    """Key encryption key name used to encrypt the private key."""

    privkey: Optional[str] = None
    """Encrypted private key material for the signing key."""

    pubkey: Optional[str] = None
    """Public key content associated with the signing key."""


class ZskListResponse(BaseModel):
    dnskey: Optional[DNSKEY] = FieldInfo(alias="DNSKEY", default=None)

    location: Optional[Literal["database", "vault"]] = FieldInfo(alias="Location", default=None)
    """Storage backend where the DNSSEC key material is stored."""

    name: Optional[str] = FieldInfo(alias="Name", default=None)
    """Internal key name for the ZSK."""

    signing_key: Optional[SigningKey] = FieldInfo(alias="SigningKey", default=None)

    tag: Optional[Literal["active", "publish", "external", "retired", "revoked", "removed"]] = FieldInfo(
        alias="Tag", default=None
    )
    """Lifecycle state tag attached to the DNSSEC key."""
