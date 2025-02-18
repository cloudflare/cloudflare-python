# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.hostnames.settings import tls_update_params
from ....types.hostnames.settings.setting import Setting
from ....types.hostnames.settings.tls_get_response import TLSGetResponse
from ....types.hostnames.settings.setting_value_param import SettingValueParam
from ....types.hostnames.settings.tls_delete_response import TLSDeleteResponse

__all__ = ["TLSResource", "AsyncTLSResource"]


class TLSResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TLSResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TLSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TLSResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TLSResourceWithStreamingResponse(self)

    def update(
        self,
        hostname: str,
        *,
        zone_id: str,
        setting_id: Literal["ciphers", "min_tls_version", "http2"],
        value: SettingValueParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Setting]:
        """
        Update the tls setting value for the hostname.

        Args:
          zone_id: Identifier

          setting_id: The TLS Setting name.

          hostname: The hostname for which the tls settings are set.

          value: The tls setting value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not setting_id:
            raise ValueError(f"Expected a non-empty value for `setting_id` but received {setting_id!r}")
        if not hostname:
            raise ValueError(f"Expected a non-empty value for `hostname` but received {hostname!r}")
        return self._put(
            f"/zones/{zone_id}/hostnames/settings/{setting_id}/{hostname}",
            body=maybe_transform({"value": value}, tls_update_params.TLSUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Setting]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Setting]], ResultWrapper[Setting]),
        )

    def delete(
        self,
        hostname: str,
        *,
        zone_id: str,
        setting_id: Literal["ciphers", "min_tls_version", "http2"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TLSDeleteResponse]:
        """
        Delete the tls setting value for the hostname.

        Args:
          zone_id: Identifier

          setting_id: The TLS Setting name.

          hostname: The hostname for which the tls settings are set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not setting_id:
            raise ValueError(f"Expected a non-empty value for `setting_id` but received {setting_id!r}")
        if not hostname:
            raise ValueError(f"Expected a non-empty value for `hostname` but received {hostname!r}")
        return self._delete(
            f"/zones/{zone_id}/hostnames/settings/{setting_id}/{hostname}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TLSDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TLSDeleteResponse]], ResultWrapper[TLSDeleteResponse]),
        )

    def get(
        self,
        setting_id: Literal["ciphers", "min_tls_version", "http2"],
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[TLSGetResponse]:
        """
        List the requested TLS setting for the hostnames under this zone.

        Args:
          zone_id: Identifier

          setting_id: The TLS Setting name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not setting_id:
            raise ValueError(f"Expected a non-empty value for `setting_id` but received {setting_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/hostnames/settings/{setting_id}",
            page=SyncSinglePage[TLSGetResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=TLSGetResponse,
        )


class AsyncTLSResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTLSResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTLSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTLSResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTLSResourceWithStreamingResponse(self)

    async def update(
        self,
        hostname: str,
        *,
        zone_id: str,
        setting_id: Literal["ciphers", "min_tls_version", "http2"],
        value: SettingValueParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Setting]:
        """
        Update the tls setting value for the hostname.

        Args:
          zone_id: Identifier

          setting_id: The TLS Setting name.

          hostname: The hostname for which the tls settings are set.

          value: The tls setting value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not setting_id:
            raise ValueError(f"Expected a non-empty value for `setting_id` but received {setting_id!r}")
        if not hostname:
            raise ValueError(f"Expected a non-empty value for `hostname` but received {hostname!r}")
        return await self._put(
            f"/zones/{zone_id}/hostnames/settings/{setting_id}/{hostname}",
            body=await async_maybe_transform({"value": value}, tls_update_params.TLSUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Setting]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Setting]], ResultWrapper[Setting]),
        )

    async def delete(
        self,
        hostname: str,
        *,
        zone_id: str,
        setting_id: Literal["ciphers", "min_tls_version", "http2"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TLSDeleteResponse]:
        """
        Delete the tls setting value for the hostname.

        Args:
          zone_id: Identifier

          setting_id: The TLS Setting name.

          hostname: The hostname for which the tls settings are set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not setting_id:
            raise ValueError(f"Expected a non-empty value for `setting_id` but received {setting_id!r}")
        if not hostname:
            raise ValueError(f"Expected a non-empty value for `hostname` but received {hostname!r}")
        return await self._delete(
            f"/zones/{zone_id}/hostnames/settings/{setting_id}/{hostname}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TLSDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TLSDeleteResponse]], ResultWrapper[TLSDeleteResponse]),
        )

    def get(
        self,
        setting_id: Literal["ciphers", "min_tls_version", "http2"],
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[TLSGetResponse, AsyncSinglePage[TLSGetResponse]]:
        """
        List the requested TLS setting for the hostnames under this zone.

        Args:
          zone_id: Identifier

          setting_id: The TLS Setting name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not setting_id:
            raise ValueError(f"Expected a non-empty value for `setting_id` but received {setting_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/hostnames/settings/{setting_id}",
            page=AsyncSinglePage[TLSGetResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=TLSGetResponse,
        )


class TLSResourceWithRawResponse:
    def __init__(self, tls: TLSResource) -> None:
        self._tls = tls

        self.update = to_raw_response_wrapper(
            tls.update,
        )
        self.delete = to_raw_response_wrapper(
            tls.delete,
        )
        self.get = to_raw_response_wrapper(
            tls.get,
        )


class AsyncTLSResourceWithRawResponse:
    def __init__(self, tls: AsyncTLSResource) -> None:
        self._tls = tls

        self.update = async_to_raw_response_wrapper(
            tls.update,
        )
        self.delete = async_to_raw_response_wrapper(
            tls.delete,
        )
        self.get = async_to_raw_response_wrapper(
            tls.get,
        )


class TLSResourceWithStreamingResponse:
    def __init__(self, tls: TLSResource) -> None:
        self._tls = tls

        self.update = to_streamed_response_wrapper(
            tls.update,
        )
        self.delete = to_streamed_response_wrapper(
            tls.delete,
        )
        self.get = to_streamed_response_wrapper(
            tls.get,
        )


class AsyncTLSResourceWithStreamingResponse:
    def __init__(self, tls: AsyncTLSResource) -> None:
        self._tls = tls

        self.update = async_to_streamed_response_wrapper(
            tls.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            tls.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            tls.get,
        )
