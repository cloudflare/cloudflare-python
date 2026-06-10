# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.zero_trust.dlp import data_class_create_params, data_class_update_params
from ....types.zero_trust.dlp.data_class_get_response import DataClassGetResponse
from ....types.zero_trust.dlp.data_class_list_response import DataClassListResponse
from ....types.zero_trust.dlp.data_class_create_response import DataClassCreateResponse
from ....types.zero_trust.dlp.data_class_update_response import DataClassUpdateResponse

__all__ = ["DataClassesResource", "AsyncDataClassesResource"]


class DataClassesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DataClassesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DataClassesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataClassesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DataClassesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        data_tags: SequenceNotStr[str],
        expression: str,
        name: str,
        sensitivity_levels: Iterable[data_class_create_params.SensitivityLevel],
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DataClassCreateResponse]:
        """
        Creates a new data class

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/dlp/data_classes", account_id=account_id),
            body=maybe_transform(
                {
                    "data_tags": data_tags,
                    "expression": expression,
                    "name": name,
                    "sensitivity_levels": sensitivity_levels,
                    "description": description,
                },
                data_class_create_params.DataClassCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DataClassCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DataClassCreateResponse]], ResultWrapper[DataClassCreateResponse]),
        )

    def update(
        self,
        data_class_id: str,
        *,
        account_id: str,
        data_tags: Optional[SequenceNotStr[str]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        expression: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        sensitivity_levels: Optional[Iterable[data_class_update_params.SensitivityLevel]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DataClassUpdateResponse]:
        """
        Update the attributes of a single data class

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not data_class_id:
            raise ValueError(f"Expected a non-empty value for `data_class_id` but received {data_class_id!r}")
        return self._put(
            path_template(
                "/accounts/{account_id}/dlp/data_classes/{data_class_id}",
                account_id=account_id,
                data_class_id=data_class_id,
            ),
            body=maybe_transform(
                {
                    "data_tags": data_tags,
                    "description": description,
                    "expression": expression,
                    "name": name,
                    "sensitivity_levels": sensitivity_levels,
                },
                data_class_update_params.DataClassUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DataClassUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DataClassUpdateResponse]], ResultWrapper[DataClassUpdateResponse]),
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
    ) -> SyncSinglePage[DataClassListResponse]:
        """
        Retrieve all data classes in an account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/dlp/data_classes", account_id=account_id),
            page=SyncSinglePage[DataClassListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=DataClassListResponse,
        )

    def delete(
        self,
        data_class_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete a single data class

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not data_class_id:
            raise ValueError(f"Expected a non-empty value for `data_class_id` but received {data_class_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/dlp/data_classes/{data_class_id}",
                account_id=account_id,
                data_class_id=data_class_id,
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
        data_class_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DataClassGetResponse]:
        """
        Retrieve a specific data class

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not data_class_id:
            raise ValueError(f"Expected a non-empty value for `data_class_id` but received {data_class_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/dlp/data_classes/{data_class_id}",
                account_id=account_id,
                data_class_id=data_class_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DataClassGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DataClassGetResponse]], ResultWrapper[DataClassGetResponse]),
        )


class AsyncDataClassesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDataClassesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDataClassesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataClassesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDataClassesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        data_tags: SequenceNotStr[str],
        expression: str,
        name: str,
        sensitivity_levels: Iterable[data_class_create_params.SensitivityLevel],
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DataClassCreateResponse]:
        """
        Creates a new data class

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/dlp/data_classes", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "data_tags": data_tags,
                    "expression": expression,
                    "name": name,
                    "sensitivity_levels": sensitivity_levels,
                    "description": description,
                },
                data_class_create_params.DataClassCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DataClassCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DataClassCreateResponse]], ResultWrapper[DataClassCreateResponse]),
        )

    async def update(
        self,
        data_class_id: str,
        *,
        account_id: str,
        data_tags: Optional[SequenceNotStr[str]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        expression: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        sensitivity_levels: Optional[Iterable[data_class_update_params.SensitivityLevel]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DataClassUpdateResponse]:
        """
        Update the attributes of a single data class

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not data_class_id:
            raise ValueError(f"Expected a non-empty value for `data_class_id` but received {data_class_id!r}")
        return await self._put(
            path_template(
                "/accounts/{account_id}/dlp/data_classes/{data_class_id}",
                account_id=account_id,
                data_class_id=data_class_id,
            ),
            body=await async_maybe_transform(
                {
                    "data_tags": data_tags,
                    "description": description,
                    "expression": expression,
                    "name": name,
                    "sensitivity_levels": sensitivity_levels,
                },
                data_class_update_params.DataClassUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DataClassUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DataClassUpdateResponse]], ResultWrapper[DataClassUpdateResponse]),
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
    ) -> AsyncPaginator[DataClassListResponse, AsyncSinglePage[DataClassListResponse]]:
        """
        Retrieve all data classes in an account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/dlp/data_classes", account_id=account_id),
            page=AsyncSinglePage[DataClassListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=DataClassListResponse,
        )

    async def delete(
        self,
        data_class_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete a single data class

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not data_class_id:
            raise ValueError(f"Expected a non-empty value for `data_class_id` but received {data_class_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/dlp/data_classes/{data_class_id}",
                account_id=account_id,
                data_class_id=data_class_id,
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
        data_class_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DataClassGetResponse]:
        """
        Retrieve a specific data class

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not data_class_id:
            raise ValueError(f"Expected a non-empty value for `data_class_id` but received {data_class_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/dlp/data_classes/{data_class_id}",
                account_id=account_id,
                data_class_id=data_class_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DataClassGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DataClassGetResponse]], ResultWrapper[DataClassGetResponse]),
        )


class DataClassesResourceWithRawResponse:
    def __init__(self, data_classes: DataClassesResource) -> None:
        self._data_classes = data_classes

        self.create = to_raw_response_wrapper(
            data_classes.create,
        )
        self.update = to_raw_response_wrapper(
            data_classes.update,
        )
        self.list = to_raw_response_wrapper(
            data_classes.list,
        )
        self.delete = to_raw_response_wrapper(
            data_classes.delete,
        )
        self.get = to_raw_response_wrapper(
            data_classes.get,
        )


class AsyncDataClassesResourceWithRawResponse:
    def __init__(self, data_classes: AsyncDataClassesResource) -> None:
        self._data_classes = data_classes

        self.create = async_to_raw_response_wrapper(
            data_classes.create,
        )
        self.update = async_to_raw_response_wrapper(
            data_classes.update,
        )
        self.list = async_to_raw_response_wrapper(
            data_classes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            data_classes.delete,
        )
        self.get = async_to_raw_response_wrapper(
            data_classes.get,
        )


class DataClassesResourceWithStreamingResponse:
    def __init__(self, data_classes: DataClassesResource) -> None:
        self._data_classes = data_classes

        self.create = to_streamed_response_wrapper(
            data_classes.create,
        )
        self.update = to_streamed_response_wrapper(
            data_classes.update,
        )
        self.list = to_streamed_response_wrapper(
            data_classes.list,
        )
        self.delete = to_streamed_response_wrapper(
            data_classes.delete,
        )
        self.get = to_streamed_response_wrapper(
            data_classes.get,
        )


class AsyncDataClassesResourceWithStreamingResponse:
    def __init__(self, data_classes: AsyncDataClassesResource) -> None:
        self._data_classes = data_classes

        self.create = async_to_streamed_response_wrapper(
            data_classes.create,
        )
        self.update = async_to_streamed_response_wrapper(
            data_classes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            data_classes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            data_classes.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            data_classes.get,
        )
