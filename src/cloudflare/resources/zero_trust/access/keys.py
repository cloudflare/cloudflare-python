# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast

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
from ....types.zero_trust.access import key_update_params
from ....types.zero_trust.access.key_get_response import KeyGetResponse
from ....types.zero_trust.access.key_rotate_response import KeyRotateResponse
from ....types.zero_trust.access.key_update_response import KeyUpdateResponse

__all__ = ["KeysResource", "AsyncKeysResource"]


class KeysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KeysResourceWithRawResponse:
        return KeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeysResourceWithStreamingResponse:
        return KeysResourceWithStreamingResponse(self)

    def update(
        self,
        identifier: str,
        *,
        key_rotation_interval_days: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[KeyUpdateResponse]:
        """
        Updates the Access key rotation settings for an account.

        Args:
          identifier: Identifier

          key_rotation_interval_days: The number of days between key rotations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return cast(
            Optional[KeyUpdateResponse],
            self._put(
                f"/accounts/{identifier}/access/keys",
                body=maybe_transform(
                    {"key_rotation_interval_days": key_rotation_interval_days}, key_update_params.KeyUpdateParams
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[KeyUpdateResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[KeyUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[KeyGetResponse]:
        """
        Gets the Access key rotation settings for an account.

        Args:
          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return cast(
            Optional[KeyGetResponse],
            self._get(
                f"/accounts/{identifier}/access/keys",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[KeyGetResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[KeyGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def rotate(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[KeyRotateResponse]:
        """
        Perfoms a key rotation for an account.

        Args:
          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return cast(
            Optional[KeyRotateResponse],
            self._post(
                f"/accounts/{identifier}/access/keys/rotate",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[KeyRotateResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[KeyRotateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncKeysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKeysResourceWithRawResponse:
        return AsyncKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeysResourceWithStreamingResponse:
        return AsyncKeysResourceWithStreamingResponse(self)

    async def update(
        self,
        identifier: str,
        *,
        key_rotation_interval_days: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[KeyUpdateResponse]:
        """
        Updates the Access key rotation settings for an account.

        Args:
          identifier: Identifier

          key_rotation_interval_days: The number of days between key rotations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return cast(
            Optional[KeyUpdateResponse],
            await self._put(
                f"/accounts/{identifier}/access/keys",
                body=await async_maybe_transform(
                    {"key_rotation_interval_days": key_rotation_interval_days}, key_update_params.KeyUpdateParams
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[KeyUpdateResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[KeyUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[KeyGetResponse]:
        """
        Gets the Access key rotation settings for an account.

        Args:
          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return cast(
            Optional[KeyGetResponse],
            await self._get(
                f"/accounts/{identifier}/access/keys",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[KeyGetResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[KeyGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def rotate(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[KeyRotateResponse]:
        """
        Perfoms a key rotation for an account.

        Args:
          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return cast(
            Optional[KeyRotateResponse],
            await self._post(
                f"/accounts/{identifier}/access/keys/rotate",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[KeyRotateResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[KeyRotateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class KeysResourceWithRawResponse:
    def __init__(self, keys: KeysResource) -> None:
        self._keys = keys

        self.update = to_raw_response_wrapper(
            keys.update,
        )
        self.get = to_raw_response_wrapper(
            keys.get,
        )
        self.rotate = to_raw_response_wrapper(
            keys.rotate,
        )


class AsyncKeysResourceWithRawResponse:
    def __init__(self, keys: AsyncKeysResource) -> None:
        self._keys = keys

        self.update = async_to_raw_response_wrapper(
            keys.update,
        )
        self.get = async_to_raw_response_wrapper(
            keys.get,
        )
        self.rotate = async_to_raw_response_wrapper(
            keys.rotate,
        )


class KeysResourceWithStreamingResponse:
    def __init__(self, keys: KeysResource) -> None:
        self._keys = keys

        self.update = to_streamed_response_wrapper(
            keys.update,
        )
        self.get = to_streamed_response_wrapper(
            keys.get,
        )
        self.rotate = to_streamed_response_wrapper(
            keys.rotate,
        )


class AsyncKeysResourceWithStreamingResponse:
    def __init__(self, keys: AsyncKeysResource) -> None:
        self._keys = keys

        self.update = async_to_streamed_response_wrapper(
            keys.update,
        )
        self.get = async_to_streamed_response_wrapper(
            keys.get,
        )
        self.rotate = async_to_streamed_response_wrapper(
            keys.rotate,
        )
