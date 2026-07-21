# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from .categories import (
    CategoriesResource,
    AsyncCategoriesResource,
    CategoriesResourceWithRawResponse,
    AsyncCategoriesResourceWithRawResponse,
    CategoriesResourceWithStreamingResponse,
    AsyncCategoriesResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .indicators.indicators import (
    IndicatorsResource,
    AsyncIndicatorsResource,
    IndicatorsResourceWithRawResponse,
    AsyncIndicatorsResourceWithRawResponse,
    IndicatorsResourceWithStreamingResponse,
    AsyncIndicatorsResourceWithStreamingResponse,
)
from .....types.cloudforce_one.threat_events import tag_edit_params, tag_list_params, tag_create_params
from .....types.cloudforce_one.threat_events.tag_edit_response import TagEditResponse
from .....types.cloudforce_one.threat_events.tag_list_response import TagListResponse
from .....types.cloudforce_one.threat_events.tag_create_response import TagCreateResponse
from .....types.cloudforce_one.threat_events.tag_delete_response import TagDeleteResponse

__all__ = ["TagsResource", "AsyncTagsResource"]


class TagsResource(SyncAPIResource):
    @cached_property
    def categories(self) -> CategoriesResource:
        return CategoriesResource(self._client)

    @cached_property
    def indicators(self) -> IndicatorsResource:
        return IndicatorsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TagsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        value: str,
        active_duration: str | Omit = omit,
        actor_category: str | Omit = omit,
        actor_category_confidence: int | Omit = omit,
        aliases: Iterable[tag_create_params.Alias] | Omit = omit,
        alias_group_names: SequenceNotStr[str] | Omit = omit,
        alias_group_names_internal: SequenceNotStr[str] | Omit = omit,
        analytic_priority: float | Omit = omit,
        attribution_confidence: str | Omit = omit,
        attribution_confidence_score: int | Omit = omit,
        attribution_organization: str | Omit = omit,
        category_uuid: str | Omit = omit,
        date_of_discovery: str | Omit = omit,
        external_reference_links: SequenceNotStr[str] | Omit = omit,
        external_references: Iterable[tag_create_params.ExternalReference] | Omit = omit,
        internal_aliases: Iterable[tag_create_params.InternalAlias] | Omit = omit,
        internal_description: str | Omit = omit,
        motive: str | Omit = omit,
        motive_confidence: int | Omit = omit,
        opsec_level: str | Omit = omit,
        origin_country_confidence: int | Omit = omit,
        origin_country_iso: str | Omit = omit,
        origin_country_tlp: Literal["red", "amber", "green", "white"] | Omit = omit,
        priority: float | Omit = omit,
        sophistication_level: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagCreateResponse:
        """
        Creates a new tag to be used accross threat events.

        Args:
          account_id: Account ID.

          actor_category: Actor variety. Allowed values: Activist, Competitor, Customer, Crime Syndicate,
              Former Employee, Nation State, Organized Crime, Nation State Affiliated,
              Terrorist, Unaffiliated.

          actor_category_confidence: Confidence (1-10) in the actor variety (actorCategory). CFONE-only: stripped
              from responses to non-CFONE accounts.

          aliases: Structured aliases ({ value, confidence 1-10, tlp }). CFONE-only: stripped from
              responses to non-CFONE accounts.

          date_of_discovery: Date the actor was discovered (ISO YYYY-MM-DD).

          external_references: Structured external references ({ url, description }). Public: returned to all
              accounts.

          internal_aliases: Internal structured aliases ({ value, confidence 1-10, tlp }). CFONE-only: never
              returned to non-CFONE accounts.

          motive: Actor motive. Allowed values: Convenience, Fear, Fun, Financial, Grudge,
              Ideology, Espionage.

          motive_confidence: Confidence (1-10) in the actor motive. CFONE-only: stripped from responses to
              non-CFONE accounts.

          origin_country_confidence: Confidence (1-10) in the origin-country attribution. CFONE-only: stripped from
              responses to non-CFONE accounts.

          origin_country_tlp: TLP marking for the origin-country attribution. CFONE-only: stripped from
              responses to non-CFONE accounts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/cloudforce-one/events/tags/create", account_id=account_id),
            body=maybe_transform(
                {
                    "value": value,
                    "active_duration": active_duration,
                    "actor_category": actor_category,
                    "actor_category_confidence": actor_category_confidence,
                    "aliases": aliases,
                    "alias_group_names": alias_group_names,
                    "alias_group_names_internal": alias_group_names_internal,
                    "analytic_priority": analytic_priority,
                    "attribution_confidence": attribution_confidence,
                    "attribution_confidence_score": attribution_confidence_score,
                    "attribution_organization": attribution_organization,
                    "category_uuid": category_uuid,
                    "date_of_discovery": date_of_discovery,
                    "external_reference_links": external_reference_links,
                    "external_references": external_references,
                    "internal_aliases": internal_aliases,
                    "internal_description": internal_description,
                    "motive": motive,
                    "motive_confidence": motive_confidence,
                    "opsec_level": opsec_level,
                    "origin_country_confidence": origin_country_confidence,
                    "origin_country_iso": origin_country_iso,
                    "origin_country_tlp": origin_country_tlp,
                    "priority": priority,
                    "sophistication_level": sophistication_level,
                },
                tag_create_params.TagCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TagCreateResponse,
        )

    def list(
        self,
        *,
        account_id: str,
        cache: Literal["from-graph"] | Omit = omit,
        category_uuid: str | Omit = omit,
        filters: Iterable[tag_list_params.Filter] | Omit = omit,
        page: float | Omit = omit,
        page_size: float | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagListResponse:
        """Returns all Source-of-Truth tags for an account.

        Supports legacy free-text
        `search` on tag value and `categoryUuid` exact match, plus a structured
        `filters` JSON array for filtering by metadata fields (originCountryISO,
        actorCategory, motive, priority, etc.). Country values may be passed as alpha-2,
        alpha-3, name, or common alias.

        Args:
          account_id: Account ID.

          cache: Cache strategy. 'from-graph' serves results from the graph-node KV cache when
              all requested UUIDs are cached; falls back to normal path on partial/zero hit.

          filters: Structured filters as a JSON array of {field, op, value} objects. Searchable
              fields: uuid, value, actorCategory, actorCategoryConfidence, aliasGroupNames,
              attributionConfidence, attributionConfidenceScore, attributionOrganization,
              categoryName, motive, motiveConfidence, opsecLevel, originCountryISO,
              originCountryConfidence, sophisticationLevel, priority, analyticPriority.
              Operators: equals, not, contains, startsWith, endsWith, gt, lt, gte, lte, like,
              in, find. Use 'in' for bulk OR within a single field, e.g.
              filters=[{"field":"originCountryISO","op":"in","value":["IR","CN"]}]. Multiple
              entries are AND-joined. Max 10 entries per request, max 100 values per 'in'.
              Per-field notes: `uuid` accepts only 'equals' and 'in' (other operators throw
              ValidationError) — matched against the canonical lowercase storage but callers
              may pass either case (the server lowercases before comparison); index-backed by
              the column's UNIQUE constraint and intended for batched UUID → tag resolution.
              `originCountryISO` uses its B-tree index for equals/not/in. `priority` uses its
              B-tree index for numeric comparisons. Other string columns (`actorCategory`,
              `motive`, etc.) are case-insensitive and unindexed; current catalog size makes
              this a non-issue. `endsWith` and `aliasGroupNames` contains/like are
              leading-wildcard scans and slow on large result sets. `aliasGroupNames` matches
              on the JSON-encoded text, so substrings can cross alias boundaries (a search for
              "apt28" will also match "apt280" if both appear in the same tag's alias list).

          search: Legacy free-text substring match on tag value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/cloudforce-one/events/tags", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cache": cache,
                        "category_uuid": category_uuid,
                        "filters": filters,
                        "page": page,
                        "page_size": page_size,
                        "search": search,
                    },
                    tag_list_params.TagListParams,
                ),
            ),
            cast_to=TagListResponse,
        )

    def delete(
        self,
        tag_uuid: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagDeleteResponse:
        """
        Deletes a Source-of-Truth tag by UUID.

        Args:
          account_id: Account ID.

          tag_uuid: Tag UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tag_uuid:
            raise ValueError(f"Expected a non-empty value for `tag_uuid` but received {tag_uuid!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/tags/{tag_uuid}", account_id=account_id, tag_uuid=tag_uuid
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TagDeleteResponse,
        )

    def edit(
        self,
        tag_uuid: str,
        *,
        account_id: str,
        active_duration: str | Omit = omit,
        actor_category: str | Omit = omit,
        actor_category_confidence: int | Omit = omit,
        aliases: Iterable[tag_edit_params.Alias] | Omit = omit,
        alias_group_names: SequenceNotStr[str] | Omit = omit,
        alias_group_names_internal: SequenceNotStr[str] | Omit = omit,
        analytic_priority: float | Omit = omit,
        attribution_confidence: str | Omit = omit,
        attribution_confidence_score: int | Omit = omit,
        attribution_organization: str | Omit = omit,
        category_uuid: str | Omit = omit,
        date_of_discovery: str | Omit = omit,
        external_reference_links: SequenceNotStr[str] | Omit = omit,
        external_references: Iterable[tag_edit_params.ExternalReference] | Omit = omit,
        internal_aliases: Iterable[tag_edit_params.InternalAlias] | Omit = omit,
        internal_description: str | Omit = omit,
        motive: str | Omit = omit,
        motive_confidence: int | Omit = omit,
        opsec_level: str | Omit = omit,
        origin_country_confidence: int | Omit = omit,
        origin_country_iso: str | Omit = omit,
        origin_country_tlp: Literal["red", "amber", "green", "white"] | Omit = omit,
        priority: float | Omit = omit,
        sophistication_level: str | Omit = omit,
        value: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagEditResponse:
        """
        Updates a Source-of-Truth tag by UUID.

        Args:
          account_id: Account ID.

          tag_uuid: Tag UUID.

          actor_category: Actor variety. Allowed values: Activist, Competitor, Customer, Crime Syndicate,
              Former Employee, Nation State, Organized Crime, Nation State Affiliated,
              Terrorist, Unaffiliated.

          actor_category_confidence: Confidence (1-10) in the actor variety (actorCategory). CFONE-only: stripped
              from responses to non-CFONE accounts.

          aliases: Structured aliases ({ value, confidence 1-10, tlp }). CFONE-only: stripped from
              responses to non-CFONE accounts.

          date_of_discovery: Date the actor was discovered (ISO YYYY-MM-DD).

          external_references: Structured external references ({ url, description }). Public: returned to all
              accounts.

          internal_aliases: Internal structured aliases ({ value, confidence 1-10, tlp }). CFONE-only: never
              returned to non-CFONE accounts.

          motive: Actor motive. Allowed values: Convenience, Fear, Fun, Financial, Grudge,
              Ideology, Espionage.

          motive_confidence: Confidence (1-10) in the actor motive. CFONE-only: stripped from responses to
              non-CFONE accounts.

          origin_country_confidence: Confidence (1-10) in the origin-country attribution. CFONE-only: stripped from
              responses to non-CFONE accounts.

          origin_country_tlp: TLP marking for the origin-country attribution. CFONE-only: stripped from
              responses to non-CFONE accounts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tag_uuid:
            raise ValueError(f"Expected a non-empty value for `tag_uuid` but received {tag_uuid!r}")
        return self._patch(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/tags/{tag_uuid}", account_id=account_id, tag_uuid=tag_uuid
            ),
            body=maybe_transform(
                {
                    "active_duration": active_duration,
                    "actor_category": actor_category,
                    "actor_category_confidence": actor_category_confidence,
                    "aliases": aliases,
                    "alias_group_names": alias_group_names,
                    "alias_group_names_internal": alias_group_names_internal,
                    "analytic_priority": analytic_priority,
                    "attribution_confidence": attribution_confidence,
                    "attribution_confidence_score": attribution_confidence_score,
                    "attribution_organization": attribution_organization,
                    "category_uuid": category_uuid,
                    "date_of_discovery": date_of_discovery,
                    "external_reference_links": external_reference_links,
                    "external_references": external_references,
                    "internal_aliases": internal_aliases,
                    "internal_description": internal_description,
                    "motive": motive,
                    "motive_confidence": motive_confidence,
                    "opsec_level": opsec_level,
                    "origin_country_confidence": origin_country_confidence,
                    "origin_country_iso": origin_country_iso,
                    "origin_country_tlp": origin_country_tlp,
                    "priority": priority,
                    "sophistication_level": sophistication_level,
                    "value": value,
                },
                tag_edit_params.TagEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TagEditResponse,
        )


class AsyncTagsResource(AsyncAPIResource):
    @cached_property
    def categories(self) -> AsyncCategoriesResource:
        return AsyncCategoriesResource(self._client)

    @cached_property
    def indicators(self) -> AsyncIndicatorsResource:
        return AsyncIndicatorsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTagsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        value: str,
        active_duration: str | Omit = omit,
        actor_category: str | Omit = omit,
        actor_category_confidence: int | Omit = omit,
        aliases: Iterable[tag_create_params.Alias] | Omit = omit,
        alias_group_names: SequenceNotStr[str] | Omit = omit,
        alias_group_names_internal: SequenceNotStr[str] | Omit = omit,
        analytic_priority: float | Omit = omit,
        attribution_confidence: str | Omit = omit,
        attribution_confidence_score: int | Omit = omit,
        attribution_organization: str | Omit = omit,
        category_uuid: str | Omit = omit,
        date_of_discovery: str | Omit = omit,
        external_reference_links: SequenceNotStr[str] | Omit = omit,
        external_references: Iterable[tag_create_params.ExternalReference] | Omit = omit,
        internal_aliases: Iterable[tag_create_params.InternalAlias] | Omit = omit,
        internal_description: str | Omit = omit,
        motive: str | Omit = omit,
        motive_confidence: int | Omit = omit,
        opsec_level: str | Omit = omit,
        origin_country_confidence: int | Omit = omit,
        origin_country_iso: str | Omit = omit,
        origin_country_tlp: Literal["red", "amber", "green", "white"] | Omit = omit,
        priority: float | Omit = omit,
        sophistication_level: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagCreateResponse:
        """
        Creates a new tag to be used accross threat events.

        Args:
          account_id: Account ID.

          actor_category: Actor variety. Allowed values: Activist, Competitor, Customer, Crime Syndicate,
              Former Employee, Nation State, Organized Crime, Nation State Affiliated,
              Terrorist, Unaffiliated.

          actor_category_confidence: Confidence (1-10) in the actor variety (actorCategory). CFONE-only: stripped
              from responses to non-CFONE accounts.

          aliases: Structured aliases ({ value, confidence 1-10, tlp }). CFONE-only: stripped from
              responses to non-CFONE accounts.

          date_of_discovery: Date the actor was discovered (ISO YYYY-MM-DD).

          external_references: Structured external references ({ url, description }). Public: returned to all
              accounts.

          internal_aliases: Internal structured aliases ({ value, confidence 1-10, tlp }). CFONE-only: never
              returned to non-CFONE accounts.

          motive: Actor motive. Allowed values: Convenience, Fear, Fun, Financial, Grudge,
              Ideology, Espionage.

          motive_confidence: Confidence (1-10) in the actor motive. CFONE-only: stripped from responses to
              non-CFONE accounts.

          origin_country_confidence: Confidence (1-10) in the origin-country attribution. CFONE-only: stripped from
              responses to non-CFONE accounts.

          origin_country_tlp: TLP marking for the origin-country attribution. CFONE-only: stripped from
              responses to non-CFONE accounts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/cloudforce-one/events/tags/create", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "value": value,
                    "active_duration": active_duration,
                    "actor_category": actor_category,
                    "actor_category_confidence": actor_category_confidence,
                    "aliases": aliases,
                    "alias_group_names": alias_group_names,
                    "alias_group_names_internal": alias_group_names_internal,
                    "analytic_priority": analytic_priority,
                    "attribution_confidence": attribution_confidence,
                    "attribution_confidence_score": attribution_confidence_score,
                    "attribution_organization": attribution_organization,
                    "category_uuid": category_uuid,
                    "date_of_discovery": date_of_discovery,
                    "external_reference_links": external_reference_links,
                    "external_references": external_references,
                    "internal_aliases": internal_aliases,
                    "internal_description": internal_description,
                    "motive": motive,
                    "motive_confidence": motive_confidence,
                    "opsec_level": opsec_level,
                    "origin_country_confidence": origin_country_confidence,
                    "origin_country_iso": origin_country_iso,
                    "origin_country_tlp": origin_country_tlp,
                    "priority": priority,
                    "sophistication_level": sophistication_level,
                },
                tag_create_params.TagCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TagCreateResponse,
        )

    async def list(
        self,
        *,
        account_id: str,
        cache: Literal["from-graph"] | Omit = omit,
        category_uuid: str | Omit = omit,
        filters: Iterable[tag_list_params.Filter] | Omit = omit,
        page: float | Omit = omit,
        page_size: float | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagListResponse:
        """Returns all Source-of-Truth tags for an account.

        Supports legacy free-text
        `search` on tag value and `categoryUuid` exact match, plus a structured
        `filters` JSON array for filtering by metadata fields (originCountryISO,
        actorCategory, motive, priority, etc.). Country values may be passed as alpha-2,
        alpha-3, name, or common alias.

        Args:
          account_id: Account ID.

          cache: Cache strategy. 'from-graph' serves results from the graph-node KV cache when
              all requested UUIDs are cached; falls back to normal path on partial/zero hit.

          filters: Structured filters as a JSON array of {field, op, value} objects. Searchable
              fields: uuid, value, actorCategory, actorCategoryConfidence, aliasGroupNames,
              attributionConfidence, attributionConfidenceScore, attributionOrganization,
              categoryName, motive, motiveConfidence, opsecLevel, originCountryISO,
              originCountryConfidence, sophisticationLevel, priority, analyticPriority.
              Operators: equals, not, contains, startsWith, endsWith, gt, lt, gte, lte, like,
              in, find. Use 'in' for bulk OR within a single field, e.g.
              filters=[{"field":"originCountryISO","op":"in","value":["IR","CN"]}]. Multiple
              entries are AND-joined. Max 10 entries per request, max 100 values per 'in'.
              Per-field notes: `uuid` accepts only 'equals' and 'in' (other operators throw
              ValidationError) — matched against the canonical lowercase storage but callers
              may pass either case (the server lowercases before comparison); index-backed by
              the column's UNIQUE constraint and intended for batched UUID → tag resolution.
              `originCountryISO` uses its B-tree index for equals/not/in. `priority` uses its
              B-tree index for numeric comparisons. Other string columns (`actorCategory`,
              `motive`, etc.) are case-insensitive and unindexed; current catalog size makes
              this a non-issue. `endsWith` and `aliasGroupNames` contains/like are
              leading-wildcard scans and slow on large result sets. `aliasGroupNames` matches
              on the JSON-encoded text, so substrings can cross alias boundaries (a search for
              "apt28" will also match "apt280" if both appear in the same tag's alias list).

          search: Legacy free-text substring match on tag value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/cloudforce-one/events/tags", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cache": cache,
                        "category_uuid": category_uuid,
                        "filters": filters,
                        "page": page,
                        "page_size": page_size,
                        "search": search,
                    },
                    tag_list_params.TagListParams,
                ),
            ),
            cast_to=TagListResponse,
        )

    async def delete(
        self,
        tag_uuid: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagDeleteResponse:
        """
        Deletes a Source-of-Truth tag by UUID.

        Args:
          account_id: Account ID.

          tag_uuid: Tag UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tag_uuid:
            raise ValueError(f"Expected a non-empty value for `tag_uuid` but received {tag_uuid!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/tags/{tag_uuid}", account_id=account_id, tag_uuid=tag_uuid
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TagDeleteResponse,
        )

    async def edit(
        self,
        tag_uuid: str,
        *,
        account_id: str,
        active_duration: str | Omit = omit,
        actor_category: str | Omit = omit,
        actor_category_confidence: int | Omit = omit,
        aliases: Iterable[tag_edit_params.Alias] | Omit = omit,
        alias_group_names: SequenceNotStr[str] | Omit = omit,
        alias_group_names_internal: SequenceNotStr[str] | Omit = omit,
        analytic_priority: float | Omit = omit,
        attribution_confidence: str | Omit = omit,
        attribution_confidence_score: int | Omit = omit,
        attribution_organization: str | Omit = omit,
        category_uuid: str | Omit = omit,
        date_of_discovery: str | Omit = omit,
        external_reference_links: SequenceNotStr[str] | Omit = omit,
        external_references: Iterable[tag_edit_params.ExternalReference] | Omit = omit,
        internal_aliases: Iterable[tag_edit_params.InternalAlias] | Omit = omit,
        internal_description: str | Omit = omit,
        motive: str | Omit = omit,
        motive_confidence: int | Omit = omit,
        opsec_level: str | Omit = omit,
        origin_country_confidence: int | Omit = omit,
        origin_country_iso: str | Omit = omit,
        origin_country_tlp: Literal["red", "amber", "green", "white"] | Omit = omit,
        priority: float | Omit = omit,
        sophistication_level: str | Omit = omit,
        value: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagEditResponse:
        """
        Updates a Source-of-Truth tag by UUID.

        Args:
          account_id: Account ID.

          tag_uuid: Tag UUID.

          actor_category: Actor variety. Allowed values: Activist, Competitor, Customer, Crime Syndicate,
              Former Employee, Nation State, Organized Crime, Nation State Affiliated,
              Terrorist, Unaffiliated.

          actor_category_confidence: Confidence (1-10) in the actor variety (actorCategory). CFONE-only: stripped
              from responses to non-CFONE accounts.

          aliases: Structured aliases ({ value, confidence 1-10, tlp }). CFONE-only: stripped from
              responses to non-CFONE accounts.

          date_of_discovery: Date the actor was discovered (ISO YYYY-MM-DD).

          external_references: Structured external references ({ url, description }). Public: returned to all
              accounts.

          internal_aliases: Internal structured aliases ({ value, confidence 1-10, tlp }). CFONE-only: never
              returned to non-CFONE accounts.

          motive: Actor motive. Allowed values: Convenience, Fear, Fun, Financial, Grudge,
              Ideology, Espionage.

          motive_confidence: Confidence (1-10) in the actor motive. CFONE-only: stripped from responses to
              non-CFONE accounts.

          origin_country_confidence: Confidence (1-10) in the origin-country attribution. CFONE-only: stripped from
              responses to non-CFONE accounts.

          origin_country_tlp: TLP marking for the origin-country attribution. CFONE-only: stripped from
              responses to non-CFONE accounts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tag_uuid:
            raise ValueError(f"Expected a non-empty value for `tag_uuid` but received {tag_uuid!r}")
        return await self._patch(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/tags/{tag_uuid}", account_id=account_id, tag_uuid=tag_uuid
            ),
            body=await async_maybe_transform(
                {
                    "active_duration": active_duration,
                    "actor_category": actor_category,
                    "actor_category_confidence": actor_category_confidence,
                    "aliases": aliases,
                    "alias_group_names": alias_group_names,
                    "alias_group_names_internal": alias_group_names_internal,
                    "analytic_priority": analytic_priority,
                    "attribution_confidence": attribution_confidence,
                    "attribution_confidence_score": attribution_confidence_score,
                    "attribution_organization": attribution_organization,
                    "category_uuid": category_uuid,
                    "date_of_discovery": date_of_discovery,
                    "external_reference_links": external_reference_links,
                    "external_references": external_references,
                    "internal_aliases": internal_aliases,
                    "internal_description": internal_description,
                    "motive": motive,
                    "motive_confidence": motive_confidence,
                    "opsec_level": opsec_level,
                    "origin_country_confidence": origin_country_confidence,
                    "origin_country_iso": origin_country_iso,
                    "origin_country_tlp": origin_country_tlp,
                    "priority": priority,
                    "sophistication_level": sophistication_level,
                    "value": value,
                },
                tag_edit_params.TagEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TagEditResponse,
        )


class TagsResourceWithRawResponse:
    def __init__(self, tags: TagsResource) -> None:
        self._tags = tags

        self.create = to_raw_response_wrapper(
            tags.create,
        )
        self.list = to_raw_response_wrapper(
            tags.list,
        )
        self.delete = to_raw_response_wrapper(
            tags.delete,
        )
        self.edit = to_raw_response_wrapper(
            tags.edit,
        )

    @cached_property
    def categories(self) -> CategoriesResourceWithRawResponse:
        return CategoriesResourceWithRawResponse(self._tags.categories)

    @cached_property
    def indicators(self) -> IndicatorsResourceWithRawResponse:
        return IndicatorsResourceWithRawResponse(self._tags.indicators)


class AsyncTagsResourceWithRawResponse:
    def __init__(self, tags: AsyncTagsResource) -> None:
        self._tags = tags

        self.create = async_to_raw_response_wrapper(
            tags.create,
        )
        self.list = async_to_raw_response_wrapper(
            tags.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tags.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            tags.edit,
        )

    @cached_property
    def categories(self) -> AsyncCategoriesResourceWithRawResponse:
        return AsyncCategoriesResourceWithRawResponse(self._tags.categories)

    @cached_property
    def indicators(self) -> AsyncIndicatorsResourceWithRawResponse:
        return AsyncIndicatorsResourceWithRawResponse(self._tags.indicators)


class TagsResourceWithStreamingResponse:
    def __init__(self, tags: TagsResource) -> None:
        self._tags = tags

        self.create = to_streamed_response_wrapper(
            tags.create,
        )
        self.list = to_streamed_response_wrapper(
            tags.list,
        )
        self.delete = to_streamed_response_wrapper(
            tags.delete,
        )
        self.edit = to_streamed_response_wrapper(
            tags.edit,
        )

    @cached_property
    def categories(self) -> CategoriesResourceWithStreamingResponse:
        return CategoriesResourceWithStreamingResponse(self._tags.categories)

    @cached_property
    def indicators(self) -> IndicatorsResourceWithStreamingResponse:
        return IndicatorsResourceWithStreamingResponse(self._tags.indicators)


class AsyncTagsResourceWithStreamingResponse:
    def __init__(self, tags: AsyncTagsResource) -> None:
        self._tags = tags

        self.create = async_to_streamed_response_wrapper(
            tags.create,
        )
        self.list = async_to_streamed_response_wrapper(
            tags.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tags.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            tags.edit,
        )

    @cached_property
    def categories(self) -> AsyncCategoriesResourceWithStreamingResponse:
        return AsyncCategoriesResourceWithStreamingResponse(self._tags.categories)

    @cached_property
    def indicators(self) -> AsyncIndicatorsResourceWithStreamingResponse:
        return AsyncIndicatorsResourceWithStreamingResponse(self._tags.indicators)
