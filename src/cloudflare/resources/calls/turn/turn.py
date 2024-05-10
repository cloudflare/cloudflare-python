# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .keys import (
    KeysResource,
    AsyncKeysResource,
    KeysResourceWithRawResponse,
    AsyncKeysResourceWithRawResponse,
    KeysResourceWithStreamingResponse,
    AsyncKeysResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["TurnResource", "AsyncTurnResource"]


class TurnResource(SyncAPIResource):
    @cached_property
    def keys(self) -> KeysResource:
        return KeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> TurnResourceWithRawResponse:
        return TurnResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TurnResourceWithStreamingResponse:
        return TurnResourceWithStreamingResponse(self)


class AsyncTurnResource(AsyncAPIResource):
    @cached_property
    def keys(self) -> AsyncKeysResource:
        return AsyncKeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTurnResourceWithRawResponse:
        return AsyncTurnResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTurnResourceWithStreamingResponse:
        return AsyncTurnResourceWithStreamingResponse(self)


class TurnResourceWithRawResponse:
    def __init__(self, turn: TurnResource) -> None:
        self._turn = turn

    @cached_property
    def keys(self) -> KeysResourceWithRawResponse:
        return KeysResourceWithRawResponse(self._turn.keys)


class AsyncTurnResourceWithRawResponse:
    def __init__(self, turn: AsyncTurnResource) -> None:
        self._turn = turn

    @cached_property
    def keys(self) -> AsyncKeysResourceWithRawResponse:
        return AsyncKeysResourceWithRawResponse(self._turn.keys)


class TurnResourceWithStreamingResponse:
    def __init__(self, turn: TurnResource) -> None:
        self._turn = turn

    @cached_property
    def keys(self) -> KeysResourceWithStreamingResponse:
        return KeysResourceWithStreamingResponse(self._turn.keys)


class AsyncTurnResourceWithStreamingResponse:
    def __init__(self, turn: AsyncTurnResource) -> None:
        self._turn = turn

    @cached_property
    def keys(self) -> AsyncKeysResourceWithStreamingResponse:
        return AsyncKeysResourceWithStreamingResponse(self._turn.keys)
