# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .prefixes.prefixes import Prefixes, AsyncPrefixes

from ..._compat import cached_property

from .services import Services, AsyncServices

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
from .prefixes import (
    Prefixes,
    AsyncPrefixes,
    PrefixesWithRawResponse,
    AsyncPrefixesWithRawResponse,
    PrefixesWithStreamingResponse,
    AsyncPrefixesWithStreamingResponse,
)
from .services import (
    Services,
    AsyncServices,
    ServicesWithRawResponse,
    AsyncServicesWithRawResponse,
    ServicesWithStreamingResponse,
    AsyncServicesWithStreamingResponse,
)
from ..._wrappers import ResultWrapper

__all__ = ["Addressing", "AsyncAddressing"]


class Addressing(SyncAPIResource):
    @cached_property
    def prefixes(self) -> Prefixes:
        return Prefixes(self._client)

    @cached_property
    def services(self) -> Services:
        return Services(self._client)

    @cached_property
    def with_raw_response(self) -> AddressingWithRawResponse:
        return AddressingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AddressingWithStreamingResponse:
        return AddressingWithStreamingResponse(self)


class AsyncAddressing(AsyncAPIResource):
    @cached_property
    def prefixes(self) -> AsyncPrefixes:
        return AsyncPrefixes(self._client)

    @cached_property
    def services(self) -> AsyncServices:
        return AsyncServices(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAddressingWithRawResponse:
        return AsyncAddressingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAddressingWithStreamingResponse:
        return AsyncAddressingWithStreamingResponse(self)


class AddressingWithRawResponse:
    def __init__(self, addressing: Addressing) -> None:
        self._addressing = addressing

    @cached_property
    def prefixes(self) -> PrefixesWithRawResponse:
        return PrefixesWithRawResponse(self._addressing.prefixes)

    @cached_property
    def services(self) -> ServicesWithRawResponse:
        return ServicesWithRawResponse(self._addressing.services)


class AsyncAddressingWithRawResponse:
    def __init__(self, addressing: AsyncAddressing) -> None:
        self._addressing = addressing

    @cached_property
    def prefixes(self) -> AsyncPrefixesWithRawResponse:
        return AsyncPrefixesWithRawResponse(self._addressing.prefixes)

    @cached_property
    def services(self) -> AsyncServicesWithRawResponse:
        return AsyncServicesWithRawResponse(self._addressing.services)


class AddressingWithStreamingResponse:
    def __init__(self, addressing: Addressing) -> None:
        self._addressing = addressing

    @cached_property
    def prefixes(self) -> PrefixesWithStreamingResponse:
        return PrefixesWithStreamingResponse(self._addressing.prefixes)

    @cached_property
    def services(self) -> ServicesWithStreamingResponse:
        return ServicesWithStreamingResponse(self._addressing.services)


class AsyncAddressingWithStreamingResponse:
    def __init__(self, addressing: AsyncAddressing) -> None:
        self._addressing = addressing

    @cached_property
    def prefixes(self) -> AsyncPrefixesWithStreamingResponse:
        return AsyncPrefixesWithStreamingResponse(self._addressing.prefixes)

    @cached_property
    def services(self) -> AsyncServicesWithStreamingResponse:
        return AsyncServicesWithStreamingResponse(self._addressing.services)
