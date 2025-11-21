# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.alerting import silence_create_params, silence_update_params
from ...types.alerting.silence_get_response import SilenceGetResponse
from ...types.alerting.silence_list_response import SilenceListResponse
from ...types.alerting.silence_create_response import SilenceCreateResponse
from ...types.alerting.silence_delete_response import SilenceDeleteResponse
from ...types.alerting.silence_update_response import SilenceUpdateResponse

__all__ = ["SilencesResource", "AsyncSilencesResource"]


class SilencesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SilencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SilencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SilencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SilencesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        body: Iterable[silence_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SilenceCreateResponse:
        """
        Creates a new silence for an account.

        Args:
          account_id: The account id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/alerting/v3/silences",
            body=maybe_transform(body, Iterable[silence_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SilenceCreateResponse,
        )

    def update(
        self,
        *,
        account_id: str,
        body: Iterable[silence_update_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[SilenceUpdateResponse]:
        """
        Updates existing silences for an account.

        Args:
          account_id: The account id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/alerting/v3/silences",
            page=SyncSinglePage[SilenceUpdateResponse],
            body=maybe_transform(body, Iterable[silence_update_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=SilenceUpdateResponse,
            method="put",
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
    ) -> SyncSinglePage[SilenceListResponse]:
        """
        Gets a list of silences for an account.

        Args:
          account_id: The account id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/alerting/v3/silences",
            page=SyncSinglePage[SilenceListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=SilenceListResponse,
        )

    def delete(
        self,
        silence_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SilenceDeleteResponse:
        """
        Deletes an existing silence for an account.

        Args:
          account_id: The account id

          silence_id: Silence ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not silence_id:
            raise ValueError(f"Expected a non-empty value for `silence_id` but received {silence_id!r}")
        return self._delete(
            f"/accounts/{account_id}/alerting/v3/silences/{silence_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SilenceDeleteResponse,
        )

    def get(
        self,
        silence_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SilenceGetResponse]:
        """
        Gets a specific silence for an account.

        Args:
          account_id: The account id

          silence_id: Silence ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not silence_id:
            raise ValueError(f"Expected a non-empty value for `silence_id` but received {silence_id!r}")
        return self._get(
            f"/accounts/{account_id}/alerting/v3/silences/{silence_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SilenceGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SilenceGetResponse]], ResultWrapper[SilenceGetResponse]),
        )


class AsyncSilencesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSilencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSilencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSilencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSilencesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        body: Iterable[silence_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SilenceCreateResponse:
        """
        Creates a new silence for an account.

        Args:
          account_id: The account id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/alerting/v3/silences",
            body=await async_maybe_transform(body, Iterable[silence_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SilenceCreateResponse,
        )

    def update(
        self,
        *,
        account_id: str,
        body: Iterable[silence_update_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SilenceUpdateResponse, AsyncSinglePage[SilenceUpdateResponse]]:
        """
        Updates existing silences for an account.

        Args:
          account_id: The account id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/alerting/v3/silences",
            page=AsyncSinglePage[SilenceUpdateResponse],
            body=maybe_transform(body, Iterable[silence_update_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=SilenceUpdateResponse,
            method="put",
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
    ) -> AsyncPaginator[SilenceListResponse, AsyncSinglePage[SilenceListResponse]]:
        """
        Gets a list of silences for an account.

        Args:
          account_id: The account id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/alerting/v3/silences",
            page=AsyncSinglePage[SilenceListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=SilenceListResponse,
        )

    async def delete(
        self,
        silence_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SilenceDeleteResponse:
        """
        Deletes an existing silence for an account.

        Args:
          account_id: The account id

          silence_id: Silence ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not silence_id:
            raise ValueError(f"Expected a non-empty value for `silence_id` but received {silence_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/alerting/v3/silences/{silence_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SilenceDeleteResponse,
        )

    async def get(
        self,
        silence_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SilenceGetResponse]:
        """
        Gets a specific silence for an account.

        Args:
          account_id: The account id

          silence_id: Silence ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not silence_id:
            raise ValueError(f"Expected a non-empty value for `silence_id` but received {silence_id!r}")
        return await self._get(
            f"/accounts/{account_id}/alerting/v3/silences/{silence_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SilenceGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SilenceGetResponse]], ResultWrapper[SilenceGetResponse]),
        )


class SilencesResourceWithRawResponse:
    def __init__(self, silences: SilencesResource) -> None:
        self._silences = silences

        self.create = to_raw_response_wrapper(
            silences.create,
        )
        self.update = to_raw_response_wrapper(
            silences.update,
        )
        self.list = to_raw_response_wrapper(
            silences.list,
        )
        self.delete = to_raw_response_wrapper(
            silences.delete,
        )
        self.get = to_raw_response_wrapper(
            silences.get,
        )


class AsyncSilencesResourceWithRawResponse:
    def __init__(self, silences: AsyncSilencesResource) -> None:
        self._silences = silences

        self.create = async_to_raw_response_wrapper(
            silences.create,
        )
        self.update = async_to_raw_response_wrapper(
            silences.update,
        )
        self.list = async_to_raw_response_wrapper(
            silences.list,
        )
        self.delete = async_to_raw_response_wrapper(
            silences.delete,
        )
        self.get = async_to_raw_response_wrapper(
            silences.get,
        )


class SilencesResourceWithStreamingResponse:
    def __init__(self, silences: SilencesResource) -> None:
        self._silences = silences

        self.create = to_streamed_response_wrapper(
            silences.create,
        )
        self.update = to_streamed_response_wrapper(
            silences.update,
        )
        self.list = to_streamed_response_wrapper(
            silences.list,
        )
        self.delete = to_streamed_response_wrapper(
            silences.delete,
        )
        self.get = to_streamed_response_wrapper(
            silences.get,
        )


class AsyncSilencesResourceWithStreamingResponse:
    def __init__(self, silences: AsyncSilencesResource) -> None:
        self._silences = silences

        self.create = async_to_streamed_response_wrapper(
            silences.create,
        )
        self.update = async_to_streamed_response_wrapper(
            silences.update,
        )
        self.list = async_to_streamed_response_wrapper(
            silences.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            silences.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            silences.get,
        )
