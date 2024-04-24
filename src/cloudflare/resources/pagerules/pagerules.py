# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
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
from ...types.pagerules import (
    pagerule_edit_params,
    pagerule_list_params,
    pagerule_create_params,
    pagerule_update_params,
)
from ...types.pagerules.route_param import RouteParam
from ...types.pagerules.target_param import TargetParam
from ...types.pagerules.pagerule_get_response import PageruleGetResponse
from ...types.pagerules.pagerule_edit_response import PageruleEditResponse
from ...types.pagerules.pagerule_list_response import PageruleListResponse
from ...types.pagerules.pagerule_create_response import PageruleCreateResponse
from ...types.pagerules.pagerule_delete_response import PageruleDeleteResponse
from ...types.pagerules.pagerule_update_response import PageruleUpdateResponse

__all__ = ["PagerulesResource", "AsyncPagerulesResource"]


class PagerulesResource(SyncAPIResource):
    @cached_property
    def settings(self) -> SettingsResource:
        return SettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PagerulesResourceWithRawResponse:
        return PagerulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PagerulesResourceWithStreamingResponse:
        return PagerulesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        actions: Iterable[RouteParam],
        targets: Iterable[TargetParam],
        priority: int | NotGiven = NOT_GIVEN,
        status: Literal["active", "disabled"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageruleCreateResponse:
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
        return cast(
            PageruleCreateResponse,
            self._post(
                f"/zones/{zone_id}/pagerules",
                body=maybe_transform(
                    {
                        "actions": actions,
                        "targets": targets,
                        "priority": priority,
                        "status": status,
                    },
                    pagerule_create_params.PageruleCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[PageruleCreateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[PageruleCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def update(
        self,
        pagerule_id: str,
        *,
        zone_id: str,
        actions: Iterable[RouteParam],
        targets: Iterable[TargetParam],
        priority: int | NotGiven = NOT_GIVEN,
        status: Literal["active", "disabled"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageruleUpdateResponse:
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
        return cast(
            PageruleUpdateResponse,
            self._put(
                f"/zones/{zone_id}/pagerules/{pagerule_id}",
                body=maybe_transform(
                    {
                        "actions": actions,
                        "targets": targets,
                        "priority": priority,
                        "status": status,
                    },
                    pagerule_update_params.PageruleUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[PageruleUpdateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[PageruleUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> PageruleListResponse:
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
                    pagerule_list_params.PageruleListParams,
                ),
                post_parser=ResultWrapper[PageruleListResponse]._unwrapper,
            ),
            cast_to=cast(Type[PageruleListResponse], ResultWrapper[PageruleListResponse]),
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
    ) -> Optional[PageruleDeleteResponse]:
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
                post_parser=ResultWrapper[Optional[PageruleDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PageruleDeleteResponse]], ResultWrapper[PageruleDeleteResponse]),
        )

    def edit(
        self,
        pagerule_id: str,
        *,
        zone_id: str,
        actions: Iterable[RouteParam] | NotGiven = NOT_GIVEN,
        priority: int | NotGiven = NOT_GIVEN,
        status: Literal["active", "disabled"] | NotGiven = NOT_GIVEN,
        targets: Iterable[TargetParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageruleEditResponse:
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
        return cast(
            PageruleEditResponse,
            self._patch(
                f"/zones/{zone_id}/pagerules/{pagerule_id}",
                body=maybe_transform(
                    {
                        "actions": actions,
                        "priority": priority,
                        "status": status,
                        "targets": targets,
                    },
                    pagerule_edit_params.PageruleEditParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[PageruleEditResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[PageruleEditResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> PageruleGetResponse:
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
        return cast(
            PageruleGetResponse,
            self._get(
                f"/zones/{zone_id}/pagerules/{pagerule_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[PageruleGetResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[PageruleGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncPagerulesResource(AsyncAPIResource):
    @cached_property
    def settings(self) -> AsyncSettingsResource:
        return AsyncSettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPagerulesResourceWithRawResponse:
        return AsyncPagerulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPagerulesResourceWithStreamingResponse:
        return AsyncPagerulesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        actions: Iterable[RouteParam],
        targets: Iterable[TargetParam],
        priority: int | NotGiven = NOT_GIVEN,
        status: Literal["active", "disabled"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageruleCreateResponse:
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
        return cast(
            PageruleCreateResponse,
            await self._post(
                f"/zones/{zone_id}/pagerules",
                body=await async_maybe_transform(
                    {
                        "actions": actions,
                        "targets": targets,
                        "priority": priority,
                        "status": status,
                    },
                    pagerule_create_params.PageruleCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[PageruleCreateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[PageruleCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def update(
        self,
        pagerule_id: str,
        *,
        zone_id: str,
        actions: Iterable[RouteParam],
        targets: Iterable[TargetParam],
        priority: int | NotGiven = NOT_GIVEN,
        status: Literal["active", "disabled"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageruleUpdateResponse:
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
        return cast(
            PageruleUpdateResponse,
            await self._put(
                f"/zones/{zone_id}/pagerules/{pagerule_id}",
                body=await async_maybe_transform(
                    {
                        "actions": actions,
                        "targets": targets,
                        "priority": priority,
                        "status": status,
                    },
                    pagerule_update_params.PageruleUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[PageruleUpdateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[PageruleUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> PageruleListResponse:
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
                    pagerule_list_params.PageruleListParams,
                ),
                post_parser=ResultWrapper[PageruleListResponse]._unwrapper,
            ),
            cast_to=cast(Type[PageruleListResponse], ResultWrapper[PageruleListResponse]),
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
    ) -> Optional[PageruleDeleteResponse]:
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
                post_parser=ResultWrapper[Optional[PageruleDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PageruleDeleteResponse]], ResultWrapper[PageruleDeleteResponse]),
        )

    async def edit(
        self,
        pagerule_id: str,
        *,
        zone_id: str,
        actions: Iterable[RouteParam] | NotGiven = NOT_GIVEN,
        priority: int | NotGiven = NOT_GIVEN,
        status: Literal["active", "disabled"] | NotGiven = NOT_GIVEN,
        targets: Iterable[TargetParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageruleEditResponse:
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
        return cast(
            PageruleEditResponse,
            await self._patch(
                f"/zones/{zone_id}/pagerules/{pagerule_id}",
                body=await async_maybe_transform(
                    {
                        "actions": actions,
                        "priority": priority,
                        "status": status,
                        "targets": targets,
                    },
                    pagerule_edit_params.PageruleEditParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[PageruleEditResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[PageruleEditResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> PageruleGetResponse:
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
        return cast(
            PageruleGetResponse,
            await self._get(
                f"/zones/{zone_id}/pagerules/{pagerule_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[PageruleGetResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[PageruleGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class PagerulesResourceWithRawResponse:
    def __init__(self, pagerules: PagerulesResource) -> None:
        self._pagerules = pagerules

        self.create = to_raw_response_wrapper(
            pagerules.create,
        )
        self.update = to_raw_response_wrapper(
            pagerules.update,
        )
        self.list = to_raw_response_wrapper(
            pagerules.list,
        )
        self.delete = to_raw_response_wrapper(
            pagerules.delete,
        )
        self.edit = to_raw_response_wrapper(
            pagerules.edit,
        )
        self.get = to_raw_response_wrapper(
            pagerules.get,
        )

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._pagerules.settings)


class AsyncPagerulesResourceWithRawResponse:
    def __init__(self, pagerules: AsyncPagerulesResource) -> None:
        self._pagerules = pagerules

        self.create = async_to_raw_response_wrapper(
            pagerules.create,
        )
        self.update = async_to_raw_response_wrapper(
            pagerules.update,
        )
        self.list = async_to_raw_response_wrapper(
            pagerules.list,
        )
        self.delete = async_to_raw_response_wrapper(
            pagerules.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            pagerules.edit,
        )
        self.get = async_to_raw_response_wrapper(
            pagerules.get,
        )

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._pagerules.settings)


class PagerulesResourceWithStreamingResponse:
    def __init__(self, pagerules: PagerulesResource) -> None:
        self._pagerules = pagerules

        self.create = to_streamed_response_wrapper(
            pagerules.create,
        )
        self.update = to_streamed_response_wrapper(
            pagerules.update,
        )
        self.list = to_streamed_response_wrapper(
            pagerules.list,
        )
        self.delete = to_streamed_response_wrapper(
            pagerules.delete,
        )
        self.edit = to_streamed_response_wrapper(
            pagerules.edit,
        )
        self.get = to_streamed_response_wrapper(
            pagerules.get,
        )

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._pagerules.settings)


class AsyncPagerulesResourceWithStreamingResponse:
    def __init__(self, pagerules: AsyncPagerulesResource) -> None:
        self._pagerules = pagerules

        self.create = async_to_streamed_response_wrapper(
            pagerules.create,
        )
        self.update = async_to_streamed_response_wrapper(
            pagerules.update,
        )
        self.list = async_to_streamed_response_wrapper(
            pagerules.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            pagerules.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            pagerules.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            pagerules.get,
        )

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._pagerules.settings)
