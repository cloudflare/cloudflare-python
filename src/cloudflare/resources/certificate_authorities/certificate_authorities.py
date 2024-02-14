# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .hostname_associations import HostnameAssociations, AsyncHostnameAssociations

from ..._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from .hostname_associations import (
    HostnameAssociations,
    AsyncHostnameAssociations,
    HostnameAssociationsWithRawResponse,
    AsyncHostnameAssociationsWithRawResponse,
    HostnameAssociationsWithStreamingResponse,
    AsyncHostnameAssociationsWithStreamingResponse,
)
from ..._wrappers import ResultWrapper

__all__ = ["CertificateAuthorities", "AsyncCertificateAuthorities"]


class CertificateAuthorities(SyncAPIResource):
    @cached_property
    def hostname_associations(self) -> HostnameAssociations:
        return HostnameAssociations(self._client)

    @cached_property
    def with_raw_response(self) -> CertificateAuthoritiesWithRawResponse:
        return CertificateAuthoritiesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CertificateAuthoritiesWithStreamingResponse:
        return CertificateAuthoritiesWithStreamingResponse(self)


class AsyncCertificateAuthorities(AsyncAPIResource):
    @cached_property
    def hostname_associations(self) -> AsyncHostnameAssociations:
        return AsyncHostnameAssociations(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCertificateAuthoritiesWithRawResponse:
        return AsyncCertificateAuthoritiesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCertificateAuthoritiesWithStreamingResponse:
        return AsyncCertificateAuthoritiesWithStreamingResponse(self)


class CertificateAuthoritiesWithRawResponse:
    def __init__(self, certificate_authorities: CertificateAuthorities) -> None:
        self._certificate_authorities = certificate_authorities

    @cached_property
    def hostname_associations(self) -> HostnameAssociationsWithRawResponse:
        return HostnameAssociationsWithRawResponse(self._certificate_authorities.hostname_associations)


class AsyncCertificateAuthoritiesWithRawResponse:
    def __init__(self, certificate_authorities: AsyncCertificateAuthorities) -> None:
        self._certificate_authorities = certificate_authorities

    @cached_property
    def hostname_associations(self) -> AsyncHostnameAssociationsWithRawResponse:
        return AsyncHostnameAssociationsWithRawResponse(self._certificate_authorities.hostname_associations)


class CertificateAuthoritiesWithStreamingResponse:
    def __init__(self, certificate_authorities: CertificateAuthorities) -> None:
        self._certificate_authorities = certificate_authorities

    @cached_property
    def hostname_associations(self) -> HostnameAssociationsWithStreamingResponse:
        return HostnameAssociationsWithStreamingResponse(self._certificate_authorities.hostname_associations)


class AsyncCertificateAuthoritiesWithStreamingResponse:
    def __init__(self, certificate_authorities: AsyncCertificateAuthorities) -> None:
        self._certificate_authorities = certificate_authorities

    @cached_property
    def hostname_associations(self) -> AsyncHostnameAssociationsWithStreamingResponse:
        return AsyncHostnameAssociationsWithStreamingResponse(self._certificate_authorities.hostname_associations)
