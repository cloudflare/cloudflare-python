# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "MetricListResponse",
    "InfrequentAccess",
    "InfrequentAccessPublished",
    "InfrequentAccessUploaded",
    "Standard",
    "StandardPublished",
    "StandardUploaded",
]


class InfrequentAccessPublished(BaseModel):
    """Metrics on number of objects/amount of storage used."""

    metadata_size: Optional[float] = FieldInfo(alias="metadataSize", default=None)
    """Amount of."""

    objects: Optional[float] = None
    """Number of objects stored."""

    payload_size: Optional[float] = FieldInfo(alias="payloadSize", default=None)
    """Amount of storage used by object data."""


class InfrequentAccessUploaded(BaseModel):
    """Metrics on number of objects/amount of storage used."""

    metadata_size: Optional[float] = FieldInfo(alias="metadataSize", default=None)
    """Amount of."""

    objects: Optional[float] = None
    """Number of objects stored."""

    payload_size: Optional[float] = FieldInfo(alias="payloadSize", default=None)
    """Amount of storage used by object data."""


class InfrequentAccess(BaseModel):
    """Metrics based on what state they are in(uploaded or published)."""

    published: Optional[InfrequentAccessPublished] = None
    """Metrics on number of objects/amount of storage used."""

    uploaded: Optional[InfrequentAccessUploaded] = None
    """Metrics on number of objects/amount of storage used."""


class StandardPublished(BaseModel):
    """Metrics on number of objects/amount of storage used."""

    metadata_size: Optional[float] = FieldInfo(alias="metadataSize", default=None)
    """Amount of."""

    objects: Optional[float] = None
    """Number of objects stored."""

    payload_size: Optional[float] = FieldInfo(alias="payloadSize", default=None)
    """Amount of storage used by object data."""


class StandardUploaded(BaseModel):
    """Metrics on number of objects/amount of storage used."""

    metadata_size: Optional[float] = FieldInfo(alias="metadataSize", default=None)
    """Amount of."""

    objects: Optional[float] = None
    """Number of objects stored."""

    payload_size: Optional[float] = FieldInfo(alias="payloadSize", default=None)
    """Amount of storage used by object data."""


class Standard(BaseModel):
    """Metrics based on what state they are in(uploaded or published)."""

    published: Optional[StandardPublished] = None
    """Metrics on number of objects/amount of storage used."""

    uploaded: Optional[StandardUploaded] = None
    """Metrics on number of objects/amount of storage used."""


class MetricListResponse(BaseModel):
    """Metrics based on the class they belong to."""

    infrequent_access: Optional[InfrequentAccess] = FieldInfo(alias="infrequentAccess", default=None)
    """Metrics based on what state they are in(uploaded or published)."""

    standard: Optional[Standard] = None
    """Metrics based on what state they are in(uploaded or published)."""
