# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

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
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .prefixes.prefixes import Prefixes, AsyncPrefixes

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
