# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import ResultWrapper
from .._base_client import make_request_options
from ..types.page_rules import (
    page_rule_edit_params,
    page_rule_list_params,
    page_rule_create_params,
    page_rule_update_params,
)
from ..types.page_rules.page_rule import PageRule
from ..types.page_rules.target_param import TargetParam
from ..types.page_rules.page_rule_list_response import PageRuleListResponse
from ..types.page_rules.page_rule_delete_response import PageRuleDeleteResponse

__all__ = ["PageRulesResource", "AsyncPageRulesResource"]


class PageRulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PageRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PageRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PageRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PageRulesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        actions: Iterable[page_rule_create_params.Action],
        targets: Iterable[TargetParam],
        priority: int | NotGiven = NOT_GIVEN,
        status: Literal["active", "disabled"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PageRule]:
        """
        Creates a new Page Rule.

        Args:
          zone_id: Identifier

          actions: The set of actions to perform if the targets of this rule match the request.
              Actions can redirect to another URL or override settings, but not both.

          targets: The rule targets to evaluate on each request.

          priority: The priority of the rule, used to define which Page Rule is processed over
              another. A higher number indicates a higher priority. For example, if you have a
              catch-all Page Rule (rule A: `/images/*`) but want a more specific Page Rule to
              take precedence (rule B: `/images/special/*`), specify a higher priority for
              rule B so it overrides rule A.

          status: The status of the Page Rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/pagerules",
            body=maybe_transform(
                {
                    "actions": actions,
                    "targets": targets,
                    "priority": priority,
                    "status": status,
                },
                page_rule_create_params.PageRuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PageRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PageRule]], ResultWrapper[PageRule]),
        )

    def update(
        self,
        pagerule_id: str,
        *,
        zone_id: str,
        actions: Iterable[page_rule_update_params.Action],
        targets: Iterable[TargetParam],
        priority: int | NotGiven = NOT_GIVEN,
        status: Literal["active", "disabled"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PageRule]:
        """Replaces the configuration of an existing Page Rule.

        The configuration of the
        updated Page Rule will exactly match the data passed in the API request.

        Args:
          zone_id: Identifier

          pagerule_id: Identifier

          actions: The set of actions to perform if the targets of this rule match the request.
              Actions can redirect to another URL or override settings, but not both.

          targets: The rule targets to evaluate on each request.

          priority: The priority of the rule, used to define which Page Rule is processed over
              another. A higher number indicates a higher priority. For example, if you have a
              catch-all Page Rule (rule A: `/images/*`) but want a more specific Page Rule to
              take precedence (rule B: `/images/special/*`), specify a higher priority for
              rule B so it overrides rule A.

          status: The status of the Page Rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not pagerule_id:
            raise ValueError(f"Expected a non-empty value for `pagerule_id` but received {pagerule_id!r}")
        return self._put(
            f"/zones/{zone_id}/pagerules/{pagerule_id}",
            body=maybe_transform(
                {
                    "actions": actions,
                    "targets": targets,
                    "priority": priority,
                    "status": status,
                },
                page_rule_update_params.PageRuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PageRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PageRule]], ResultWrapper[PageRule]),
        )

    def list(
        self,
        *,
        zone_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
        order: Literal["status", "priority"] | NotGiven = NOT_GIVEN,
        status: Literal["active", "disabled"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PageRuleListResponse]:
        """
        Fetches Page Rules in a zone.

        Args:
          zone_id: Identifier

          direction: The direction used to sort returned Page Rules.

          match: When set to `all`, all the search requirements must match. When set to `any`,
              only one of the search requirements has to match.

          order: The field used to sort returned Page Rules.

          status: The status of the Page Rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/pagerules",
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
                        "status": status,
                    },
                    page_rule_list_params.PageRuleListParams,
                ),
                post_parser=ResultWrapper[Optional[PageRuleListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PageRuleListResponse]], ResultWrapper[PageRuleListResponse]),
        )

    def delete(
        self,
        pagerule_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PageRuleDeleteResponse]:
        """
        Deletes an existing Page Rule.

        Args:
          zone_id: Identifier

          pagerule_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not pagerule_id:
            raise ValueError(f"Expected a non-empty value for `pagerule_id` but received {pagerule_id!r}")
        return self._delete(
            f"/zones/{zone_id}/pagerules/{pagerule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PageRuleDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PageRuleDeleteResponse]], ResultWrapper[PageRuleDeleteResponse]),
        )

    def edit(
        self,
        pagerule_id: str,
        *,
        zone_id: str,
        actions: Iterable[page_rule_edit_params.Action] | NotGiven = NOT_GIVEN,
        priority: int | NotGiven = NOT_GIVEN,
        status: Literal["active", "disabled"] | NotGiven = NOT_GIVEN,
        targets: Iterable[TargetParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PageRule]:
        """
        Updates one or more fields of an existing Page Rule.

        Args:
          zone_id: Identifier

          pagerule_id: Identifier

          actions: The set of actions to perform if the targets of this rule match the request.
              Actions can redirect to another URL or override settings, but not both.

          priority: The priority of the rule, used to define which Page Rule is processed over
              another. A higher number indicates a higher priority. For example, if you have a
              catch-all Page Rule (rule A: `/images/*`) but want a more specific Page Rule to
              take precedence (rule B: `/images/special/*`), specify a higher priority for
              rule B so it overrides rule A.

          status: The status of the Page Rule.

          targets: The rule targets to evaluate on each request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not pagerule_id:
            raise ValueError(f"Expected a non-empty value for `pagerule_id` but received {pagerule_id!r}")
        return self._patch(
            f"/zones/{zone_id}/pagerules/{pagerule_id}",
            body=maybe_transform(
                {
                    "actions": actions,
                    "priority": priority,
                    "status": status,
                    "targets": targets,
                },
                page_rule_edit_params.PageRuleEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PageRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PageRule]], ResultWrapper[PageRule]),
        )

    def get(
        self,
        pagerule_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PageRule]:
        """
        Fetches the details of a Page Rule.

        Args:
          zone_id: Identifier

          pagerule_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not pagerule_id:
            raise ValueError(f"Expected a non-empty value for `pagerule_id` but received {pagerule_id!r}")
        return self._get(
            f"/zones/{zone_id}/pagerules/{pagerule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PageRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PageRule]], ResultWrapper[PageRule]),
        )


class AsyncPageRulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPageRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPageRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPageRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPageRulesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        actions: Iterable[page_rule_create_params.Action],
        targets: Iterable[TargetParam],
        priority: int | NotGiven = NOT_GIVEN,
        status: Literal["active", "disabled"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PageRule]:
        """
        Creates a new Page Rule.

        Args:
          zone_id: Identifier

          actions: The set of actions to perform if the targets of this rule match the request.
              Actions can redirect to another URL or override settings, but not both.

          targets: The rule targets to evaluate on each request.

          priority: The priority of the rule, used to define which Page Rule is processed over
              another. A higher number indicates a higher priority. For example, if you have a
              catch-all Page Rule (rule A: `/images/*`) but want a more specific Page Rule to
              take precedence (rule B: `/images/special/*`), specify a higher priority for
              rule B so it overrides rule A.

          status: The status of the Page Rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/pagerules",
            body=await async_maybe_transform(
                {
                    "actions": actions,
                    "targets": targets,
                    "priority": priority,
                    "status": status,
                },
                page_rule_create_params.PageRuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PageRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PageRule]], ResultWrapper[PageRule]),
        )

    async def update(
        self,
        pagerule_id: str,
        *,
        zone_id: str,
        actions: Iterable[page_rule_update_params.Action],
        targets: Iterable[TargetParam],
        priority: int | NotGiven = NOT_GIVEN,
        status: Literal["active", "disabled"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PageRule]:
        """Replaces the configuration of an existing Page Rule.

        The configuration of the
        updated Page Rule will exactly match the data passed in the API request.

        Args:
          zone_id: Identifier

          pagerule_id: Identifier

          actions: The set of actions to perform if the targets of this rule match the request.
              Actions can redirect to another URL or override settings, but not both.

          targets: The rule targets to evaluate on each request.

          priority: The priority of the rule, used to define which Page Rule is processed over
              another. A higher number indicates a higher priority. For example, if you have a
              catch-all Page Rule (rule A: `/images/*`) but want a more specific Page Rule to
              take precedence (rule B: `/images/special/*`), specify a higher priority for
              rule B so it overrides rule A.

          status: The status of the Page Rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not pagerule_id:
            raise ValueError(f"Expected a non-empty value for `pagerule_id` but received {pagerule_id!r}")
        return await self._put(
            f"/zones/{zone_id}/pagerules/{pagerule_id}",
            body=await async_maybe_transform(
                {
                    "actions": actions,
                    "targets": targets,
                    "priority": priority,
                    "status": status,
                },
                page_rule_update_params.PageRuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PageRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PageRule]], ResultWrapper[PageRule]),
        )

    async def list(
        self,
        *,
        zone_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
        order: Literal["status", "priority"] | NotGiven = NOT_GIVEN,
        status: Literal["active", "disabled"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PageRuleListResponse]:
        """
        Fetches Page Rules in a zone.

        Args:
          zone_id: Identifier

          direction: The direction used to sort returned Page Rules.

          match: When set to `all`, all the search requirements must match. When set to `any`,
              only one of the search requirements has to match.

          order: The field used to sort returned Page Rules.

          status: The status of the Page Rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/pagerules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "direction": direction,
                        "match": match,
                        "order": order,
                        "status": status,
                    },
                    page_rule_list_params.PageRuleListParams,
                ),
                post_parser=ResultWrapper[Optional[PageRuleListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PageRuleListResponse]], ResultWrapper[PageRuleListResponse]),
        )

    async def delete(
        self,
        pagerule_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PageRuleDeleteResponse]:
        """
        Deletes an existing Page Rule.

        Args:
          zone_id: Identifier

          pagerule_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not pagerule_id:
            raise ValueError(f"Expected a non-empty value for `pagerule_id` but received {pagerule_id!r}")
        return await self._delete(
            f"/zones/{zone_id}/pagerules/{pagerule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PageRuleDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PageRuleDeleteResponse]], ResultWrapper[PageRuleDeleteResponse]),
        )

    async def edit(
        self,
        pagerule_id: str,
        *,
        zone_id: str,
        actions: Iterable[page_rule_edit_params.Action] | NotGiven = NOT_GIVEN,
        priority: int | NotGiven = NOT_GIVEN,
        status: Literal["active", "disabled"] | NotGiven = NOT_GIVEN,
        targets: Iterable[TargetParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PageRule]:
        """
        Updates one or more fields of an existing Page Rule.

        Args:
          zone_id: Identifier

          pagerule_id: Identifier

          actions: The set of actions to perform if the targets of this rule match the request.
              Actions can redirect to another URL or override settings, but not both.

          priority: The priority of the rule, used to define which Page Rule is processed over
              another. A higher number indicates a higher priority. For example, if you have a
              catch-all Page Rule (rule A: `/images/*`) but want a more specific Page Rule to
              take precedence (rule B: `/images/special/*`), specify a higher priority for
              rule B so it overrides rule A.

          status: The status of the Page Rule.

          targets: The rule targets to evaluate on each request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not pagerule_id:
            raise ValueError(f"Expected a non-empty value for `pagerule_id` but received {pagerule_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/pagerules/{pagerule_id}",
            body=await async_maybe_transform(
                {
                    "actions": actions,
                    "priority": priority,
                    "status": status,
                    "targets": targets,
                },
                page_rule_edit_params.PageRuleEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PageRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PageRule]], ResultWrapper[PageRule]),
        )

    async def get(
        self,
        pagerule_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PageRule]:
        """
        Fetches the details of a Page Rule.

        Args:
          zone_id: Identifier

          pagerule_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not pagerule_id:
            raise ValueError(f"Expected a non-empty value for `pagerule_id` but received {pagerule_id!r}")
        return await self._get(
            f"/zones/{zone_id}/pagerules/{pagerule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PageRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PageRule]], ResultWrapper[PageRule]),
        )


class PageRulesResourceWithRawResponse:
    def __init__(self, page_rules: PageRulesResource) -> None:
        self._page_rules = page_rules

        self.create = to_raw_response_wrapper(
            page_rules.create,
        )
        self.update = to_raw_response_wrapper(
            page_rules.update,
        )
        self.list = to_raw_response_wrapper(
            page_rules.list,
        )
        self.delete = to_raw_response_wrapper(
            page_rules.delete,
        )
        self.edit = to_raw_response_wrapper(
            page_rules.edit,
        )
        self.get = to_raw_response_wrapper(
            page_rules.get,
        )


class AsyncPageRulesResourceWithRawResponse:
    def __init__(self, page_rules: AsyncPageRulesResource) -> None:
        self._page_rules = page_rules

        self.create = async_to_raw_response_wrapper(
            page_rules.create,
        )
        self.update = async_to_raw_response_wrapper(
            page_rules.update,
        )
        self.list = async_to_raw_response_wrapper(
            page_rules.list,
        )
        self.delete = async_to_raw_response_wrapper(
            page_rules.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            page_rules.edit,
        )
        self.get = async_to_raw_response_wrapper(
            page_rules.get,
        )


class PageRulesResourceWithStreamingResponse:
    def __init__(self, page_rules: PageRulesResource) -> None:
        self._page_rules = page_rules

        self.create = to_streamed_response_wrapper(
            page_rules.create,
        )
        self.update = to_streamed_response_wrapper(
            page_rules.update,
        )
        self.list = to_streamed_response_wrapper(
            page_rules.list,
        )
        self.delete = to_streamed_response_wrapper(
            page_rules.delete,
        )
        self.edit = to_streamed_response_wrapper(
            page_rules.edit,
        )
        self.get = to_streamed_response_wrapper(
            page_rules.get,
        )


class AsyncPageRulesResourceWithStreamingResponse:
    def __init__(self, page_rules: AsyncPageRulesResource) -> None:
        self._page_rules = page_rules

        self.create = async_to_streamed_response_wrapper(
            page_rules.create,
        )
        self.update = async_to_streamed_response_wrapper(
            page_rules.update,
        )
        self.list = async_to_streamed_response_wrapper(
            page_rules.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            page_rules.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            page_rules.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            page_rules.get,
        )
