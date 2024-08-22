# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RayIDGetParams"]


class RayIDGetParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    fields: str
    """
    The `/received` route by default returns a limited set of fields, and allows
    customers to override the default field set by specifying individual fields. The
    reasons for this are: 1. Most customers require only a small subset of fields,
    but that subset varies from customer to customer; 2. Flat schema is much easier
    to work with downstream (importing into BigTable etc); 3. Performance (time to
    process, file size). If `?fields=` is not specified, default field set is
    returned. This default field set may change at any time. When `?fields=` is
    provided, each record is returned with the specified fields. `fields` must be
    specified as a comma separated list without any whitespaces, and all fields must
    exist. The order in which fields are specified does not matter, and the order of
    fields in the response is not specified.
    """

    timestamps: Literal["unix", "unixnano", "rfc3339"]
    """By default, timestamps in responses are returned as Unix nanosecond integers.

    The `?timestamps=` argument can be set to change the format in which response
    timestamps are returned. Possible values are: `unix`, `unixnano`, `rfc3339`.
    Note that `unix` and `unixnano` return timestamps as integers; `rfc3339` returns
    timestamps as strings.
    """
