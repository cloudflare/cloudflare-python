# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, Iterable, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from .....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ....._base_client import AsyncPaginator, make_request_options
from .....types.zero_trust.access.infrastructure import (
    target_list_params,
    target_create_params,
    target_update_params,
    target_bulk_update_params,
)
from .....types.zero_trust.access.infrastructure.target_get_response import TargetGetResponse
from .....types.zero_trust.access.infrastructure.target_list_response import TargetListResponse
from .....types.zero_trust.access.infrastructure.target_create_response import TargetCreateResponse
from .....types.zero_trust.access.infrastructure.target_update_response import TargetUpdateResponse
from .....types.zero_trust.access.infrastructure.target_bulk_update_response import TargetBulkUpdateResponse

__all__ = ["TargetsResource", "AsyncTargetsResource"]


class TargetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TargetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TargetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TargetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TargetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        hostname: str,
        ip: target_create_params.IP,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TargetCreateResponse]:
        """
        Create new target

        Args:
          account_id: Account identifier

          hostname: A non-unique field that refers to a target. Case insensitive, maximum length of
              255 characters, supports the use of special characters dash and period, does not
              support spaces, and must start and end with an alphanumeric character.

          ip: The IPv4/IPv6 address that identifies where to reach a target

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/infrastructure/targets",
            body=maybe_transform(
                {
                    "hostname": hostname,
                    "ip": ip,
                },
                target_create_params.TargetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TargetCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TargetCreateResponse]], ResultWrapper[TargetCreateResponse]),
        )

    def update(
        self,
        target_id: str,
        *,
        account_id: str,
        hostname: str,
        ip: target_update_params.IP,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TargetUpdateResponse]:
        """
        Update target

        Args:
          account_id: Account identifier

          target_id: Target identifier

          hostname: A non-unique field that refers to a target. Case insensitive, maximum length of
              255 characters, supports the use of special characters dash and period, does not
              support spaces, and must start and end with an alphanumeric character.

          ip: The IPv4/IPv6 address that identifies where to reach a target

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not target_id:
            raise ValueError(f"Expected a non-empty value for `target_id` but received {target_id!r}")
        return self._put(
            f"/accounts/{account_id}/infrastructure/targets/{target_id}",
            body=maybe_transform(
                {
                    "hostname": hostname,
                    "ip": ip,
                },
                target_update_params.TargetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TargetUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TargetUpdateResponse]], ResultWrapper[TargetUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        created_after: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        hostname: Optional[str] | NotGiven = NOT_GIVEN,
        hostname_contains: Optional[str] | NotGiven = NOT_GIVEN,
        ip_like: Optional[str] | NotGiven = NOT_GIVEN,
        ip_v4: Optional[str] | NotGiven = NOT_GIVEN,
        ip_v6: Optional[str] | NotGiven = NOT_GIVEN,
        ips: List[str] | NotGiven = NOT_GIVEN,
        ipv4_end: Optional[str] | NotGiven = NOT_GIVEN,
        ipv4_start: Optional[str] | NotGiven = NOT_GIVEN,
        ipv6_end: Optional[str] | NotGiven = NOT_GIVEN,
        ipv6_start: Optional[str] | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        order: Literal["hostname", "created_at"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        target_ids: List[str] | NotGiven = NOT_GIVEN,
        virtual_network_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[TargetListResponse]:
        """Lists and sorts an account’s targets.

        Filters are optional and are ANDed
        together.

        Args:
          account_id: Account identifier

          created_after: Date and time at which the target was created after (inclusive)

          created_before: Date and time at which the target was created before (inclusive)

          direction: The sorting direction.

          hostname: Hostname of a target

          hostname_contains: Partial match to the hostname of a target

          ip_like: Filters for targets whose IP addresses look like the specified string. Supports
              `*` as a wildcard character

          ip_v4: IPv4 address of the target

          ip_v6: IPv6 address of the target

          ips: Filters for targets that have any of the following IP addresses. Specify `ips`
              multiple times in query parameter to build list of candidates.

          ipv4_end: Defines an IPv4 filter range's ending value (inclusive). Requires `ipv4_start`
              to be specified as well.

          ipv4_start: Defines an IPv4 filter range's starting value (inclusive). Requires `ipv4_end`
              to be specified as well.

          ipv6_end: Defines an IPv6 filter range's ending value (inclusive). Requires `ipv6_start`
              to be specified as well.

          ipv6_start: Defines an IPv6 filter range's starting value (inclusive). Requires `ipv6_end`
              to be specified as well.

          modified_after: Date and time at which the target was modified after (inclusive)

          modified_before: Date and time at which the target was modified before (inclusive)

          order: The field to sort by.

          page: Current page in the response

          per_page: Max amount of entries returned per page

          target_ids: Filters for targets that have any of the following UUIDs. Specify `target_ids`
              multiple times in query parameter to build list of candidates.

          virtual_network_id: Private virtual network identifier of the target

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/infrastructure/targets",
            page=SyncV4PagePaginationArray[TargetListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "hostname": hostname,
                        "hostname_contains": hostname_contains,
                        "ip_like": ip_like,
                        "ip_v4": ip_v4,
                        "ip_v6": ip_v6,
                        "ips": ips,
                        "ipv4_end": ipv4_end,
                        "ipv4_start": ipv4_start,
                        "ipv6_end": ipv6_end,
                        "ipv6_start": ipv6_start,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "target_ids": target_ids,
                        "virtual_network_id": virtual_network_id,
                    },
                    target_list_params.TargetListParams,
                ),
            ),
            model=TargetListResponse,
        )

    def delete(
        self,
        target_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete target

        Args:
          account_id: Account identifier

          target_id: Target identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not target_id:
            raise ValueError(f"Expected a non-empty value for `target_id` but received {target_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/accounts/{account_id}/infrastructure/targets/{target_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def bulk_delete(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Removes one or more targets.

        Args:
          account_id: Account identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/accounts/{account_id}/infrastructure/targets/batch",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def bulk_update(
        self,
        *,
        account_id: str,
        body: Iterable[target_bulk_update_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TargetBulkUpdateResponse:
        """
        Adds one or more targets.

        Args:
          account_id: Account identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._put(
            f"/accounts/{account_id}/infrastructure/targets/batch",
            body=maybe_transform(body, Iterable[target_bulk_update_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TargetBulkUpdateResponse,
        )

    def get(
        self,
        target_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TargetGetResponse]:
        """
        Get target

        Args:
          account_id: Account identifier

          target_id: Target identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not target_id:
            raise ValueError(f"Expected a non-empty value for `target_id` but received {target_id!r}")
        return self._get(
            f"/accounts/{account_id}/infrastructure/targets/{target_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TargetGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TargetGetResponse]], ResultWrapper[TargetGetResponse]),
        )


class AsyncTargetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTargetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTargetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTargetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTargetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        hostname: str,
        ip: target_create_params.IP,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TargetCreateResponse]:
        """
        Create new target

        Args:
          account_id: Account identifier

          hostname: A non-unique field that refers to a target. Case insensitive, maximum length of
              255 characters, supports the use of special characters dash and period, does not
              support spaces, and must start and end with an alphanumeric character.

          ip: The IPv4/IPv6 address that identifies where to reach a target

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/infrastructure/targets",
            body=await async_maybe_transform(
                {
                    "hostname": hostname,
                    "ip": ip,
                },
                target_create_params.TargetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TargetCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TargetCreateResponse]], ResultWrapper[TargetCreateResponse]),
        )

    async def update(
        self,
        target_id: str,
        *,
        account_id: str,
        hostname: str,
        ip: target_update_params.IP,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TargetUpdateResponse]:
        """
        Update target

        Args:
          account_id: Account identifier

          target_id: Target identifier

          hostname: A non-unique field that refers to a target. Case insensitive, maximum length of
              255 characters, supports the use of special characters dash and period, does not
              support spaces, and must start and end with an alphanumeric character.

          ip: The IPv4/IPv6 address that identifies where to reach a target

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not target_id:
            raise ValueError(f"Expected a non-empty value for `target_id` but received {target_id!r}")
        return await self._put(
            f"/accounts/{account_id}/infrastructure/targets/{target_id}",
            body=await async_maybe_transform(
                {
                    "hostname": hostname,
                    "ip": ip,
                },
                target_update_params.TargetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TargetUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TargetUpdateResponse]], ResultWrapper[TargetUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        created_after: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        hostname: Optional[str] | NotGiven = NOT_GIVEN,
        hostname_contains: Optional[str] | NotGiven = NOT_GIVEN,
        ip_like: Optional[str] | NotGiven = NOT_GIVEN,
        ip_v4: Optional[str] | NotGiven = NOT_GIVEN,
        ip_v6: Optional[str] | NotGiven = NOT_GIVEN,
        ips: List[str] | NotGiven = NOT_GIVEN,
        ipv4_end: Optional[str] | NotGiven = NOT_GIVEN,
        ipv4_start: Optional[str] | NotGiven = NOT_GIVEN,
        ipv6_end: Optional[str] | NotGiven = NOT_GIVEN,
        ipv6_start: Optional[str] | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        order: Literal["hostname", "created_at"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        target_ids: List[str] | NotGiven = NOT_GIVEN,
        virtual_network_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[TargetListResponse, AsyncV4PagePaginationArray[TargetListResponse]]:
        """Lists and sorts an account’s targets.

        Filters are optional and are ANDed
        together.

        Args:
          account_id: Account identifier

          created_after: Date and time at which the target was created after (inclusive)

          created_before: Date and time at which the target was created before (inclusive)

          direction: The sorting direction.

          hostname: Hostname of a target

          hostname_contains: Partial match to the hostname of a target

          ip_like: Filters for targets whose IP addresses look like the specified string. Supports
              `*` as a wildcard character

          ip_v4: IPv4 address of the target

          ip_v6: IPv6 address of the target

          ips: Filters for targets that have any of the following IP addresses. Specify `ips`
              multiple times in query parameter to build list of candidates.

          ipv4_end: Defines an IPv4 filter range's ending value (inclusive). Requires `ipv4_start`
              to be specified as well.

          ipv4_start: Defines an IPv4 filter range's starting value (inclusive). Requires `ipv4_end`
              to be specified as well.

          ipv6_end: Defines an IPv6 filter range's ending value (inclusive). Requires `ipv6_start`
              to be specified as well.

          ipv6_start: Defines an IPv6 filter range's starting value (inclusive). Requires `ipv6_end`
              to be specified as well.

          modified_after: Date and time at which the target was modified after (inclusive)

          modified_before: Date and time at which the target was modified before (inclusive)

          order: The field to sort by.

          page: Current page in the response

          per_page: Max amount of entries returned per page

          target_ids: Filters for targets that have any of the following UUIDs. Specify `target_ids`
              multiple times in query parameter to build list of candidates.

          virtual_network_id: Private virtual network identifier of the target

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/infrastructure/targets",
            page=AsyncV4PagePaginationArray[TargetListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "hostname": hostname,
                        "hostname_contains": hostname_contains,
                        "ip_like": ip_like,
                        "ip_v4": ip_v4,
                        "ip_v6": ip_v6,
                        "ips": ips,
                        "ipv4_end": ipv4_end,
                        "ipv4_start": ipv4_start,
                        "ipv6_end": ipv6_end,
                        "ipv6_start": ipv6_start,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "target_ids": target_ids,
                        "virtual_network_id": virtual_network_id,
                    },
                    target_list_params.TargetListParams,
                ),
            ),
            model=TargetListResponse,
        )

    async def delete(
        self,
        target_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete target

        Args:
          account_id: Account identifier

          target_id: Target identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not target_id:
            raise ValueError(f"Expected a non-empty value for `target_id` but received {target_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/accounts/{account_id}/infrastructure/targets/{target_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def bulk_delete(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Removes one or more targets.

        Args:
          account_id: Account identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/accounts/{account_id}/infrastructure/targets/batch",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def bulk_update(
        self,
        *,
        account_id: str,
        body: Iterable[target_bulk_update_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TargetBulkUpdateResponse:
        """
        Adds one or more targets.

        Args:
          account_id: Account identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._put(
            f"/accounts/{account_id}/infrastructure/targets/batch",
            body=await async_maybe_transform(body, Iterable[target_bulk_update_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TargetBulkUpdateResponse,
        )

    async def get(
        self,
        target_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TargetGetResponse]:
        """
        Get target

        Args:
          account_id: Account identifier

          target_id: Target identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not target_id:
            raise ValueError(f"Expected a non-empty value for `target_id` but received {target_id!r}")
        return await self._get(
            f"/accounts/{account_id}/infrastructure/targets/{target_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TargetGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TargetGetResponse]], ResultWrapper[TargetGetResponse]),
        )


class TargetsResourceWithRawResponse:
    def __init__(self, targets: TargetsResource) -> None:
        self._targets = targets

        self.create = to_raw_response_wrapper(
            targets.create,
        )
        self.update = to_raw_response_wrapper(
            targets.update,
        )
        self.list = to_raw_response_wrapper(
            targets.list,
        )
        self.delete = to_raw_response_wrapper(
            targets.delete,
        )
        self.bulk_delete = to_raw_response_wrapper(
            targets.bulk_delete,
        )
        self.bulk_update = to_raw_response_wrapper(
            targets.bulk_update,
        )
        self.get = to_raw_response_wrapper(
            targets.get,
        )


class AsyncTargetsResourceWithRawResponse:
    def __init__(self, targets: AsyncTargetsResource) -> None:
        self._targets = targets

        self.create = async_to_raw_response_wrapper(
            targets.create,
        )
        self.update = async_to_raw_response_wrapper(
            targets.update,
        )
        self.list = async_to_raw_response_wrapper(
            targets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            targets.delete,
        )
        self.bulk_delete = async_to_raw_response_wrapper(
            targets.bulk_delete,
        )
        self.bulk_update = async_to_raw_response_wrapper(
            targets.bulk_update,
        )
        self.get = async_to_raw_response_wrapper(
            targets.get,
        )


class TargetsResourceWithStreamingResponse:
    def __init__(self, targets: TargetsResource) -> None:
        self._targets = targets

        self.create = to_streamed_response_wrapper(
            targets.create,
        )
        self.update = to_streamed_response_wrapper(
            targets.update,
        )
        self.list = to_streamed_response_wrapper(
            targets.list,
        )
        self.delete = to_streamed_response_wrapper(
            targets.delete,
        )
        self.bulk_delete = to_streamed_response_wrapper(
            targets.bulk_delete,
        )
        self.bulk_update = to_streamed_response_wrapper(
            targets.bulk_update,
        )
        self.get = to_streamed_response_wrapper(
            targets.get,
        )


class AsyncTargetsResourceWithStreamingResponse:
    def __init__(self, targets: AsyncTargetsResource) -> None:
        self._targets = targets

        self.create = async_to_streamed_response_wrapper(
            targets.create,
        )
        self.update = async_to_streamed_response_wrapper(
            targets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            targets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            targets.delete,
        )
        self.bulk_delete = async_to_streamed_response_wrapper(
            targets.bulk_delete,
        )
        self.bulk_update = async_to_streamed_response_wrapper(
            targets.bulk_update,
        )
        self.get = async_to_streamed_response_wrapper(
            targets.get,
        )
