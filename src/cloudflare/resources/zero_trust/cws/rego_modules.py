# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ....pagination import SyncCursorPagination, AsyncCursorPagination
from ...._base_client import AsyncPaginator, make_request_options
from ....types.zero_trust.cws import rego_module_list_params, rego_module_create_params, rego_module_update_params
from ....types.zero_trust.cws.rego_module import RegoModule
from ....types.zero_trust.cws.rego_module_delete_response import RegoModuleDeleteResponse

__all__ = ["RegoModulesResource", "AsyncRegoModulesResource"]


class RegoModulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RegoModulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RegoModulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegoModulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RegoModulesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        rego_source: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegoModule:
        """
        Creates a library Rego module and derives its package path from the source.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          name: Name of the Rego module (unique per account)

          rego_source: Library Rego source with a package beginning with "lib." Maximum 16384 UTF-8
              bytes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/cws/rego-modules", account_id=account_id),
            body=maybe_transform(
                {
                    "name": name,
                    "rego_source": rego_source,
                },
                rego_module_create_params.RegoModuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RegoModule]._unwrapper,
            ),
            cast_to=cast(Type[RegoModule], ResultWrapper[RegoModule]),
        )

    def update(
        self,
        rego_module_id: str,
        *,
        account_id: str,
        name: str,
        rego_source: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegoModule:
        """
        Replaces the module and validates policies and libraries that depend on it.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          rego_module_id: ID of the Rego module to update

          name: Name of the Rego module (unique per account)

          rego_source: Library Rego source with a package beginning with "lib." Maximum 16384 UTF-8
              bytes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rego_module_id:
            raise ValueError(f"Expected a non-empty value for `rego_module_id` but received {rego_module_id!r}")
        return self._put(
            path_template(
                "/accounts/{account_id}/cws/rego-modules/{rego_module_id}",
                account_id=account_id,
                rego_module_id=rego_module_id,
            ),
            body=maybe_transform(
                {
                    "name": name,
                    "rego_source": rego_source,
                },
                rego_module_update_params.RegoModuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RegoModule]._unwrapper,
            ),
            cast_to=cast(Type[RegoModule], ResultWrapper[RegoModule]),
        )

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        name: str | Omit = omit,
        order: Literal["name", "created_at", "updated_at"] | Omit = omit,
        package_path: str | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[RegoModule]:
        """
        Returns a paginated list of library Rego modules in the account.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          cursor: Pagination cursor from previous response

          direction: Sort direction (default: asc)

          name: Filter by Rego module name (case-insensitive substring match)

          order: Field to order results by (default: created_at)

          package_path: Filter by package path (case-sensitive literal substring match)

          per_page: Number of items per page (1-100, default 20)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/cws/rego-modules", account_id=account_id),
            page=SyncCursorPagination[RegoModule],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "direction": direction,
                        "name": name,
                        "order": order,
                        "package_path": package_path,
                        "per_page": per_page,
                    },
                    rego_module_list_params.RegoModuleListParams,
                ),
            ),
            model=RegoModule,
        )

    def delete(
        self,
        rego_module_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegoModuleDeleteResponse:
        """
        Deletes the module if no policy or library references its rules.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          rego_module_id: ID of the Rego module to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rego_module_id:
            raise ValueError(f"Expected a non-empty value for `rego_module_id` but received {rego_module_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/cws/rego-modules/{rego_module_id}",
                account_id=account_id,
                rego_module_id=rego_module_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RegoModuleDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[RegoModuleDeleteResponse], ResultWrapper[RegoModuleDeleteResponse]),
        )

    def get(
        self,
        rego_module_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegoModule:
        """
        Returns the library Rego module with the specified ID.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          rego_module_id: ID of the Rego module to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rego_module_id:
            raise ValueError(f"Expected a non-empty value for `rego_module_id` but received {rego_module_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/cws/rego-modules/{rego_module_id}",
                account_id=account_id,
                rego_module_id=rego_module_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RegoModule]._unwrapper,
            ),
            cast_to=cast(Type[RegoModule], ResultWrapper[RegoModule]),
        )


class AsyncRegoModulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRegoModulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRegoModulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegoModulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRegoModulesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        rego_source: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegoModule:
        """
        Creates a library Rego module and derives its package path from the source.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          name: Name of the Rego module (unique per account)

          rego_source: Library Rego source with a package beginning with "lib." Maximum 16384 UTF-8
              bytes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/cws/rego-modules", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "rego_source": rego_source,
                },
                rego_module_create_params.RegoModuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RegoModule]._unwrapper,
            ),
            cast_to=cast(Type[RegoModule], ResultWrapper[RegoModule]),
        )

    async def update(
        self,
        rego_module_id: str,
        *,
        account_id: str,
        name: str,
        rego_source: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegoModule:
        """
        Replaces the module and validates policies and libraries that depend on it.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          rego_module_id: ID of the Rego module to update

          name: Name of the Rego module (unique per account)

          rego_source: Library Rego source with a package beginning with "lib." Maximum 16384 UTF-8
              bytes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rego_module_id:
            raise ValueError(f"Expected a non-empty value for `rego_module_id` but received {rego_module_id!r}")
        return await self._put(
            path_template(
                "/accounts/{account_id}/cws/rego-modules/{rego_module_id}",
                account_id=account_id,
                rego_module_id=rego_module_id,
            ),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "rego_source": rego_source,
                },
                rego_module_update_params.RegoModuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RegoModule]._unwrapper,
            ),
            cast_to=cast(Type[RegoModule], ResultWrapper[RegoModule]),
        )

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        name: str | Omit = omit,
        order: Literal["name", "created_at", "updated_at"] | Omit = omit,
        package_path: str | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RegoModule, AsyncCursorPagination[RegoModule]]:
        """
        Returns a paginated list of library Rego modules in the account.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          cursor: Pagination cursor from previous response

          direction: Sort direction (default: asc)

          name: Filter by Rego module name (case-insensitive substring match)

          order: Field to order results by (default: created_at)

          package_path: Filter by package path (case-sensitive literal substring match)

          per_page: Number of items per page (1-100, default 20)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/cws/rego-modules", account_id=account_id),
            page=AsyncCursorPagination[RegoModule],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "direction": direction,
                        "name": name,
                        "order": order,
                        "package_path": package_path,
                        "per_page": per_page,
                    },
                    rego_module_list_params.RegoModuleListParams,
                ),
            ),
            model=RegoModule,
        )

    async def delete(
        self,
        rego_module_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegoModuleDeleteResponse:
        """
        Deletes the module if no policy or library references its rules.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          rego_module_id: ID of the Rego module to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rego_module_id:
            raise ValueError(f"Expected a non-empty value for `rego_module_id` but received {rego_module_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/cws/rego-modules/{rego_module_id}",
                account_id=account_id,
                rego_module_id=rego_module_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RegoModuleDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[RegoModuleDeleteResponse], ResultWrapper[RegoModuleDeleteResponse]),
        )

    async def get(
        self,
        rego_module_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegoModule:
        """
        Returns the library Rego module with the specified ID.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          rego_module_id: ID of the Rego module to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rego_module_id:
            raise ValueError(f"Expected a non-empty value for `rego_module_id` but received {rego_module_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/cws/rego-modules/{rego_module_id}",
                account_id=account_id,
                rego_module_id=rego_module_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RegoModule]._unwrapper,
            ),
            cast_to=cast(Type[RegoModule], ResultWrapper[RegoModule]),
        )


class RegoModulesResourceWithRawResponse:
    def __init__(self, rego_modules: RegoModulesResource) -> None:
        self._rego_modules = rego_modules

        self.create = to_raw_response_wrapper(
            rego_modules.create,
        )
        self.update = to_raw_response_wrapper(
            rego_modules.update,
        )
        self.list = to_raw_response_wrapper(
            rego_modules.list,
        )
        self.delete = to_raw_response_wrapper(
            rego_modules.delete,
        )
        self.get = to_raw_response_wrapper(
            rego_modules.get,
        )


class AsyncRegoModulesResourceWithRawResponse:
    def __init__(self, rego_modules: AsyncRegoModulesResource) -> None:
        self._rego_modules = rego_modules

        self.create = async_to_raw_response_wrapper(
            rego_modules.create,
        )
        self.update = async_to_raw_response_wrapper(
            rego_modules.update,
        )
        self.list = async_to_raw_response_wrapper(
            rego_modules.list,
        )
        self.delete = async_to_raw_response_wrapper(
            rego_modules.delete,
        )
        self.get = async_to_raw_response_wrapper(
            rego_modules.get,
        )


class RegoModulesResourceWithStreamingResponse:
    def __init__(self, rego_modules: RegoModulesResource) -> None:
        self._rego_modules = rego_modules

        self.create = to_streamed_response_wrapper(
            rego_modules.create,
        )
        self.update = to_streamed_response_wrapper(
            rego_modules.update,
        )
        self.list = to_streamed_response_wrapper(
            rego_modules.list,
        )
        self.delete = to_streamed_response_wrapper(
            rego_modules.delete,
        )
        self.get = to_streamed_response_wrapper(
            rego_modules.get,
        )


class AsyncRegoModulesResourceWithStreamingResponse:
    def __init__(self, rego_modules: AsyncRegoModulesResource) -> None:
        self._rego_modules = rego_modules

        self.create = async_to_streamed_response_wrapper(
            rego_modules.create,
        )
        self.update = async_to_streamed_response_wrapper(
            rego_modules.update,
        )
        self.list = async_to_streamed_response_wrapper(
            rego_modules.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            rego_modules.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            rego_modules.get,
        )
