# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.settings import TLSClientAuthUpdateResponse, TLSClientAuthGetResponse

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
from ...types.settings import tls_client_auth_update_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["TLSClientAuth", "AsyncTLSClientAuth"]


class TLSClientAuth(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TLSClientAuthWithRawResponse:
        return TLSClientAuthWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TLSClientAuthWithStreamingResponse:
        return TLSClientAuthWithStreamingResponse(self)

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
    ) -> Optional[TLSClientAuthUpdateResponse]:
        """
        TLS Client Auth requires Cloudflare to connect to your origin server using a
        client certificate (Enterprise Only).

        Args:
          zone_id: Identifier

          value: value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/tls_client_auth",
            body=maybe_transform({"value": value}, tls_client_auth_update_params.TLSClientAuthUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[TLSClientAuthUpdateResponse]], ResultWrapper[TLSClientAuthUpdateResponse]),
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
    ) -> Optional[TLSClientAuthGetResponse]:
        """
        TLS Client Auth requires Cloudflare to connect to your origin server using a
        client certificate (Enterprise Only).

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
            f"/zones/{zone_id}/settings/tls_client_auth",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[TLSClientAuthGetResponse]], ResultWrapper[TLSClientAuthGetResponse]),
        )


class AsyncTLSClientAuth(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTLSClientAuthWithRawResponse:
        return AsyncTLSClientAuthWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTLSClientAuthWithStreamingResponse:
        return AsyncTLSClientAuthWithStreamingResponse(self)

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
    ) -> Optional[TLSClientAuthUpdateResponse]:
        """
        TLS Client Auth requires Cloudflare to connect to your origin server using a
        client certificate (Enterprise Only).

        Args:
          zone_id: Identifier

          value: value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/tls_client_auth",
            body=maybe_transform({"value": value}, tls_client_auth_update_params.TLSClientAuthUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[TLSClientAuthUpdateResponse]], ResultWrapper[TLSClientAuthUpdateResponse]),
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
    ) -> Optional[TLSClientAuthGetResponse]:
        """
        TLS Client Auth requires Cloudflare to connect to your origin server using a
        client certificate (Enterprise Only).

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
            f"/zones/{zone_id}/settings/tls_client_auth",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[TLSClientAuthGetResponse]], ResultWrapper[TLSClientAuthGetResponse]),
        )


class TLSClientAuthWithRawResponse:
    def __init__(self, tls_client_auth: TLSClientAuth) -> None:
        self._tls_client_auth = tls_client_auth

        self.update = to_raw_response_wrapper(
            tls_client_auth.update,
        )
        self.get = to_raw_response_wrapper(
            tls_client_auth.get,
        )


class AsyncTLSClientAuthWithRawResponse:
    def __init__(self, tls_client_auth: AsyncTLSClientAuth) -> None:
        self._tls_client_auth = tls_client_auth

        self.update = async_to_raw_response_wrapper(
            tls_client_auth.update,
        )
        self.get = async_to_raw_response_wrapper(
            tls_client_auth.get,
        )


class TLSClientAuthWithStreamingResponse:
    def __init__(self, tls_client_auth: TLSClientAuth) -> None:
        self._tls_client_auth = tls_client_auth

        self.update = to_streamed_response_wrapper(
            tls_client_auth.update,
        )
        self.get = to_streamed_response_wrapper(
            tls_client_auth.get,
        )


class AsyncTLSClientAuthWithStreamingResponse:
    def __init__(self, tls_client_auth: AsyncTLSClientAuth) -> None:
        self._tls_client_auth = tls_client_auth

        self.update = async_to_streamed_response_wrapper(
            tls_client_auth.update,
        )
        self.get = async_to_streamed_response_wrapper(
            tls_client_auth.get,
        )
