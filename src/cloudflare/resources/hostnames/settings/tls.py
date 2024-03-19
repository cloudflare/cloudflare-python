# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, Optional, cast
from typing_extensions import Literal

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
from ...._base_client import (
    make_request_options,
)
from ....types.hostnames.settings import (
    TLSGetResponse,
    TLSCertificatesAndHostnamesSettingObject,
    TLSCertificatesAndHostnamesSettingObjectDelete,
    tls_update_params,
)

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
    ) -> TLSCertificatesAndHostnamesSettingObject:
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
            cast_to=cast(
                Type[TLSCertificatesAndHostnamesSettingObject], ResultWrapper[TLSCertificatesAndHostnamesSettingObject]
            ),
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
    ) -> TLSCertificatesAndHostnamesSettingObjectDelete:
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
            cast_to=cast(
                Type[TLSCertificatesAndHostnamesSettingObjectDelete],
                ResultWrapper[TLSCertificatesAndHostnamesSettingObjectDelete],
            ),
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
    ) -> TLSCertificatesAndHostnamesSettingObject:
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
            body=await async_maybe_transform({"value": value}, tls_update_params.TLSUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[TLSCertificatesAndHostnamesSettingObject], ResultWrapper[TLSCertificatesAndHostnamesSettingObject]
            ),
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
    ) -> TLSCertificatesAndHostnamesSettingObjectDelete:
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
            cast_to=cast(
                Type[TLSCertificatesAndHostnamesSettingObjectDelete],
                ResultWrapper[TLSCertificatesAndHostnamesSettingObjectDelete],
            ),
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
