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
    Certificates,
    AsyncCertificates,
    CertificatesWithRawResponse,
    AsyncCertificatesWithRawResponse,
    CertificatesWithStreamingResponse,
    AsyncCertificatesWithStreamingResponse,
)
from ...._base_client import (
    make_request_options,
)
from ....types.origin_tls_client_auth import (
    HostnameUpdateResponse,
    TLSCertificatesAndHostnamesHostnameCertidObject,
    hostname_update_params,
)

__all__ = ["Hostnames", "AsyncHostnames"]


class Hostnames(SyncAPIResource):
    @cached_property
    def certificates(self) -> Certificates:
        return Certificates(self._client)

    @cached_property
    def with_raw_response(self) -> HostnamesWithRawResponse:
        return HostnamesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HostnamesWithStreamingResponse:
        return HostnamesWithStreamingResponse(self)

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
                post_parser=ResultWrapper._unwrapper,
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
    ) -> TLSCertificatesAndHostnamesHostnameCertidObject:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[TLSCertificatesAndHostnamesHostnameCertidObject],
                ResultWrapper[TLSCertificatesAndHostnamesHostnameCertidObject],
            ),
        )


class AsyncHostnames(AsyncAPIResource):
    @cached_property
    def certificates(self) -> AsyncCertificates:
        return AsyncCertificates(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHostnamesWithRawResponse:
        return AsyncHostnamesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHostnamesWithStreamingResponse:
        return AsyncHostnamesWithStreamingResponse(self)

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
                post_parser=ResultWrapper._unwrapper,
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
    ) -> TLSCertificatesAndHostnamesHostnameCertidObject:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[TLSCertificatesAndHostnamesHostnameCertidObject],
                ResultWrapper[TLSCertificatesAndHostnamesHostnameCertidObject],
            ),
        )


class HostnamesWithRawResponse:
    def __init__(self, hostnames: Hostnames) -> None:
        self._hostnames = hostnames

        self.update = to_raw_response_wrapper(
            hostnames.update,
        )
        self.get = to_raw_response_wrapper(
            hostnames.get,
        )

    @cached_property
    def certificates(self) -> CertificatesWithRawResponse:
        return CertificatesWithRawResponse(self._hostnames.certificates)


class AsyncHostnamesWithRawResponse:
    def __init__(self, hostnames: AsyncHostnames) -> None:
        self._hostnames = hostnames

        self.update = async_to_raw_response_wrapper(
            hostnames.update,
        )
        self.get = async_to_raw_response_wrapper(
            hostnames.get,
        )

    @cached_property
    def certificates(self) -> AsyncCertificatesWithRawResponse:
        return AsyncCertificatesWithRawResponse(self._hostnames.certificates)


class HostnamesWithStreamingResponse:
    def __init__(self, hostnames: Hostnames) -> None:
        self._hostnames = hostnames

        self.update = to_streamed_response_wrapper(
            hostnames.update,
        )
        self.get = to_streamed_response_wrapper(
            hostnames.get,
        )

    @cached_property
    def certificates(self) -> CertificatesWithStreamingResponse:
        return CertificatesWithStreamingResponse(self._hostnames.certificates)


class AsyncHostnamesWithStreamingResponse:
    def __init__(self, hostnames: AsyncHostnames) -> None:
        self._hostnames = hostnames

        self.update = async_to_streamed_response_wrapper(
            hostnames.update,
        )
        self.get = async_to_streamed_response_wrapper(
            hostnames.get,
        )

    @cached_property
    def certificates(self) -> AsyncCertificatesWithStreamingResponse:
        return AsyncCertificatesWithStreamingResponse(self._hostnames.certificates)
