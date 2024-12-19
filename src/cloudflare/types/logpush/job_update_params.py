# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .output_options_param import OutputOptionsParam

__all__ = ["JobUpdateParams"]


class JobUpdateParams(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    destination_conf: str
    """Uniquely identifies a resource (such as an s3 bucket) where data will be pushed.

    Additional configuration parameters supported by the destination may be
    included.
    """

    enabled: bool
    """Flag that indicates if the job is enabled."""

    frequency: Optional[Literal["high", "low"]]
    """This field is deprecated.

    Please use `max_upload_*` parameters instead. The frequency at which Cloudflare
    sends batches of logs to your destination. Setting frequency to high sends your
    logs in larger quantities of smaller files. Setting frequency to low sends logs
    in smaller quantities of larger files.
    """

    kind: Optional[Literal["edge"]]
    """
    The kind parameter (optional) is used to differentiate between Logpush and Edge
    Log Delivery jobs. Currently, Edge Log Delivery is only supported for the
    `http_requests` dataset.
    """

    logpull_options: Optional[str]
    """This field is deprecated.

    Use `output_options` instead. Configuration string. It specifies things like
    requested fields and timestamp formats. If migrating from the logpull api, copy
    the url (full url or just the query string) of your call here, and logpush will
    keep on making this call for you, setting start and end times appropriately.
    """

    max_upload_bytes: Optional[int]
    """The maximum uncompressed file size of a batch of logs.

    This setting value must be between `5 MB` and `1 GB`, or `0` to disable it. Note
    that you cannot set a minimum file size; this means that log files may be much
    smaller than this batch size. This parameter is not available for jobs with
    `edge` as its kind.
    """

    max_upload_interval_seconds: Optional[int]
    """The maximum interval in seconds for log batches.

    This setting must be between 30 and 300 seconds (5 minutes), or `0` to disable
    it. Note that you cannot specify a minimum interval for log batches; this means
    that log files may be sent in shorter intervals than this. This parameter is
    only used for jobs with `edge` as its kind.
    """

    max_upload_records: Optional[int]
    """The maximum number of log lines per batch.

    This setting must be between 1000 and 1,000,000 lines, or `0` to disable it.
    Note that you cannot specify a minimum number of log lines per batch; this means
    that log files may contain many fewer lines than this. This parameter is not
    available for jobs with `edge` as its kind.
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
