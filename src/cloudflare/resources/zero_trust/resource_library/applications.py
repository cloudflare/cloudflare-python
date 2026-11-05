# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import overload

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, required_args, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncCursorPaginationAfter, AsyncCursorPaginationAfter
from ...._base_client import AsyncPaginator, make_request_options
from ....types.zero_trust.resource_library import (
    application_list_params,
    application_create_params,
    application_update_params,
)
from ....types.zero_trust.resource_library.application_get_response import ApplicationGetResponse
from ....types.zero_trust.resource_library.application_list_response import ApplicationListResponse
from ....types.zero_trust.resource_library.application_create_response import ApplicationCreateResponse
from ....types.zero_trust.resource_library.application_update_response import ApplicationUpdateResponse

__all__ = ["ApplicationsResource", "AsyncApplicationsResource"]


class ApplicationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ApplicationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ApplicationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ApplicationsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        account_id: str,
        hostnames: SequenceNotStr[str],
        category_id: int | Omit = omit,
        human_id: str | Omit = omit,
        ip_subnets: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        port_protocols: SequenceNotStr[str] | Omit = omit,
        support_domains: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationCreateResponse]:
        """
        Create a custom application for an account from a name, category, and optional
        network matchers.

        Args:
          hostnames: Hostnames matched by the application.

          category_id: Numeric identifier for an application category.

          human_id: Human-readable identifier for the application.

          ip_subnets: IP subnets for this application. Custom application create and update requests
              accept IPv4 prefix lengths /8 through /32 and IPv6 prefix lengths /32 through
              /128.

          name: Application name.

          port_protocols: Ports matched by the application, in `protocol/port` or inclusive
              `protocol/start-end` format (for example, `tcp/443` or `udp/10000-20000`). TCP
              and UDP ports must be between 0 and 65535.

          support_domains: Support domains matched by the application.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        account_id: str,
        ip_subnets: SequenceNotStr[str],
        category_id: int | Omit = omit,
        hostnames: SequenceNotStr[str] | Omit = omit,
        human_id: str | Omit = omit,
        name: str | Omit = omit,
        port_protocols: SequenceNotStr[str] | Omit = omit,
        support_domains: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationCreateResponse]:
        """
        Create a custom application for an account from a name, category, and optional
        network matchers.

        Args:
          ip_subnets: IP subnets for this application. Custom application create and update requests
              accept IPv4 prefix lengths /8 through /32 and IPv6 prefix lengths /32 through
              /128.

          category_id: Numeric identifier for an application category.

          hostnames: Hostnames matched by the application.

          human_id: Human-readable identifier for the application.

          name: Application name.

          port_protocols: Ports matched by the application, in `protocol/port` or inclusive
              `protocol/start-end` format (for example, `tcp/443` or `udp/10000-20000`). TCP
              and UDP ports must be between 0 and 65535.

          support_domains: Support domains matched by the application.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id", "hostnames"], ["account_id", "ip_subnets"])
    def create(
        self,
        *,
        account_id: str,
        hostnames: SequenceNotStr[str] | Omit = omit,
        category_id: int | Omit = omit,
        human_id: str | Omit = omit,
        ip_subnets: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        port_protocols: SequenceNotStr[str] | Omit = omit,
        support_domains: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationCreateResponse]:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/resource-library/applications", account_id=account_id),
            body=maybe_transform(
                {
                    "hostnames": hostnames,
                    "category_id": category_id,
                    "human_id": human_id,
                    "ip_subnets": ip_subnets,
                    "name": name,
                    "port_protocols": port_protocols,
                    "support_domains": support_domains,
                },
                application_create_params.ApplicationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ApplicationCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ApplicationCreateResponse]], ResultWrapper[ApplicationCreateResponse]),
        )

    def update(
        self,
        id: int,
        *,
        account_id: str,
        hostnames: SequenceNotStr[str] | Omit = omit,
        ip_subnets: SequenceNotStr[str] | Omit = omit,
        port_protocols: SequenceNotStr[str] | Omit = omit,
        support_domains: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationUpdateResponse]:
        """
        Replace the supplied network matchers for a custom application and create a new
        version. Omitted matcher lists remain unchanged; send an empty list to clear a
        matcher type.

        Args:
          id: Numeric identifier for the application.

          hostnames: Hostnames matched by the application.

          ip_subnets: IP subnets for this application. Custom application create and update requests
              accept IPv4 prefix lengths /8 through /32 and IPv6 prefix lengths /32 through
              /128.

          port_protocols: Ports matched by the application, in `protocol/port` or inclusive
              `protocol/start-end` format (for example, `tcp/443` or `udp/10000-20000`). TCP
              and UDP ports must be between 0 and 65535.

          support_domains: Support domains matched by the application.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._patch(
            path_template("/accounts/{account_id}/resource-library/applications/{id}", account_id=account_id, id=id),
            body=maybe_transform(
                {
                    "hostnames": hostnames,
                    "ip_subnets": ip_subnets,
                    "port_protocols": port_protocols,
                    "support_domains": support_domains,
                },
                application_update_params.ApplicationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ApplicationUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ApplicationUpdateResponse]], ResultWrapper[ApplicationUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        fields: str | Omit = omit,
        filter: str | Omit = omit,
        limit: int | Omit = omit,
        lookup: str | Omit = omit,
        offset: int | Omit = omit,
        order_by: str | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPaginationAfter[ApplicationListResponse]:
        """
        List the applications available to an account, both the applications Cloudflare
        curates and the custom applications the account has defined.

        Results are paginated. Page with `cursor` so that applications added or removed
        between requests do not make other results repeat or go missing; `offset` paging
        can repeat or miss results when the list changes between requests. Use `filter`
        and `search` to narrow the list, `order_by` to sort it, and `fields` to reduce
        each result to only the properties you need. Use `lookup` to find complete
        application names mentioned in a rule sentence, ignoring case. Lookup does not
        correct misspellings. It ranks matches by relevance and uses the same filters,
        fields, and pagination as listing. `lookup` cannot be combined with `search`.

        Invalid UTF-8 or a NUL character (U+0000) in any query parameter name or value
        returns `400`.

        The authenticated principal must have access to the account identified by
        `account_id`.

        Args:
          cursor: Opaque value from `result_info.cursor` of the previous response. Returns the
              results that follow it. Send the same `filter`, `search`, `lookup`, and
              `order_by` values as the request that returned it; `limit` and `fields` may
              change. An empty value is the same as no cursor. A modified cursor, or one used
              with different values, returns `400`.

          fields: Return only the listed properties on each application, as a comma-separated
              list. Use this to keep responses small when you only need part of each
              application, for example populating a picker with `fields=id,name` instead of
              downloading every hostname and IP subnet.

              Omit this parameter to receive the full application object, including when
              lookup is used.

              `id` is always returned.

              Selectable properties: `id`, `name`, `human_id`, `version`, `hostnames`,
              `support_domains`, `ip_subnets`, `port_protocols`, `supported`, `gen_ai_score`,
              `application_confidence_score`, `created_at`, `updated_at`, `review_status`.

              Unknown or empty property names return `400`.

          filter:
              Filter applications using `key:value` format. Supported filter keys:

              - `name`: application name (for example, `name:HR`).
              - `id`: application ID (for example, `id:498`).
              - `human_id`: human-readable ID (for example, `human_id:HR`).
              - `hostname`: hostname or support domain (for example,
                `hostname:portal.example.com`).
              - `source`: application source name (for example, `source:cloudflare`).
              - `ip_subnet`: CIDR containment; returns applications where a stored subnet
                contains the search value (for example, `ip_subnet:10.0.1.5/32` matches
                `10.0.0.0/16`).
              - `category_id`: category ID (for example, `category_id:12`).
              - `category_name`: category name (for example, `category_name:HR`).
              - `supported`: supported Cloudflare product. Values: `GATEWAY`, `ACCESS`,
                `CASB`.
              - `review_status`: account-specific Gateway review status. Values: `approved`,
                `unapproved`, `in_review`, `unreviewed`.

          limit: Number of results to return. Defaults to 25; values are clamped to 1–250.

          lookup: Find complete, case-insensitive application name mentions in a phrase or rule
              sentence. Misspelled names do not match. Returns matching applications ranked by
              relevance. Must be between 2 and 1000 characters, with no control characters
              other than tab and line breaks. Uses the same filters, fields, and pagination as
              listing. `search` cannot be combined with lookup. Results are ranked by
              relevance, so `order_by` is ignored. To keep the text out of URLs, send it to
              `POST .../applications/lookup` instead.

          offset: Number of results to skip. Defaults to 0; negative values are clamped to 0.
              Ignored when `cursor` is provided.

          order_by: Order results using field:direction format. Supported fields are name, id,
              human_id, category_id, application_type, application_confidence_score, and
              gen_ai_score. Supported directions are asc and desc. Ignored when search is
              provided; results are ranked by relevance instead. Also ignored when lookup is
              provided.

          search: Fuzzy search across application name and hostnames. Results are ranked by
              relevance. Must be between 2 and 200 characters. Can be combined with filter
              parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/resource-library/applications", account_id=account_id),
            page=SyncCursorPaginationAfter[ApplicationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "fields": fields,
                        "filter": filter,
                        "limit": limit,
                        "lookup": lookup,
                        "offset": offset,
                        "order_by": order_by,
                        "search": search,
                    },
                    application_list_params.ApplicationListParams,
                ),
            ),
            model=ApplicationListResponse,
        )

    def delete(
        self,
        id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Delete a custom application and all of its versions.

        Deletion is rejected when
        other resources reference the application.

        Args:
          id: Numeric identifier for the application.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._delete(
            path_template("/accounts/{account_id}/resource-library/applications/{id}", account_id=account_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def get(
        self,
        id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationGetResponse]:
        """
        Retrieve an application available to the account by its numeric application ID.

        Args:
          id: Numeric identifier for the application.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/resource-library/applications/{id}", account_id=account_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ApplicationGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ApplicationGetResponse]], ResultWrapper[ApplicationGetResponse]),
        )


class AsyncApplicationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncApplicationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncApplicationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncApplicationsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        account_id: str,
        hostnames: SequenceNotStr[str],
        category_id: int | Omit = omit,
        human_id: str | Omit = omit,
        ip_subnets: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        port_protocols: SequenceNotStr[str] | Omit = omit,
        support_domains: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationCreateResponse]:
        """
        Create a custom application for an account from a name, category, and optional
        network matchers.

        Args:
          hostnames: Hostnames matched by the application.

          category_id: Numeric identifier for an application category.

          human_id: Human-readable identifier for the application.

          ip_subnets: IP subnets for this application. Custom application create and update requests
              accept IPv4 prefix lengths /8 through /32 and IPv6 prefix lengths /32 through
              /128.

          name: Application name.

          port_protocols: Ports matched by the application, in `protocol/port` or inclusive
              `protocol/start-end` format (for example, `tcp/443` or `udp/10000-20000`). TCP
              and UDP ports must be between 0 and 65535.

          support_domains: Support domains matched by the application.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        account_id: str,
        ip_subnets: SequenceNotStr[str],
        category_id: int | Omit = omit,
        hostnames: SequenceNotStr[str] | Omit = omit,
        human_id: str | Omit = omit,
        name: str | Omit = omit,
        port_protocols: SequenceNotStr[str] | Omit = omit,
        support_domains: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationCreateResponse]:
        """
        Create a custom application for an account from a name, category, and optional
        network matchers.

        Args:
          ip_subnets: IP subnets for this application. Custom application create and update requests
              accept IPv4 prefix lengths /8 through /32 and IPv6 prefix lengths /32 through
              /128.

          category_id: Numeric identifier for an application category.

          hostnames: Hostnames matched by the application.

          human_id: Human-readable identifier for the application.

          name: Application name.

          port_protocols: Ports matched by the application, in `protocol/port` or inclusive
              `protocol/start-end` format (for example, `tcp/443` or `udp/10000-20000`). TCP
              and UDP ports must be between 0 and 65535.

          support_domains: Support domains matched by the application.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id", "hostnames"], ["account_id", "ip_subnets"])
    async def create(
        self,
        *,
        account_id: str,
        hostnames: SequenceNotStr[str] | Omit = omit,
        category_id: int | Omit = omit,
        human_id: str | Omit = omit,
        ip_subnets: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        port_protocols: SequenceNotStr[str] | Omit = omit,
        support_domains: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationCreateResponse]:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/resource-library/applications", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "hostnames": hostnames,
                    "category_id": category_id,
                    "human_id": human_id,
                    "ip_subnets": ip_subnets,
                    "name": name,
                    "port_protocols": port_protocols,
                    "support_domains": support_domains,
                },
                application_create_params.ApplicationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ApplicationCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ApplicationCreateResponse]], ResultWrapper[ApplicationCreateResponse]),
        )

    async def update(
        self,
        id: int,
        *,
        account_id: str,
        hostnames: SequenceNotStr[str] | Omit = omit,
        ip_subnets: SequenceNotStr[str] | Omit = omit,
        port_protocols: SequenceNotStr[str] | Omit = omit,
        support_domains: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationUpdateResponse]:
        """
        Replace the supplied network matchers for a custom application and create a new
        version. Omitted matcher lists remain unchanged; send an empty list to clear a
        matcher type.

        Args:
          id: Numeric identifier for the application.

          hostnames: Hostnames matched by the application.

          ip_subnets: IP subnets for this application. Custom application create and update requests
              accept IPv4 prefix lengths /8 through /32 and IPv6 prefix lengths /32 through
              /128.

          port_protocols: Ports matched by the application, in `protocol/port` or inclusive
              `protocol/start-end` format (for example, `tcp/443` or `udp/10000-20000`). TCP
              and UDP ports must be between 0 and 65535.

          support_domains: Support domains matched by the application.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._patch(
            path_template("/accounts/{account_id}/resource-library/applications/{id}", account_id=account_id, id=id),
            body=await async_maybe_transform(
                {
                    "hostnames": hostnames,
                    "ip_subnets": ip_subnets,
                    "port_protocols": port_protocols,
                    "support_domains": support_domains,
                },
                application_update_params.ApplicationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ApplicationUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ApplicationUpdateResponse]], ResultWrapper[ApplicationUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        fields: str | Omit = omit,
        filter: str | Omit = omit,
        limit: int | Omit = omit,
        lookup: str | Omit = omit,
        offset: int | Omit = omit,
        order_by: str | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ApplicationListResponse, AsyncCursorPaginationAfter[ApplicationListResponse]]:
        """
        List the applications available to an account, both the applications Cloudflare
        curates and the custom applications the account has defined.

        Results are paginated. Page with `cursor` so that applications added or removed
        between requests do not make other results repeat or go missing; `offset` paging
        can repeat or miss results when the list changes between requests. Use `filter`
        and `search` to narrow the list, `order_by` to sort it, and `fields` to reduce
        each result to only the properties you need. Use `lookup` to find complete
        application names mentioned in a rule sentence, ignoring case. Lookup does not
        correct misspellings. It ranks matches by relevance and uses the same filters,
        fields, and pagination as listing. `lookup` cannot be combined with `search`.

        Invalid UTF-8 or a NUL character (U+0000) in any query parameter name or value
        returns `400`.

        The authenticated principal must have access to the account identified by
        `account_id`.

        Args:
          cursor: Opaque value from `result_info.cursor` of the previous response. Returns the
              results that follow it. Send the same `filter`, `search`, `lookup`, and
              `order_by` values as the request that returned it; `limit` and `fields` may
              change. An empty value is the same as no cursor. A modified cursor, or one used
              with different values, returns `400`.

          fields: Return only the listed properties on each application, as a comma-separated
              list. Use this to keep responses small when you only need part of each
              application, for example populating a picker with `fields=id,name` instead of
              downloading every hostname and IP subnet.

              Omit this parameter to receive the full application object, including when
              lookup is used.

              `id` is always returned.

              Selectable properties: `id`, `name`, `human_id`, `version`, `hostnames`,
              `support_domains`, `ip_subnets`, `port_protocols`, `supported`, `gen_ai_score`,
              `application_confidence_score`, `created_at`, `updated_at`, `review_status`.

              Unknown or empty property names return `400`.

          filter:
              Filter applications using `key:value` format. Supported filter keys:

              - `name`: application name (for example, `name:HR`).
              - `id`: application ID (for example, `id:498`).
              - `human_id`: human-readable ID (for example, `human_id:HR`).
              - `hostname`: hostname or support domain (for example,
                `hostname:portal.example.com`).
              - `source`: application source name (for example, `source:cloudflare`).
              - `ip_subnet`: CIDR containment; returns applications where a stored subnet
                contains the search value (for example, `ip_subnet:10.0.1.5/32` matches
                `10.0.0.0/16`).
              - `category_id`: category ID (for example, `category_id:12`).
              - `category_name`: category name (for example, `category_name:HR`).
              - `supported`: supported Cloudflare product. Values: `GATEWAY`, `ACCESS`,
                `CASB`.
              - `review_status`: account-specific Gateway review status. Values: `approved`,
                `unapproved`, `in_review`, `unreviewed`.

          limit: Number of results to return. Defaults to 25; values are clamped to 1–250.

          lookup: Find complete, case-insensitive application name mentions in a phrase or rule
              sentence. Misspelled names do not match. Returns matching applications ranked by
              relevance. Must be between 2 and 1000 characters, with no control characters
              other than tab and line breaks. Uses the same filters, fields, and pagination as
              listing. `search` cannot be combined with lookup. Results are ranked by
              relevance, so `order_by` is ignored. To keep the text out of URLs, send it to
              `POST .../applications/lookup` instead.

          offset: Number of results to skip. Defaults to 0; negative values are clamped to 0.
              Ignored when `cursor` is provided.

          order_by: Order results using field:direction format. Supported fields are name, id,
              human_id, category_id, application_type, application_confidence_score, and
              gen_ai_score. Supported directions are asc and desc. Ignored when search is
              provided; results are ranked by relevance instead. Also ignored when lookup is
              provided.

          search: Fuzzy search across application name and hostnames. Results are ranked by
              relevance. Must be between 2 and 200 characters. Can be combined with filter
              parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/resource-library/applications", account_id=account_id),
            page=AsyncCursorPaginationAfter[ApplicationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "fields": fields,
                        "filter": filter,
                        "limit": limit,
                        "lookup": lookup,
                        "offset": offset,
                        "order_by": order_by,
                        "search": search,
                    },
                    application_list_params.ApplicationListParams,
                ),
            ),
            model=ApplicationListResponse,
        )

    async def delete(
        self,
        id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Delete a custom application and all of its versions.

        Deletion is rejected when
        other resources reference the application.

        Args:
          id: Numeric identifier for the application.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._delete(
            path_template("/accounts/{account_id}/resource-library/applications/{id}", account_id=account_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def get(
        self,
        id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationGetResponse]:
        """
        Retrieve an application available to the account by its numeric application ID.

        Args:
          id: Numeric identifier for the application.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/resource-library/applications/{id}", account_id=account_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ApplicationGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ApplicationGetResponse]], ResultWrapper[ApplicationGetResponse]),
        )


class ApplicationsResourceWithRawResponse:
    def __init__(self, applications: ApplicationsResource) -> None:
        self._applications = applications

        self.create = to_raw_response_wrapper(
            applications.create,
        )
        self.update = to_raw_response_wrapper(
            applications.update,
        )
        self.list = to_raw_response_wrapper(
            applications.list,
        )
        self.delete = to_raw_response_wrapper(
            applications.delete,
        )
        self.get = to_raw_response_wrapper(
            applications.get,
        )


class AsyncApplicationsResourceWithRawResponse:
    def __init__(self, applications: AsyncApplicationsResource) -> None:
        self._applications = applications

        self.create = async_to_raw_response_wrapper(
            applications.create,
        )
        self.update = async_to_raw_response_wrapper(
            applications.update,
        )
        self.list = async_to_raw_response_wrapper(
            applications.list,
        )
        self.delete = async_to_raw_response_wrapper(
            applications.delete,
        )
        self.get = async_to_raw_response_wrapper(
            applications.get,
        )


class ApplicationsResourceWithStreamingResponse:
    def __init__(self, applications: ApplicationsResource) -> None:
        self._applications = applications

        self.create = to_streamed_response_wrapper(
            applications.create,
        )
        self.update = to_streamed_response_wrapper(
            applications.update,
        )
        self.list = to_streamed_response_wrapper(
            applications.list,
        )
        self.delete = to_streamed_response_wrapper(
            applications.delete,
        )
        self.get = to_streamed_response_wrapper(
            applications.get,
        )


class AsyncApplicationsResourceWithStreamingResponse:
    def __init__(self, applications: AsyncApplicationsResource) -> None:
        self._applications = applications

        self.create = async_to_streamed_response_wrapper(
            applications.create,
        )
        self.update = async_to_streamed_response_wrapper(
            applications.update,
        )
        self.list = async_to_streamed_response_wrapper(
            applications.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            applications.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            applications.get,
        )
