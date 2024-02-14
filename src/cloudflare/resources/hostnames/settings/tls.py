# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.hostnames.settings import TLSUpdateResponse, TLSDeleteResponse, TLSGetResponse

from typing import Type, Union, List, Optional

from typing_extensions import Literal

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ....types.hostnames.settings import tls_update_params
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["TLS", "AsyncTLS"]


class TLS(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TLSWithRawResponse:
        return TLSWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TLSWithStreamingResponse:
        return TLSWithStreamingResponse(self)

    def update(
        self,
        hostname: str,
        *,
        zone_id: str,
        setting_id: Literal["ciphers", "min_tls_version", "http2"],
        value: Union[float, str, List[str]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TLSUpdateResponse:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TLSUpdateResponse], ResultWrapper[TLSUpdateResponse]),
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
    ) -> TLSDeleteResponse:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TLSDeleteResponse], ResultWrapper[TLSDeleteResponse]),
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
    ) -> Optional[TLSGetResponse]:
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
        return self._get(
            f"/zones/{zone_id}/hostnames/settings/{setting_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[TLSGetResponse]], ResultWrapper[TLSGetResponse]),
        )


class AsyncTLS(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTLSWithRawResponse:
        return AsyncTLSWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTLSWithStreamingResponse:
        return AsyncTLSWithStreamingResponse(self)

    async def update(
        self,
        hostname: str,
        *,
        zone_id: str,
        setting_id: Literal["ciphers", "min_tls_version", "http2"],
        value: Union[float, str, List[str]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TLSUpdateResponse:
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
            body=maybe_transform({"value": value}, tls_update_params.TLSUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TLSUpdateResponse], ResultWrapper[TLSUpdateResponse]),
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
    ) -> TLSDeleteResponse:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TLSDeleteResponse], ResultWrapper[TLSDeleteResponse]),
        )

    async def get(
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
    ) -> Optional[TLSGetResponse]:
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
        return await self._get(
            f"/zones/{zone_id}/hostnames/settings/{setting_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[TLSGetResponse]], ResultWrapper[TLSGetResponse]),
        )


class TLSWithRawResponse:
    def __init__(self, tls: TLS) -> None:
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


class AsyncTLSWithRawResponse:
    def __init__(self, tls: AsyncTLS) -> None:
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


class TLSWithStreamingResponse:
    def __init__(self, tls: TLS) -> None:
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


class AsyncTLSWithStreamingResponse:
    def __init__(self, tls: AsyncTLS) -> None:
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
