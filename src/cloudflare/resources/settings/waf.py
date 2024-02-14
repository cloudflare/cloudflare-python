# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.settings import WAFUpdateResponse, WAFGetResponse

from typing import Type, Optional

from typing_extensions import Literal

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
from ...types.settings import waf_update_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["WAF", "AsyncWAF"]


class WAF(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WAFWithRawResponse:
        return WAFWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WAFWithStreamingResponse:
        return WAFWithStreamingResponse(self)

    def update(
        self,
        zone_id: str,
        *,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[WAFUpdateResponse]:
        """The WAF examines HTTP requests to your website.

        It inspects both GET and POST
        requests and applies rules to help filter out illegitimate traffic from
        legitimate website visitors. The Cloudflare WAF inspects website addresses or
        URLs to detect anything out of the ordinary. If the Cloudflare WAF determines
        suspicious user behavior, then the WAF will 'challenge' the web visitor with a
        page that asks them to submit a CAPTCHA successfully to continue their action.
        If the challenge is failed, the action will be stopped. What this means is that
        Cloudflare's WAF will block any traffic identified as illegitimate before it
        reaches your origin web server.
        (https://support.cloudflare.com/hc/en-us/articles/200172016).

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/waf",
            body=maybe_transform({"value": value}, waf_update_params.WAFUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[WAFUpdateResponse]], ResultWrapper[WAFUpdateResponse]),
        )

    def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[WAFGetResponse]:
        """The WAF examines HTTP requests to your website.

        It inspects both GET and POST
        requests and applies rules to help filter out illegitimate traffic from
        legitimate website visitors. The Cloudflare WAF inspects website addresses or
        URLs to detect anything out of the ordinary. If the Cloudflare WAF determines
        suspicious user behavior, then the WAF will 'challenge' the web visitor with a
        page that asks them to submit a CAPTCHA successfully to continue their action.
        If the challenge is failed, the action will be stopped. What this means is that
        Cloudflare's WAF will block any traffic identified as illegitimate before it
        reaches your origin web server.
        (https://support.cloudflare.com/hc/en-us/articles/200172016).

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
            f"/zones/{zone_id}/settings/waf",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[WAFGetResponse]], ResultWrapper[WAFGetResponse]),
        )


class AsyncWAF(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWAFWithRawResponse:
        return AsyncWAFWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWAFWithStreamingResponse:
        return AsyncWAFWithStreamingResponse(self)

    async def update(
        self,
        zone_id: str,
        *,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[WAFUpdateResponse]:
        """The WAF examines HTTP requests to your website.

        It inspects both GET and POST
        requests and applies rules to help filter out illegitimate traffic from
        legitimate website visitors. The Cloudflare WAF inspects website addresses or
        URLs to detect anything out of the ordinary. If the Cloudflare WAF determines
        suspicious user behavior, then the WAF will 'challenge' the web visitor with a
        page that asks them to submit a CAPTCHA successfully to continue their action.
        If the challenge is failed, the action will be stopped. What this means is that
        Cloudflare's WAF will block any traffic identified as illegitimate before it
        reaches your origin web server.
        (https://support.cloudflare.com/hc/en-us/articles/200172016).

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/waf",
            body=maybe_transform({"value": value}, waf_update_params.WAFUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[WAFUpdateResponse]], ResultWrapper[WAFUpdateResponse]),
        )

    async def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[WAFGetResponse]:
        """The WAF examines HTTP requests to your website.

        It inspects both GET and POST
        requests and applies rules to help filter out illegitimate traffic from
        legitimate website visitors. The Cloudflare WAF inspects website addresses or
        URLs to detect anything out of the ordinary. If the Cloudflare WAF determines
        suspicious user behavior, then the WAF will 'challenge' the web visitor with a
        page that asks them to submit a CAPTCHA successfully to continue their action.
        If the challenge is failed, the action will be stopped. What this means is that
        Cloudflare's WAF will block any traffic identified as illegitimate before it
        reaches your origin web server.
        (https://support.cloudflare.com/hc/en-us/articles/200172016).

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
            f"/zones/{zone_id}/settings/waf",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[WAFGetResponse]], ResultWrapper[WAFGetResponse]),
        )


class WAFWithRawResponse:
    def __init__(self, waf: WAF) -> None:
        self._waf = waf

        self.update = to_raw_response_wrapper(
            waf.update,
        )
        self.get = to_raw_response_wrapper(
            waf.get,
        )


class AsyncWAFWithRawResponse:
    def __init__(self, waf: AsyncWAF) -> None:
        self._waf = waf

        self.update = async_to_raw_response_wrapper(
            waf.update,
        )
        self.get = async_to_raw_response_wrapper(
            waf.get,
        )


class WAFWithStreamingResponse:
    def __init__(self, waf: WAF) -> None:
        self._waf = waf

        self.update = to_streamed_response_wrapper(
            waf.update,
        )
        self.get = to_streamed_response_wrapper(
            waf.get,
        )


class AsyncWAFWithStreamingResponse:
    def __init__(self, waf: AsyncWAF) -> None:
        self._waf = waf

        self.update = async_to_streamed_response_wrapper(
            waf.update,
        )
        self.get = async_to_streamed_response_wrapper(
            waf.get,
        )
