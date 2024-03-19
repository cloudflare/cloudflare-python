# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...types import PageShieldGetZoneSettings, PageShieldUpdateZoneSettings, page_shield_update_params
from .scripts import (
    Scripts,
    AsyncScripts,
    ScriptsWithRawResponse,
    AsyncScriptsWithRawResponse,
    ScriptsWithStreamingResponse,
    AsyncScriptsWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .policies import (
    Policies,
    AsyncPolicies,
    PoliciesWithRawResponse,
    AsyncPoliciesWithRawResponse,
    PoliciesWithStreamingResponse,
    AsyncPoliciesWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from .connections import (
    Connections,
    AsyncConnections,
    ConnectionsWithRawResponse,
    AsyncConnectionsWithRawResponse,
    ConnectionsWithStreamingResponse,
    AsyncConnectionsWithStreamingResponse,
)
from ..._base_client import (
    make_request_options,
)

__all__ = ["PageShield", "AsyncPageShield"]


class PageShield(SyncAPIResource):
    @cached_property
    def policies(self) -> Policies:
        return Policies(self._client)

    @cached_property
    def connections(self) -> Connections:
        return Connections(self._client)

    @cached_property
    def scripts(self) -> Scripts:
        return Scripts(self._client)

    @cached_property
    def with_raw_response(self) -> PageShieldWithRawResponse:
        return PageShieldWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PageShieldWithStreamingResponse:
        return PageShieldWithStreamingResponse(self)

    def update(
        self,
        *,
        zone_id: str,
        enabled: bool | NotGiven = NOT_GIVEN,
        use_cloudflare_reporting_endpoint: bool | NotGiven = NOT_GIVEN,
        use_connection_url_path: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageShieldUpdateZoneSettings:
        """
        Updates Page Shield settings.

        Args:
          zone_id: Identifier

          enabled: When true, indicates that Page Shield is enabled.

          use_cloudflare_reporting_endpoint: When true, CSP reports will be sent to
              https://csp-reporting.cloudflare.com/cdn-cgi/script_monitor/report

          use_connection_url_path: When true, the paths associated with connections URLs will also be analyzed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            f"/zones/{zone_id}/page_shield",
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "use_cloudflare_reporting_endpoint": use_cloudflare_reporting_endpoint,
                    "use_connection_url_path": use_connection_url_path,
                },
                page_shield_update_params.PageShieldUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PageShieldUpdateZoneSettings], ResultWrapper[PageShieldUpdateZoneSettings]),
        )

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageShieldGetZoneSettings:
        """
        Fetches the Page Shield settings.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/page_shield",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PageShieldGetZoneSettings], ResultWrapper[PageShieldGetZoneSettings]),
        )


class AsyncPageShield(AsyncAPIResource):
    @cached_property
    def policies(self) -> AsyncPolicies:
        return AsyncPolicies(self._client)

    @cached_property
    def connections(self) -> AsyncConnections:
        return AsyncConnections(self._client)

    @cached_property
    def scripts(self) -> AsyncScripts:
        return AsyncScripts(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPageShieldWithRawResponse:
        return AsyncPageShieldWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPageShieldWithStreamingResponse:
        return AsyncPageShieldWithStreamingResponse(self)

    async def update(
        self,
        *,
        zone_id: str,
        enabled: bool | NotGiven = NOT_GIVEN,
        use_cloudflare_reporting_endpoint: bool | NotGiven = NOT_GIVEN,
        use_connection_url_path: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageShieldUpdateZoneSettings:
        """
        Updates Page Shield settings.

        Args:
          zone_id: Identifier

          enabled: When true, indicates that Page Shield is enabled.

          use_cloudflare_reporting_endpoint: When true, CSP reports will be sent to
              https://csp-reporting.cloudflare.com/cdn-cgi/script_monitor/report

          use_connection_url_path: When true, the paths associated with connections URLs will also be analyzed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            f"/zones/{zone_id}/page_shield",
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "use_cloudflare_reporting_endpoint": use_cloudflare_reporting_endpoint,
                    "use_connection_url_path": use_connection_url_path,
                },
                page_shield_update_params.PageShieldUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PageShieldUpdateZoneSettings], ResultWrapper[PageShieldUpdateZoneSettings]),
        )

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageShieldGetZoneSettings:
        """
        Fetches the Page Shield settings.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/page_shield",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PageShieldGetZoneSettings], ResultWrapper[PageShieldGetZoneSettings]),
        )


class PageShieldWithRawResponse:
    def __init__(self, page_shield: PageShield) -> None:
        self._page_shield = page_shield

        self.update = to_raw_response_wrapper(
            page_shield.update,
        )
        self.get = to_raw_response_wrapper(
            page_shield.get,
        )

    @cached_property
    def policies(self) -> PoliciesWithRawResponse:
        return PoliciesWithRawResponse(self._page_shield.policies)

    @cached_property
    def connections(self) -> ConnectionsWithRawResponse:
        return ConnectionsWithRawResponse(self._page_shield.connections)

    @cached_property
    def scripts(self) -> ScriptsWithRawResponse:
        return ScriptsWithRawResponse(self._page_shield.scripts)


class AsyncPageShieldWithRawResponse:
    def __init__(self, page_shield: AsyncPageShield) -> None:
        self._page_shield = page_shield

        self.update = async_to_raw_response_wrapper(
            page_shield.update,
        )
        self.get = async_to_raw_response_wrapper(
            page_shield.get,
        )

    @cached_property
    def policies(self) -> AsyncPoliciesWithRawResponse:
        return AsyncPoliciesWithRawResponse(self._page_shield.policies)

    @cached_property
    def connections(self) -> AsyncConnectionsWithRawResponse:
        return AsyncConnectionsWithRawResponse(self._page_shield.connections)

    @cached_property
    def scripts(self) -> AsyncScriptsWithRawResponse:
        return AsyncScriptsWithRawResponse(self._page_shield.scripts)


class PageShieldWithStreamingResponse:
    def __init__(self, page_shield: PageShield) -> None:
        self._page_shield = page_shield

        self.update = to_streamed_response_wrapper(
            page_shield.update,
        )
        self.get = to_streamed_response_wrapper(
            page_shield.get,
        )

    @cached_property
    def policies(self) -> PoliciesWithStreamingResponse:
        return PoliciesWithStreamingResponse(self._page_shield.policies)

    @cached_property
    def connections(self) -> ConnectionsWithStreamingResponse:
        return ConnectionsWithStreamingResponse(self._page_shield.connections)

    @cached_property
    def scripts(self) -> ScriptsWithStreamingResponse:
        return ScriptsWithStreamingResponse(self._page_shield.scripts)


class AsyncPageShieldWithStreamingResponse:
    def __init__(self, page_shield: AsyncPageShield) -> None:
        self._page_shield = page_shield

        self.update = async_to_streamed_response_wrapper(
            page_shield.update,
        )
        self.get = async_to_streamed_response_wrapper(
            page_shield.get,
        )

    @cached_property
    def policies(self) -> AsyncPoliciesWithStreamingResponse:
        return AsyncPoliciesWithStreamingResponse(self._page_shield.policies)

    @cached_property
    def connections(self) -> AsyncConnectionsWithStreamingResponse:
        return AsyncConnectionsWithStreamingResponse(self._page_shield.connections)

    @cached_property
    def scripts(self) -> AsyncScriptsWithStreamingResponse:
        return AsyncScriptsWithStreamingResponse(self._page_shield.scripts)
