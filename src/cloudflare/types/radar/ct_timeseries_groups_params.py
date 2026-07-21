# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["CTTimeseriesGroupsParams"]


class CTTimeseriesGroupsParams(TypedDict, total=False):
    agg_interval: Annotated[Literal["15m", "1h", "1d", "1w"], PropertyInfo(alias="aggInterval")]
    """Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).

    Refer to
    [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).
    When omitted, the interval is auto-selected from the requested date range; finer
    intervals are only available for shorter ranges. If the requested interval is
    too granular for the date range, the request is rejected.
    """

    ca: SequenceNotStr[str]
    """Filters results by certificate authority."""

    ca_owner: Annotated[SequenceNotStr[str], PropertyInfo(alias="caOwner")]
    """Filters results by certificate authority owner."""

    date_end: Annotated[SequenceNotStr[Union[str, datetime]], PropertyInfo(alias="dateEnd", format="iso8601")]
    """End of the date range (inclusive).

    Alternative to `dateRange`; provide together with `dateStart`. When requesting
    comparison series, every series must resolve to the same duration as the main
    series. Each `dateStart`/`dateEnd` is floored to the nearest 15 minutes before
    evaluation, so windows whose durations match only before alignment may be
    rejected.
    """

    date_range: Annotated[SequenceNotStr[str], PropertyInfo(alias="dateRange")]
    """
    Filters results by relative date range ending at the current time, with each
    value producing a separate series. Use `<n>d` for days (up to `364d`) or `<n>w`
    for weeks (up to `52w`). Append `control` to request the equivalent previous
    period for comparison: the comparison window is shifted back by the current
    window's length rounded up to a whole number of weeks, so it keeps the same
    weekday alignment and does not overlap the current window (e.g. `7dcontrol`
    covers days -14 to -7, `10dcontrol` covers days -24 to -14). For example, pass
    `7d` and `7dcontrol` to compare this week with the previous week. All series
    must resolve to the same duration as the main series; relative ranges (including
    `control`) satisfy this automatically. Use this parameter or set specific start
    and end dates (`dateStart` and `dateEnd` parameters).
    """

    date_start: Annotated[SequenceNotStr[Union[str, datetime]], PropertyInfo(alias="dateStart", format="iso8601")]
    """Start of the date range.

    Alternative to `dateRange`; provide together with `dateEnd`. When requesting
    comparison series, every series must resolve to the same duration as the main
    series. Each `dateStart`/`dateEnd` is floored to the nearest 15 minutes before
    evaluation, so windows whose durations match only before alignment may be
    rejected.
    """

    duration: List[
        Literal[
            "LTE_3D",
            "GT_3D_LTE_7D",
            "GT_7D_LTE_10D",
            "GT_10D_LTE_47D",
            "GT_47D_LTE_100D",
            "GT_100D_LTE_200D",
            "GT_200D",
        ]
    ]
    """Filters results by certificate duration."""

    entry_type: Annotated[List[Literal["PRECERTIFICATE", "CERTIFICATE"]], PropertyInfo(alias="entryType")]
    """Filters results by entry type (certificate vs.

    pre-certificate). Incompatible with the `tld` filter/dimension.
    """

    expiration_status: Annotated[List[Literal["EXPIRED", "VALID"]], PropertyInfo(alias="expirationStatus")]
    """Filters results by expiration status (expired vs. valid)."""

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    has_ips: Annotated[Iterable[bool], PropertyInfo(alias="hasIps")]
    """
    Filters results based on whether the certificates are bound to specific IP
    addresses.
    """

    has_wildcards: Annotated[Iterable[bool], PropertyInfo(alias="hasWildcards")]
    """Filters results based on whether the certificates contain wildcard domains."""

    limit_per_group: Annotated[int, PropertyInfo(alias="limitPerGroup")]
    """
    Limits the number of objects per group to the top items within the specified
    time range. When item count exceeds the limit, extra items appear grouped under
    an "other" category. Only supported on high-cardinality dimensions; otherwise
    the request is rejected. Minimum value is 2.
    """

    log: SequenceNotStr[str]
    """Filters results by certificate log.

    Incompatible with the `tld` filter/dimension.
    """

    log_api: Annotated[List[Literal["RFC6962", "STATIC"]], PropertyInfo(alias="logApi")]
    """Filters results by certificate log API (RFC6962 vs.

    static). Incompatible with the `tld` filter/dimension.
    """

    log_operator: Annotated[SequenceNotStr[str], PropertyInfo(alias="logOperator")]
    """Filters results by certificate log operator.

    Incompatible with the `tld` filter/dimension.
    """

    name: SequenceNotStr[str]
    """Array of names used to label the series in the response."""

    normalization: Literal["RAW_VALUES", "PERCENTAGE"]
    """Normalization method applied to the results.

    Refer to
    [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).
    """

    public_key_algorithm: Annotated[List[Literal["DSA", "ECDSA", "RSA"]], PropertyInfo(alias="publicKeyAlgorithm")]
    """Filters results by public key algorithm."""

    signature_algorithm: Annotated[
        List[
            Literal[
                "DSA_SHA_1",
                "DSA_SHA_256",
                "ECDSA_SHA_1",
                "ECDSA_SHA_256",
                "ECDSA_SHA_384",
                "ECDSA_SHA_512",
                "PSS_SHA_256",
                "PSS_SHA_384",
                "PSS_SHA_512",
                "RSA_MD2",
                "RSA_MD5",
                "RSA_SHA_1",
                "RSA_SHA_256",
                "RSA_SHA_384",
                "RSA_SHA_512",
            ]
        ],
        PropertyInfo(alias="signatureAlgorithm"),
    ]
    """Filters results by signature algorithm."""

    tld: SequenceNotStr[str]
    """Filters results by top-level domain.

    Incompatible with the `log`, `logApi`, `logOperator`, and `entryType`
    filters/dimensions.
    """

    unique_entries: Annotated[List[Literal["true", "false"]], PropertyInfo(alias="uniqueEntries")]
    """Specifies whether to filter out duplicate certificates and pre-certificates.

    Set to true for unique entries only.
    """

    validation_level: Annotated[
        List[Literal["DOMAIN", "ORGANIZATION", "EXTENDED"]], PropertyInfo(alias="validationLevel")
    ]
    """Filters results by validation level."""
