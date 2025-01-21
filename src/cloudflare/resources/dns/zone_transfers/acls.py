# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.dns.zone_transfers import acl_create_params, acl_update_params
from ....types.dns.zone_transfers.acl import ACL
from ....types.dns.zone_transfers.acl_delete_response import ACLDeleteResponse

__all__ = ["ACLsResource", "AsyncACLsResource"]


class ACLsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ACLsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ACLsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ACLsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ACLsResourceWithStreamingResponse(self)

    def create(
        self,
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
    ) -> Optional[ACL]:
        """
        Create ACL.

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
        return self._post(
            f"/accounts/{account_id}/secondary_dns/acls",
            body=maybe_transform(
                {
                    "ip_range": ip_range,
                    "name": name,
                },
                acl_create_params.ACLCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ACL]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ACL]], ResultWrapper[ACL]),
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
    ) -> Optional[ACL]:
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
                post_parser=ResultWrapper[Optional[ACL]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ACL]], ResultWrapper[ACL]),
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
    ) -> SyncSinglePage[ACL]:
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
        return self._get_api_list(
            f"/accounts/{account_id}/secondary_dns/acls",
            page=SyncSinglePage[ACL],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ACL,
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
    ) -> Optional[ACLDeleteResponse]:
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
                post_parser=ResultWrapper[Optional[ACLDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ACLDeleteResponse]], ResultWrapper[ACLDeleteResponse]),
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
    ) -> Optional[ACL]:
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
                post_parser=ResultWrapper[Optional[ACL]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ACL]], ResultWrapper[ACL]),
        )


class AsyncACLsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncACLsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncACLsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncACLsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncACLsResourceWithStreamingResponse(self)

    async def create(
        self,
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
    ) -> Optional[ACL]:
        """
        Create ACL.

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
        return await self._post(
            f"/accounts/{account_id}/secondary_dns/acls",
            body=await async_maybe_transform(
                {
                    "ip_range": ip_range,
                    "name": name,
                },
                acl_create_params.ACLCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ACL]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ACL]], ResultWrapper[ACL]),
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
    ) -> Optional[ACL]:
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
                post_parser=ResultWrapper[Optional[ACL]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ACL]], ResultWrapper[ACL]),
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
    ) -> AsyncPaginator[ACL, AsyncSinglePage[ACL]]:
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
        return self._get_api_list(
            f"/accounts/{account_id}/secondary_dns/acls",
            page=AsyncSinglePage[ACL],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ACL,
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
    ) -> Optional[ACLDeleteResponse]:
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
                post_parser=ResultWrapper[Optional[ACLDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ACLDeleteResponse]], ResultWrapper[ACLDeleteResponse]),
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
    ) -> Optional[ACL]:
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
                post_parser=ResultWrapper[Optional[ACL]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ACL]], ResultWrapper[ACL]),
        )


class ACLsResourceWithRawResponse:
    def __init__(self, acls: ACLsResource) -> None:
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


class AsyncACLsResourceWithRawResponse:
    def __init__(self, acls: AsyncACLsResource) -> None:
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


class ACLsResourceWithStreamingResponse:
    def __init__(self, acls: ACLsResource) -> None:
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


class AsyncACLsResourceWithStreamingResponse:
    def __init__(self, acls: AsyncACLsResource) -> None:
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
