# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._compat import cached_property
from .rules.rules import (
    RulesResource,
    AsyncRulesResource,
    RulesResourceWithRawResponse,
    AsyncRulesResourceWithRawResponse,
    RulesResourceWithStreamingResponse,
    AsyncRulesResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource
from .filters.filters import (
    FiltersResource,
    AsyncFiltersResource,
    FiltersResourceWithRawResponse,
    AsyncFiltersResourceWithRawResponse,
    FiltersResourceWithStreamingResponse,
    AsyncFiltersResourceWithStreamingResponse,
)

__all__ = ["SynProtectionResource", "AsyncSynProtectionResource"]


class SynProtectionResource(SyncAPIResource):
    @cached_property
    def filters(self) -> FiltersResource:
        return FiltersResource(self._client)

    @cached_property
    def rules(self) -> RulesResource:
        return RulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> SynProtectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SynProtectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SynProtectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SynProtectionResourceWithStreamingResponse(self)


class AsyncSynProtectionResource(AsyncAPIResource):
    @cached_property
    def filters(self) -> AsyncFiltersResource:
        return AsyncFiltersResource(self._client)

    @cached_property
    def rules(self) -> AsyncRulesResource:
        return AsyncRulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSynProtectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSynProtectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSynProtectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSynProtectionResourceWithStreamingResponse(self)


class SynProtectionResourceWithRawResponse:
    def __init__(self, syn_protection: SynProtectionResource) -> None:
        self._syn_protection = syn_protection

    @cached_property
    def filters(self) -> FiltersResourceWithRawResponse:
        return FiltersResourceWithRawResponse(self._syn_protection.filters)

    @cached_property
    def rules(self) -> RulesResourceWithRawResponse:
        return RulesResourceWithRawResponse(self._syn_protection.rules)


class AsyncSynProtectionResourceWithRawResponse:
    def __init__(self, syn_protection: AsyncSynProtectionResource) -> None:
        self._syn_protection = syn_protection

    @cached_property
    def filters(self) -> AsyncFiltersResourceWithRawResponse:
        return AsyncFiltersResourceWithRawResponse(self._syn_protection.filters)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithRawResponse:
        return AsyncRulesResourceWithRawResponse(self._syn_protection.rules)


class SynProtectionResourceWithStreamingResponse:
    def __init__(self, syn_protection: SynProtectionResource) -> None:
        self._syn_protection = syn_protection

    @cached_property
    def filters(self) -> FiltersResourceWithStreamingResponse:
        return FiltersResourceWithStreamingResponse(self._syn_protection.filters)

    @cached_property
    def rules(self) -> RulesResourceWithStreamingResponse:
        return RulesResourceWithStreamingResponse(self._syn_protection.rules)


class AsyncSynProtectionResourceWithStreamingResponse:
    def __init__(self, syn_protection: AsyncSynProtectionResource) -> None:
        self._syn_protection = syn_protection

    @cached_property
    def filters(self) -> AsyncFiltersResourceWithStreamingResponse:
        return AsyncFiltersResourceWithStreamingResponse(self._syn_protection.filters)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithStreamingResponse:
        return AsyncRulesResourceWithStreamingResponse(self._syn_protection.rules)
