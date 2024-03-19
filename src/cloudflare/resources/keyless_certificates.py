# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ..types import (
    KeylessCertificateListResponse,
    TLSCertificatesAndHostnamesBase,
    KeylessCertificateDeleteResponse,
    keyless_certificate_edit_params,
    keyless_certificate_create_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import ResultWrapper
from .._base_client import (
    make_request_options,
)

__all__ = ["KeylessCertificates", "AsyncKeylessCertificates"]


class KeylessCertificates(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KeylessCertificatesWithRawResponse:
        return KeylessCertificatesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeylessCertificatesWithStreamingResponse:
        return KeylessCertificatesWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        certificate: str,
        host: str,
        port: float,
        bundle_method: Literal["ubiquitous", "optimal", "force"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        tunnel: keyless_certificate_create_params.Tunnel | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TLSCertificatesAndHostnamesBase:
        """
        Create Keyless SSL Configuration

        Args:
          zone_id: Identifier

          certificate: The zone's SSL certificate or SSL certificate and intermediate(s).

          host: The keyless SSL name.

          port: The keyless SSL port used to communicate between Cloudflare and the client's
              Keyless SSL server.

          bundle_method: A ubiquitous bundle has the highest probability of being verified everywhere,
              even by clients using outdated or unusual trust stores. An optimal bundle uses
              the shortest chain and newest intermediates. And the force bundle verifies the
              chain, but does not otherwise modify it.

          name: The keyless SSL name.

          tunnel: Configuration for using Keyless SSL through a Cloudflare Tunnel

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/keyless_certificates",
            body=maybe_transform(
                {
                    "certificate": certificate,
                    "host": host,
                    "port": port,
                    "bundle_method": bundle_method,
                    "name": name,
                    "tunnel": tunnel,
                },
                keyless_certificate_create_params.KeylessCertificateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TLSCertificatesAndHostnamesBase], ResultWrapper[TLSCertificatesAndHostnamesBase]),
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
    ) -> Optional[KeylessCertificateListResponse]:
        """
        List all Keyless SSL configurations for a given zone.

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
            f"/zones/{zone_id}/keyless_certificates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[KeylessCertificateListResponse]], ResultWrapper[KeylessCertificateListResponse]),
        )

    def delete(
        self,
        keyless_certificate_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeylessCertificateDeleteResponse:
        """
        Delete Keyless SSL Configuration

        Args:
          zone_id: Identifier

          keyless_certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not keyless_certificate_id:
            raise ValueError(
                f"Expected a non-empty value for `keyless_certificate_id` but received {keyless_certificate_id!r}"
            )
        return self._delete(
            f"/zones/{zone_id}/keyless_certificates/{keyless_certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[KeylessCertificateDeleteResponse], ResultWrapper[KeylessCertificateDeleteResponse]),
        )

    def edit(
        self,
        keyless_certificate_id: str,
        *,
        zone_id: str,
        enabled: bool | NotGiven = NOT_GIVEN,
        host: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        port: float | NotGiven = NOT_GIVEN,
        tunnel: keyless_certificate_edit_params.Tunnel | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TLSCertificatesAndHostnamesBase:
        """This will update attributes of a Keyless SSL.

        Consists of one or more of the
        following: host,name,port.

        Args:
          zone_id: Identifier

          keyless_certificate_id: Identifier

          enabled: Whether or not the Keyless SSL is on or off.

          host: The keyless SSL name.

          name: The keyless SSL name.

          port: The keyless SSL port used to communicate between Cloudflare and the client's
              Keyless SSL server.

          tunnel: Configuration for using Keyless SSL through a Cloudflare Tunnel

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not keyless_certificate_id:
            raise ValueError(
                f"Expected a non-empty value for `keyless_certificate_id` but received {keyless_certificate_id!r}"
            )
        return self._patch(
            f"/zones/{zone_id}/keyless_certificates/{keyless_certificate_id}",
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "host": host,
                    "name": name,
                    "port": port,
                    "tunnel": tunnel,
                },
                keyless_certificate_edit_params.KeylessCertificateEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TLSCertificatesAndHostnamesBase], ResultWrapper[TLSCertificatesAndHostnamesBase]),
        )

    def get(
        self,
        keyless_certificate_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TLSCertificatesAndHostnamesBase:
        """
        Get details for one Keyless SSL configuration.

        Args:
          zone_id: Identifier

          keyless_certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not keyless_certificate_id:
            raise ValueError(
                f"Expected a non-empty value for `keyless_certificate_id` but received {keyless_certificate_id!r}"
            )
        return self._get(
            f"/zones/{zone_id}/keyless_certificates/{keyless_certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TLSCertificatesAndHostnamesBase], ResultWrapper[TLSCertificatesAndHostnamesBase]),
        )


class AsyncKeylessCertificates(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKeylessCertificatesWithRawResponse:
        return AsyncKeylessCertificatesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeylessCertificatesWithStreamingResponse:
        return AsyncKeylessCertificatesWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        certificate: str,
        host: str,
        port: float,
        bundle_method: Literal["ubiquitous", "optimal", "force"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        tunnel: keyless_certificate_create_params.Tunnel | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TLSCertificatesAndHostnamesBase:
        """
        Create Keyless SSL Configuration

        Args:
          zone_id: Identifier

          certificate: The zone's SSL certificate or SSL certificate and intermediate(s).

          host: The keyless SSL name.

          port: The keyless SSL port used to communicate between Cloudflare and the client's
              Keyless SSL server.

          bundle_method: A ubiquitous bundle has the highest probability of being verified everywhere,
              even by clients using outdated or unusual trust stores. An optimal bundle uses
              the shortest chain and newest intermediates. And the force bundle verifies the
              chain, but does not otherwise modify it.

          name: The keyless SSL name.

          tunnel: Configuration for using Keyless SSL through a Cloudflare Tunnel

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/keyless_certificates",
            body=await async_maybe_transform(
                {
                    "certificate": certificate,
                    "host": host,
                    "port": port,
                    "bundle_method": bundle_method,
                    "name": name,
                    "tunnel": tunnel,
                },
                keyless_certificate_create_params.KeylessCertificateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TLSCertificatesAndHostnamesBase], ResultWrapper[TLSCertificatesAndHostnamesBase]),
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
    ) -> Optional[KeylessCertificateListResponse]:
        """
        List all Keyless SSL configurations for a given zone.

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
            f"/zones/{zone_id}/keyless_certificates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[KeylessCertificateListResponse]], ResultWrapper[KeylessCertificateListResponse]),
        )

    async def delete(
        self,
        keyless_certificate_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeylessCertificateDeleteResponse:
        """
        Delete Keyless SSL Configuration

        Args:
          zone_id: Identifier

          keyless_certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not keyless_certificate_id:
            raise ValueError(
                f"Expected a non-empty value for `keyless_certificate_id` but received {keyless_certificate_id!r}"
            )
        return await self._delete(
            f"/zones/{zone_id}/keyless_certificates/{keyless_certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[KeylessCertificateDeleteResponse], ResultWrapper[KeylessCertificateDeleteResponse]),
        )

    async def edit(
        self,
        keyless_certificate_id: str,
        *,
        zone_id: str,
        enabled: bool | NotGiven = NOT_GIVEN,
        host: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        port: float | NotGiven = NOT_GIVEN,
        tunnel: keyless_certificate_edit_params.Tunnel | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TLSCertificatesAndHostnamesBase:
        """This will update attributes of a Keyless SSL.

        Consists of one or more of the
        following: host,name,port.

        Args:
          zone_id: Identifier

          keyless_certificate_id: Identifier

          enabled: Whether or not the Keyless SSL is on or off.

          host: The keyless SSL name.

          name: The keyless SSL name.

          port: The keyless SSL port used to communicate between Cloudflare and the client's
              Keyless SSL server.

          tunnel: Configuration for using Keyless SSL through a Cloudflare Tunnel

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not keyless_certificate_id:
            raise ValueError(
                f"Expected a non-empty value for `keyless_certificate_id` but received {keyless_certificate_id!r}"
            )
        return await self._patch(
            f"/zones/{zone_id}/keyless_certificates/{keyless_certificate_id}",
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "host": host,
                    "name": name,
                    "port": port,
                    "tunnel": tunnel,
                },
                keyless_certificate_edit_params.KeylessCertificateEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TLSCertificatesAndHostnamesBase], ResultWrapper[TLSCertificatesAndHostnamesBase]),
        )

    async def get(
        self,
        keyless_certificate_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TLSCertificatesAndHostnamesBase:
        """
        Get details for one Keyless SSL configuration.

        Args:
          zone_id: Identifier

          keyless_certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not keyless_certificate_id:
            raise ValueError(
                f"Expected a non-empty value for `keyless_certificate_id` but received {keyless_certificate_id!r}"
            )
        return await self._get(
            f"/zones/{zone_id}/keyless_certificates/{keyless_certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TLSCertificatesAndHostnamesBase], ResultWrapper[TLSCertificatesAndHostnamesBase]),
        )


class KeylessCertificatesWithRawResponse:
    def __init__(self, keyless_certificates: KeylessCertificates) -> None:
        self._keyless_certificates = keyless_certificates

        self.create = to_raw_response_wrapper(
            keyless_certificates.create,
        )
        self.list = to_raw_response_wrapper(
            keyless_certificates.list,
        )
        self.delete = to_raw_response_wrapper(
            keyless_certificates.delete,
        )
        self.edit = to_raw_response_wrapper(
            keyless_certificates.edit,
        )
        self.get = to_raw_response_wrapper(
            keyless_certificates.get,
        )


class AsyncKeylessCertificatesWithRawResponse:
    def __init__(self, keyless_certificates: AsyncKeylessCertificates) -> None:
        self._keyless_certificates = keyless_certificates

        self.create = async_to_raw_response_wrapper(
            keyless_certificates.create,
        )
        self.list = async_to_raw_response_wrapper(
            keyless_certificates.list,
        )
        self.delete = async_to_raw_response_wrapper(
            keyless_certificates.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            keyless_certificates.edit,
        )
        self.get = async_to_raw_response_wrapper(
            keyless_certificates.get,
        )


class KeylessCertificatesWithStreamingResponse:
    def __init__(self, keyless_certificates: KeylessCertificates) -> None:
        self._keyless_certificates = keyless_certificates

        self.create = to_streamed_response_wrapper(
            keyless_certificates.create,
        )
        self.list = to_streamed_response_wrapper(
            keyless_certificates.list,
        )
        self.delete = to_streamed_response_wrapper(
            keyless_certificates.delete,
        )
        self.edit = to_streamed_response_wrapper(
            keyless_certificates.edit,
        )
        self.get = to_streamed_response_wrapper(
            keyless_certificates.get,
        )


class AsyncKeylessCertificatesWithStreamingResponse:
    def __init__(self, keyless_certificates: AsyncKeylessCertificates) -> None:
        self._keyless_certificates = keyless_certificates

        self.create = async_to_streamed_response_wrapper(
            keyless_certificates.create,
        )
        self.list = async_to_streamed_response_wrapper(
            keyless_certificates.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            keyless_certificates.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            keyless_certificates.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            keyless_certificates.get,
        )
