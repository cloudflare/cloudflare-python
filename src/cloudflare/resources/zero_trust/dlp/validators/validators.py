# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from .....pagination import SyncSinglePage, AsyncSinglePage
from .proximity_words import (
    ProximityWordsResource,
    AsyncProximityWordsResource,
    ProximityWordsResourceWithRawResponse,
    AsyncProximityWordsResourceWithRawResponse,
    ProximityWordsResourceWithStreamingResponse,
    AsyncProximityWordsResourceWithStreamingResponse,
)
from ....._base_client import AsyncPaginator, make_request_options
from .....types.zero_trust.dlp import validator_list_params
from .....types.zero_trust.dlp.validator import Validator

__all__ = ["ValidatorsResource", "AsyncValidatorsResource"]


class ValidatorsResource(SyncAPIResource):
    @cached_property
    def proximity_words(self) -> ProximityWordsResource:
        return ProximityWordsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ValidatorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ValidatorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ValidatorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ValidatorsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        kind: Optional[Literal["proximity_words", "worker"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[Validator]:
        """
        Lists the validators configured for the account, of every kind.

        Args:
          kind: Only return validators of this kind. Omit to return every kind.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/dlp/validators", account_id=account_id),
            page=SyncSinglePage[Validator],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"kind": kind}, validator_list_params.ValidatorListParams),
            ),
            model=cast(Any, Validator),  # Union types cannot be passed in as arguments in the type system
        )

    def get(
        self,
        validator_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Validator]:
        """
        Fetches a validator of any kind by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not validator_id:
            raise ValueError(f"Expected a non-empty value for `validator_id` but received {validator_id!r}")
        return cast(
            Optional[Validator],
            self._get(
                path_template(
                    "/accounts/{account_id}/dlp/validators/{validator_id}",
                    account_id=account_id,
                    validator_id=validator_id,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[Validator]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[Validator]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncValidatorsResource(AsyncAPIResource):
    @cached_property
    def proximity_words(self) -> AsyncProximityWordsResource:
        return AsyncProximityWordsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncValidatorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncValidatorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncValidatorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncValidatorsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        kind: Optional[Literal["proximity_words", "worker"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Validator, AsyncSinglePage[Validator]]:
        """
        Lists the validators configured for the account, of every kind.

        Args:
          kind: Only return validators of this kind. Omit to return every kind.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/dlp/validators", account_id=account_id),
            page=AsyncSinglePage[Validator],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"kind": kind}, validator_list_params.ValidatorListParams),
            ),
            model=cast(Any, Validator),  # Union types cannot be passed in as arguments in the type system
        )

    async def get(
        self,
        validator_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Validator]:
        """
        Fetches a validator of any kind by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not validator_id:
            raise ValueError(f"Expected a non-empty value for `validator_id` but received {validator_id!r}")
        return cast(
            Optional[Validator],
            await self._get(
                path_template(
                    "/accounts/{account_id}/dlp/validators/{validator_id}",
                    account_id=account_id,
                    validator_id=validator_id,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[Validator]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[Validator]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ValidatorsResourceWithRawResponse:
    def __init__(self, validators: ValidatorsResource) -> None:
        self._validators = validators

        self.list = to_raw_response_wrapper(
            validators.list,
        )
        self.get = to_raw_response_wrapper(
            validators.get,
        )

    @cached_property
    def proximity_words(self) -> ProximityWordsResourceWithRawResponse:
        return ProximityWordsResourceWithRawResponse(self._validators.proximity_words)


class AsyncValidatorsResourceWithRawResponse:
    def __init__(self, validators: AsyncValidatorsResource) -> None:
        self._validators = validators

        self.list = async_to_raw_response_wrapper(
            validators.list,
        )
        self.get = async_to_raw_response_wrapper(
            validators.get,
        )

    @cached_property
    def proximity_words(self) -> AsyncProximityWordsResourceWithRawResponse:
        return AsyncProximityWordsResourceWithRawResponse(self._validators.proximity_words)


class ValidatorsResourceWithStreamingResponse:
    def __init__(self, validators: ValidatorsResource) -> None:
        self._validators = validators

        self.list = to_streamed_response_wrapper(
            validators.list,
        )
        self.get = to_streamed_response_wrapper(
            validators.get,
        )

    @cached_property
    def proximity_words(self) -> ProximityWordsResourceWithStreamingResponse:
        return ProximityWordsResourceWithStreamingResponse(self._validators.proximity_words)


class AsyncValidatorsResourceWithStreamingResponse:
    def __init__(self, validators: AsyncValidatorsResource) -> None:
        self._validators = validators

        self.list = async_to_streamed_response_wrapper(
            validators.list,
        )
        self.get = async_to_streamed_response_wrapper(
            validators.get,
        )

    @cached_property
    def proximity_words(self) -> AsyncProximityWordsResourceWithStreamingResponse:
        return AsyncProximityWordsResourceWithStreamingResponse(self._validators.proximity_words)
