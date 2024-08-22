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
from .site_info import (
    SiteInfoResource,
    AsyncSiteInfoResource,
    SiteInfoResourceWithRawResponse,
    AsyncSiteInfoResourceWithRawResponse,
    SiteInfoResourceWithStreamingResponse,
    AsyncSiteInfoResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["RUMResource", "AsyncRUMResource"]


class RUMResource(SyncAPIResource):
    @cached_property
    def site_info(self) -> SiteInfoResource:
        return SiteInfoResource(self._client)

    @cached_property
    def rules(self) -> RulesResource:
        return RulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> RUMResourceWithRawResponse:
        return RUMResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RUMResourceWithStreamingResponse:
        return RUMResourceWithStreamingResponse(self)


class AsyncRUMResource(AsyncAPIResource):
    @cached_property
    def site_info(self) -> AsyncSiteInfoResource:
        return AsyncSiteInfoResource(self._client)

    @cached_property
    def rules(self) -> AsyncRulesResource:
        return AsyncRulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRUMResourceWithRawResponse:
        return AsyncRUMResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRUMResourceWithStreamingResponse:
        return AsyncRUMResourceWithStreamingResponse(self)


class RUMResourceWithRawResponse:
    def __init__(self, rum: RUMResource) -> None:
        self._rum = rum

    @cached_property
    def site_info(self) -> SiteInfoResourceWithRawResponse:
        return SiteInfoResourceWithRawResponse(self._rum.site_info)

    @cached_property
    def rules(self) -> RulesResourceWithRawResponse:
        return RulesResourceWithRawResponse(self._rum.rules)


class AsyncRUMResourceWithRawResponse:
    def __init__(self, rum: AsyncRUMResource) -> None:
        self._rum = rum

    @cached_property
    def site_info(self) -> AsyncSiteInfoResourceWithRawResponse:
        return AsyncSiteInfoResourceWithRawResponse(self._rum.site_info)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithRawResponse:
        return AsyncRulesResourceWithRawResponse(self._rum.rules)


class RUMResourceWithStreamingResponse:
    def __init__(self, rum: RUMResource) -> None:
        self._rum = rum

    @cached_property
    def site_info(self) -> SiteInfoResourceWithStreamingResponse:
        return SiteInfoResourceWithStreamingResponse(self._rum.site_info)

    @cached_property
    def rules(self) -> RulesResourceWithStreamingResponse:
        return RulesResourceWithStreamingResponse(self._rum.rules)


class AsyncRUMResourceWithStreamingResponse:
    def __init__(self, rum: AsyncRUMResource) -> None:
        self._rum = rum

    @cached_property
    def site_info(self) -> AsyncSiteInfoResourceWithStreamingResponse:
        return AsyncSiteInfoResourceWithStreamingResponse(self._rum.site_info)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithStreamingResponse:
        return AsyncRulesResourceWithStreamingResponse(self._rum.rules)
