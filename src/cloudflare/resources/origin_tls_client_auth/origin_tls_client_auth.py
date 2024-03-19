# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Optional, cast

import httpx

from ...types import (
    OriginTLSClientAuthGetResponse,
    OriginTLSClientAuthListResponse,
    OriginTLSClientAuthCreateResponse,
    OriginTLSClientAuthDeleteResponse,
    origin_tls_client_auth_create_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .settings import (
    Settings,
    AsyncSettings,
    SettingsWithRawResponse,
    AsyncSettingsWithRawResponse,
    SettingsWithStreamingResponse,
    AsyncSettingsWithStreamingResponse,
)
from ..._compat import cached_property
from .hostnames import (
    Hostnames,
    AsyncHostnames,
    HostnamesWithRawResponse,
    AsyncHostnamesWithRawResponse,
    HostnamesWithStreamingResponse,
    AsyncHostnamesWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from .hostnames.hostnames import Hostnames, AsyncHostnames

__all__ = ["OriginTLSClientAuth", "AsyncOriginTLSClientAuth"]


class OriginTLSClientAuth(SyncAPIResource):
    @cached_property
    def hostnames(self) -> Hostnames:
        return Hostnames(self._client)

    @cached_property
    def settings(self) -> Settings:
        return Settings(self._client)

    @cached_property
    def with_raw_response(self) -> OriginTLSClientAuthWithRawResponse:
        return OriginTLSClientAuthWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OriginTLSClientAuthWithStreamingResponse:
        return OriginTLSClientAuthWithStreamingResponse(self)

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
    ) -> OriginTLSClientAuthCreateResponse:
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
        return cast(
            OriginTLSClientAuthCreateResponse,
            self._post(
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
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[OriginTLSClientAuthCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
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
    ) -> Optional[OriginTLSClientAuthListResponse]:
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
        return self._get(
            f"/zones/{zone_id}/origin_tls_client_auth",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginTLSClientAuthListResponse]], ResultWrapper[OriginTLSClientAuthListResponse]
            ),
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
    ) -> OriginTLSClientAuthDeleteResponse:
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
        return cast(
            OriginTLSClientAuthDeleteResponse,
            self._delete(
                f"/zones/{zone_id}/origin_tls_client_auth/{certificate_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[OriginTLSClientAuthDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
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
    ) -> OriginTLSClientAuthGetResponse:
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
        return cast(
            OriginTLSClientAuthGetResponse,
            self._get(
                f"/zones/{zone_id}/origin_tls_client_auth/{certificate_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[OriginTLSClientAuthGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncOriginTLSClientAuth(AsyncAPIResource):
    @cached_property
    def hostnames(self) -> AsyncHostnames:
        return AsyncHostnames(self._client)

    @cached_property
    def settings(self) -> AsyncSettings:
        return AsyncSettings(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOriginTLSClientAuthWithRawResponse:
        return AsyncOriginTLSClientAuthWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOriginTLSClientAuthWithStreamingResponse:
        return AsyncOriginTLSClientAuthWithStreamingResponse(self)

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
    ) -> OriginTLSClientAuthCreateResponse:
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
        return cast(
            OriginTLSClientAuthCreateResponse,
            await self._post(
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
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[OriginTLSClientAuthCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OriginTLSClientAuthListResponse]:
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
        return await self._get(
            f"/zones/{zone_id}/origin_tls_client_auth",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginTLSClientAuthListResponse]], ResultWrapper[OriginTLSClientAuthListResponse]
            ),
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
    ) -> OriginTLSClientAuthDeleteResponse:
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
        return cast(
            OriginTLSClientAuthDeleteResponse,
            await self._delete(
                f"/zones/{zone_id}/origin_tls_client_auth/{certificate_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[OriginTLSClientAuthDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
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
    ) -> OriginTLSClientAuthGetResponse:
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
        return cast(
            OriginTLSClientAuthGetResponse,
            await self._get(
                f"/zones/{zone_id}/origin_tls_client_auth/{certificate_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[OriginTLSClientAuthGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class OriginTLSClientAuthWithRawResponse:
    def __init__(self, origin_tls_client_auth: OriginTLSClientAuth) -> None:
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
    def hostnames(self) -> HostnamesWithRawResponse:
        return HostnamesWithRawResponse(self._origin_tls_client_auth.hostnames)

    @cached_property
    def settings(self) -> SettingsWithRawResponse:
        return SettingsWithRawResponse(self._origin_tls_client_auth.settings)


class AsyncOriginTLSClientAuthWithRawResponse:
    def __init__(self, origin_tls_client_auth: AsyncOriginTLSClientAuth) -> None:
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
    def hostnames(self) -> AsyncHostnamesWithRawResponse:
        return AsyncHostnamesWithRawResponse(self._origin_tls_client_auth.hostnames)

    @cached_property
    def settings(self) -> AsyncSettingsWithRawResponse:
        return AsyncSettingsWithRawResponse(self._origin_tls_client_auth.settings)


class OriginTLSClientAuthWithStreamingResponse:
    def __init__(self, origin_tls_client_auth: OriginTLSClientAuth) -> None:
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
    def hostnames(self) -> HostnamesWithStreamingResponse:
        return HostnamesWithStreamingResponse(self._origin_tls_client_auth.hostnames)

    @cached_property
    def settings(self) -> SettingsWithStreamingResponse:
        return SettingsWithStreamingResponse(self._origin_tls_client_auth.settings)


class AsyncOriginTLSClientAuthWithStreamingResponse:
    def __init__(self, origin_tls_client_auth: AsyncOriginTLSClientAuth) -> None:
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
    def hostnames(self) -> AsyncHostnamesWithStreamingResponse:
        return AsyncHostnamesWithStreamingResponse(self._origin_tls_client_auth.hostnames)

    @cached_property
    def settings(self) -> AsyncSettingsWithStreamingResponse:
        return AsyncSettingsWithStreamingResponse(self._origin_tls_client_auth.settings)
