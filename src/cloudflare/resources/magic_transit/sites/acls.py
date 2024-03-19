# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

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
from ....types.magic_transit.sites import (
    ACLGetResponse,
    ACLListResponse,
    ACLCreateResponse,
    ACLDeleteResponse,
    ACLUpdateResponse,
    acl_create_params,
    acl_update_params,
)

__all__ = ["ACLs", "AsyncACLs"]


class ACLs(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ACLsWithRawResponse:
        return ACLsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ACLsWithStreamingResponse:
        return ACLsWithStreamingResponse(self)

    def create(
        self,
        site_id: str,
        *,
        account_id: str,
        acl: acl_create_params.ACL | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACLCreateResponse:
        """
        Creates a new Site ACL.

        Args:
          account_id: Identifier

          site_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        return self._post(
            f"/accounts/{account_id}/magic/sites/{site_id}/acls",
            body=maybe_transform({"acl": acl}, acl_create_params.ACLCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ACLCreateResponse], ResultWrapper[ACLCreateResponse]),
        )

    def update(
        self,
        acl_identifier: str,
        *,
        account_id: str,
        site_id: str,
        acl: acl_update_params.ACL | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACLUpdateResponse:
        """
        Update a specific Site ACL.

        Args:
          account_id: Identifier

          site_id: Identifier

          acl_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if not acl_identifier:
            raise ValueError(f"Expected a non-empty value for `acl_identifier` but received {acl_identifier!r}")
        return self._put(
            f"/accounts/{account_id}/magic/sites/{site_id}/acls/{acl_identifier}",
            body=maybe_transform({"acl": acl}, acl_update_params.ACLUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ACLUpdateResponse], ResultWrapper[ACLUpdateResponse]),
        )

    def list(
        self,
        site_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACLListResponse:
        """
        Lists Site ACLs associated with an account.

        Args:
          account_id: Identifier

          site_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        return self._get(
            f"/accounts/{account_id}/magic/sites/{site_id}/acls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ACLListResponse], ResultWrapper[ACLListResponse]),
        )

    def delete(
        self,
        acl_identifier: str,
        *,
        account_id: str,
        site_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACLDeleteResponse:
        """
        Remove a specific Site ACL.

        Args:
          account_id: Identifier

          site_id: Identifier

          acl_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if not acl_identifier:
            raise ValueError(f"Expected a non-empty value for `acl_identifier` but received {acl_identifier!r}")
        return self._delete(
            f"/accounts/{account_id}/magic/sites/{site_id}/acls/{acl_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ACLDeleteResponse], ResultWrapper[ACLDeleteResponse]),
        )

    def get(
        self,
        acl_identifier: str,
        *,
        account_id: str,
        site_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACLGetResponse:
        """
        Get a specific Site ACL.

        Args:
          account_id: Identifier

          site_id: Identifier

          acl_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if not acl_identifier:
            raise ValueError(f"Expected a non-empty value for `acl_identifier` but received {acl_identifier!r}")
        return self._get(
            f"/accounts/{account_id}/magic/sites/{site_id}/acls/{acl_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ACLGetResponse], ResultWrapper[ACLGetResponse]),
        )


class AsyncACLs(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncACLsWithRawResponse:
        return AsyncACLsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncACLsWithStreamingResponse:
        return AsyncACLsWithStreamingResponse(self)

    async def create(
        self,
        site_id: str,
        *,
        account_id: str,
        acl: acl_create_params.ACL | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACLCreateResponse:
        """
        Creates a new Site ACL.

        Args:
          account_id: Identifier

          site_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        return await self._post(
            f"/accounts/{account_id}/magic/sites/{site_id}/acls",
            body=await async_maybe_transform({"acl": acl}, acl_create_params.ACLCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ACLCreateResponse], ResultWrapper[ACLCreateResponse]),
        )

    async def update(
        self,
        acl_identifier: str,
        *,
        account_id: str,
        site_id: str,
        acl: acl_update_params.ACL | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACLUpdateResponse:
        """
        Update a specific Site ACL.

        Args:
          account_id: Identifier

          site_id: Identifier

          acl_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if not acl_identifier:
            raise ValueError(f"Expected a non-empty value for `acl_identifier` but received {acl_identifier!r}")
        return await self._put(
            f"/accounts/{account_id}/magic/sites/{site_id}/acls/{acl_identifier}",
            body=await async_maybe_transform({"acl": acl}, acl_update_params.ACLUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ACLUpdateResponse], ResultWrapper[ACLUpdateResponse]),
        )

    async def list(
        self,
        site_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACLListResponse:
        """
        Lists Site ACLs associated with an account.

        Args:
          account_id: Identifier

          site_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        return await self._get(
            f"/accounts/{account_id}/magic/sites/{site_id}/acls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ACLListResponse], ResultWrapper[ACLListResponse]),
        )

    async def delete(
        self,
        acl_identifier: str,
        *,
        account_id: str,
        site_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACLDeleteResponse:
        """
        Remove a specific Site ACL.

        Args:
          account_id: Identifier

          site_id: Identifier

          acl_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if not acl_identifier:
            raise ValueError(f"Expected a non-empty value for `acl_identifier` but received {acl_identifier!r}")
        return await self._delete(
            f"/accounts/{account_id}/magic/sites/{site_id}/acls/{acl_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ACLDeleteResponse], ResultWrapper[ACLDeleteResponse]),
        )

    async def get(
        self,
        acl_identifier: str,
        *,
        account_id: str,
        site_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACLGetResponse:
        """
        Get a specific Site ACL.

        Args:
          account_id: Identifier

          site_id: Identifier

          acl_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if not acl_identifier:
            raise ValueError(f"Expected a non-empty value for `acl_identifier` but received {acl_identifier!r}")
        return await self._get(
            f"/accounts/{account_id}/magic/sites/{site_id}/acls/{acl_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ACLGetResponse], ResultWrapper[ACLGetResponse]),
        )


class ACLsWithRawResponse:
    def __init__(self, acls: ACLs) -> None:
        self._acls = acls

        self.create = to_raw_response_wrapper(
            acls.create,
        )
        self.update = to_raw_response_wrapper(
            acls.update,
        )
        self.list = to_raw_response_wrapper(
            acls.list,
        )
        self.delete = to_raw_response_wrapper(
            acls.delete,
        )
        self.get = to_raw_response_wrapper(
            acls.get,
        )


class AsyncACLsWithRawResponse:
    def __init__(self, acls: AsyncACLs) -> None:
        self._acls = acls

        self.create = async_to_raw_response_wrapper(
            acls.create,
        )
        self.update = async_to_raw_response_wrapper(
            acls.update,
        )
        self.list = async_to_raw_response_wrapper(
            acls.list,
        )
        self.delete = async_to_raw_response_wrapper(
            acls.delete,
        )
        self.get = async_to_raw_response_wrapper(
            acls.get,
        )


class ACLsWithStreamingResponse:
    def __init__(self, acls: ACLs) -> None:
        self._acls = acls

        self.create = to_streamed_response_wrapper(
            acls.create,
        )
        self.update = to_streamed_response_wrapper(
            acls.update,
        )
        self.list = to_streamed_response_wrapper(
            acls.list,
        )
        self.delete = to_streamed_response_wrapper(
            acls.delete,
        )
        self.get = to_streamed_response_wrapper(
            acls.get,
        )


class AsyncACLsWithStreamingResponse:
    def __init__(self, acls: AsyncACLs) -> None:
        self._acls = acls

        self.create = async_to_streamed_response_wrapper(
            acls.create,
        )
        self.update = async_to_streamed_response_wrapper(
            acls.update,
        )
        self.list = async_to_streamed_response_wrapper(
            acls.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            acls.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            acls.get,
        )
