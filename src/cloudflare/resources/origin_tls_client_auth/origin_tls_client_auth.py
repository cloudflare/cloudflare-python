# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
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
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from .hostnames.hostnames import (
    HostnamesResource,
    AsyncHostnamesResource,
    HostnamesResourceWithRawResponse,
    AsyncHostnamesResourceWithRawResponse,
    HostnamesResourceWithStreamingResponse,
    AsyncHostnamesResourceWithStreamingResponse,
)
from ...types.origin_tls_client_auth import origin_tls_client_auth_create_params
from ...types.origin_tls_client_auth.origin_tls_client_auth_get_response import OriginTLSClientAuthGetResponse
from ...types.origin_tls_client_auth.origin_tls_client_auth_list_response import OriginTLSClientAuthListResponse
from ...types.origin_tls_client_auth.origin_tls_client_auth_create_response import OriginTLSClientAuthCreateResponse
from ...types.origin_tls_client_auth.origin_tls_client_auth_delete_response import OriginTLSClientAuthDeleteResponse

__all__ = ["OriginTLSClientAuthResource", "AsyncOriginTLSClientAuthResource"]


class OriginTLSClientAuthResource(SyncAPIResource):
    @cached_property
    def hostnames(self) -> HostnamesResource:
        return HostnamesResource(self._client)

    @cached_property
    def settings(self) -> SettingsResource:
        return SettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> OriginTLSClientAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return OriginTLSClientAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OriginTLSClientAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return OriginTLSClientAuthResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        certificate: str,
        private_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OriginTLSClientAuthCreateResponse]:
        """
        Upload your own certificate you want Cloudflare to use for edge-to-origin
        communication to override the shared certificate. Please note that it is
        important to keep only one certificate active. Also, make sure to enable
        zone-level authenticated origin pulls by making a PUT call to settings endpoint
        to see the uploaded certificate in use.

        Args:
          zone_id: Identifier

          certificate: The zone's leaf certificate.

          private_key: The zone's private key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/origin_tls_client_auth",
            body=maybe_transform(
                {
                    "certificate": certificate,
                    "private_key": private_key,
                },
                origin_tls_client_auth_create_params.OriginTLSClientAuthCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginTLSClientAuthCreateResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginTLSClientAuthCreateResponse]], ResultWrapper[OriginTLSClientAuthCreateResponse]
            ),
        )

    def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[OriginTLSClientAuthListResponse]:
        """
        List Certificates

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/origin_tls_client_auth",
            page=SyncSinglePage[OriginTLSClientAuthListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=OriginTLSClientAuthListResponse,
        )

    def delete(
        self,
        certificate_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OriginTLSClientAuthDeleteResponse]:
        """
        Delete Certificate

        Args:
          zone_id: Identifier

          certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not certificate_id:
            raise ValueError(f"Expected a non-empty value for `certificate_id` but received {certificate_id!r}")
        return self._delete(
            f"/zones/{zone_id}/origin_tls_client_auth/{certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginTLSClientAuthDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginTLSClientAuthDeleteResponse]], ResultWrapper[OriginTLSClientAuthDeleteResponse]
            ),
        )

    def get(
        self,
        certificate_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OriginTLSClientAuthGetResponse]:
        """
        Get Certificate Details

        Args:
          zone_id: Identifier

          certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not certificate_id:
            raise ValueError(f"Expected a non-empty value for `certificate_id` but received {certificate_id!r}")
        return self._get(
            f"/zones/{zone_id}/origin_tls_client_auth/{certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginTLSClientAuthGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OriginTLSClientAuthGetResponse]], ResultWrapper[OriginTLSClientAuthGetResponse]),
        )


class AsyncOriginTLSClientAuthResource(AsyncAPIResource):
    @cached_property
    def hostnames(self) -> AsyncHostnamesResource:
        return AsyncHostnamesResource(self._client)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        return AsyncSettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOriginTLSClientAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOriginTLSClientAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOriginTLSClientAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncOriginTLSClientAuthResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        certificate: str,
        private_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OriginTLSClientAuthCreateResponse]:
        """
        Upload your own certificate you want Cloudflare to use for edge-to-origin
        communication to override the shared certificate. Please note that it is
        important to keep only one certificate active. Also, make sure to enable
        zone-level authenticated origin pulls by making a PUT call to settings endpoint
        to see the uploaded certificate in use.

        Args:
          zone_id: Identifier

          certificate: The zone's leaf certificate.

          private_key: The zone's private key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/origin_tls_client_auth",
            body=await async_maybe_transform(
                {
                    "certificate": certificate,
                    "private_key": private_key,
                },
                origin_tls_client_auth_create_params.OriginTLSClientAuthCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginTLSClientAuthCreateResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginTLSClientAuthCreateResponse]], ResultWrapper[OriginTLSClientAuthCreateResponse]
            ),
        )

    def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[OriginTLSClientAuthListResponse, AsyncSinglePage[OriginTLSClientAuthListResponse]]:
        """
        List Certificates

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/origin_tls_client_auth",
            page=AsyncSinglePage[OriginTLSClientAuthListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=OriginTLSClientAuthListResponse,
        )

    async def delete(
        self,
        certificate_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OriginTLSClientAuthDeleteResponse]:
        """
        Delete Certificate

        Args:
          zone_id: Identifier

          certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not certificate_id:
            raise ValueError(f"Expected a non-empty value for `certificate_id` but received {certificate_id!r}")
        return await self._delete(
            f"/zones/{zone_id}/origin_tls_client_auth/{certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginTLSClientAuthDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginTLSClientAuthDeleteResponse]], ResultWrapper[OriginTLSClientAuthDeleteResponse]
            ),
        )

    async def get(
        self,
        certificate_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OriginTLSClientAuthGetResponse]:
        """
        Get Certificate Details

        Args:
          zone_id: Identifier

          certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not certificate_id:
            raise ValueError(f"Expected a non-empty value for `certificate_id` but received {certificate_id!r}")
        return await self._get(
            f"/zones/{zone_id}/origin_tls_client_auth/{certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginTLSClientAuthGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OriginTLSClientAuthGetResponse]], ResultWrapper[OriginTLSClientAuthGetResponse]),
        )


class OriginTLSClientAuthResourceWithRawResponse:
    def __init__(self, origin_tls_client_auth: OriginTLSClientAuthResource) -> None:
        self._origin_tls_client_auth = origin_tls_client_auth

        self.create = to_raw_response_wrapper(
            origin_tls_client_auth.create,
        )
        self.list = to_raw_response_wrapper(
            origin_tls_client_auth.list,
        )
        self.delete = to_raw_response_wrapper(
            origin_tls_client_auth.delete,
        )
        self.get = to_raw_response_wrapper(
            origin_tls_client_auth.get,
        )

    @cached_property
    def hostnames(self) -> HostnamesResourceWithRawResponse:
        return HostnamesResourceWithRawResponse(self._origin_tls_client_auth.hostnames)

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._origin_tls_client_auth.settings)


class AsyncOriginTLSClientAuthResourceWithRawResponse:
    def __init__(self, origin_tls_client_auth: AsyncOriginTLSClientAuthResource) -> None:
        self._origin_tls_client_auth = origin_tls_client_auth

        self.create = async_to_raw_response_wrapper(
            origin_tls_client_auth.create,
        )
        self.list = async_to_raw_response_wrapper(
            origin_tls_client_auth.list,
        )
        self.delete = async_to_raw_response_wrapper(
            origin_tls_client_auth.delete,
        )
        self.get = async_to_raw_response_wrapper(
            origin_tls_client_auth.get,
        )

    @cached_property
    def hostnames(self) -> AsyncHostnamesResourceWithRawResponse:
        return AsyncHostnamesResourceWithRawResponse(self._origin_tls_client_auth.hostnames)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._origin_tls_client_auth.settings)


class OriginTLSClientAuthResourceWithStreamingResponse:
    def __init__(self, origin_tls_client_auth: OriginTLSClientAuthResource) -> None:
        self._origin_tls_client_auth = origin_tls_client_auth

        self.create = to_streamed_response_wrapper(
            origin_tls_client_auth.create,
        )
        self.list = to_streamed_response_wrapper(
            origin_tls_client_auth.list,
        )
        self.delete = to_streamed_response_wrapper(
            origin_tls_client_auth.delete,
        )
        self.get = to_streamed_response_wrapper(
            origin_tls_client_auth.get,
        )

    @cached_property
    def hostnames(self) -> HostnamesResourceWithStreamingResponse:
        return HostnamesResourceWithStreamingResponse(self._origin_tls_client_auth.hostnames)

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._origin_tls_client_auth.settings)


class AsyncOriginTLSClientAuthResourceWithStreamingResponse:
    def __init__(self, origin_tls_client_auth: AsyncOriginTLSClientAuthResource) -> None:
        self._origin_tls_client_auth = origin_tls_client_auth

        self.create = async_to_streamed_response_wrapper(
            origin_tls_client_auth.create,
        )
        self.list = async_to_streamed_response_wrapper(
            origin_tls_client_auth.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            origin_tls_client_auth.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            origin_tls_client_auth.get,
        )

    @cached_property
    def hostnames(self) -> AsyncHostnamesResourceWithStreamingResponse:
        return AsyncHostnamesResourceWithStreamingResponse(self._origin_tls_client_auth.hostnames)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._origin_tls_client_auth.settings)
