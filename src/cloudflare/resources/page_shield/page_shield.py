# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .policies import PoliciesResource, AsyncPoliciesResource

from ..._compat import cached_property

from .connections import ConnectionsResource, AsyncConnectionsResource

from .scripts import ScriptsResource, AsyncScriptsResource

from .cookies import CookiesResource, AsyncCookiesResource

from ...types.page_shield.page_shield_update_response import PageShieldUpdateResponse

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from ..._base_client import make_request_options

from ...types.page_shield.setting import Setting

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
from ...types import shared_params
from ...types.page_shield import page_shield_update_params
from .policies import (
    PoliciesResource,
    AsyncPoliciesResource,
    PoliciesResourceWithRawResponse,
    AsyncPoliciesResourceWithRawResponse,
    PoliciesResourceWithStreamingResponse,
    AsyncPoliciesResourceWithStreamingResponse,
)
from .connections import (
    ConnectionsResource,
    AsyncConnectionsResource,
    ConnectionsResourceWithRawResponse,
    AsyncConnectionsResourceWithRawResponse,
    ConnectionsResourceWithStreamingResponse,
    AsyncConnectionsResourceWithStreamingResponse,
)
from .scripts import (
    ScriptsResource,
    AsyncScriptsResource,
    ScriptsResourceWithRawResponse,
    AsyncScriptsResourceWithRawResponse,
    ScriptsResourceWithStreamingResponse,
    AsyncScriptsResourceWithStreamingResponse,
)
from .cookies import (
    CookiesResource,
    AsyncCookiesResource,
    CookiesResourceWithRawResponse,
    AsyncCookiesResourceWithRawResponse,
    CookiesResourceWithStreamingResponse,
    AsyncCookiesResourceWithStreamingResponse,
)
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["PageShieldResource", "AsyncPageShieldResource"]


class PageShieldResource(SyncAPIResource):
    @cached_property
    def policies(self) -> PoliciesResource:
        return PoliciesResource(self._client)

    @cached_property
    def connections(self) -> ConnectionsResource:
        return ConnectionsResource(self._client)

    @cached_property
    def scripts(self) -> ScriptsResource:
        return ScriptsResource(self._client)

    @cached_property
    def cookies(self) -> CookiesResource:
        return CookiesResource(self._client)

    @cached_property
    def with_raw_response(self) -> PageShieldResourceWithRawResponse:
        return PageShieldResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PageShieldResourceWithStreamingResponse:
        return PageShieldResourceWithStreamingResponse(self)

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
    ) -> Optional[PageShieldUpdateResponse]:
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
                post_parser=ResultWrapper[Optional[PageShieldUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PageShieldUpdateResponse]], ResultWrapper[PageShieldUpdateResponse]),
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
    ) -> Optional[Setting]:
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
                post_parser=ResultWrapper[Optional[Setting]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Setting]], ResultWrapper[Setting]),
        )


class AsyncPageShieldResource(AsyncAPIResource):
    @cached_property
    def policies(self) -> AsyncPoliciesResource:
        return AsyncPoliciesResource(self._client)

    @cached_property
    def connections(self) -> AsyncConnectionsResource:
        return AsyncConnectionsResource(self._client)

    @cached_property
    def scripts(self) -> AsyncScriptsResource:
        return AsyncScriptsResource(self._client)

    @cached_property
    def cookies(self) -> AsyncCookiesResource:
        return AsyncCookiesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPageShieldResourceWithRawResponse:
        return AsyncPageShieldResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPageShieldResourceWithStreamingResponse:
        return AsyncPageShieldResourceWithStreamingResponse(self)

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
    ) -> Optional[PageShieldUpdateResponse]:
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
                post_parser=ResultWrapper[Optional[PageShieldUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PageShieldUpdateResponse]], ResultWrapper[PageShieldUpdateResponse]),
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
    ) -> Optional[Setting]:
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
                post_parser=ResultWrapper[Optional[Setting]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Setting]], ResultWrapper[Setting]),
        )


class PageShieldResourceWithRawResponse:
    def __init__(self, page_shield: PageShieldResource) -> None:
        self._page_shield = page_shield

        self.update = to_raw_response_wrapper(
            page_shield.update,
        )
        self.get = to_raw_response_wrapper(
            page_shield.get,
        )

    @cached_property
    def policies(self) -> PoliciesResourceWithRawResponse:
        return PoliciesResourceWithRawResponse(self._page_shield.policies)

    @cached_property
    def connections(self) -> ConnectionsResourceWithRawResponse:
        return ConnectionsResourceWithRawResponse(self._page_shield.connections)

    @cached_property
    def scripts(self) -> ScriptsResourceWithRawResponse:
        return ScriptsResourceWithRawResponse(self._page_shield.scripts)

    @cached_property
    def cookies(self) -> CookiesResourceWithRawResponse:
        return CookiesResourceWithRawResponse(self._page_shield.cookies)


class AsyncPageShieldResourceWithRawResponse:
    def __init__(self, page_shield: AsyncPageShieldResource) -> None:
        self._page_shield = page_shield

        self.update = async_to_raw_response_wrapper(
            page_shield.update,
        )
        self.get = async_to_raw_response_wrapper(
            page_shield.get,
        )

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithRawResponse:
        return AsyncPoliciesResourceWithRawResponse(self._page_shield.policies)

    @cached_property
    def connections(self) -> AsyncConnectionsResourceWithRawResponse:
        return AsyncConnectionsResourceWithRawResponse(self._page_shield.connections)

    @cached_property
    def scripts(self) -> AsyncScriptsResourceWithRawResponse:
        return AsyncScriptsResourceWithRawResponse(self._page_shield.scripts)

    @cached_property
    def cookies(self) -> AsyncCookiesResourceWithRawResponse:
        return AsyncCookiesResourceWithRawResponse(self._page_shield.cookies)


class PageShieldResourceWithStreamingResponse:
    def __init__(self, page_shield: PageShieldResource) -> None:
        self._page_shield = page_shield

        self.update = to_streamed_response_wrapper(
            page_shield.update,
        )
        self.get = to_streamed_response_wrapper(
            page_shield.get,
        )

    @cached_property
    def policies(self) -> PoliciesResourceWithStreamingResponse:
        return PoliciesResourceWithStreamingResponse(self._page_shield.policies)

    @cached_property
    def connections(self) -> ConnectionsResourceWithStreamingResponse:
        return ConnectionsResourceWithStreamingResponse(self._page_shield.connections)

    @cached_property
    def scripts(self) -> ScriptsResourceWithStreamingResponse:
        return ScriptsResourceWithStreamingResponse(self._page_shield.scripts)

    @cached_property
    def cookies(self) -> CookiesResourceWithStreamingResponse:
        return CookiesResourceWithStreamingResponse(self._page_shield.cookies)


class AsyncPageShieldResourceWithStreamingResponse:
    def __init__(self, page_shield: AsyncPageShieldResource) -> None:
        self._page_shield = page_shield

        self.update = async_to_streamed_response_wrapper(
            page_shield.update,
        )
        self.get = async_to_streamed_response_wrapper(
            page_shield.get,
        )

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithStreamingResponse:
        return AsyncPoliciesResourceWithStreamingResponse(self._page_shield.policies)

    @cached_property
    def connections(self) -> AsyncConnectionsResourceWithStreamingResponse:
        return AsyncConnectionsResourceWithStreamingResponse(self._page_shield.connections)

    @cached_property
    def scripts(self) -> AsyncScriptsResourceWithStreamingResponse:
        return AsyncScriptsResourceWithStreamingResponse(self._page_shield.scripts)

    @cached_property
    def cookies(self) -> AsyncCookiesResourceWithStreamingResponse:
        return AsyncCookiesResourceWithStreamingResponse(self._page_shield.cookies)
