# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, Type, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.stream import (
    KeyDeleteResponse,
    KeyStreamSigningKeysListSigningKeysResponse,
    KeyStreamSigningKeysCreateSigningKeysResponse,
)

__all__ = ["Keys", "AsyncKeys"]


class Keys(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KeysWithRawResponse:
        return KeysWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeysWithStreamingResponse:
        return KeysWithStreamingResponse(self)

    def delete(
        self,
        identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeyDeleteResponse:
        """
        Deletes signing keys and revokes all signed URLs generated with the key.

        Args:
          account_id: Identifier

          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return cast(
            KeyDeleteResponse,
            self._delete(
                f"/accounts/{account_id}/stream/keys/{identifier}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[KeyDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def stream_signing_keys_create_signing_keys(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeyStreamSigningKeysCreateSigningKeysResponse:
        """Creates an RSA private key in PEM and JWK formats.

        Key files are only displayed
        once after creation. Keys are created, used, and deleted independently of
        videos, and every key can sign any video.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/stream/keys",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[KeyStreamSigningKeysCreateSigningKeysResponse],
                ResultWrapper[KeyStreamSigningKeysCreateSigningKeysResponse],
            ),
        )

    def stream_signing_keys_list_signing_keys(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeyStreamSigningKeysListSigningKeysResponse:
        """
        Lists the video ID and creation date and time when a signing key was created.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/stream/keys",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[KeyStreamSigningKeysListSigningKeysResponse],
                ResultWrapper[KeyStreamSigningKeysListSigningKeysResponse],
            ),
        )


class AsyncKeys(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKeysWithRawResponse:
        return AsyncKeysWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeysWithStreamingResponse:
        return AsyncKeysWithStreamingResponse(self)

    async def delete(
        self,
        identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeyDeleteResponse:
        """
        Deletes signing keys and revokes all signed URLs generated with the key.

        Args:
          account_id: Identifier

          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return cast(
            KeyDeleteResponse,
            await self._delete(
                f"/accounts/{account_id}/stream/keys/{identifier}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[KeyDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def stream_signing_keys_create_signing_keys(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeyStreamSigningKeysCreateSigningKeysResponse:
        """Creates an RSA private key in PEM and JWK formats.

        Key files are only displayed
        once after creation. Keys are created, used, and deleted independently of
        videos, and every key can sign any video.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/stream/keys",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[KeyStreamSigningKeysCreateSigningKeysResponse],
                ResultWrapper[KeyStreamSigningKeysCreateSigningKeysResponse],
            ),
        )

    async def stream_signing_keys_list_signing_keys(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeyStreamSigningKeysListSigningKeysResponse:
        """
        Lists the video ID and creation date and time when a signing key was created.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/stream/keys",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[KeyStreamSigningKeysListSigningKeysResponse],
                ResultWrapper[KeyStreamSigningKeysListSigningKeysResponse],
            ),
        )


class KeysWithRawResponse:
    def __init__(self, keys: Keys) -> None:
        self._keys = keys

        self.delete = to_raw_response_wrapper(
            keys.delete,
        )
        self.stream_signing_keys_create_signing_keys = to_raw_response_wrapper(
            keys.stream_signing_keys_create_signing_keys,
        )
        self.stream_signing_keys_list_signing_keys = to_raw_response_wrapper(
            keys.stream_signing_keys_list_signing_keys,
        )


class AsyncKeysWithRawResponse:
    def __init__(self, keys: AsyncKeys) -> None:
        self._keys = keys

        self.delete = async_to_raw_response_wrapper(
            keys.delete,
        )
        self.stream_signing_keys_create_signing_keys = async_to_raw_response_wrapper(
            keys.stream_signing_keys_create_signing_keys,
        )
        self.stream_signing_keys_list_signing_keys = async_to_raw_response_wrapper(
            keys.stream_signing_keys_list_signing_keys,
        )


class KeysWithStreamingResponse:
    def __init__(self, keys: Keys) -> None:
        self._keys = keys

        self.delete = to_streamed_response_wrapper(
            keys.delete,
        )
        self.stream_signing_keys_create_signing_keys = to_streamed_response_wrapper(
            keys.stream_signing_keys_create_signing_keys,
        )
        self.stream_signing_keys_list_signing_keys = to_streamed_response_wrapper(
            keys.stream_signing_keys_list_signing_keys,
        )


class AsyncKeysWithStreamingResponse:
    def __init__(self, keys: AsyncKeys) -> None:
        self._keys = keys

        self.delete = async_to_streamed_response_wrapper(
            keys.delete,
        )
        self.stream_signing_keys_create_signing_keys = async_to_streamed_response_wrapper(
            keys.stream_signing_keys_create_signing_keys,
        )
        self.stream_signing_keys_list_signing_keys = async_to_streamed_response_wrapper(
            keys.stream_signing_keys_list_signing_keys,
        )
