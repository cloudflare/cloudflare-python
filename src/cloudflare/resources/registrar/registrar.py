# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .domains import Domains, AsyncDomains

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
from .domains import (
    Domains,
    AsyncDomains,
    DomainsWithRawResponse,
    AsyncDomainsWithRawResponse,
    DomainsWithStreamingResponse,
    AsyncDomainsWithStreamingResponse,
)
from ..._wrappers import ResultWrapper

__all__ = ["Registrar", "AsyncRegistrar"]


class Registrar(SyncAPIResource):
    @cached_property
    def domains(self) -> Domains:
        return Domains(self._client)

    @cached_property
    def with_raw_response(self) -> RegistrarWithRawResponse:
        return RegistrarWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegistrarWithStreamingResponse:
        return RegistrarWithStreamingResponse(self)


class AsyncRegistrar(AsyncAPIResource):
    @cached_property
    def domains(self) -> AsyncDomains:
        return AsyncDomains(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRegistrarWithRawResponse:
        return AsyncRegistrarWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegistrarWithStreamingResponse:
        return AsyncRegistrarWithStreamingResponse(self)


class RegistrarWithRawResponse:
    def __init__(self, registrar: Registrar) -> None:
        self._registrar = registrar

    @cached_property
    def domains(self) -> DomainsWithRawResponse:
        return DomainsWithRawResponse(self._registrar.domains)


class AsyncRegistrarWithRawResponse:
    def __init__(self, registrar: AsyncRegistrar) -> None:
        self._registrar = registrar

    @cached_property
    def domains(self) -> AsyncDomainsWithRawResponse:
        return AsyncDomainsWithRawResponse(self._registrar.domains)


class RegistrarWithStreamingResponse:
    def __init__(self, registrar: Registrar) -> None:
        self._registrar = registrar

    @cached_property
    def domains(self) -> DomainsWithStreamingResponse:
        return DomainsWithStreamingResponse(self._registrar.domains)


class AsyncRegistrarWithStreamingResponse:
    def __init__(self, registrar: AsyncRegistrar) -> None:
        self._registrar = registrar

    @cached_property
    def domains(self) -> AsyncDomainsWithStreamingResponse:
        return AsyncDomainsWithStreamingResponse(self._registrar.domains)
