# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CtSummaryParams"]


class CtSummaryParams(TypedDict, total=False):
    ca: List[str]
    """Filters results by certificate authority."""

    ca_owner: Annotated[List[str], PropertyInfo(alias="caOwner")]
    """Filters results by certificate authority owner."""

    date_end: Annotated[List[Union[str, datetime]], PropertyInfo(alias="dateEnd", format="iso8601")]
    """End of the date range (inclusive)."""

    date_range: Annotated[List[str], PropertyInfo(alias="dateRange")]
    """Filters results by date range.

    For example, use `7d` and `7dcontrol` to compare this week with the previous
    week. Use this parameter or set specific start and end dates (`dateStart` and
    `dateEnd` parameters).
    """

    date_start: Annotated[List[Union[str, datetime]], PropertyInfo(alias="dateStart", format="iso8601")]
    """Start of the date range."""

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
    """Filters results by entry type (certificate vs. pre-certificate)."""

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
    an "other" category.
    """

    log: List[str]
    """Filters results by certificate log."""

    log_api: Annotated[List[Literal["RFC6962", "STATIC"]], PropertyInfo(alias="logApi")]
    """Filters results by certificate log API (RFC6962 vs. static)."""

    log_operator: Annotated[List[str], PropertyInfo(alias="logOperator")]
    """Filters results by certificate log operator."""

    name: List[str]
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

    tld: List[str]
    """Filters results by top-level domain."""

    unique_entries: Annotated[List[Literal["true", "false"]], PropertyInfo(alias="uniqueEntries")]
    """Specifies whether to filter out duplicate certificates and pre-certificates.

    Set to true for unique entries only.
    """

    validation_level: Annotated[
        List[Literal["DOMAIN", "ORGANIZATION", "EXTENDED"]], PropertyInfo(alias="validationLevel")
    ]
    """Filters results by validation level."""
