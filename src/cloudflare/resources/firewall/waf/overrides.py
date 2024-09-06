# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.firewall.waf.override import Override

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from ...._base_client import make_request_options, AsyncPaginator

from typing import Type, List, Optional

from ....types.firewall.waf.override_url import OverrideURL

from ....types.firewall.waf.rewrite_action_param import RewriteActionParam

from ....types.firewall.waf.waf_rule_param import WAFRuleParam

from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray

from ....types.firewall.waf.override_delete_response import OverrideDeleteResponse

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.firewall.waf import override_create_params
from ....types.firewall.waf import override_update_params
from ....types.firewall.waf import override_list_params
from ....types.firewall.waf import RewriteAction
from ....types.firewall.waf import WAFRule
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["OverridesResource", "AsyncOverridesResource"]


class OverridesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OverridesResourceWithRawResponse:
        return OverridesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OverridesResourceWithStreamingResponse:
        return OverridesResourceWithStreamingResponse(self)

    def create(
        self,
        zone_identifier: str,
        *,
        urls: List[OverrideURL],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Override:
        """
        Creates a URI-based WAF override for a zone.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_identifier: Identifier

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
            f"/zones/{zone_identifier}/firewall/waf/overrides",
            body=maybe_transform({"urls": urls}, override_create_params.OverrideCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Override]._unwrapper,
            ),
            cast_to=cast(Type[Override], ResultWrapper[Override]),
        )

    def update(
        self,
        zone_identifier: str,
        *,
        path_id: str,
        body_id: str,
        rewrite_action: RewriteActionParam,
        rules: WAFRuleParam,
        urls: List[OverrideURL],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Override:
        """
        Updates an existing URI-based WAF override.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          path_id: The unique identifier of the WAF override.

          zone_identifier: Identifier

          body_id: Identifier

          rewrite_action: Specifies that, when a WAF rule matches, its configured action will be replaced
              by the action configured in this object.

          rules: An object that allows you to override the action of specific WAF rules. Each key
              of this object must be the ID of a WAF rule, and each value must be a valid WAF
              action. Unless you are disabling a rule, ensure that you also enable the rule
              group that this WAF rule belongs to. When creating a new URI-based WAF override,
              you must provide a `groups` object or a `rules` object.

          urls: The URLs to include in the current WAF override. You can use wildcards. Each
              entered URL will be escaped before use, which means you can only use simple
              wildcard patterns.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._put(
            f"/zones/{zone_identifier}/firewall/waf/overrides/{path_id}",
            body=maybe_transform(
                {
                    "id": body_id,
                    "rewrite_action": rewrite_action,
                    "rules": rules,
                    "urls": urls,
                },
                override_update_params.OverrideUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Override]._unwrapper,
            ),
            cast_to=cast(Type[Override], ResultWrapper[Override]),
        )

    def list(
        self,
        zone_identifier: str,
        *,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[Override]:
        """
        Fetches the URI-based WAF overrides in a zone.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_identifier: Identifier

          page: The page number of paginated results.

          per_page: The number of WAF overrides per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get_api_list(
            f"/zones/{zone_identifier}/firewall/waf/overrides",
            page=SyncV4PagePaginationArray[Override],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    override_list_params.OverrideListParams,
                ),
            ),
            model=Override,
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
    ) -> Optional[OverrideDeleteResponse]:
        """
        Deletes an existing URI-based WAF override.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the WAF override.

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
            f"/zones/{zone_identifier}/firewall/waf/overrides/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OverrideDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OverrideDeleteResponse]], ResultWrapper[OverrideDeleteResponse]),
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
    ) -> Override:
        """
        Fetches the details of a URI-based WAF override.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the WAF override.

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
            f"/zones/{zone_identifier}/firewall/waf/overrides/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Override]._unwrapper,
            ),
            cast_to=cast(Type[Override], ResultWrapper[Override]),
        )


class AsyncOverridesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOverridesResourceWithRawResponse:
        return AsyncOverridesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOverridesResourceWithStreamingResponse:
        return AsyncOverridesResourceWithStreamingResponse(self)

    async def create(
        self,
        zone_identifier: str,
        *,
        urls: List[OverrideURL],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Override:
        """
        Creates a URI-based WAF override for a zone.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_identifier: Identifier

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
            f"/zones/{zone_identifier}/firewall/waf/overrides",
            body=await async_maybe_transform({"urls": urls}, override_create_params.OverrideCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Override]._unwrapper,
            ),
            cast_to=cast(Type[Override], ResultWrapper[Override]),
        )

    async def update(
        self,
        zone_identifier: str,
        *,
        path_id: str,
        body_id: str,
        rewrite_action: RewriteActionParam,
        rules: WAFRuleParam,
        urls: List[OverrideURL],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Override:
        """
        Updates an existing URI-based WAF override.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          path_id: The unique identifier of the WAF override.

          zone_identifier: Identifier

          body_id: Identifier

          rewrite_action: Specifies that, when a WAF rule matches, its configured action will be replaced
              by the action configured in this object.

          rules: An object that allows you to override the action of specific WAF rules. Each key
              of this object must be the ID of a WAF rule, and each value must be a valid WAF
              action. Unless you are disabling a rule, ensure that you also enable the rule
              group that this WAF rule belongs to. When creating a new URI-based WAF override,
              you must provide a `groups` object or a `rules` object.

          urls: The URLs to include in the current WAF override. You can use wildcards. Each
              entered URL will be escaped before use, which means you can only use simple
              wildcard patterns.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._put(
            f"/zones/{zone_identifier}/firewall/waf/overrides/{path_id}",
            body=await async_maybe_transform(
                {
                    "id": body_id,
                    "rewrite_action": rewrite_action,
                    "rules": rules,
                    "urls": urls,
                },
                override_update_params.OverrideUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Override]._unwrapper,
            ),
            cast_to=cast(Type[Override], ResultWrapper[Override]),
        )

    def list(
        self,
        zone_identifier: str,
        *,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Override, AsyncV4PagePaginationArray[Override]]:
        """
        Fetches the URI-based WAF overrides in a zone.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_identifier: Identifier

          page: The page number of paginated results.

          per_page: The number of WAF overrides per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get_api_list(
            f"/zones/{zone_identifier}/firewall/waf/overrides",
            page=AsyncV4PagePaginationArray[Override],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    override_list_params.OverrideListParams,
                ),
            ),
            model=Override,
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
    ) -> Optional[OverrideDeleteResponse]:
        """
        Deletes an existing URI-based WAF override.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the WAF override.

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
            f"/zones/{zone_identifier}/firewall/waf/overrides/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OverrideDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OverrideDeleteResponse]], ResultWrapper[OverrideDeleteResponse]),
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
    ) -> Override:
        """
        Fetches the details of a URI-based WAF override.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the WAF override.

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
            f"/zones/{zone_identifier}/firewall/waf/overrides/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Override]._unwrapper,
            ),
            cast_to=cast(Type[Override], ResultWrapper[Override]),
        )


class OverridesResourceWithRawResponse:
    def __init__(self, overrides: OverridesResource) -> None:
        self._overrides = overrides

        self.create = to_raw_response_wrapper(
            overrides.create,
        )
        self.update = to_raw_response_wrapper(
            overrides.update,
        )
        self.list = to_raw_response_wrapper(
            overrides.list,
        )
        self.delete = to_raw_response_wrapper(
            overrides.delete,
        )
        self.get = to_raw_response_wrapper(
            overrides.get,
        )


class AsyncOverridesResourceWithRawResponse:
    def __init__(self, overrides: AsyncOverridesResource) -> None:
        self._overrides = overrides

        self.create = async_to_raw_response_wrapper(
            overrides.create,
        )
        self.update = async_to_raw_response_wrapper(
            overrides.update,
        )
        self.list = async_to_raw_response_wrapper(
            overrides.list,
        )
        self.delete = async_to_raw_response_wrapper(
            overrides.delete,
        )
        self.get = async_to_raw_response_wrapper(
            overrides.get,
        )


class OverridesResourceWithStreamingResponse:
    def __init__(self, overrides: OverridesResource) -> None:
        self._overrides = overrides

        self.create = to_streamed_response_wrapper(
            overrides.create,
        )
        self.update = to_streamed_response_wrapper(
            overrides.update,
        )
        self.list = to_streamed_response_wrapper(
            overrides.list,
        )
        self.delete = to_streamed_response_wrapper(
            overrides.delete,
        )
        self.get = to_streamed_response_wrapper(
            overrides.get,
        )


class AsyncOverridesResourceWithStreamingResponse:
    def __init__(self, overrides: AsyncOverridesResource) -> None:
        self._overrides = overrides

        self.create = async_to_streamed_response_wrapper(
            overrides.create,
        )
        self.update = async_to_streamed_response_wrapper(
            overrides.update,
        )
        self.list = async_to_streamed_response_wrapper(
            overrides.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            overrides.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            overrides.get,
        )
