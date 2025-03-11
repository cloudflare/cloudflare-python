# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OutputOptionsParam"]


class OutputOptionsParam(TypedDict, total=False):
    batch_prefix: Optional[str]
    """String to be prepended before each batch."""

    batch_suffix: Optional[str]
    """String to be appended after each batch."""

    cve_2021_44228: Annotated[Optional[bool], PropertyInfo(alias="CVE-2021-44228")]
    """
    If set to true, will cause all occurrences of `${` in the generated files to be
    replaced with `x{`.
    """

    field_delimiter: Optional[str]
    """String to join fields. This field be ignored when `record_template` is set."""

    field_names: List[str]
    """List of field names to be included in the Logpush output.

    For the moment, there is no option to add all fields at once, so you must
    specify all the fields names you are interested in.
    """

    output_type: Literal["ndjson", "csv"]
    """Specifies the output type, such as `ndjson` or `csv`.

    This sets default values for the rest of the settings, depending on the chosen
    output type. Some formatting rules, like string quoting, are different between
    output types.
    """

    record_delimiter: Optional[str]
    """String to be inserted in-between the records as separator."""

    record_prefix: Optional[str]
    """String to be prepended before each record."""

    record_suffix: Optional[str]
    """String to be appended after each record."""

    record_template: Optional[str]
    """
    String to use as template for each record instead of the default comma-separated
    list. All fields used in the template must be present in `field_names` as well,
    otherwise they will end up as null. Format as a Go `text/template` without any
    standard functions, like conditionals, loops, sub-templates, etc.
    """

    sample_rate: Optional[float]
    """Floating number to specify sampling rate.

    Sampling is applied on top of filtering, and regardless of the current
    `sample_interval` of the data.
    """

    timestamp_format: Literal["unixnano", "unix", "rfc3339"]
    """
    String to specify the format for timestamps, such as `unixnano`, `unix`, or
    `rfc3339`.
    """
