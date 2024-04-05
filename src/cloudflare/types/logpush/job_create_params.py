# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .datasets import OutputOptionsParam

__all__ = ["JobCreateParams"]


class JobCreateParams(TypedDict, total=False):
    destination_conf: Required[str]
    """Uniquely identifies a resource (such as an s3 bucket) where data will be pushed.

    Additional configuration parameters supported by the destination may be
    included.
    """

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    dataset: Optional[str]
    """Name of the dataset."""

    enabled: bool
    """Flag that indicates if the job is enabled."""

    frequency: Optional[Literal["high", "low"]]
    """The frequency at which Cloudflare sends batches of logs to your destination.

    Setting frequency to high sends your logs in larger quantities of smaller files.
    Setting frequency to low sends logs in smaller quantities of larger files.
    """

    logpull_options: Optional[str]
    """This field is deprecated.

    Use `output_options` instead. Configuration string. It specifies things like
    requested fields and timestamp formats. If migrating from the logpull api, copy
    the url (full url or just the query string) of your call here, and logpush will
    keep on making this call for you, setting start and end times appropriately.
    """

    name: Optional[str]
    """Optional human readable job name.

    Not unique. Cloudflare suggests that you set this to a meaningful string, like
    the domain name, to make it easier to identify your job.
    """

    output_options: Optional[OutputOptionsParam]
    """The structured replacement for `logpull_options`.

    When including this field, the `logpull_option` field will be ignored.
    """

    ownership_challenge: str
    """Ownership challenge token to prove destination ownership."""
