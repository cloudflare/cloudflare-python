# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .rules import (
    RulesResource,
    AsyncRulesResource,
    RulesResourceWithRawResponse,
    AsyncRulesResourceWithRawResponse,
    RulesResourceWithStreamingResponse,
    AsyncRulesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["MonetizationResource", "AsyncMonetizationResource"]


class MonetizationResource(SyncAPIResource):
    @cached_property
    def rules(self) -> RulesResource:
        return RulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> MonetizationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return MonetizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MonetizationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return MonetizationResourceWithStreamingResponse(self)


class AsyncMonetizationResource(AsyncAPIResource):
    @cached_property
    def rules(self) -> AsyncRulesResource:
        return AsyncRulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMonetizationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMonetizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMonetizationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncMonetizationResourceWithStreamingResponse(self)


class MonetizationResourceWithRawResponse:
    def __init__(self, monetization: MonetizationResource) -> None:
        self._monetization = monetization

    @cached_property
    def rules(self) -> RulesResourceWithRawResponse:
        return RulesResourceWithRawResponse(self._monetization.rules)


class AsyncMonetizationResourceWithRawResponse:
    def __init__(self, monetization: AsyncMonetizationResource) -> None:
        self._monetization = monetization

    @cached_property
    def rules(self) -> AsyncRulesResourceWithRawResponse:
        return AsyncRulesResourceWithRawResponse(self._monetization.rules)


class MonetizationResourceWithStreamingResponse:
    def __init__(self, monetization: MonetizationResource) -> None:
        self._monetization = monetization

    @cached_property
    def rules(self) -> RulesResourceWithStreamingResponse:
        return RulesResourceWithStreamingResponse(self._monetization.rules)


class AsyncMonetizationResourceWithStreamingResponse:
    def __init__(self, monetization: AsyncMonetizationResource) -> None:
        self._monetization = monetization

    @cached_property
    def rules(self) -> AsyncRulesResourceWithStreamingResponse:
        return AsyncRulesResourceWithStreamingResponse(self._monetization.rules)
