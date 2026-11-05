# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast

import httpx

from ....._types import Body, Query, Headers, NotGiven, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
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
from ....._base_client import AsyncPaginator, make_request_options
from .....types.zero_trust.dlp.validators import proximity_word_create_params, proximity_word_update_params
from .....types.zero_trust.dlp.validators.word_param import WordParam
from .....types.zero_trust.dlp.validators.proximity_word_validator import ProximityWordValidator

__all__ = ["ProximityWordsResource", "AsyncProximityWordsResource"]


class ProximityWordsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProximityWordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ProximityWordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProximityWordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ProximityWordsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        words: Iterable[WordParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ProximityWordValidator]:
        """
        Creates a reusable list of weighted words that detection entries can attach to
        in order to refine their matches. An account may own at most 100 validators
        across all kinds.

        Args:
          name: A name for this validator, at most 50 characters.

          words: The words that raise confidence when found near a match, at most 100 per
              validator. Matching ignores case, so the list may not contain the same word
              twice with different capitalisation. Words are stored as sent.

              For example, a validator for medical record numbers might use
              `[{"word": "patient", "weight": "strong"}, {"word": "diagnosis", "weight": "moderate"}, {"word": "mrn", "weight": "weak"}]`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/dlp/validators/proximity_words", account_id=account_id),
            body=maybe_transform(
                {
                    "name": name,
                    "words": words,
                },
                proximity_word_create_params.ProximityWordCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ProximityWordValidator]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ProximityWordValidator]], ResultWrapper[ProximityWordValidator]),
        )

    def update(
        self,
        validator_id: str,
        *,
        account_id: str,
        name: str,
        words: Iterable[WordParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ProximityWordValidator]:
        """Replaces the name and word list of a `proximity_words` validator.

        Attachments to
        detection entries are owned from the entry side and are not affected.

        Args:
          name: A name for this validator, at most 50 characters.

          words: The words that raise confidence when found near a match, at most 100 per
              validator. Matching ignores case, so the list may not contain the same word
              twice with different capitalisation. Words are stored as sent.

              For example, a validator for medical record numbers might use
              `[{"word": "patient", "weight": "strong"}, {"word": "diagnosis", "weight": "moderate"}, {"word": "mrn", "weight": "weak"}]`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not validator_id:
            raise ValueError(f"Expected a non-empty value for `validator_id` but received {validator_id!r}")
        return self._put(
            path_template(
                "/accounts/{account_id}/dlp/validators/proximity_words/{validator_id}",
                account_id=account_id,
                validator_id=validator_id,
            ),
            body=maybe_transform(
                {
                    "name": name,
                    "words": words,
                },
                proximity_word_update_params.ProximityWordUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ProximityWordValidator]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ProximityWordValidator]], ResultWrapper[ProximityWordValidator]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[ProximityWordValidator]:
        """
        Lists the `proximity_words` validators configured for the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/dlp/validators/proximity_words", account_id=account_id),
            page=SyncSinglePage[ProximityWordValidator],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ProximityWordValidator,
        )

    def delete(
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
    ) -> object:
        """Deletes a `proximity_words` validator.

        Fails with `409` while any detection
        entry is still attached to it; detach it from those entries first.

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
        return self._delete(
            path_template(
                "/accounts/{account_id}/dlp/validators/proximity_words/{validator_id}",
                account_id=account_id,
                validator_id=validator_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
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
    ) -> Optional[ProximityWordValidator]:
        """
        Fetches a `proximity_words` validator by ID.

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
        return self._get(
            path_template(
                "/accounts/{account_id}/dlp/validators/proximity_words/{validator_id}",
                account_id=account_id,
                validator_id=validator_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ProximityWordValidator]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ProximityWordValidator]], ResultWrapper[ProximityWordValidator]),
        )


class AsyncProximityWordsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProximityWordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProximityWordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProximityWordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncProximityWordsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        words: Iterable[WordParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ProximityWordValidator]:
        """
        Creates a reusable list of weighted words that detection entries can attach to
        in order to refine their matches. An account may own at most 100 validators
        across all kinds.

        Args:
          name: A name for this validator, at most 50 characters.

          words: The words that raise confidence when found near a match, at most 100 per
              validator. Matching ignores case, so the list may not contain the same word
              twice with different capitalisation. Words are stored as sent.

              For example, a validator for medical record numbers might use
              `[{"word": "patient", "weight": "strong"}, {"word": "diagnosis", "weight": "moderate"}, {"word": "mrn", "weight": "weak"}]`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/dlp/validators/proximity_words", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "words": words,
                },
                proximity_word_create_params.ProximityWordCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ProximityWordValidator]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ProximityWordValidator]], ResultWrapper[ProximityWordValidator]),
        )

    async def update(
        self,
        validator_id: str,
        *,
        account_id: str,
        name: str,
        words: Iterable[WordParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ProximityWordValidator]:
        """Replaces the name and word list of a `proximity_words` validator.

        Attachments to
        detection entries are owned from the entry side and are not affected.

        Args:
          name: A name for this validator, at most 50 characters.

          words: The words that raise confidence when found near a match, at most 100 per
              validator. Matching ignores case, so the list may not contain the same word
              twice with different capitalisation. Words are stored as sent.

              For example, a validator for medical record numbers might use
              `[{"word": "patient", "weight": "strong"}, {"word": "diagnosis", "weight": "moderate"}, {"word": "mrn", "weight": "weak"}]`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not validator_id:
            raise ValueError(f"Expected a non-empty value for `validator_id` but received {validator_id!r}")
        return await self._put(
            path_template(
                "/accounts/{account_id}/dlp/validators/proximity_words/{validator_id}",
                account_id=account_id,
                validator_id=validator_id,
            ),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "words": words,
                },
                proximity_word_update_params.ProximityWordUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ProximityWordValidator]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ProximityWordValidator]], ResultWrapper[ProximityWordValidator]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ProximityWordValidator, AsyncSinglePage[ProximityWordValidator]]:
        """
        Lists the `proximity_words` validators configured for the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/dlp/validators/proximity_words", account_id=account_id),
            page=AsyncSinglePage[ProximityWordValidator],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ProximityWordValidator,
        )

    async def delete(
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
    ) -> object:
        """Deletes a `proximity_words` validator.

        Fails with `409` while any detection
        entry is still attached to it; detach it from those entries first.

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
        return await self._delete(
            path_template(
                "/accounts/{account_id}/dlp/validators/proximity_words/{validator_id}",
                account_id=account_id,
                validator_id=validator_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
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
    ) -> Optional[ProximityWordValidator]:
        """
        Fetches a `proximity_words` validator by ID.

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
        return await self._get(
            path_template(
                "/accounts/{account_id}/dlp/validators/proximity_words/{validator_id}",
                account_id=account_id,
                validator_id=validator_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ProximityWordValidator]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ProximityWordValidator]], ResultWrapper[ProximityWordValidator]),
        )


class ProximityWordsResourceWithRawResponse:
    def __init__(self, proximity_words: ProximityWordsResource) -> None:
        self._proximity_words = proximity_words

        self.create = to_raw_response_wrapper(
            proximity_words.create,
        )
        self.update = to_raw_response_wrapper(
            proximity_words.update,
        )
        self.list = to_raw_response_wrapper(
            proximity_words.list,
        )
        self.delete = to_raw_response_wrapper(
            proximity_words.delete,
        )
        self.get = to_raw_response_wrapper(
            proximity_words.get,
        )


class AsyncProximityWordsResourceWithRawResponse:
    def __init__(self, proximity_words: AsyncProximityWordsResource) -> None:
        self._proximity_words = proximity_words

        self.create = async_to_raw_response_wrapper(
            proximity_words.create,
        )
        self.update = async_to_raw_response_wrapper(
            proximity_words.update,
        )
        self.list = async_to_raw_response_wrapper(
            proximity_words.list,
        )
        self.delete = async_to_raw_response_wrapper(
            proximity_words.delete,
        )
        self.get = async_to_raw_response_wrapper(
            proximity_words.get,
        )


class ProximityWordsResourceWithStreamingResponse:
    def __init__(self, proximity_words: ProximityWordsResource) -> None:
        self._proximity_words = proximity_words

        self.create = to_streamed_response_wrapper(
            proximity_words.create,
        )
        self.update = to_streamed_response_wrapper(
            proximity_words.update,
        )
        self.list = to_streamed_response_wrapper(
            proximity_words.list,
        )
        self.delete = to_streamed_response_wrapper(
            proximity_words.delete,
        )
        self.get = to_streamed_response_wrapper(
            proximity_words.get,
        )


class AsyncProximityWordsResourceWithStreamingResponse:
    def __init__(self, proximity_words: AsyncProximityWordsResource) -> None:
        self._proximity_words = proximity_words

        self.create = async_to_streamed_response_wrapper(
            proximity_words.create,
        )
        self.update = async_to_streamed_response_wrapper(
            proximity_words.update,
        )
        self.list = async_to_streamed_response_wrapper(
            proximity_words.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            proximity_words.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            proximity_words.get,
        )
