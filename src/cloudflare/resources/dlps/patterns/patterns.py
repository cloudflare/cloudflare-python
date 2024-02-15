# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .validates import (
    Validates,
    AsyncValidates,
    ValidatesWithRawResponse,
    AsyncValidatesWithRawResponse,
    ValidatesWithStreamingResponse,
    AsyncValidatesWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Patterns", "AsyncPatterns"]


class Patterns(SyncAPIResource):
    @cached_property
    def validates(self) -> Validates:
        return Validates(self._client)

    @cached_property
    def with_raw_response(self) -> PatternsWithRawResponse:
        return PatternsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PatternsWithStreamingResponse:
        return PatternsWithStreamingResponse(self)


class AsyncPatterns(AsyncAPIResource):
    @cached_property
    def validates(self) -> AsyncValidates:
        return AsyncValidates(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPatternsWithRawResponse:
        return AsyncPatternsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPatternsWithStreamingResponse:
        return AsyncPatternsWithStreamingResponse(self)


class PatternsWithRawResponse:
    def __init__(self, patterns: Patterns) -> None:
        self._patterns = patterns

    @cached_property
    def validates(self) -> ValidatesWithRawResponse:
        return ValidatesWithRawResponse(self._patterns.validates)


class AsyncPatternsWithRawResponse:
    def __init__(self, patterns: AsyncPatterns) -> None:
        self._patterns = patterns

    @cached_property
    def validates(self) -> AsyncValidatesWithRawResponse:
        return AsyncValidatesWithRawResponse(self._patterns.validates)


class PatternsWithStreamingResponse:
    def __init__(self, patterns: Patterns) -> None:
        self._patterns = patterns

    @cached_property
    def validates(self) -> ValidatesWithStreamingResponse:
        return ValidatesWithStreamingResponse(self._patterns.validates)


class AsyncPatternsWithStreamingResponse:
    def __init__(self, patterns: AsyncPatterns) -> None:
        self._patterns = patterns

    @cached_property
    def validates(self) -> AsyncValidatesWithStreamingResponse:
        return AsyncValidatesWithStreamingResponse(self._patterns.validates)
