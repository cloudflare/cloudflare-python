# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
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
from ....types.zones.settings import security_level_edit_params
from ....types.zones.settings.security_level import SecurityLevel

__all__ = ["SecurityLevelResource", "AsyncSecurityLevelResource"]


class SecurityLevelResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SecurityLevelResourceWithRawResponse:
        return SecurityLevelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecurityLevelResourceWithStreamingResponse:
        return SecurityLevelResourceWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: Literal["off", "essentially_off", "low", "medium", "high", "under_attack"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SecurityLevel]:
        """
        Choose the appropriate security profile for your website, which will
        automatically adjust each of the security settings. If you choose to customize
        an individual security setting, the profile will become Custom.
        (https://support.cloudflare.com/hc/en-us/articles/200170056).

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/security_level",
            body=maybe_transform({"value": value}, security_level_edit_params.SecurityLevelEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SecurityLevel]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SecurityLevel]], ResultWrapper[SecurityLevel]),
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
    ) -> Optional[SecurityLevel]:
        """
        Choose the appropriate security profile for your website, which will
        automatically adjust each of the security settings. If you choose to customize
        an individual security setting, the profile will become Custom.
        (https://support.cloudflare.com/hc/en-us/articles/200170056).

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
            f"/zones/{zone_id}/settings/security_level",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SecurityLevel]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SecurityLevel]], ResultWrapper[SecurityLevel]),
        )


class AsyncSecurityLevelResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSecurityLevelResourceWithRawResponse:
        return AsyncSecurityLevelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecurityLevelResourceWithStreamingResponse:
        return AsyncSecurityLevelResourceWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: Literal["off", "essentially_off", "low", "medium", "high", "under_attack"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SecurityLevel]:
        """
        Choose the appropriate security profile for your website, which will
        automatically adjust each of the security settings. If you choose to customize
        an individual security setting, the profile will become Custom.
        (https://support.cloudflare.com/hc/en-us/articles/200170056).

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/security_level",
            body=await async_maybe_transform({"value": value}, security_level_edit_params.SecurityLevelEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SecurityLevel]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SecurityLevel]], ResultWrapper[SecurityLevel]),
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
    ) -> Optional[SecurityLevel]:
        """
        Choose the appropriate security profile for your website, which will
        automatically adjust each of the security settings. If you choose to customize
        an individual security setting, the profile will become Custom.
        (https://support.cloudflare.com/hc/en-us/articles/200170056).

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
            f"/zones/{zone_id}/settings/security_level",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SecurityLevel]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SecurityLevel]], ResultWrapper[SecurityLevel]),
        )


class SecurityLevelResourceWithRawResponse:
    def __init__(self, security_level: SecurityLevelResource) -> None:
        self._security_level = security_level

        self.edit = to_raw_response_wrapper(
            security_level.edit,
        )
        self.get = to_raw_response_wrapper(
            security_level.get,
        )


class AsyncSecurityLevelResourceWithRawResponse:
    def __init__(self, security_level: AsyncSecurityLevelResource) -> None:
        self._security_level = security_level

        self.edit = async_to_raw_response_wrapper(
            security_level.edit,
        )
        self.get = async_to_raw_response_wrapper(
            security_level.get,
        )


class SecurityLevelResourceWithStreamingResponse:
    def __init__(self, security_level: SecurityLevelResource) -> None:
        self._security_level = security_level

        self.edit = to_streamed_response_wrapper(
            security_level.edit,
        )
        self.get = to_streamed_response_wrapper(
            security_level.get,
        )


class AsyncSecurityLevelResourceWithStreamingResponse:
    def __init__(self, security_level: AsyncSecurityLevelResource) -> None:
        self._security_level = security_level

        self.edit = async_to_streamed_response_wrapper(
            security_level.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            security_level.get,
        )
