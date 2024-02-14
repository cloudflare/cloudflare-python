# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.settings import ChallengeTTLUpdateResponse, ChallengeTTLGetResponse

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
from ...types.settings import challenge_ttl_update_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["ChallengeTTL", "AsyncChallengeTTL"]


class ChallengeTTL(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChallengeTTLWithRawResponse:
        return ChallengeTTLWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChallengeTTLWithStreamingResponse:
        return ChallengeTTLWithStreamingResponse(self)

    def update(
        self,
        zone_id: str,
        *,
        value: Literal[300, 900, 1800, 2700, 3600, 7200, 10800, 14400, 28800, 57600, 86400, 604800, 2592000, 31536000],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ChallengeTTLUpdateResponse]:
        """
        Specify how long a visitor is allowed access to your site after successfully
        completing a challenge (such as a CAPTCHA). After the TTL has expired the
        visitor will have to complete a new challenge. We recommend a 15 - 45 minute
        setting and will attempt to honor any setting above 45 minutes.
        (https://support.cloudflare.com/hc/en-us/articles/200170136).

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
            f"/zones/{zone_id}/settings/challenge_ttl",
            body=maybe_transform({"value": value}, challenge_ttl_update_params.ChallengeTTLUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ChallengeTTLUpdateResponse]], ResultWrapper[ChallengeTTLUpdateResponse]),
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
    ) -> Optional[ChallengeTTLGetResponse]:
        """
        Specify how long a visitor is allowed access to your site after successfully
        completing a challenge (such as a CAPTCHA). After the TTL has expired the
        visitor will have to complete a new challenge. We recommend a 15 - 45 minute
        setting and will attempt to honor any setting above 45 minutes.
        (https://support.cloudflare.com/hc/en-us/articles/200170136).

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
            f"/zones/{zone_id}/settings/challenge_ttl",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ChallengeTTLGetResponse]], ResultWrapper[ChallengeTTLGetResponse]),
        )


class AsyncChallengeTTL(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChallengeTTLWithRawResponse:
        return AsyncChallengeTTLWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChallengeTTLWithStreamingResponse:
        return AsyncChallengeTTLWithStreamingResponse(self)

    async def update(
        self,
        zone_id: str,
        *,
        value: Literal[300, 900, 1800, 2700, 3600, 7200, 10800, 14400, 28800, 57600, 86400, 604800, 2592000, 31536000],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ChallengeTTLUpdateResponse]:
        """
        Specify how long a visitor is allowed access to your site after successfully
        completing a challenge (such as a CAPTCHA). After the TTL has expired the
        visitor will have to complete a new challenge. We recommend a 15 - 45 minute
        setting and will attempt to honor any setting above 45 minutes.
        (https://support.cloudflare.com/hc/en-us/articles/200170136).

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
            f"/zones/{zone_id}/settings/challenge_ttl",
            body=maybe_transform({"value": value}, challenge_ttl_update_params.ChallengeTTLUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ChallengeTTLUpdateResponse]], ResultWrapper[ChallengeTTLUpdateResponse]),
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
    ) -> Optional[ChallengeTTLGetResponse]:
        """
        Specify how long a visitor is allowed access to your site after successfully
        completing a challenge (such as a CAPTCHA). After the TTL has expired the
        visitor will have to complete a new challenge. We recommend a 15 - 45 minute
        setting and will attempt to honor any setting above 45 minutes.
        (https://support.cloudflare.com/hc/en-us/articles/200170136).

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
            f"/zones/{zone_id}/settings/challenge_ttl",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ChallengeTTLGetResponse]], ResultWrapper[ChallengeTTLGetResponse]),
        )


class ChallengeTTLWithRawResponse:
    def __init__(self, challenge_ttl: ChallengeTTL) -> None:
        self._challenge_ttl = challenge_ttl

        self.update = to_raw_response_wrapper(
            challenge_ttl.update,
        )
        self.get = to_raw_response_wrapper(
            challenge_ttl.get,
        )


class AsyncChallengeTTLWithRawResponse:
    def __init__(self, challenge_ttl: AsyncChallengeTTL) -> None:
        self._challenge_ttl = challenge_ttl

        self.update = async_to_raw_response_wrapper(
            challenge_ttl.update,
        )
        self.get = async_to_raw_response_wrapper(
            challenge_ttl.get,
        )


class ChallengeTTLWithStreamingResponse:
    def __init__(self, challenge_ttl: ChallengeTTL) -> None:
        self._challenge_ttl = challenge_ttl

        self.update = to_streamed_response_wrapper(
            challenge_ttl.update,
        )
        self.get = to_streamed_response_wrapper(
            challenge_ttl.get,
        )


class AsyncChallengeTTLWithStreamingResponse:
    def __init__(self, challenge_ttl: AsyncChallengeTTL) -> None:
        self._challenge_ttl = challenge_ttl

        self.update = async_to_streamed_response_wrapper(
            challenge_ttl.update,
        )
        self.get = async_to_streamed_response_wrapper(
            challenge_ttl.get,
        )
