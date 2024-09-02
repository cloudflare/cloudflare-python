# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .domains import DomainsResource, AsyncDomainsResource

from ..._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from .domains import (
    DomainsResource,
    AsyncDomainsResource,
    DomainsResourceWithRawResponse,
    AsyncDomainsResourceWithRawResponse,
    DomainsResourceWithStreamingResponse,
    AsyncDomainsResourceWithStreamingResponse,
)

__all__ = ["RegistrarResource", "AsyncRegistrarResource"]


class RegistrarResource(SyncAPIResource):
    @cached_property
    def domains(self) -> DomainsResource:
        return DomainsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RegistrarResourceWithRawResponse:
        return RegistrarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegistrarResourceWithStreamingResponse:
        return RegistrarResourceWithStreamingResponse(self)


class AsyncRegistrarResource(AsyncAPIResource):
    @cached_property
    def domains(self) -> AsyncDomainsResource:
        return AsyncDomainsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRegistrarResourceWithRawResponse:
        return AsyncRegistrarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegistrarResourceWithStreamingResponse:
        return AsyncRegistrarResourceWithStreamingResponse(self)


class RegistrarResourceWithRawResponse:
    def __init__(self, registrar: RegistrarResource) -> None:
        self._registrar = registrar

    @cached_property
    def domains(self) -> DomainsResourceWithRawResponse:
        return DomainsResourceWithRawResponse(self._registrar.domains)


class AsyncRegistrarResourceWithRawResponse:
    def __init__(self, registrar: AsyncRegistrarResource) -> None:
        self._registrar = registrar

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithRawResponse:
        return AsyncDomainsResourceWithRawResponse(self._registrar.domains)


class RegistrarResourceWithStreamingResponse:
    def __init__(self, registrar: RegistrarResource) -> None:
        self._registrar = registrar

    @cached_property
    def domains(self) -> DomainsResourceWithStreamingResponse:
        return DomainsResourceWithStreamingResponse(self._registrar.domains)


class AsyncRegistrarResourceWithStreamingResponse:
    def __init__(self, registrar: AsyncRegistrarResource) -> None:
        self._registrar = registrar

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithStreamingResponse:
        return AsyncDomainsResourceWithStreamingResponse(self._registrar.domains)
