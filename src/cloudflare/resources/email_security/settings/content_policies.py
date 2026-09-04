# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import AsyncPaginator, make_request_options
from ....types.email_security.settings import (
    content_policy_edit_params,
    content_policy_list_params,
    content_policy_batch_params,
    content_policy_create_params,
)
from ....types.email_security.settings.content_policy_get_response import ContentPolicyGetResponse
from ....types.email_security.settings.content_policy_edit_response import ContentPolicyEditResponse
from ....types.email_security.settings.content_policy_list_response import ContentPolicyListResponse
from ....types.email_security.settings.content_policy_batch_response import ContentPolicyBatchResponse
from ....types.email_security.settings.content_policy_create_response import ContentPolicyCreateResponse
from ....types.email_security.settings.content_policy_delete_response import ContentPolicyDeleteResponse

__all__ = ["ContentPoliciesResource", "AsyncContentPoliciesResource"]


class ContentPoliciesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContentPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ContentPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContentPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ContentPoliciesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        enabled: bool,
        name: str,
        pattern: str,
        targets: List[Literal["SUBJECT", "BODY"]],
        notes: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ContentPolicyCreateResponse]:
        """Creates a new content policy.

        Emails whose subject or body matches the pattern
        will be subject to the configured action.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/email-security/settings/content_policies", account_id=account_id),
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "name": name,
                    "pattern": pattern,
                    "targets": targets,
                    "notes": notes,
                },
                content_policy_create_params.ContentPolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ContentPolicyCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ContentPolicyCreateResponse]], ResultWrapper[ContentPolicyCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | Omit = omit,
        enabled: bool | Omit = omit,
        name: str | Omit = omit,
        order: Literal["name", "created_at"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[ContentPolicyListResponse]:
        """Returns a paginated list of content policies.

        These policies match against the
        subject or body of emails using a pattern. Supports filtering by name or enabled
        status, and searching across name and pattern fields.

        Args:
          account_id: Identifier.

          direction: The sorting direction.

          enabled: Filter by enabled status.

          name: Filter by exact policy name.

          order: Field to sort by.

          page: Current page within paginated list of results.

          per_page: The number of results per page. Maximum value is 1000.

          search: Search term for filtering records. Behavior may change.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/email-security/settings/content_policies", account_id=account_id),
            page=SyncV4PagePaginationArray[ContentPolicyListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "enabled": enabled,
                        "name": name,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                    },
                    content_policy_list_params.ContentPolicyListParams,
                ),
            ),
            model=ContentPolicyListResponse,
        )

    def delete(
        self,
        policy_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ContentPolicyDeleteResponse]:
        """Removes a content policy.

        After deletion, emails will no longer be evaluated
        against this pattern.

        Args:
          account_id: Identifier.

          policy_id: Content policy identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/email-security/settings/content_policies/{policy_id}",
                account_id=account_id,
                policy_id=policy_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ContentPolicyDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ContentPolicyDeleteResponse]], ResultWrapper[ContentPolicyDeleteResponse]),
        )

    def batch(
        self,
        *,
        account_id: str,
        deletes: Iterable[content_policy_batch_params.Delete],
        patches: Iterable[content_policy_batch_params.Patch],
        posts: Iterable[content_policy_batch_params.Post],
        puts: Iterable[content_policy_batch_params.Put],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ContentPolicyBatchResponse]:
        """Executes multiple operations atomically.

        All four operation arrays (deletes,
        patches, puts, posts) are required and executed in order. Send empty arrays for
        unused operations.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/email-security/settings/content_policies/batch", account_id=account_id
            ),
            body=maybe_transform(
                {
                    "deletes": deletes,
                    "patches": patches,
                    "posts": posts,
                    "puts": puts,
                },
                content_policy_batch_params.ContentPolicyBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ContentPolicyBatchResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ContentPolicyBatchResponse]], ResultWrapper[ContentPolicyBatchResponse]),
        )

    def edit(
        self,
        policy_id: str,
        *,
        account_id: str,
        enabled: bool | Omit = omit,
        name: str | Omit = omit,
        notes: Optional[str] | Omit = omit,
        pattern: str | Omit = omit,
        targets: List[Literal["SUBJECT", "BODY"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ContentPolicyEditResponse]:
        """Updates an existing content policy.

        Only provided fields will be modified.

        Args:
          account_id: Identifier.

          policy_id: Content policy identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return self._patch(
            path_template(
                "/accounts/{account_id}/email-security/settings/content_policies/{policy_id}",
                account_id=account_id,
                policy_id=policy_id,
            ),
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "name": name,
                    "notes": notes,
                    "pattern": pattern,
                    "targets": targets,
                },
                content_policy_edit_params.ContentPolicyEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ContentPolicyEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ContentPolicyEditResponse]], ResultWrapper[ContentPolicyEditResponse]),
        )

    def get(
        self,
        policy_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ContentPolicyGetResponse]:
        """
        Retrieves details for a specific content policy including its pattern, targets,
        and metadata.

        Args:
          account_id: Identifier.

          policy_id: Content policy identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/email-security/settings/content_policies/{policy_id}",
                account_id=account_id,
                policy_id=policy_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ContentPolicyGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ContentPolicyGetResponse]], ResultWrapper[ContentPolicyGetResponse]),
        )


class AsyncContentPoliciesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContentPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContentPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContentPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncContentPoliciesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        enabled: bool,
        name: str,
        pattern: str,
        targets: List[Literal["SUBJECT", "BODY"]],
        notes: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ContentPolicyCreateResponse]:
        """Creates a new content policy.

        Emails whose subject or body matches the pattern
        will be subject to the configured action.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/email-security/settings/content_policies", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "name": name,
                    "pattern": pattern,
                    "targets": targets,
                    "notes": notes,
                },
                content_policy_create_params.ContentPolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ContentPolicyCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ContentPolicyCreateResponse]], ResultWrapper[ContentPolicyCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | Omit = omit,
        enabled: bool | Omit = omit,
        name: str | Omit = omit,
        order: Literal["name", "created_at"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ContentPolicyListResponse, AsyncV4PagePaginationArray[ContentPolicyListResponse]]:
        """Returns a paginated list of content policies.

        These policies match against the
        subject or body of emails using a pattern. Supports filtering by name or enabled
        status, and searching across name and pattern fields.

        Args:
          account_id: Identifier.

          direction: The sorting direction.

          enabled: Filter by enabled status.

          name: Filter by exact policy name.

          order: Field to sort by.

          page: Current page within paginated list of results.

          per_page: The number of results per page. Maximum value is 1000.

          search: Search term for filtering records. Behavior may change.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/email-security/settings/content_policies", account_id=account_id),
            page=AsyncV4PagePaginationArray[ContentPolicyListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "enabled": enabled,
                        "name": name,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                    },
                    content_policy_list_params.ContentPolicyListParams,
                ),
            ),
            model=ContentPolicyListResponse,
        )

    async def delete(
        self,
        policy_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ContentPolicyDeleteResponse]:
        """Removes a content policy.

        After deletion, emails will no longer be evaluated
        against this pattern.

        Args:
          account_id: Identifier.

          policy_id: Content policy identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/email-security/settings/content_policies/{policy_id}",
                account_id=account_id,
                policy_id=policy_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ContentPolicyDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ContentPolicyDeleteResponse]], ResultWrapper[ContentPolicyDeleteResponse]),
        )

    async def batch(
        self,
        *,
        account_id: str,
        deletes: Iterable[content_policy_batch_params.Delete],
        patches: Iterable[content_policy_batch_params.Patch],
        posts: Iterable[content_policy_batch_params.Post],
        puts: Iterable[content_policy_batch_params.Put],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ContentPolicyBatchResponse]:
        """Executes multiple operations atomically.

        All four operation arrays (deletes,
        patches, puts, posts) are required and executed in order. Send empty arrays for
        unused operations.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/email-security/settings/content_policies/batch", account_id=account_id
            ),
            body=await async_maybe_transform(
                {
                    "deletes": deletes,
                    "patches": patches,
                    "posts": posts,
                    "puts": puts,
                },
                content_policy_batch_params.ContentPolicyBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ContentPolicyBatchResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ContentPolicyBatchResponse]], ResultWrapper[ContentPolicyBatchResponse]),
        )

    async def edit(
        self,
        policy_id: str,
        *,
        account_id: str,
        enabled: bool | Omit = omit,
        name: str | Omit = omit,
        notes: Optional[str] | Omit = omit,
        pattern: str | Omit = omit,
        targets: List[Literal["SUBJECT", "BODY"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ContentPolicyEditResponse]:
        """Updates an existing content policy.

        Only provided fields will be modified.

        Args:
          account_id: Identifier.

          policy_id: Content policy identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return await self._patch(
            path_template(
                "/accounts/{account_id}/email-security/settings/content_policies/{policy_id}",
                account_id=account_id,
                policy_id=policy_id,
            ),
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "name": name,
                    "notes": notes,
                    "pattern": pattern,
                    "targets": targets,
                },
                content_policy_edit_params.ContentPolicyEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ContentPolicyEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ContentPolicyEditResponse]], ResultWrapper[ContentPolicyEditResponse]),
        )

    async def get(
        self,
        policy_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ContentPolicyGetResponse]:
        """
        Retrieves details for a specific content policy including its pattern, targets,
        and metadata.

        Args:
          account_id: Identifier.

          policy_id: Content policy identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/email-security/settings/content_policies/{policy_id}",
                account_id=account_id,
                policy_id=policy_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ContentPolicyGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ContentPolicyGetResponse]], ResultWrapper[ContentPolicyGetResponse]),
        )


class ContentPoliciesResourceWithRawResponse:
    def __init__(self, content_policies: ContentPoliciesResource) -> None:
        self._content_policies = content_policies

        self.create = to_raw_response_wrapper(
            content_policies.create,
        )
        self.list = to_raw_response_wrapper(
            content_policies.list,
        )
        self.delete = to_raw_response_wrapper(
            content_policies.delete,
        )
        self.batch = to_raw_response_wrapper(
            content_policies.batch,
        )
        self.edit = to_raw_response_wrapper(
            content_policies.edit,
        )
        self.get = to_raw_response_wrapper(
            content_policies.get,
        )


class AsyncContentPoliciesResourceWithRawResponse:
    def __init__(self, content_policies: AsyncContentPoliciesResource) -> None:
        self._content_policies = content_policies

        self.create = async_to_raw_response_wrapper(
            content_policies.create,
        )
        self.list = async_to_raw_response_wrapper(
            content_policies.list,
        )
        self.delete = async_to_raw_response_wrapper(
            content_policies.delete,
        )
        self.batch = async_to_raw_response_wrapper(
            content_policies.batch,
        )
        self.edit = async_to_raw_response_wrapper(
            content_policies.edit,
        )
        self.get = async_to_raw_response_wrapper(
            content_policies.get,
        )


class ContentPoliciesResourceWithStreamingResponse:
    def __init__(self, content_policies: ContentPoliciesResource) -> None:
        self._content_policies = content_policies

        self.create = to_streamed_response_wrapper(
            content_policies.create,
        )
        self.list = to_streamed_response_wrapper(
            content_policies.list,
        )
        self.delete = to_streamed_response_wrapper(
            content_policies.delete,
        )
        self.batch = to_streamed_response_wrapper(
            content_policies.batch,
        )
        self.edit = to_streamed_response_wrapper(
            content_policies.edit,
        )
        self.get = to_streamed_response_wrapper(
            content_policies.get,
        )


class AsyncContentPoliciesResourceWithStreamingResponse:
    def __init__(self, content_policies: AsyncContentPoliciesResource) -> None:
        self._content_policies = content_policies

        self.create = async_to_streamed_response_wrapper(
            content_policies.create,
        )
        self.list = async_to_streamed_response_wrapper(
            content_policies.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            content_policies.delete,
        )
        self.batch = async_to_streamed_response_wrapper(
            content_policies.batch,
        )
        self.edit = async_to_streamed_response_wrapper(
            content_policies.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            content_policies.get,
        )
