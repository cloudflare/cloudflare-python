# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast
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
from ....types.zero_trust.cws import domain_acl_list_params, domain_acl_create_params, domain_acl_update_params
from ....types.zero_trust.cws.domain_acl import DomainACL
from ....types.zero_trust.cws.domain_acl_delete_response import DomainACLDeleteResponse

__all__ = ["DomainACLsResource", "AsyncDomainACLsResource"]


class DomainACLsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DomainACLsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DomainACLsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DomainACLsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DomainACLsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        default_action: Literal["ALLOW", "BLOCK"],
        entries: Optional[Iterable[domain_acl_create_params.Entry]],
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainACL:
        """
        Creates a domain access control list with its default action and entries.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          default_action: Default action when no entry matches

          entries: Domain entries for this ACL. Each domain must appear at most once.

          name: Name of the domain ACL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/cws/domain-acls", account_id=account_id),
            body=maybe_transform(
                {
                    "default_action": default_action,
                    "entries": entries,
                    "name": name,
                },
                domain_acl_create_params.DomainACLCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DomainACL]._unwrapper,
            ),
            cast_to=cast(Type[DomainACL], ResultWrapper[DomainACL]),
        )

    def update(
        self,
        domain_acl_id: str,
        *,
        account_id: str,
        default_action: Literal["ALLOW", "BLOCK"],
        entries: Optional[Iterable[domain_acl_update_params.Entry]],
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainACL:
        """
        Replaces the domain access control list's name, default action, and entries.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          domain_acl_id: ID of the domain ACL to update

          default_action: Default action when no entry matches

          entries: Replacement set of domain entries. Each domain must appear at most once.

          name: Name of the domain ACL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain_acl_id:
            raise ValueError(f"Expected a non-empty value for `domain_acl_id` but received {domain_acl_id!r}")
        return self._put(
            path_template(
                "/accounts/{account_id}/cws/domain-acls/{domain_acl_id}",
                account_id=account_id,
                domain_acl_id=domain_acl_id,
            ),
            body=maybe_transform(
                {
                    "default_action": default_action,
                    "entries": entries,
                    "name": name,
                },
                domain_acl_update_params.DomainACLUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DomainACL]._unwrapper,
            ),
            cast_to=cast(Type[DomainACL], ResultWrapper[DomainACL]),
        )

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        deployment_id: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        name: str | Omit = omit,
        order: Literal["name", "created_at", "updated_at"] | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[DomainACL]:
        """
        Returns a paginated list of domain access control lists in the account.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          cursor: Pagination cursor from previous response

          deployment_id: Filter to domain ACLs attached to this deployment

          direction: Sort direction (default: asc)

          name: Filter by domain ACL name (case-insensitive substring match)

          order: Field to order results by (default: created_at)

          per_page: Number of items per page (1-100, default 20)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/cws/domain-acls", account_id=account_id),
            page=SyncCursorPagination[DomainACL],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "deployment_id": deployment_id,
                        "direction": direction,
                        "name": name,
                        "order": order,
                        "per_page": per_page,
                    },
                    domain_acl_list_params.DomainACLListParams,
                ),
            ),
            model=DomainACL,
        )

    def delete(
        self,
        domain_acl_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainACLDeleteResponse:
        """
        Deletes the domain ACL if it is not attached to a deployment.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          domain_acl_id: ID of the domain ACL to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain_acl_id:
            raise ValueError(f"Expected a non-empty value for `domain_acl_id` but received {domain_acl_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/cws/domain-acls/{domain_acl_id}",
                account_id=account_id,
                domain_acl_id=domain_acl_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DomainACLDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[DomainACLDeleteResponse], ResultWrapper[DomainACLDeleteResponse]),
        )

    def get(
        self,
        domain_acl_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainACL:
        """
        Returns the domain access control list with the specified ID.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          domain_acl_id: ID of the domain ACL to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain_acl_id:
            raise ValueError(f"Expected a non-empty value for `domain_acl_id` but received {domain_acl_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/cws/domain-acls/{domain_acl_id}",
                account_id=account_id,
                domain_acl_id=domain_acl_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DomainACL]._unwrapper,
            ),
            cast_to=cast(Type[DomainACL], ResultWrapper[DomainACL]),
        )


class AsyncDomainACLsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDomainACLsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDomainACLsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDomainACLsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDomainACLsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        default_action: Literal["ALLOW", "BLOCK"],
        entries: Optional[Iterable[domain_acl_create_params.Entry]],
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainACL:
        """
        Creates a domain access control list with its default action and entries.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          default_action: Default action when no entry matches

          entries: Domain entries for this ACL. Each domain must appear at most once.

          name: Name of the domain ACL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/cws/domain-acls", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "default_action": default_action,
                    "entries": entries,
                    "name": name,
                },
                domain_acl_create_params.DomainACLCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DomainACL]._unwrapper,
            ),
            cast_to=cast(Type[DomainACL], ResultWrapper[DomainACL]),
        )

    async def update(
        self,
        domain_acl_id: str,
        *,
        account_id: str,
        default_action: Literal["ALLOW", "BLOCK"],
        entries: Optional[Iterable[domain_acl_update_params.Entry]],
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainACL:
        """
        Replaces the domain access control list's name, default action, and entries.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          domain_acl_id: ID of the domain ACL to update

          default_action: Default action when no entry matches

          entries: Replacement set of domain entries. Each domain must appear at most once.

          name: Name of the domain ACL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain_acl_id:
            raise ValueError(f"Expected a non-empty value for `domain_acl_id` but received {domain_acl_id!r}")
        return await self._put(
            path_template(
                "/accounts/{account_id}/cws/domain-acls/{domain_acl_id}",
                account_id=account_id,
                domain_acl_id=domain_acl_id,
            ),
            body=await async_maybe_transform(
                {
                    "default_action": default_action,
                    "entries": entries,
                    "name": name,
                },
                domain_acl_update_params.DomainACLUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DomainACL]._unwrapper,
            ),
            cast_to=cast(Type[DomainACL], ResultWrapper[DomainACL]),
        )

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        deployment_id: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        name: str | Omit = omit,
        order: Literal["name", "created_at", "updated_at"] | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[DomainACL, AsyncCursorPagination[DomainACL]]:
        """
        Returns a paginated list of domain access control lists in the account.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          cursor: Pagination cursor from previous response

          deployment_id: Filter to domain ACLs attached to this deployment

          direction: Sort direction (default: asc)

          name: Filter by domain ACL name (case-insensitive substring match)

          order: Field to order results by (default: created_at)

          per_page: Number of items per page (1-100, default 20)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/cws/domain-acls", account_id=account_id),
            page=AsyncCursorPagination[DomainACL],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "deployment_id": deployment_id,
                        "direction": direction,
                        "name": name,
                        "order": order,
                        "per_page": per_page,
                    },
                    domain_acl_list_params.DomainACLListParams,
                ),
            ),
            model=DomainACL,
        )

    async def delete(
        self,
        domain_acl_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainACLDeleteResponse:
        """
        Deletes the domain ACL if it is not attached to a deployment.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          domain_acl_id: ID of the domain ACL to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain_acl_id:
            raise ValueError(f"Expected a non-empty value for `domain_acl_id` but received {domain_acl_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/cws/domain-acls/{domain_acl_id}",
                account_id=account_id,
                domain_acl_id=domain_acl_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DomainACLDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[DomainACLDeleteResponse], ResultWrapper[DomainACLDeleteResponse]),
        )

    async def get(
        self,
        domain_acl_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainACL:
        """
        Returns the domain access control list with the specified ID.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          domain_acl_id: ID of the domain ACL to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain_acl_id:
            raise ValueError(f"Expected a non-empty value for `domain_acl_id` but received {domain_acl_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/cws/domain-acls/{domain_acl_id}",
                account_id=account_id,
                domain_acl_id=domain_acl_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DomainACL]._unwrapper,
            ),
            cast_to=cast(Type[DomainACL], ResultWrapper[DomainACL]),
        )


class DomainACLsResourceWithRawResponse:
    def __init__(self, domain_acls: DomainACLsResource) -> None:
        self._domain_acls = domain_acls

        self.create = to_raw_response_wrapper(
            domain_acls.create,
        )
        self.update = to_raw_response_wrapper(
            domain_acls.update,
        )
        self.list = to_raw_response_wrapper(
            domain_acls.list,
        )
        self.delete = to_raw_response_wrapper(
            domain_acls.delete,
        )
        self.get = to_raw_response_wrapper(
            domain_acls.get,
        )


class AsyncDomainACLsResourceWithRawResponse:
    def __init__(self, domain_acls: AsyncDomainACLsResource) -> None:
        self._domain_acls = domain_acls

        self.create = async_to_raw_response_wrapper(
            domain_acls.create,
        )
        self.update = async_to_raw_response_wrapper(
            domain_acls.update,
        )
        self.list = async_to_raw_response_wrapper(
            domain_acls.list,
        )
        self.delete = async_to_raw_response_wrapper(
            domain_acls.delete,
        )
        self.get = async_to_raw_response_wrapper(
            domain_acls.get,
        )


class DomainACLsResourceWithStreamingResponse:
    def __init__(self, domain_acls: DomainACLsResource) -> None:
        self._domain_acls = domain_acls

        self.create = to_streamed_response_wrapper(
            domain_acls.create,
        )
        self.update = to_streamed_response_wrapper(
            domain_acls.update,
        )
        self.list = to_streamed_response_wrapper(
            domain_acls.list,
        )
        self.delete = to_streamed_response_wrapper(
            domain_acls.delete,
        )
        self.get = to_streamed_response_wrapper(
            domain_acls.get,
        )


class AsyncDomainACLsResourceWithStreamingResponse:
    def __init__(self, domain_acls: AsyncDomainACLsResource) -> None:
        self._domain_acls = domain_acls

        self.create = async_to_streamed_response_wrapper(
            domain_acls.create,
        )
        self.update = async_to_streamed_response_wrapper(
            domain_acls.update,
        )
        self.list = async_to_streamed_response_wrapper(
            domain_acls.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            domain_acls.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            domain_acls.get,
        )
