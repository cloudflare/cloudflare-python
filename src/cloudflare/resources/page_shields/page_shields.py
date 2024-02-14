# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .connections import Connections, AsyncConnections

from ..._compat import cached_property

from .scripts import Scripts, AsyncScripts

from ...types import PageShieldListResponse, PageShieldPageShieldUpdatePageShieldSettingsResponse

from typing import Type

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

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
from ...types import page_shield_page_shield_update_page_shield_settings_params
from .connections import (
    Connections,
    AsyncConnections,
    ConnectionsWithRawResponse,
    AsyncConnectionsWithRawResponse,
    ConnectionsWithStreamingResponse,
    AsyncConnectionsWithStreamingResponse,
)
from .scripts import (
    Scripts,
    AsyncScripts,
    ScriptsWithRawResponse,
    AsyncScriptsWithRawResponse,
    ScriptsWithStreamingResponse,
    AsyncScriptsWithStreamingResponse,
)
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["PageShields", "AsyncPageShields"]


class PageShields(SyncAPIResource):
    @cached_property
    def connections(self) -> Connections:
        return Connections(self._client)

    @cached_property
    def scripts(self) -> Scripts:
        return Scripts(self._client)

    @cached_property
    def with_raw_response(self) -> PageShieldsWithRawResponse:
        return PageShieldsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PageShieldsWithStreamingResponse:
        return PageShieldsWithStreamingResponse(self)

    def list(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageShieldListResponse:
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
            cast_to=cast(Type[PageShieldListResponse], ResultWrapper[PageShieldListResponse]),
        )

    def page_shield_update_page_shield_settings(
        self,
        zone_id: str,
        *,
        enabled: bool | NotGiven = NOT_GIVEN,
        use_cloudflare_reporting_endpoint: bool | NotGiven = NOT_GIVEN,
        use_connection_url_path: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageShieldPageShieldUpdatePageShieldSettingsResponse:
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
                page_shield_page_shield_update_page_shield_settings_params.PageShieldPageShieldUpdatePageShieldSettingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[PageShieldPageShieldUpdatePageShieldSettingsResponse],
                ResultWrapper[PageShieldPageShieldUpdatePageShieldSettingsResponse],
            ),
        )


class AsyncPageShields(AsyncAPIResource):
    @cached_property
    def connections(self) -> AsyncConnections:
        return AsyncConnections(self._client)

    @cached_property
    def scripts(self) -> AsyncScripts:
        return AsyncScripts(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPageShieldsWithRawResponse:
        return AsyncPageShieldsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPageShieldsWithStreamingResponse:
        return AsyncPageShieldsWithStreamingResponse(self)

    async def list(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageShieldListResponse:
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
            cast_to=cast(Type[PageShieldListResponse], ResultWrapper[PageShieldListResponse]),
        )

    async def page_shield_update_page_shield_settings(
        self,
        zone_id: str,
        *,
        enabled: bool | NotGiven = NOT_GIVEN,
        use_cloudflare_reporting_endpoint: bool | NotGiven = NOT_GIVEN,
        use_connection_url_path: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageShieldPageShieldUpdatePageShieldSettingsResponse:
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
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "use_cloudflare_reporting_endpoint": use_cloudflare_reporting_endpoint,
                    "use_connection_url_path": use_connection_url_path,
                },
                page_shield_page_shield_update_page_shield_settings_params.PageShieldPageShieldUpdatePageShieldSettingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[PageShieldPageShieldUpdatePageShieldSettingsResponse],
                ResultWrapper[PageShieldPageShieldUpdatePageShieldSettingsResponse],
            ),
        )


class PageShieldsWithRawResponse:
    def __init__(self, page_shields: PageShields) -> None:
        self._page_shields = page_shields

        self.list = to_raw_response_wrapper(
            page_shields.list,
        )
        self.page_shield_update_page_shield_settings = to_raw_response_wrapper(
            page_shields.page_shield_update_page_shield_settings,
        )

    @cached_property
    def connections(self) -> ConnectionsWithRawResponse:
        return ConnectionsWithRawResponse(self._page_shields.connections)

    @cached_property
    def scripts(self) -> ScriptsWithRawResponse:
        return ScriptsWithRawResponse(self._page_shields.scripts)


class AsyncPageShieldsWithRawResponse:
    def __init__(self, page_shields: AsyncPageShields) -> None:
        self._page_shields = page_shields

        self.list = async_to_raw_response_wrapper(
            page_shields.list,
        )
        self.page_shield_update_page_shield_settings = async_to_raw_response_wrapper(
            page_shields.page_shield_update_page_shield_settings,
        )

    @cached_property
    def connections(self) -> AsyncConnectionsWithRawResponse:
        return AsyncConnectionsWithRawResponse(self._page_shields.connections)

    @cached_property
    def scripts(self) -> AsyncScriptsWithRawResponse:
        return AsyncScriptsWithRawResponse(self._page_shields.scripts)


class PageShieldsWithStreamingResponse:
    def __init__(self, page_shields: PageShields) -> None:
        self._page_shields = page_shields

        self.list = to_streamed_response_wrapper(
            page_shields.list,
        )
        self.page_shield_update_page_shield_settings = to_streamed_response_wrapper(
            page_shields.page_shield_update_page_shield_settings,
        )

    @cached_property
    def connections(self) -> ConnectionsWithStreamingResponse:
        return ConnectionsWithStreamingResponse(self._page_shields.connections)

    @cached_property
    def scripts(self) -> ScriptsWithStreamingResponse:
        return ScriptsWithStreamingResponse(self._page_shields.scripts)


class AsyncPageShieldsWithStreamingResponse:
    def __init__(self, page_shields: AsyncPageShields) -> None:
        self._page_shields = page_shields

        self.list = async_to_streamed_response_wrapper(
            page_shields.list,
        )
        self.page_shield_update_page_shield_settings = async_to_streamed_response_wrapper(
            page_shields.page_shield_update_page_shield_settings,
        )

    @cached_property
    def connections(self) -> AsyncConnectionsWithStreamingResponse:
        return AsyncConnectionsWithStreamingResponse(self._page_shields.connections)

    @cached_property
    def scripts(self) -> AsyncScriptsWithStreamingResponse:
        return AsyncScriptsWithStreamingResponse(self._page_shields.scripts)
