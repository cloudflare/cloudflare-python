# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

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
from ..pagination import SyncSinglePage, AsyncSinglePage
from .._base_client import AsyncPaginator, make_request_options
from ..types.custom_hostnames import BundleMethod
from ..types.keyless_certificates import keyless_certificate_edit_params, keyless_certificate_create_params
from ..types.custom_hostnames.bundle_method import BundleMethod
from ..types.keyless_certificates.tunnel_param import TunnelParam
from ..types.keyless_certificates.keyless_certificate import KeylessCertificate
from ..types.keyless_certificates.keyless_certificate_delete_response import KeylessCertificateDeleteResponse

__all__ = ["KeylessCertificatesResource", "AsyncKeylessCertificatesResource"]


class KeylessCertificatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KeylessCertificatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return KeylessCertificatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeylessCertificatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return KeylessCertificatesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        certificate: str,
        host: str,
        port: float,
        bundle_method: BundleMethod | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        tunnel: TunnelParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[KeylessCertificate]:
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
                post_parser=ResultWrapper[Optional[KeylessCertificate]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[KeylessCertificate]], ResultWrapper[KeylessCertificate]),
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
    ) -> SyncSinglePage[KeylessCertificate]:
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
        return self._get_api_list(
            f"/zones/{zone_id}/keyless_certificates",
            page=SyncSinglePage[KeylessCertificate],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=KeylessCertificate,
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
    ) -> Optional[KeylessCertificateDeleteResponse]:
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
                post_parser=ResultWrapper[Optional[KeylessCertificateDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[KeylessCertificateDeleteResponse]], ResultWrapper[KeylessCertificateDeleteResponse]
            ),
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
        tunnel: TunnelParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[KeylessCertificate]:
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
                post_parser=ResultWrapper[Optional[KeylessCertificate]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[KeylessCertificate]], ResultWrapper[KeylessCertificate]),
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
    ) -> Optional[KeylessCertificate]:
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
                post_parser=ResultWrapper[Optional[KeylessCertificate]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[KeylessCertificate]], ResultWrapper[KeylessCertificate]),
        )


class AsyncKeylessCertificatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKeylessCertificatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKeylessCertificatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeylessCertificatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncKeylessCertificatesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        certificate: str,
        host: str,
        port: float,
        bundle_method: BundleMethod | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        tunnel: TunnelParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[KeylessCertificate]:
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
                post_parser=ResultWrapper[Optional[KeylessCertificate]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[KeylessCertificate]], ResultWrapper[KeylessCertificate]),
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
    ) -> AsyncPaginator[KeylessCertificate, AsyncSinglePage[KeylessCertificate]]:
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
        return self._get_api_list(
            f"/zones/{zone_id}/keyless_certificates",
            page=AsyncSinglePage[KeylessCertificate],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=KeylessCertificate,
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
    ) -> Optional[KeylessCertificateDeleteResponse]:
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
                post_parser=ResultWrapper[Optional[KeylessCertificateDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[KeylessCertificateDeleteResponse]], ResultWrapper[KeylessCertificateDeleteResponse]
            ),
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
        tunnel: TunnelParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[KeylessCertificate]:
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
                post_parser=ResultWrapper[Optional[KeylessCertificate]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[KeylessCertificate]], ResultWrapper[KeylessCertificate]),
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
    ) -> Optional[KeylessCertificate]:
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
                post_parser=ResultWrapper[Optional[KeylessCertificate]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[KeylessCertificate]], ResultWrapper[KeylessCertificate]),
        )


class KeylessCertificatesResourceWithRawResponse:
    def __init__(self, keyless_certificates: KeylessCertificatesResource) -> None:
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


class AsyncKeylessCertificatesResourceWithRawResponse:
    def __init__(self, keyless_certificates: AsyncKeylessCertificatesResource) -> None:
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


class KeylessCertificatesResourceWithStreamingResponse:
    def __init__(self, keyless_certificates: KeylessCertificatesResource) -> None:
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


class AsyncKeylessCertificatesResourceWithStreamingResponse:
    def __init__(self, keyless_certificates: AsyncKeylessCertificatesResource) -> None:
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
