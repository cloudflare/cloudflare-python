# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Type, Optional, cast

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .hostnames import (
    HostnamesResource,
    AsyncHostnamesResource,
    HostnamesResourceWithRawResponse,
    AsyncHostnamesResourceWithRawResponse,
    HostnamesResourceWithStreamingResponse,
    AsyncHostnamesResourceWithStreamingResponse,
)
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
from .zone_certificates import (
    ZoneCertificatesResource,
    AsyncZoneCertificatesResource,
    ZoneCertificatesResourceWithRawResponse,
    AsyncZoneCertificatesResourceWithRawResponse,
    ZoneCertificatesResourceWithStreamingResponse,
    AsyncZoneCertificatesResourceWithStreamingResponse,
)
from .hostname_certificates import (
    HostnameCertificatesResource,
    AsyncHostnameCertificatesResource,
    HostnameCertificatesResourceWithRawResponse,
    AsyncHostnameCertificatesResourceWithRawResponse,
    HostnameCertificatesResourceWithStreamingResponse,
    AsyncHostnameCertificatesResourceWithStreamingResponse,
)
from ...types.origin_tls_client_auth import origin_tls_client_auth_create_params
from ...types.origin_tls_client_auth.origin_tls_client_auth_get_response import OriginTLSClientAuthGetResponse
from ...types.origin_tls_client_auth.origin_tls_client_auth_list_response import OriginTLSClientAuthListResponse
from ...types.origin_tls_client_auth.origin_tls_client_auth_create_response import OriginTLSClientAuthCreateResponse
from ...types.origin_tls_client_auth.origin_tls_client_auth_delete_response import OriginTLSClientAuthDeleteResponse

__all__ = ["OriginTLSClientAuthResource", "AsyncOriginTLSClientAuthResource"]


class OriginTLSClientAuthResource(SyncAPIResource):
    @cached_property
    def zone_certificates(self) -> ZoneCertificatesResource:
        return ZoneCertificatesResource(self._client)

    @cached_property
    def hostnames(self) -> HostnamesResource:
        return HostnamesResource(self._client)

    @cached_property
    def hostname_certificates(self) -> HostnameCertificatesResource:
        return HostnameCertificatesResource(self._client)

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

    @typing_extensions.deprecated(
        "Use zone_certificates.create for zone-level certificates. This method will be removed in a future major version."
    )
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OriginTLSClientAuthCreateResponse]:
        """
        Upload your own certificate you want Cloudflare to use for edge-to-origin
        communication to override the shared certificate. Please note that it is
        important to keep only one certificate active. Also, make sure to enable
        zone-level authenticated origin pulls by making a PUT call to settings endpoint
        to see the uploaded certificate in use.

        Args:
          zone_id: Identifier.

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

    @typing_extensions.deprecated(
        "Use zone_certificates.list for zone-level certificates. This method will be removed in a future major version."
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[OriginTLSClientAuthListResponse]:
        """
        List Certificates

        Args:
          zone_id: Identifier.

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

    @typing_extensions.deprecated(
        "Use zone_certificates.delete for zone-level certificates. This method will be removed in a future major version."
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OriginTLSClientAuthDeleteResponse]:
        """
        Delete Certificate

        Args:
          zone_id: Identifier.

          certificate_id: Identifier.

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

    @typing_extensions.deprecated(
        "Use zone_certificates.get for zone-level certificates. This method will be removed in a future major version."
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OriginTLSClientAuthGetResponse]:
        """
        Get Certificate Details

        Args:
          zone_id: Identifier.

          certificate_id: Identifier.

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
    def zone_certificates(self) -> AsyncZoneCertificatesResource:
        return AsyncZoneCertificatesResource(self._client)

    @cached_property
    def hostnames(self) -> AsyncHostnamesResource:
        return AsyncHostnamesResource(self._client)

    @cached_property
    def hostname_certificates(self) -> AsyncHostnameCertificatesResource:
        return AsyncHostnameCertificatesResource(self._client)

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

    @typing_extensions.deprecated(
        "Use zone_certificates.create for zone-level certificates. This method will be removed in a future major version."
    )
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OriginTLSClientAuthCreateResponse]:
        """
        Upload your own certificate you want Cloudflare to use for edge-to-origin
        communication to override the shared certificate. Please note that it is
        important to keep only one certificate active. Also, make sure to enable
        zone-level authenticated origin pulls by making a PUT call to settings endpoint
        to see the uploaded certificate in use.

        Args:
          zone_id: Identifier.

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

    @typing_extensions.deprecated(
        "Use zone_certificates.list for zone-level certificates. This method will be removed in a future major version."
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[OriginTLSClientAuthListResponse, AsyncSinglePage[OriginTLSClientAuthListResponse]]:
        """
        List Certificates

        Args:
          zone_id: Identifier.

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

    @typing_extensions.deprecated(
        "Use zone_certificates.delete for zone-level certificates. This method will be removed in a future major version."
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OriginTLSClientAuthDeleteResponse]:
        """
        Delete Certificate

        Args:
          zone_id: Identifier.

          certificate_id: Identifier.

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

    @typing_extensions.deprecated(
        "Use zone_certificates.get for zone-level certificates. This method will be removed in a future major version."
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OriginTLSClientAuthGetResponse]:
        """
        Get Certificate Details

        Args:
          zone_id: Identifier.

          certificate_id: Identifier.

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

        self.create = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                origin_tls_client_auth.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                origin_tls_client_auth.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                origin_tls_client_auth.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                origin_tls_client_auth.get,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def zone_certificates(self) -> ZoneCertificatesResourceWithRawResponse:
        return ZoneCertificatesResourceWithRawResponse(self._origin_tls_client_auth.zone_certificates)

    @cached_property
    def hostnames(self) -> HostnamesResourceWithRawResponse:
        return HostnamesResourceWithRawResponse(self._origin_tls_client_auth.hostnames)

    @cached_property
    def hostname_certificates(self) -> HostnameCertificatesResourceWithRawResponse:
        return HostnameCertificatesResourceWithRawResponse(self._origin_tls_client_auth.hostname_certificates)

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._origin_tls_client_auth.settings)


class AsyncOriginTLSClientAuthResourceWithRawResponse:
    def __init__(self, origin_tls_client_auth: AsyncOriginTLSClientAuthResource) -> None:
        self._origin_tls_client_auth = origin_tls_client_auth

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                origin_tls_client_auth.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                origin_tls_client_auth.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                origin_tls_client_auth.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                origin_tls_client_auth.get,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def zone_certificates(self) -> AsyncZoneCertificatesResourceWithRawResponse:
        return AsyncZoneCertificatesResourceWithRawResponse(self._origin_tls_client_auth.zone_certificates)

    @cached_property
    def hostnames(self) -> AsyncHostnamesResourceWithRawResponse:
        return AsyncHostnamesResourceWithRawResponse(self._origin_tls_client_auth.hostnames)

    @cached_property
    def hostname_certificates(self) -> AsyncHostnameCertificatesResourceWithRawResponse:
        return AsyncHostnameCertificatesResourceWithRawResponse(self._origin_tls_client_auth.hostname_certificates)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._origin_tls_client_auth.settings)


class OriginTLSClientAuthResourceWithStreamingResponse:
    def __init__(self, origin_tls_client_auth: OriginTLSClientAuthResource) -> None:
        self._origin_tls_client_auth = origin_tls_client_auth

        self.create = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                origin_tls_client_auth.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                origin_tls_client_auth.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                origin_tls_client_auth.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                origin_tls_client_auth.get,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def zone_certificates(self) -> ZoneCertificatesResourceWithStreamingResponse:
        return ZoneCertificatesResourceWithStreamingResponse(self._origin_tls_client_auth.zone_certificates)

    @cached_property
    def hostnames(self) -> HostnamesResourceWithStreamingResponse:
        return HostnamesResourceWithStreamingResponse(self._origin_tls_client_auth.hostnames)

    @cached_property
    def hostname_certificates(self) -> HostnameCertificatesResourceWithStreamingResponse:
        return HostnameCertificatesResourceWithStreamingResponse(self._origin_tls_client_auth.hostname_certificates)

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._origin_tls_client_auth.settings)


class AsyncOriginTLSClientAuthResourceWithStreamingResponse:
    def __init__(self, origin_tls_client_auth: AsyncOriginTLSClientAuthResource) -> None:
        self._origin_tls_client_auth = origin_tls_client_auth

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                origin_tls_client_auth.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                origin_tls_client_auth.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                origin_tls_client_auth.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                origin_tls_client_auth.get,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def zone_certificates(self) -> AsyncZoneCertificatesResourceWithStreamingResponse:
        return AsyncZoneCertificatesResourceWithStreamingResponse(self._origin_tls_client_auth.zone_certificates)

    @cached_property
    def hostnames(self) -> AsyncHostnamesResourceWithStreamingResponse:
        return AsyncHostnamesResourceWithStreamingResponse(self._origin_tls_client_auth.hostnames)

    @cached_property
    def hostname_certificates(self) -> AsyncHostnameCertificatesResourceWithStreamingResponse:
        return AsyncHostnameCertificatesResourceWithStreamingResponse(
            self._origin_tls_client_auth.hostname_certificates
        )

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._origin_tls_client_auth.settings)
