# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["DatabaseImportParams", "Variant0", "Variant1", "Variant2"]


class Variant0(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    action: Required[Literal["init"]]
    """Indicates you have a new SQL file to upload."""

    etag: Required[str]
    """Required when action is 'init' or 'ingest'.

    An md5 hash of the file you're uploading. Used to check if it already exists,
    and validate its contents before ingesting.
    """


class Variant1(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    action: Required[Literal["ingest"]]
    """Indicates you've finished uploading to tell the D1 to start consuming it"""

    etag: Required[str]
    """An md5 hash of the file you're uploading.

    Used to check if it already exists, and validate its contents before ingesting.
    """

    filename: Required[str]
    """The filename you have successfully uploaded."""


class Variant2(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    action: Required[Literal["poll"]]
    """Indicates you've finished uploading to tell the D1 to start consuming it"""

    current_bookmark: Required[str]
    """This identifies the currently-running import, checking its status."""


DatabaseImportParams: TypeAlias = Union[Variant0, Variant1, Variant2]
