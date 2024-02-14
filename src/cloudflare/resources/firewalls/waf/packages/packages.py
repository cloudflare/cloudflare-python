# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .groups import Groups, AsyncGroups

from ....._compat import cached_property

from .rules import Rules, AsyncRules

from .....types.firewalls.waf import PackageListResponse, PackageGetResponse

from typing_extensions import Literal

from ....._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from .....types import shared_params
from .....types.firewalls.waf import package_list_params
from .groups import (
    Groups,
    AsyncGroups,
    GroupsWithRawResponse,
    AsyncGroupsWithRawResponse,
    GroupsWithStreamingResponse,
    AsyncGroupsWithStreamingResponse,
)
from .rules import (
    Rules,
    AsyncRules,
    RulesWithRawResponse,
    AsyncRulesWithRawResponse,
    RulesWithStreamingResponse,
    AsyncRulesWithStreamingResponse,
)
from ....._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Packages", "AsyncPackages"]


class Packages(SyncAPIResource):
    @cached_property
    def groups(self) -> Groups:
        return Groups(self._client)

    @cached_property
    def rules(self) -> Rules:
        return Rules(self._client)

    @cached_property
    def with_raw_response(self) -> PackagesWithRawResponse:
        return PackagesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PackagesWithStreamingResponse:
        return PackagesWithStreamingResponse(self)

    def list(
        self,
        zone_identifier: str,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
        order: Literal["name"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PackageListResponse:
        """
        Fetches WAF packages for a zone.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_identifier: Identifier

          direction: The direction used to sort returned packages.

          match: When set to `all`, all the search requirements must match. When set to `any`,
              only one of the search requirements has to match.

          order: The field used to sort returned packages.

          page: The page number of paginated results.

          per_page: The number of packages per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return cast(
            PackageListResponse,
            self._get(
                f"/zones/{zone_identifier}/firewall/waf/packages",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "direction": direction,
                            "match": match,
                            "order": order,
                            "page": page,
                            "per_page": per_page,
                        },
                        package_list_params.PackageListParams,
                    ),
                ),
                cast_to=cast(
                    Any, PackageListResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        identifier: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PackageGetResponse:
        """
        Fetches the details of a WAF package.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_identifier: Identifier

          identifier: The unique identifier of a WAF package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return cast(
            PackageGetResponse,
            self._get(
                f"/zones/{zone_identifier}/firewall/waf/packages/{identifier}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, PackageGetResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncPackages(AsyncAPIResource):
    @cached_property
    def groups(self) -> AsyncGroups:
        return AsyncGroups(self._client)

    @cached_property
    def rules(self) -> AsyncRules:
        return AsyncRules(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPackagesWithRawResponse:
        return AsyncPackagesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPackagesWithStreamingResponse:
        return AsyncPackagesWithStreamingResponse(self)

    async def list(
        self,
        zone_identifier: str,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
        order: Literal["name"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PackageListResponse:
        """
        Fetches WAF packages for a zone.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_identifier: Identifier

          direction: The direction used to sort returned packages.

          match: When set to `all`, all the search requirements must match. When set to `any`,
              only one of the search requirements has to match.

          order: The field used to sort returned packages.

          page: The page number of paginated results.

          per_page: The number of packages per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return cast(
            PackageListResponse,
            await self._get(
                f"/zones/{zone_identifier}/firewall/waf/packages",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "direction": direction,
                            "match": match,
                            "order": order,
                            "page": page,
                            "per_page": per_page,
                        },
                        package_list_params.PackageListParams,
                    ),
                ),
                cast_to=cast(
                    Any, PackageListResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        identifier: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PackageGetResponse:
        """
        Fetches the details of a WAF package.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_identifier: Identifier

          identifier: The unique identifier of a WAF package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return cast(
            PackageGetResponse,
            await self._get(
                f"/zones/{zone_identifier}/firewall/waf/packages/{identifier}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, PackageGetResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class PackagesWithRawResponse:
    def __init__(self, packages: Packages) -> None:
        self._packages = packages

        self.list = to_raw_response_wrapper(
            packages.list,
        )
        self.get = to_raw_response_wrapper(
            packages.get,
        )

    @cached_property
    def groups(self) -> GroupsWithRawResponse:
        return GroupsWithRawResponse(self._packages.groups)

    @cached_property
    def rules(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self._packages.rules)


class AsyncPackagesWithRawResponse:
    def __init__(self, packages: AsyncPackages) -> None:
        self._packages = packages

        self.list = async_to_raw_response_wrapper(
            packages.list,
        )
        self.get = async_to_raw_response_wrapper(
            packages.get,
        )

    @cached_property
    def groups(self) -> AsyncGroupsWithRawResponse:
        return AsyncGroupsWithRawResponse(self._packages.groups)

    @cached_property
    def rules(self) -> AsyncRulesWithRawResponse:
        return AsyncRulesWithRawResponse(self._packages.rules)


class PackagesWithStreamingResponse:
    def __init__(self, packages: Packages) -> None:
        self._packages = packages

        self.list = to_streamed_response_wrapper(
            packages.list,
        )
        self.get = to_streamed_response_wrapper(
            packages.get,
        )

    @cached_property
    def groups(self) -> GroupsWithStreamingResponse:
        return GroupsWithStreamingResponse(self._packages.groups)

    @cached_property
    def rules(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self._packages.rules)


class AsyncPackagesWithStreamingResponse:
    def __init__(self, packages: AsyncPackages) -> None:
        self._packages = packages

        self.list = async_to_streamed_response_wrapper(
            packages.list,
        )
        self.get = async_to_streamed_response_wrapper(
            packages.get,
        )

    @cached_property
    def groups(self) -> AsyncGroupsWithStreamingResponse:
        return AsyncGroupsWithStreamingResponse(self._packages.groups)

    @cached_property
    def rules(self) -> AsyncRulesWithStreamingResponse:
        return AsyncRulesWithStreamingResponse(self._packages.rules)
