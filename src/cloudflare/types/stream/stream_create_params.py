# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["StreamCreateParams"]


class StreamCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    body: Required[object]

    tus_resumable: Required[Annotated[Literal["1.0.0"], PropertyInfo(alias="Tus-Resumable")]]
    """Specifies the TUS protocol version.

    This value must be included in every upload request. Notes: The only supported
    version of TUS protocol is 1.0.0.
    """

    upload_length: Required[Annotated[int, PropertyInfo(alias="Upload-Length")]]
    """Indicates the size of the entire upload in bytes.

    The value must be a non-negative integer.
    """

    direct_user: bool
    """
    Provisions a URL to let your end users upload videos directly to Cloudflare
    Stream without exposing your API token to clients.
    """

    upload_creator: Annotated[str, PropertyInfo(alias="Upload-Creator")]
    """A user-defined identifier for the media creator."""

    upload_metadata: Annotated[str, PropertyInfo(alias="Upload-Metadata")]
    """Comma-separated key-value pairs following the TUS protocol specification.

    Values are Base-64 encoded. Supported keys: `name`, `requiresignedurls`,
    `allowedorigins`, `thumbnailtimestamppct`, `watermark`, `scheduleddeletion`.
    """
