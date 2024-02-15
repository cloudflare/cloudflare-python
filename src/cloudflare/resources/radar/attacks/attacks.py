# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .layer3 import (
    Layer3,
    AsyncLayer3,
    Layer3WithRawResponse,
    AsyncLayer3WithRawResponse,
    Layer3WithStreamingResponse,
    AsyncLayer3WithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .layer3.layer3 import Layer3, AsyncLayer3

__all__ = ["Attacks", "AsyncAttacks"]


class Attacks(SyncAPIResource):
    @cached_property
    def layer3(self) -> Layer3:
        return Layer3(self._client)

    @cached_property
    def with_raw_response(self) -> AttacksWithRawResponse:
        return AttacksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AttacksWithStreamingResponse:
        return AttacksWithStreamingResponse(self)


class AsyncAttacks(AsyncAPIResource):
    @cached_property
    def layer3(self) -> AsyncLayer3:
        return AsyncLayer3(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAttacksWithRawResponse:
        return AsyncAttacksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAttacksWithStreamingResponse:
        return AsyncAttacksWithStreamingResponse(self)


class AttacksWithRawResponse:
    def __init__(self, attacks: Attacks) -> None:
        self._attacks = attacks

    @cached_property
    def layer3(self) -> Layer3WithRawResponse:
        return Layer3WithRawResponse(self._attacks.layer3)


class AsyncAttacksWithRawResponse:
    def __init__(self, attacks: AsyncAttacks) -> None:
        self._attacks = attacks

    @cached_property
    def layer3(self) -> AsyncLayer3WithRawResponse:
        return AsyncLayer3WithRawResponse(self._attacks.layer3)


class AttacksWithStreamingResponse:
    def __init__(self, attacks: Attacks) -> None:
        self._attacks = attacks

    @cached_property
    def layer3(self) -> Layer3WithStreamingResponse:
        return Layer3WithStreamingResponse(self._attacks.layer3)


class AsyncAttacksWithStreamingResponse:
    def __init__(self, attacks: AsyncAttacks) -> None:
        self._attacks = attacks

    @cached_property
    def layer3(self) -> AsyncLayer3WithStreamingResponse:
        return AsyncLayer3WithStreamingResponse(self._attacks.layer3)
