# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
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
from ....types.zero_trust.gateway import pacfile_create_params, pacfile_update_params
from ....types.zero_trust.gateway.pacfile_get_response import PacfileGetResponse
from ....types.zero_trust.gateway.pacfile_list_response import PacfileListResponse
from ....types.zero_trust.gateway.pacfile_create_response import PacfileCreateResponse
from ....types.zero_trust.gateway.pacfile_update_response import PacfileUpdateResponse

__all__ = ["PacfilesResource", "AsyncPacfilesResource"]


class PacfilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PacfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PacfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PacfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PacfilesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        contents: str,
        name: str,
        description: str | Omit = omit,
        slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[PacfileCreateResponse]:
        """
        Create a new Zero Trust Gateway PAC file.

        Args:
          contents: Actual contents of the PAC file

          name: Name of the PAC file.

          description: Detailed description of the PAC file.

          slug: URL-friendly version of the PAC file name. If not provided, it will be
              auto-generated

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/gateway/pacfiles",
            body=maybe_transform(
                {
                    "contents": contents,
                    "name": name,
                    "description": description,
                    "slug": slug,
                },
                pacfile_create_params.PacfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PacfileCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PacfileCreateResponse]], ResultWrapper[PacfileCreateResponse]),
        )

    def update(
        self,
        pacfile_id: str,
        *,
        account_id: str,
        contents: str,
        description: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[PacfileUpdateResponse]:
        """
        Update a configured Zero Trust Gateway PAC file.

        Args:
          contents: Actual contents of the PAC file

          description: Detailed description of the PAC file.

          name: Name of the PAC file.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pacfile_id:
            raise ValueError(f"Expected a non-empty value for `pacfile_id` but received {pacfile_id!r}")
        return self._put(
            f"/accounts/{account_id}/gateway/pacfiles/{pacfile_id}",
            body=maybe_transform(
                {
                    "contents": contents,
                    "description": description,
                    "name": name,
                },
                pacfile_update_params.PacfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PacfileUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PacfileUpdateResponse]], ResultWrapper[PacfileUpdateResponse]),
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
    ) -> SyncSinglePage[PacfileListResponse]:
        """
        List all Zero Trust Gateway PAC files for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/gateway/pacfiles",
            page=SyncSinglePage[PacfileListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=PacfileListResponse,
        )

    def delete(
        self,
        pacfile_id: str,
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
        Delete a configured Zero Trust Gateway PAC file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pacfile_id:
            raise ValueError(f"Expected a non-empty value for `pacfile_id` but received {pacfile_id!r}")
        return self._delete(
            f"/accounts/{account_id}/gateway/pacfiles/{pacfile_id}",
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
        pacfile_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[PacfileGetResponse]:
        """
        Get a single Zero Trust Gateway PAC file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pacfile_id:
            raise ValueError(f"Expected a non-empty value for `pacfile_id` but received {pacfile_id!r}")
        return self._get(
            f"/accounts/{account_id}/gateway/pacfiles/{pacfile_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PacfileGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PacfileGetResponse]], ResultWrapper[PacfileGetResponse]),
        )


class AsyncPacfilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPacfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPacfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPacfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPacfilesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        contents: str,
        name: str,
        description: str | Omit = omit,
        slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[PacfileCreateResponse]:
        """
        Create a new Zero Trust Gateway PAC file.

        Args:
          contents: Actual contents of the PAC file

          name: Name of the PAC file.

          description: Detailed description of the PAC file.

          slug: URL-friendly version of the PAC file name. If not provided, it will be
              auto-generated

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/gateway/pacfiles",
            body=await async_maybe_transform(
                {
                    "contents": contents,
                    "name": name,
                    "description": description,
                    "slug": slug,
                },
                pacfile_create_params.PacfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PacfileCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PacfileCreateResponse]], ResultWrapper[PacfileCreateResponse]),
        )

    async def update(
        self,
        pacfile_id: str,
        *,
        account_id: str,
        contents: str,
        description: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[PacfileUpdateResponse]:
        """
        Update a configured Zero Trust Gateway PAC file.

        Args:
          contents: Actual contents of the PAC file

          description: Detailed description of the PAC file.

          name: Name of the PAC file.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pacfile_id:
            raise ValueError(f"Expected a non-empty value for `pacfile_id` but received {pacfile_id!r}")
        return await self._put(
            f"/accounts/{account_id}/gateway/pacfiles/{pacfile_id}",
            body=await async_maybe_transform(
                {
                    "contents": contents,
                    "description": description,
                    "name": name,
                },
                pacfile_update_params.PacfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PacfileUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PacfileUpdateResponse]], ResultWrapper[PacfileUpdateResponse]),
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
    ) -> AsyncPaginator[PacfileListResponse, AsyncSinglePage[PacfileListResponse]]:
        """
        List all Zero Trust Gateway PAC files for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/gateway/pacfiles",
            page=AsyncSinglePage[PacfileListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=PacfileListResponse,
        )

    async def delete(
        self,
        pacfile_id: str,
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
        Delete a configured Zero Trust Gateway PAC file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pacfile_id:
            raise ValueError(f"Expected a non-empty value for `pacfile_id` but received {pacfile_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/gateway/pacfiles/{pacfile_id}",
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
        pacfile_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[PacfileGetResponse]:
        """
        Get a single Zero Trust Gateway PAC file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pacfile_id:
            raise ValueError(f"Expected a non-empty value for `pacfile_id` but received {pacfile_id!r}")
        return await self._get(
            f"/accounts/{account_id}/gateway/pacfiles/{pacfile_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PacfileGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PacfileGetResponse]], ResultWrapper[PacfileGetResponse]),
        )


class PacfilesResourceWithRawResponse:
    def __init__(self, pacfiles: PacfilesResource) -> None:
        self._pacfiles = pacfiles

        self.create = to_raw_response_wrapper(
            pacfiles.create,
        )
        self.update = to_raw_response_wrapper(
            pacfiles.update,
        )
        self.list = to_raw_response_wrapper(
            pacfiles.list,
        )
        self.delete = to_raw_response_wrapper(
            pacfiles.delete,
        )
        self.get = to_raw_response_wrapper(
            pacfiles.get,
        )


class AsyncPacfilesResourceWithRawResponse:
    def __init__(self, pacfiles: AsyncPacfilesResource) -> None:
        self._pacfiles = pacfiles

        self.create = async_to_raw_response_wrapper(
            pacfiles.create,
        )
        self.update = async_to_raw_response_wrapper(
            pacfiles.update,
        )
        self.list = async_to_raw_response_wrapper(
            pacfiles.list,
        )
        self.delete = async_to_raw_response_wrapper(
            pacfiles.delete,
        )
        self.get = async_to_raw_response_wrapper(
            pacfiles.get,
        )


class PacfilesResourceWithStreamingResponse:
    def __init__(self, pacfiles: PacfilesResource) -> None:
        self._pacfiles = pacfiles

        self.create = to_streamed_response_wrapper(
            pacfiles.create,
        )
        self.update = to_streamed_response_wrapper(
            pacfiles.update,
        )
        self.list = to_streamed_response_wrapper(
            pacfiles.list,
        )
        self.delete = to_streamed_response_wrapper(
            pacfiles.delete,
        )
        self.get = to_streamed_response_wrapper(
            pacfiles.get,
        )


class AsyncPacfilesResourceWithStreamingResponse:
    def __init__(self, pacfiles: AsyncPacfilesResource) -> None:
        self._pacfiles = pacfiles

        self.create = async_to_streamed_response_wrapper(
            pacfiles.create,
        )
        self.update = async_to_streamed_response_wrapper(
            pacfiles.update,
        )
        self.list = async_to_streamed_response_wrapper(
            pacfiles.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            pacfiles.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            pacfiles.get,
        )
