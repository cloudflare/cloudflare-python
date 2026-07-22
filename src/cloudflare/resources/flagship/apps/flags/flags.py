# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Type, Union, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from .changelog import (
    ChangelogResource,
    AsyncChangelogResource,
    ChangelogResourceWithRawResponse,
    AsyncChangelogResourceWithRawResponse,
    ChangelogResourceWithStreamingResponse,
    AsyncChangelogResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from .....pagination import SyncCursorPaginationAfter, AsyncCursorPaginationAfter
from ....._base_client import AsyncPaginator, make_request_options
from .....types.flagship.apps import flag_list_params, flag_create_params, flag_update_params
from .....types.flagship.apps.flag_get_response import FlagGetResponse
from .....types.flagship.apps.flag_list_response import FlagListResponse
from .....types.flagship.apps.flag_create_response import FlagCreateResponse
from .....types.flagship.apps.flag_delete_response import FlagDeleteResponse
from .....types.flagship.apps.flag_update_response import FlagUpdateResponse

__all__ = ["FlagsResource", "AsyncFlagsResource"]


class FlagsResource(SyncAPIResource):
    @cached_property
    def changelog(self) -> ChangelogResource:
        return ChangelogResource(self._client)

    @cached_property
    def with_raw_response(self) -> FlagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return FlagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FlagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return FlagsResourceWithStreamingResponse(self)

    def create(
        self,
        app_id: str,
        *,
        account_id: str,
        default_variation: str,
        enabled: bool,
        key: str,
        rules: Iterable[flag_create_params.Rule],
        variations: Dict[str, Union[Optional[str], float, bool, Dict[str, object], Iterable[object]]],
        description: Optional[str] | Omit = omit,
        type: Literal["boolean", "string", "number", "json"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlagCreateResponse:
        """Creates a flag.

        Returns 409 if the key already exists. `type` is inferred from
        variation values and may be omitted.

        Args:
          account_id: Cloudflare account ID.

          app_id: App identifier.

          default_variation: Variation the API serves when the flag is off, or when it's on but no rule
              matches the context. Must be a key in `variations`.

          enabled: When false, the flag bypasses all rules and always serves `default_variation`.

          key: Unique identifier for the flag within an app. Used in all evaluation and SDK
              calls.

          rules: Targeting rules evaluated in ascending `priority`; the first matching rule wins.
              An empty array means the flag always serves `default_variation`.

          variations: Map of variation name to value. All values share the same type (boolean, string,
              number, or JSON object/array), and each serialized value stays within 10KB.

          type: Value type of the flag's variations. The API infers this from the variation
              values on write, so you can omit it in requests.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/flagship/apps/{app_id}/flags", account_id=account_id, app_id=app_id),
            body=maybe_transform(
                {
                    "default_variation": default_variation,
                    "enabled": enabled,
                    "key": key,
                    "rules": rules,
                    "variations": variations,
                    "description": description,
                    "type": type,
                },
                flag_create_params.FlagCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FlagCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[FlagCreateResponse], ResultWrapper[FlagCreateResponse]),
        )

    def update(
        self,
        flag_key: str,
        *,
        account_id: str,
        app_id: str,
        default_variation: str,
        enabled: bool,
        key: str,
        rules: Iterable[flag_update_params.Rule],
        variations: Dict[str, Union[Optional[str], float, bool, Dict[str, object], Iterable[object]]],
        description: Optional[str] | Omit = omit,
        type: Literal["boolean", "string", "number", "json"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlagUpdateResponse:
        """Replaces the entire flag definition.

        Omitted fields are dropped, not preserved —
        read before writing. Each update appends a changelog entry.

        Args:
          account_id: Cloudflare account ID.

          app_id: App identifier.

          flag_key: Flag key (slug).

          default_variation: Variation the API serves when the flag is off, or when it's on but no rule
              matches the context. Must be a key in `variations`.

          enabled: When false, the flag bypasses all rules and always serves `default_variation`.

          key: Unique identifier for the flag within an app. Used in all evaluation and SDK
              calls.

          rules: Targeting rules evaluated in ascending `priority`; the first matching rule wins.
              An empty array means the flag always serves `default_variation`.

          variations: Map of variation name to value. All values share the same type (boolean, string,
              number, or JSON object/array), and each serialized value stays within 10KB.

          type: Value type of the flag's variations. The API infers this from the variation
              values on write, so you can omit it in requests.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not flag_key:
            raise ValueError(f"Expected a non-empty value for `flag_key` but received {flag_key!r}")
        return self._put(
            path_template(
                "/accounts/{account_id}/flagship/apps/{app_id}/flags/{flag_key}",
                account_id=account_id,
                app_id=app_id,
                flag_key=flag_key,
            ),
            body=maybe_transform(
                {
                    "default_variation": default_variation,
                    "enabled": enabled,
                    "key": key,
                    "rules": rules,
                    "variations": variations,
                    "description": description,
                    "type": type,
                },
                flag_update_params.FlagUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FlagUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[FlagUpdateResponse], ResultWrapper[FlagUpdateResponse]),
        )

    def list(
        self,
        app_id: str,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        limit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPaginationAfter[FlagListResponse]:
        """Lists an app's flags ordered by key.

        Pass `cursor` from `result_info` to page
        forward; a null cursor indicates the last page.

        Args:
          account_id: Cloudflare account ID.

          app_id: App identifier.

          cursor: Pagination cursor from a previous response.

          limit: Max items to return (1–200).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/flagship/apps/{app_id}/flags", account_id=account_id, app_id=app_id),
            page=SyncCursorPaginationAfter[FlagListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    flag_list_params.FlagListParams,
                ),
            ),
            model=FlagListResponse,
        )

    def delete(
        self,
        flag_key: str,
        *,
        account_id: str,
        app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlagDeleteResponse:
        """Deletes a flag permanently.

        Subsequent evaluations fall back to the
        caller-supplied default. Cannot be undone.

        Args:
          account_id: Cloudflare account ID.

          app_id: App identifier.

          flag_key: Flag key (slug).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not flag_key:
            raise ValueError(f"Expected a non-empty value for `flag_key` but received {flag_key!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/flagship/apps/{app_id}/flags/{flag_key}",
                account_id=account_id,
                app_id=app_id,
                flag_key=flag_key,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FlagDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[FlagDeleteResponse], ResultWrapper[FlagDeleteResponse]),
        )

    def get(
        self,
        flag_key: str,
        *,
        account_id: str,
        app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlagGetResponse:
        """
        Returns the full flag definition including rules, variations, and audit fields.

        Args:
          account_id: Cloudflare account ID.

          app_id: App identifier.

          flag_key: Flag key (slug).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not flag_key:
            raise ValueError(f"Expected a non-empty value for `flag_key` but received {flag_key!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/flagship/apps/{app_id}/flags/{flag_key}",
                account_id=account_id,
                app_id=app_id,
                flag_key=flag_key,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FlagGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[FlagGetResponse], ResultWrapper[FlagGetResponse]),
        )


class AsyncFlagsResource(AsyncAPIResource):
    @cached_property
    def changelog(self) -> AsyncChangelogResource:
        return AsyncChangelogResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFlagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFlagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFlagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncFlagsResourceWithStreamingResponse(self)

    async def create(
        self,
        app_id: str,
        *,
        account_id: str,
        default_variation: str,
        enabled: bool,
        key: str,
        rules: Iterable[flag_create_params.Rule],
        variations: Dict[str, Union[Optional[str], float, bool, Dict[str, object], Iterable[object]]],
        description: Optional[str] | Omit = omit,
        type: Literal["boolean", "string", "number", "json"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlagCreateResponse:
        """Creates a flag.

        Returns 409 if the key already exists. `type` is inferred from
        variation values and may be omitted.

        Args:
          account_id: Cloudflare account ID.

          app_id: App identifier.

          default_variation: Variation the API serves when the flag is off, or when it's on but no rule
              matches the context. Must be a key in `variations`.

          enabled: When false, the flag bypasses all rules and always serves `default_variation`.

          key: Unique identifier for the flag within an app. Used in all evaluation and SDK
              calls.

          rules: Targeting rules evaluated in ascending `priority`; the first matching rule wins.
              An empty array means the flag always serves `default_variation`.

          variations: Map of variation name to value. All values share the same type (boolean, string,
              number, or JSON object/array), and each serialized value stays within 10KB.

          type: Value type of the flag's variations. The API infers this from the variation
              values on write, so you can omit it in requests.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/flagship/apps/{app_id}/flags", account_id=account_id, app_id=app_id),
            body=await async_maybe_transform(
                {
                    "default_variation": default_variation,
                    "enabled": enabled,
                    "key": key,
                    "rules": rules,
                    "variations": variations,
                    "description": description,
                    "type": type,
                },
                flag_create_params.FlagCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FlagCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[FlagCreateResponse], ResultWrapper[FlagCreateResponse]),
        )

    async def update(
        self,
        flag_key: str,
        *,
        account_id: str,
        app_id: str,
        default_variation: str,
        enabled: bool,
        key: str,
        rules: Iterable[flag_update_params.Rule],
        variations: Dict[str, Union[Optional[str], float, bool, Dict[str, object], Iterable[object]]],
        description: Optional[str] | Omit = omit,
        type: Literal["boolean", "string", "number", "json"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlagUpdateResponse:
        """Replaces the entire flag definition.

        Omitted fields are dropped, not preserved —
        read before writing. Each update appends a changelog entry.

        Args:
          account_id: Cloudflare account ID.

          app_id: App identifier.

          flag_key: Flag key (slug).

          default_variation: Variation the API serves when the flag is off, or when it's on but no rule
              matches the context. Must be a key in `variations`.

          enabled: When false, the flag bypasses all rules and always serves `default_variation`.

          key: Unique identifier for the flag within an app. Used in all evaluation and SDK
              calls.

          rules: Targeting rules evaluated in ascending `priority`; the first matching rule wins.
              An empty array means the flag always serves `default_variation`.

          variations: Map of variation name to value. All values share the same type (boolean, string,
              number, or JSON object/array), and each serialized value stays within 10KB.

          type: Value type of the flag's variations. The API infers this from the variation
              values on write, so you can omit it in requests.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not flag_key:
            raise ValueError(f"Expected a non-empty value for `flag_key` but received {flag_key!r}")
        return await self._put(
            path_template(
                "/accounts/{account_id}/flagship/apps/{app_id}/flags/{flag_key}",
                account_id=account_id,
                app_id=app_id,
                flag_key=flag_key,
            ),
            body=await async_maybe_transform(
                {
                    "default_variation": default_variation,
                    "enabled": enabled,
                    "key": key,
                    "rules": rules,
                    "variations": variations,
                    "description": description,
                    "type": type,
                },
                flag_update_params.FlagUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FlagUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[FlagUpdateResponse], ResultWrapper[FlagUpdateResponse]),
        )

    def list(
        self,
        app_id: str,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        limit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[FlagListResponse, AsyncCursorPaginationAfter[FlagListResponse]]:
        """Lists an app's flags ordered by key.

        Pass `cursor` from `result_info` to page
        forward; a null cursor indicates the last page.

        Args:
          account_id: Cloudflare account ID.

          app_id: App identifier.

          cursor: Pagination cursor from a previous response.

          limit: Max items to return (1–200).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/flagship/apps/{app_id}/flags", account_id=account_id, app_id=app_id),
            page=AsyncCursorPaginationAfter[FlagListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    flag_list_params.FlagListParams,
                ),
            ),
            model=FlagListResponse,
        )

    async def delete(
        self,
        flag_key: str,
        *,
        account_id: str,
        app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlagDeleteResponse:
        """Deletes a flag permanently.

        Subsequent evaluations fall back to the
        caller-supplied default. Cannot be undone.

        Args:
          account_id: Cloudflare account ID.

          app_id: App identifier.

          flag_key: Flag key (slug).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not flag_key:
            raise ValueError(f"Expected a non-empty value for `flag_key` but received {flag_key!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/flagship/apps/{app_id}/flags/{flag_key}",
                account_id=account_id,
                app_id=app_id,
                flag_key=flag_key,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FlagDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[FlagDeleteResponse], ResultWrapper[FlagDeleteResponse]),
        )

    async def get(
        self,
        flag_key: str,
        *,
        account_id: str,
        app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlagGetResponse:
        """
        Returns the full flag definition including rules, variations, and audit fields.

        Args:
          account_id: Cloudflare account ID.

          app_id: App identifier.

          flag_key: Flag key (slug).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not flag_key:
            raise ValueError(f"Expected a non-empty value for `flag_key` but received {flag_key!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/flagship/apps/{app_id}/flags/{flag_key}",
                account_id=account_id,
                app_id=app_id,
                flag_key=flag_key,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FlagGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[FlagGetResponse], ResultWrapper[FlagGetResponse]),
        )


class FlagsResourceWithRawResponse:
    def __init__(self, flags: FlagsResource) -> None:
        self._flags = flags

        self.create = to_raw_response_wrapper(
            flags.create,
        )
        self.update = to_raw_response_wrapper(
            flags.update,
        )
        self.list = to_raw_response_wrapper(
            flags.list,
        )
        self.delete = to_raw_response_wrapper(
            flags.delete,
        )
        self.get = to_raw_response_wrapper(
            flags.get,
        )

    @cached_property
    def changelog(self) -> ChangelogResourceWithRawResponse:
        return ChangelogResourceWithRawResponse(self._flags.changelog)


class AsyncFlagsResourceWithRawResponse:
    def __init__(self, flags: AsyncFlagsResource) -> None:
        self._flags = flags

        self.create = async_to_raw_response_wrapper(
            flags.create,
        )
        self.update = async_to_raw_response_wrapper(
            flags.update,
        )
        self.list = async_to_raw_response_wrapper(
            flags.list,
        )
        self.delete = async_to_raw_response_wrapper(
            flags.delete,
        )
        self.get = async_to_raw_response_wrapper(
            flags.get,
        )

    @cached_property
    def changelog(self) -> AsyncChangelogResourceWithRawResponse:
        return AsyncChangelogResourceWithRawResponse(self._flags.changelog)


class FlagsResourceWithStreamingResponse:
    def __init__(self, flags: FlagsResource) -> None:
        self._flags = flags

        self.create = to_streamed_response_wrapper(
            flags.create,
        )
        self.update = to_streamed_response_wrapper(
            flags.update,
        )
        self.list = to_streamed_response_wrapper(
            flags.list,
        )
        self.delete = to_streamed_response_wrapper(
            flags.delete,
        )
        self.get = to_streamed_response_wrapper(
            flags.get,
        )

    @cached_property
    def changelog(self) -> ChangelogResourceWithStreamingResponse:
        return ChangelogResourceWithStreamingResponse(self._flags.changelog)


class AsyncFlagsResourceWithStreamingResponse:
    def __init__(self, flags: AsyncFlagsResource) -> None:
        self._flags = flags

        self.create = async_to_streamed_response_wrapper(
            flags.create,
        )
        self.update = async_to_streamed_response_wrapper(
            flags.update,
        )
        self.list = async_to_streamed_response_wrapper(
            flags.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            flags.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            flags.get,
        )

    @cached_property
    def changelog(self) -> AsyncChangelogResourceWithStreamingResponse:
        return AsyncChangelogResourceWithStreamingResponse(self._flags.changelog)
