# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .output_options import OutputOptions

__all__ = ["JobCreateResponse"]


class JobCreateResponse(BaseModel):
    id: Optional[int] = None
    """Unique id of the job."""

    dataset: Optional[str] = None
    """Name of the dataset."""

    destination_conf: Optional[str] = None
    """Uniquely identifies a resource (such as an s3 bucket) where data will be pushed.

    Additional configuration parameters supported by the destination may be
    included.
    """

    enabled: Optional[bool] = None
    """Flag that indicates if the job is enabled."""

    error_message: Optional[datetime] = None
    """If not null, the job is currently failing.

    Failures are usually repetitive (example: no permissions to write to destination
    bucket). Only the last failure is recorded. On successful execution of a job the
    error_message and last_error are set to null.
    """

    frequency: Optional[Literal["high", "low"]] = None
    """The frequency at which Cloudflare sends batches of logs to your destination.

    Setting frequency to high sends your logs in larger quantities of smaller files.
    Setting frequency to low sends logs in smaller quantities of larger files.
    """

    last_complete: Optional[datetime] = None
    """Records the last time for which logs have been successfully pushed.

    If the last successful push was for logs range 2018-07-23T10:00:00Z to
    2018-07-23T10:01:00Z then the value of this field will be 2018-07-23T10:01:00Z.
    If the job has never run or has just been enabled and hasn't run yet then the
    field will be empty.
    """

    last_error: Optional[datetime] = None
    """Records the last time the job failed.

    If not null, the job is currently failing. If null, the job has either never
    failed or has run successfully at least once since last failure. See also the
    error_message field.
    """

    logpull_options: Optional[str] = None
    """This field is deprecated.

    Use `output_options` instead. Configuration string. It specifies things like
    requested fields and timestamp formats. If migrating from the logpull api, copy
    the url (full url or just the query string) of your call here, and logpush will
    keep on making this call for you, setting start and end times appropriately.
    """

    name: Optional[str] = None
    """Optional human readable job name.

    Not unique. Cloudflare suggests that you set this to a meaningful string, like
    the domain name, to make it easier to identify your job.
    """

    output_options: Optional[OutputOptions] = None
    """The structured replacement for `logpull_options`.

    When including this field, the `logpull_option` field will be ignored.
    """
