# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .hostnames.hostnames import HostnamesResource, AsyncHostnamesResource

from ..._compat import cached_property

from .settings import SettingsResource, AsyncSettingsResource

from ...types.origin_tls_client_auth.zone_authenticated_origin_pull import ZoneAuthenticatedOriginPull

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from ..._base_client import make_request_options, AsyncPaginator

from ...pagination import SyncSinglePage, AsyncSinglePage

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
from ...types.origin_tls_client_auth import origin_tls_client_auth_create_params
from .hostnames import (
    HostnamesResource,
    AsyncHostnamesResource,
    HostnamesResourceWithRawResponse,
    AsyncHostnamesResourceWithRawResponse,
    HostnamesResourceWithStreamingResponse,
    AsyncHostnamesResourceWithStreamingResponse,
)
from .settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

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
        return OriginTLSClientAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OriginTLSClientAuthResourceWithStreamingResponse:
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
    ) -> Optional[ZoneAuthenticatedOriginPull]:
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
                post_parser=ResultWrapper[Optional[ZoneAuthenticatedOriginPull]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneAuthenticatedOriginPull]], ResultWrapper[ZoneAuthenticatedOriginPull]),
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
    ) -> SyncSinglePage[ZoneAuthenticatedOriginPull]:
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
            page=SyncSinglePage[ZoneAuthenticatedOriginPull],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ZoneAuthenticatedOriginPull,
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
    ) -> Optional[ZoneAuthenticatedOriginPull]:
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
                post_parser=ResultWrapper[Optional[ZoneAuthenticatedOriginPull]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneAuthenticatedOriginPull]], ResultWrapper[ZoneAuthenticatedOriginPull]),
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
    ) -> Optional[ZoneAuthenticatedOriginPull]:
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
                post_parser=ResultWrapper[Optional[ZoneAuthenticatedOriginPull]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneAuthenticatedOriginPull]], ResultWrapper[ZoneAuthenticatedOriginPull]),
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
        return AsyncOriginTLSClientAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOriginTLSClientAuthResourceWithStreamingResponse:
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
    ) -> Optional[ZoneAuthenticatedOriginPull]:
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
                post_parser=ResultWrapper[Optional[ZoneAuthenticatedOriginPull]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneAuthenticatedOriginPull]], ResultWrapper[ZoneAuthenticatedOriginPull]),
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
    ) -> AsyncPaginator[ZoneAuthenticatedOriginPull, AsyncSinglePage[ZoneAuthenticatedOriginPull]]:
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
            page=AsyncSinglePage[ZoneAuthenticatedOriginPull],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ZoneAuthenticatedOriginPull,
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
    ) -> Optional[ZoneAuthenticatedOriginPull]:
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
                post_parser=ResultWrapper[Optional[ZoneAuthenticatedOriginPull]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneAuthenticatedOriginPull]], ResultWrapper[ZoneAuthenticatedOriginPull]),
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
    ) -> Optional[ZoneAuthenticatedOriginPull]:
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
                post_parser=ResultWrapper[Optional[ZoneAuthenticatedOriginPull]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneAuthenticatedOriginPull]], ResultWrapper[ZoneAuthenticatedOriginPull]),
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
