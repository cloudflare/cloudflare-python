# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .rotates import Rotates, AsyncRotates

from ...._compat import cached_property

from ....types.access import (
    KeyAccessKeyConfigurationGetTheAccessKeyConfigurationResponse,
    KeyAccessKeyConfigurationUpdateTheAccessKeyConfigurationResponse,
)

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
from ....types.access import key_access_key_configuration_update_the_access_key_configuration_params
from .rotates import (
    Rotates,
    AsyncRotates,
    RotatesWithRawResponse,
    AsyncRotatesWithRawResponse,
    RotatesWithStreamingResponse,
    AsyncRotatesWithStreamingResponse,
)
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Keys", "AsyncKeys"]


class Keys(SyncAPIResource):
    @cached_property
    def rotates(self) -> Rotates:
        return Rotates(self._client)

    @cached_property
    def with_raw_response(self) -> KeysWithRawResponse:
        return KeysWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeysWithStreamingResponse:
        return KeysWithStreamingResponse(self)

    def access_key_configuration_get_the_access_key_configuration(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeyAccessKeyConfigurationGetTheAccessKeyConfigurationResponse:
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
            KeyAccessKeyConfigurationGetTheAccessKeyConfigurationResponse,
            self._get(
                f"/accounts/{identifier}/access/keys",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[KeyAccessKeyConfigurationGetTheAccessKeyConfigurationResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def access_key_configuration_update_the_access_key_configuration(
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
    ) -> KeyAccessKeyConfigurationUpdateTheAccessKeyConfigurationResponse:
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
            KeyAccessKeyConfigurationUpdateTheAccessKeyConfigurationResponse,
            self._put(
                f"/accounts/{identifier}/access/keys",
                body=maybe_transform(
                    {"key_rotation_interval_days": key_rotation_interval_days},
                    key_access_key_configuration_update_the_access_key_configuration_params.KeyAccessKeyConfigurationUpdateTheAccessKeyConfigurationParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[KeyAccessKeyConfigurationUpdateTheAccessKeyConfigurationResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncKeys(AsyncAPIResource):
    @cached_property
    def rotates(self) -> AsyncRotates:
        return AsyncRotates(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncKeysWithRawResponse:
        return AsyncKeysWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeysWithStreamingResponse:
        return AsyncKeysWithStreamingResponse(self)

    async def access_key_configuration_get_the_access_key_configuration(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeyAccessKeyConfigurationGetTheAccessKeyConfigurationResponse:
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
            KeyAccessKeyConfigurationGetTheAccessKeyConfigurationResponse,
            await self._get(
                f"/accounts/{identifier}/access/keys",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[KeyAccessKeyConfigurationGetTheAccessKeyConfigurationResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def access_key_configuration_update_the_access_key_configuration(
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
    ) -> KeyAccessKeyConfigurationUpdateTheAccessKeyConfigurationResponse:
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
            KeyAccessKeyConfigurationUpdateTheAccessKeyConfigurationResponse,
            await self._put(
                f"/accounts/{identifier}/access/keys",
                body=maybe_transform(
                    {"key_rotation_interval_days": key_rotation_interval_days},
                    key_access_key_configuration_update_the_access_key_configuration_params.KeyAccessKeyConfigurationUpdateTheAccessKeyConfigurationParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[KeyAccessKeyConfigurationUpdateTheAccessKeyConfigurationResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class KeysWithRawResponse:
    def __init__(self, keys: Keys) -> None:
        self._keys = keys

        self.access_key_configuration_get_the_access_key_configuration = to_raw_response_wrapper(
            keys.access_key_configuration_get_the_access_key_configuration,
        )
        self.access_key_configuration_update_the_access_key_configuration = to_raw_response_wrapper(
            keys.access_key_configuration_update_the_access_key_configuration,
        )

    @cached_property
    def rotates(self) -> RotatesWithRawResponse:
        return RotatesWithRawResponse(self._keys.rotates)


class AsyncKeysWithRawResponse:
    def __init__(self, keys: AsyncKeys) -> None:
        self._keys = keys

        self.access_key_configuration_get_the_access_key_configuration = async_to_raw_response_wrapper(
            keys.access_key_configuration_get_the_access_key_configuration,
        )
        self.access_key_configuration_update_the_access_key_configuration = async_to_raw_response_wrapper(
            keys.access_key_configuration_update_the_access_key_configuration,
        )

    @cached_property
    def rotates(self) -> AsyncRotatesWithRawResponse:
        return AsyncRotatesWithRawResponse(self._keys.rotates)


class KeysWithStreamingResponse:
    def __init__(self, keys: Keys) -> None:
        self._keys = keys

        self.access_key_configuration_get_the_access_key_configuration = to_streamed_response_wrapper(
            keys.access_key_configuration_get_the_access_key_configuration,
        )
        self.access_key_configuration_update_the_access_key_configuration = to_streamed_response_wrapper(
            keys.access_key_configuration_update_the_access_key_configuration,
        )

    @cached_property
    def rotates(self) -> RotatesWithStreamingResponse:
        return RotatesWithStreamingResponse(self._keys.rotates)


class AsyncKeysWithStreamingResponse:
    def __init__(self, keys: AsyncKeys) -> None:
        self._keys = keys

        self.access_key_configuration_get_the_access_key_configuration = async_to_streamed_response_wrapper(
            keys.access_key_configuration_get_the_access_key_configuration,
        )
        self.access_key_configuration_update_the_access_key_configuration = async_to_streamed_response_wrapper(
            keys.access_key_configuration_update_the_access_key_configuration,
        )

    @cached_property
    def rotates(self) -> AsyncRotatesWithStreamingResponse:
        return AsyncRotatesWithStreamingResponse(self._keys.rotates)
