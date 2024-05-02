# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast

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
from .certificates import (
    CertificatesResource,
    AsyncCertificatesResource,
    CertificatesResourceWithRawResponse,
    AsyncCertificatesResourceWithRawResponse,
    CertificatesResourceWithStreamingResponse,
    AsyncCertificatesResourceWithStreamingResponse,
)
from ...._base_client import (
    make_request_options,
)
from ....types.origin_tls_client_auth import hostname_update_params
from ....types.origin_tls_client_auth.hostname_update_response import HostnameUpdateResponse
from ....types.origin_tls_client_auth.authenticated_origin_pull import AuthenticatedOriginPull

__all__ = ["HostnamesResource", "AsyncHostnamesResource"]


class HostnamesResource(SyncAPIResource):
    @cached_property
    def certificates(self) -> CertificatesResource:
        return CertificatesResource(self._client)

    @cached_property
    def with_raw_response(self) -> HostnamesResourceWithRawResponse:
        return HostnamesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HostnamesResourceWithStreamingResponse:
        return HostnamesResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        zone_id: str,
        config: Iterable[hostname_update_params.Config],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HostnameUpdateResponse]:
        """
        Associate a hostname to a certificate and enable, disable or invalidate the
        association. If disabled, client certificate will not be sent to the hostname
        even if activated at the zone level. 100 maximum associations on a single
        certificate are allowed. Note: Use a null value for parameter _enabled_ to
        invalidate the association.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            f"/zones/{zone_id}/origin_tls_client_auth/hostnames",
            body=maybe_transform({"config": config}, hostname_update_params.HostnameUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[HostnameUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[HostnameUpdateResponse]], ResultWrapper[HostnameUpdateResponse]),
        )

    def get(
        self,
        hostname: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AuthenticatedOriginPull]:
        """
        Get the Hostname Status for Client Authentication

        Args:
          zone_id: Identifier

          hostname: The hostname on the origin for which the client certificate uploaded will be
              used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not hostname:
            raise ValueError(f"Expected a non-empty value for `hostname` but received {hostname!r}")
        return self._get(
            f"/zones/{zone_id}/origin_tls_client_auth/hostnames/{hostname}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AuthenticatedOriginPull]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AuthenticatedOriginPull]], ResultWrapper[AuthenticatedOriginPull]),
        )


class AsyncHostnamesResource(AsyncAPIResource):
    @cached_property
    def certificates(self) -> AsyncCertificatesResource:
        return AsyncCertificatesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHostnamesResourceWithRawResponse:
        return AsyncHostnamesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHostnamesResourceWithStreamingResponse:
        return AsyncHostnamesResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        zone_id: str,
        config: Iterable[hostname_update_params.Config],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HostnameUpdateResponse]:
        """
        Associate a hostname to a certificate and enable, disable or invalidate the
        association. If disabled, client certificate will not be sent to the hostname
        even if activated at the zone level. 100 maximum associations on a single
        certificate are allowed. Note: Use a null value for parameter _enabled_ to
        invalidate the association.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            f"/zones/{zone_id}/origin_tls_client_auth/hostnames",
            body=await async_maybe_transform({"config": config}, hostname_update_params.HostnameUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[HostnameUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[HostnameUpdateResponse]], ResultWrapper[HostnameUpdateResponse]),
        )

    async def get(
        self,
        hostname: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AuthenticatedOriginPull]:
        """
        Get the Hostname Status for Client Authentication

        Args:
          zone_id: Identifier

          hostname: The hostname on the origin for which the client certificate uploaded will be
              used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not hostname:
            raise ValueError(f"Expected a non-empty value for `hostname` but received {hostname!r}")
        return await self._get(
            f"/zones/{zone_id}/origin_tls_client_auth/hostnames/{hostname}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AuthenticatedOriginPull]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AuthenticatedOriginPull]], ResultWrapper[AuthenticatedOriginPull]),
        )


class HostnamesResourceWithRawResponse:
    def __init__(self, hostnames: HostnamesResource) -> None:
        self._hostnames = hostnames

        self.update = to_raw_response_wrapper(
            hostnames.update,
        )
        self.get = to_raw_response_wrapper(
            hostnames.get,
        )

    @cached_property
    def certificates(self) -> CertificatesResourceWithRawResponse:
        return CertificatesResourceWithRawResponse(self._hostnames.certificates)


class AsyncHostnamesResourceWithRawResponse:
    def __init__(self, hostnames: AsyncHostnamesResource) -> None:
        self._hostnames = hostnames

        self.update = async_to_raw_response_wrapper(
            hostnames.update,
        )
        self.get = async_to_raw_response_wrapper(
            hostnames.get,
        )

    @cached_property
    def certificates(self) -> AsyncCertificatesResourceWithRawResponse:
        return AsyncCertificatesResourceWithRawResponse(self._hostnames.certificates)


class HostnamesResourceWithStreamingResponse:
    def __init__(self, hostnames: HostnamesResource) -> None:
        self._hostnames = hostnames

        self.update = to_streamed_response_wrapper(
            hostnames.update,
        )
        self.get = to_streamed_response_wrapper(
            hostnames.get,
        )

    @cached_property
    def certificates(self) -> CertificatesResourceWithStreamingResponse:
        return CertificatesResourceWithStreamingResponse(self._hostnames.certificates)


class AsyncHostnamesResourceWithStreamingResponse:
    def __init__(self, hostnames: AsyncHostnamesResource) -> None:
        self._hostnames = hostnames

        self.update = async_to_streamed_response_wrapper(
            hostnames.update,
        )
        self.get = async_to_streamed_response_wrapper(
            hostnames.get,
        )

    @cached_property
    def certificates(self) -> AsyncCertificatesResourceWithStreamingResponse:
        return AsyncCertificatesResourceWithStreamingResponse(self._hostnames.certificates)
