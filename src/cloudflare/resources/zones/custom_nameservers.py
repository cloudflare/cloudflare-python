# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.zones import CustomNameserverGetResponse, CustomNameserverUpdateResponse, custom_nameserver_update_params
from ..._base_client import (
    make_request_options,
)

__all__ = ["CustomNameservers", "AsyncCustomNameservers"]


class CustomNameservers(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomNameserversWithRawResponse:
        return CustomNameserversWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomNameserversWithStreamingResponse:
        return CustomNameserversWithStreamingResponse(self)

    def update(
        self,
        *,
        zone_id: str,
        enabled: bool | NotGiven = NOT_GIVEN,
        ns_set: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CustomNameserverUpdateResponse]:
        """
        Set metadata for account-level custom nameservers on a zone.

        If you would like new zones in the account to use account custom nameservers by
        default, use PUT /accounts/:identifier to set the account setting
        use_account_custom_ns_by_default to true.

        Args:
          zone_id: Identifier

          enabled: Whether zone uses account-level custom nameservers.

          ns_set: The number of the name server set to assign to the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            Optional[CustomNameserverUpdateResponse],
            self._put(
                f"/zones/{zone_id}/custom_ns",
                body=maybe_transform(
                    {
                        "enabled": enabled,
                        "ns_set": ns_set,
                    },
                    custom_nameserver_update_params.CustomNameserverUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CustomNameserverUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CustomNameserverGetResponse]:
        """
        Get metadata for account-level custom nameservers on a zone.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            Optional[CustomNameserverGetResponse],
            self._get(
                f"/zones/{zone_id}/custom_ns",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CustomNameserverGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncCustomNameservers(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomNameserversWithRawResponse:
        return AsyncCustomNameserversWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomNameserversWithStreamingResponse:
        return AsyncCustomNameserversWithStreamingResponse(self)

    async def update(
        self,
        *,
        zone_id: str,
        enabled: bool | NotGiven = NOT_GIVEN,
        ns_set: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CustomNameserverUpdateResponse]:
        """
        Set metadata for account-level custom nameservers on a zone.

        If you would like new zones in the account to use account custom nameservers by
        default, use PUT /accounts/:identifier to set the account setting
        use_account_custom_ns_by_default to true.

        Args:
          zone_id: Identifier

          enabled: Whether zone uses account-level custom nameservers.

          ns_set: The number of the name server set to assign to the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            Optional[CustomNameserverUpdateResponse],
            await self._put(
                f"/zones/{zone_id}/custom_ns",
                body=await async_maybe_transform(
                    {
                        "enabled": enabled,
                        "ns_set": ns_set,
                    },
                    custom_nameserver_update_params.CustomNameserverUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CustomNameserverUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CustomNameserverGetResponse]:
        """
        Get metadata for account-level custom nameservers on a zone.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            Optional[CustomNameserverGetResponse],
            await self._get(
                f"/zones/{zone_id}/custom_ns",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CustomNameserverGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class CustomNameserversWithRawResponse:
    def __init__(self, custom_nameservers: CustomNameservers) -> None:
        self._custom_nameservers = custom_nameservers

        self.update = to_raw_response_wrapper(
            custom_nameservers.update,
        )
        self.get = to_raw_response_wrapper(
            custom_nameservers.get,
        )


class AsyncCustomNameserversWithRawResponse:
    def __init__(self, custom_nameservers: AsyncCustomNameservers) -> None:
        self._custom_nameservers = custom_nameservers

        self.update = async_to_raw_response_wrapper(
            custom_nameservers.update,
        )
        self.get = async_to_raw_response_wrapper(
            custom_nameservers.get,
        )


class CustomNameserversWithStreamingResponse:
    def __init__(self, custom_nameservers: CustomNameservers) -> None:
        self._custom_nameservers = custom_nameservers

        self.update = to_streamed_response_wrapper(
            custom_nameservers.update,
        )
        self.get = to_streamed_response_wrapper(
            custom_nameservers.get,
        )


class AsyncCustomNameserversWithStreamingResponse:
    def __init__(self, custom_nameservers: AsyncCustomNameservers) -> None:
        self._custom_nameservers = custom_nameservers

        self.update = async_to_streamed_response_wrapper(
            custom_nameservers.update,
        )
        self.get = async_to_streamed_response_wrapper(
            custom_nameservers.get,
        )
