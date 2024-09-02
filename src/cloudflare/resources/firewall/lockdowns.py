# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.firewall.lockdown import Lockdown

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from ..._base_client import make_request_options, AsyncPaginator

from typing import Type, List, Union, Optional

from ...types.firewall.configuration_param import ConfigurationParam

from ...types.firewall.waf.override_url import OverrideURL

from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray

from datetime import datetime

from ...types.firewall.lockdown_delete_response import LockdownDeleteResponse

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from ...types.firewall import lockdown_create_params
from ...types.firewall import lockdown_update_params
from ...types.firewall import lockdown_list_params
from ...types.firewall import Configuration
from ...types.firewall import Configuration
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["LockdownsResource", "AsyncLockdownsResource"]


class LockdownsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LockdownsResourceWithRawResponse:
        return LockdownsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LockdownsResourceWithStreamingResponse:
        return LockdownsResourceWithStreamingResponse(self)

    def create(
        self,
        zone_identifier: str,
        *,
        configurations: ConfigurationParam,
        urls: List[OverrideURL],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Lockdown:
        """
        Creates a new Zone Lockdown rule.

        Args:
          zone_identifier: Identifier

          configurations: A list of IP addresses or CIDR ranges that will be allowed to access the URLs
              specified in the Zone Lockdown rule. You can include any number of `ip` or
              `ip_range` configurations.

          urls: The URLs to include in the current WAF override. You can use wildcards. Each
              entered URL will be escaped before use, which means you can only use simple
              wildcard patterns.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._post(
            f"/zones/{zone_identifier}/firewall/lockdowns",
            body=maybe_transform(
                {
                    "configurations": configurations,
                    "urls": urls,
                },
                lockdown_create_params.LockdownCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Lockdown]._unwrapper,
            ),
            cast_to=cast(Type[Lockdown], ResultWrapper[Lockdown]),
        )

    def update(
        self,
        id: str,
        *,
        zone_identifier: str,
        configurations: ConfigurationParam,
        urls: List[OverrideURL],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Lockdown:
        """
        Updates an existing Zone Lockdown rule.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the Zone Lockdown rule.

          configurations: A list of IP addresses or CIDR ranges that will be allowed to access the URLs
              specified in the Zone Lockdown rule. You can include any number of `ip` or
              `ip_range` configurations.

          urls: The URLs to include in the current WAF override. You can use wildcards. Each
              entered URL will be escaped before use, which means you can only use simple
              wildcard patterns.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/zones/{zone_identifier}/firewall/lockdowns/{id}",
            body=maybe_transform(
                {
                    "configurations": configurations,
                    "urls": urls,
                },
                lockdown_update_params.LockdownUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Lockdown]._unwrapper,
            ),
            cast_to=cast(Type[Lockdown], ResultWrapper[Lockdown]),
        )

    def list(
        self,
        zone_identifier: str,
        *,
        created_on: Union[str, datetime] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        description_search: str | NotGiven = NOT_GIVEN,
        ip: str | NotGiven = NOT_GIVEN,
        ip_range_search: str | NotGiven = NOT_GIVEN,
        ip_search: str | NotGiven = NOT_GIVEN,
        modified_on: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        uri_search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[Lockdown]:
        """Fetches Zone Lockdown rules.

        You can filter the results using several optional
        parameters.

        Args:
          zone_identifier: Identifier

          created_on: The timestamp of when the rule was created.

          description: A string to search for in the description of existing rules.

          description_search: A string to search for in the description of existing rules.

          ip: A single IP address to search for in existing rules.

          ip_range_search: A single IP address range to search for in existing rules.

          ip_search: A single IP address to search for in existing rules.

          modified_on: The timestamp of when the rule was last modified.

          page: Page number of paginated results.

          per_page: The maximum number of results per page. You can only set the value to `1` or to
              a multiple of 5 such as `5`, `10`, `15`, or `20`.

          priority: The priority of the rule to control the processing order. A lower number
              indicates higher priority. If not provided, any rules with a configured priority
              will be processed before rules without a priority.

          uri_search: A single URI to search for in the list of URLs of existing rules.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get_api_list(
            f"/zones/{zone_identifier}/firewall/lockdowns",
            page=SyncV4PagePaginationArray[Lockdown],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_on": created_on,
                        "description": description,
                        "description_search": description_search,
                        "ip": ip,
                        "ip_range_search": ip_range_search,
                        "ip_search": ip_search,
                        "modified_on": modified_on,
                        "page": page,
                        "per_page": per_page,
                        "priority": priority,
                        "uri_search": uri_search,
                    },
                    lockdown_list_params.LockdownListParams,
                ),
            ),
            model=Lockdown,
        )

    def delete(
        self,
        id: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[LockdownDeleteResponse]:
        """
        Deletes an existing Zone Lockdown rule.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the Zone Lockdown rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/zones/{zone_identifier}/firewall/lockdowns/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[LockdownDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[LockdownDeleteResponse]], ResultWrapper[LockdownDeleteResponse]),
        )

    def get(
        self,
        id: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Lockdown:
        """
        Fetches the details of a Zone Lockdown rule.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the Zone Lockdown rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/zones/{zone_identifier}/firewall/lockdowns/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Lockdown]._unwrapper,
            ),
            cast_to=cast(Type[Lockdown], ResultWrapper[Lockdown]),
        )


class AsyncLockdownsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLockdownsResourceWithRawResponse:
        return AsyncLockdownsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLockdownsResourceWithStreamingResponse:
        return AsyncLockdownsResourceWithStreamingResponse(self)

    async def create(
        self,
        zone_identifier: str,
        *,
        configurations: ConfigurationParam,
        urls: List[OverrideURL],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Lockdown:
        """
        Creates a new Zone Lockdown rule.

        Args:
          zone_identifier: Identifier

          configurations: A list of IP addresses or CIDR ranges that will be allowed to access the URLs
              specified in the Zone Lockdown rule. You can include any number of `ip` or
              `ip_range` configurations.

          urls: The URLs to include in the current WAF override. You can use wildcards. Each
              entered URL will be escaped before use, which means you can only use simple
              wildcard patterns.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._post(
            f"/zones/{zone_identifier}/firewall/lockdowns",
            body=await async_maybe_transform(
                {
                    "configurations": configurations,
                    "urls": urls,
                },
                lockdown_create_params.LockdownCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Lockdown]._unwrapper,
            ),
            cast_to=cast(Type[Lockdown], ResultWrapper[Lockdown]),
        )

    async def update(
        self,
        id: str,
        *,
        zone_identifier: str,
        configurations: ConfigurationParam,
        urls: List[OverrideURL],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Lockdown:
        """
        Updates an existing Zone Lockdown rule.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the Zone Lockdown rule.

          configurations: A list of IP addresses or CIDR ranges that will be allowed to access the URLs
              specified in the Zone Lockdown rule. You can include any number of `ip` or
              `ip_range` configurations.

          urls: The URLs to include in the current WAF override. You can use wildcards. Each
              entered URL will be escaped before use, which means you can only use simple
              wildcard patterns.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/zones/{zone_identifier}/firewall/lockdowns/{id}",
            body=await async_maybe_transform(
                {
                    "configurations": configurations,
                    "urls": urls,
                },
                lockdown_update_params.LockdownUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Lockdown]._unwrapper,
            ),
            cast_to=cast(Type[Lockdown], ResultWrapper[Lockdown]),
        )

    def list(
        self,
        zone_identifier: str,
        *,
        created_on: Union[str, datetime] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        description_search: str | NotGiven = NOT_GIVEN,
        ip: str | NotGiven = NOT_GIVEN,
        ip_range_search: str | NotGiven = NOT_GIVEN,
        ip_search: str | NotGiven = NOT_GIVEN,
        modified_on: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        uri_search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Lockdown, AsyncV4PagePaginationArray[Lockdown]]:
        """Fetches Zone Lockdown rules.

        You can filter the results using several optional
        parameters.

        Args:
          zone_identifier: Identifier

          created_on: The timestamp of when the rule was created.

          description: A string to search for in the description of existing rules.

          description_search: A string to search for in the description of existing rules.

          ip: A single IP address to search for in existing rules.

          ip_range_search: A single IP address range to search for in existing rules.

          ip_search: A single IP address to search for in existing rules.

          modified_on: The timestamp of when the rule was last modified.

          page: Page number of paginated results.

          per_page: The maximum number of results per page. You can only set the value to `1` or to
              a multiple of 5 such as `5`, `10`, `15`, or `20`.

          priority: The priority of the rule to control the processing order. A lower number
              indicates higher priority. If not provided, any rules with a configured priority
              will be processed before rules without a priority.

          uri_search: A single URI to search for in the list of URLs of existing rules.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get_api_list(
            f"/zones/{zone_identifier}/firewall/lockdowns",
            page=AsyncV4PagePaginationArray[Lockdown],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_on": created_on,
                        "description": description,
                        "description_search": description_search,
                        "ip": ip,
                        "ip_range_search": ip_range_search,
                        "ip_search": ip_search,
                        "modified_on": modified_on,
                        "page": page,
                        "per_page": per_page,
                        "priority": priority,
                        "uri_search": uri_search,
                    },
                    lockdown_list_params.LockdownListParams,
                ),
            ),
            model=Lockdown,
        )

    async def delete(
        self,
        id: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[LockdownDeleteResponse]:
        """
        Deletes an existing Zone Lockdown rule.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the Zone Lockdown rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/zones/{zone_identifier}/firewall/lockdowns/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[LockdownDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[LockdownDeleteResponse]], ResultWrapper[LockdownDeleteResponse]),
        )

    async def get(
        self,
        id: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Lockdown:
        """
        Fetches the details of a Zone Lockdown rule.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the Zone Lockdown rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/zones/{zone_identifier}/firewall/lockdowns/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Lockdown]._unwrapper,
            ),
            cast_to=cast(Type[Lockdown], ResultWrapper[Lockdown]),
        )


class LockdownsResourceWithRawResponse:
    def __init__(self, lockdowns: LockdownsResource) -> None:
        self._lockdowns = lockdowns

        self.create = to_raw_response_wrapper(
            lockdowns.create,
        )
        self.update = to_raw_response_wrapper(
            lockdowns.update,
        )
        self.list = to_raw_response_wrapper(
            lockdowns.list,
        )
        self.delete = to_raw_response_wrapper(
            lockdowns.delete,
        )
        self.get = to_raw_response_wrapper(
            lockdowns.get,
        )


class AsyncLockdownsResourceWithRawResponse:
    def __init__(self, lockdowns: AsyncLockdownsResource) -> None:
        self._lockdowns = lockdowns

        self.create = async_to_raw_response_wrapper(
            lockdowns.create,
        )
        self.update = async_to_raw_response_wrapper(
            lockdowns.update,
        )
        self.list = async_to_raw_response_wrapper(
            lockdowns.list,
        )
        self.delete = async_to_raw_response_wrapper(
            lockdowns.delete,
        )
        self.get = async_to_raw_response_wrapper(
            lockdowns.get,
        )


class LockdownsResourceWithStreamingResponse:
    def __init__(self, lockdowns: LockdownsResource) -> None:
        self._lockdowns = lockdowns

        self.create = to_streamed_response_wrapper(
            lockdowns.create,
        )
        self.update = to_streamed_response_wrapper(
            lockdowns.update,
        )
        self.list = to_streamed_response_wrapper(
            lockdowns.list,
        )
        self.delete = to_streamed_response_wrapper(
            lockdowns.delete,
        )
        self.get = to_streamed_response_wrapper(
            lockdowns.get,
        )


class AsyncLockdownsResourceWithStreamingResponse:
    def __init__(self, lockdowns: AsyncLockdownsResource) -> None:
        self._lockdowns = lockdowns

        self.create = async_to_streamed_response_wrapper(
            lockdowns.create,
        )
        self.update = async_to_streamed_response_wrapper(
            lockdowns.update,
        )
        self.list = async_to_streamed_response_wrapper(
            lockdowns.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            lockdowns.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            lockdowns.get,
        )
