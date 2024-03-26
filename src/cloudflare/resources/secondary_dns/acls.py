# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from ...types.secondary_dns import (
    ACLListResponse,
    SecondaryDNSACL,
    ACLDeleteResponse,
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
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecondaryDNSACL:
        """
        Create ACL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/secondary_dns/acls",
            body=maybe_transform(body, acl_create_params.ACLCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SecondaryDNSACL], ResultWrapper[SecondaryDNSACL]),
        )

    def update(
        self,
        acl_id: str,
        *,
        account_id: str,
        ip_range: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecondaryDNSACL:
        """
        Modify ACL.

        Args:
          ip_range: Allowed IPv4/IPv6 address range of primary or secondary nameservers. This will
              be applied for the entire account. The IP range is used to allow additional
              NOTIFY IPs for secondary zones and IPs Cloudflare allows AXFR/IXFR requests from
              for primary zones. CIDRs are limited to a maximum of /24 for IPv4 and /64 for
              IPv6 respectively.

          name: The name of the acl.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not acl_id:
            raise ValueError(f"Expected a non-empty value for `acl_id` but received {acl_id!r}")
        return self._put(
            f"/accounts/{account_id}/secondary_dns/acls/{acl_id}",
            body=maybe_transform(
                {
                    "ip_range": ip_range,
                    "name": name,
                },
                acl_update_params.ACLUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SecondaryDNSACL], ResultWrapper[SecondaryDNSACL]),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ACLListResponse]:
        """
        List ACLs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/secondary_dns/acls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ACLListResponse]], ResultWrapper[ACLListResponse]),
        )

    def delete(
        self,
        acl_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACLDeleteResponse:
        """
        Delete ACL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not acl_id:
            raise ValueError(f"Expected a non-empty value for `acl_id` but received {acl_id!r}")
        return self._delete(
            f"/accounts/{account_id}/secondary_dns/acls/{acl_id}",
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
        acl_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecondaryDNSACL:
        """
        Get ACL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not acl_id:
            raise ValueError(f"Expected a non-empty value for `acl_id` but received {acl_id!r}")
        return self._get(
            f"/accounts/{account_id}/secondary_dns/acls/{acl_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SecondaryDNSACL], ResultWrapper[SecondaryDNSACL]),
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
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecondaryDNSACL:
        """
        Create ACL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/secondary_dns/acls",
            body=await async_maybe_transform(body, acl_create_params.ACLCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SecondaryDNSACL], ResultWrapper[SecondaryDNSACL]),
        )

    async def update(
        self,
        acl_id: str,
        *,
        account_id: str,
        ip_range: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecondaryDNSACL:
        """
        Modify ACL.

        Args:
          ip_range: Allowed IPv4/IPv6 address range of primary or secondary nameservers. This will
              be applied for the entire account. The IP range is used to allow additional
              NOTIFY IPs for secondary zones and IPs Cloudflare allows AXFR/IXFR requests from
              for primary zones. CIDRs are limited to a maximum of /24 for IPv4 and /64 for
              IPv6 respectively.

          name: The name of the acl.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not acl_id:
            raise ValueError(f"Expected a non-empty value for `acl_id` but received {acl_id!r}")
        return await self._put(
            f"/accounts/{account_id}/secondary_dns/acls/{acl_id}",
            body=await async_maybe_transform(
                {
                    "ip_range": ip_range,
                    "name": name,
                },
                acl_update_params.ACLUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SecondaryDNSACL], ResultWrapper[SecondaryDNSACL]),
        )

    async def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ACLListResponse]:
        """
        List ACLs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/secondary_dns/acls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ACLListResponse]], ResultWrapper[ACLListResponse]),
        )

    async def delete(
        self,
        acl_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACLDeleteResponse:
        """
        Delete ACL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not acl_id:
            raise ValueError(f"Expected a non-empty value for `acl_id` but received {acl_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/secondary_dns/acls/{acl_id}",
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
        acl_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecondaryDNSACL:
        """
        Get ACL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not acl_id:
            raise ValueError(f"Expected a non-empty value for `acl_id` but received {acl_id!r}")
        return await self._get(
            f"/accounts/{account_id}/secondary_dns/acls/{acl_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SecondaryDNSACL], ResultWrapper[SecondaryDNSACL]),
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
