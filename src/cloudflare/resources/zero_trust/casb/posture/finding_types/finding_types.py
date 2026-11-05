# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ......_types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ......_utils import path_template, maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_wrappers import ResultWrapper
from ......pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ......_base_client import AsyncPaginator, make_request_options
from .remediation_types import (
    RemediationTypesResource,
    AsyncRemediationTypesResource,
    RemediationTypesResourceWithRawResponse,
    AsyncRemediationTypesResourceWithRawResponse,
    RemediationTypesResourceWithStreamingResponse,
    AsyncRemediationTypesResourceWithStreamingResponse,
)
from ......types.zero_trust.casb.posture import (
    finding_type_list_params,
    finding_type_create_params,
    finding_type_update_params,
    finding_type_validate_params,
)
from ......types.zero_trust.casb.posture.finding_type_get_response import FindingTypeGetResponse
from ......types.zero_trust.casb.posture.finding_type_list_response import FindingTypeListResponse
from ......types.zero_trust.casb.posture.finding_type_create_response import FindingTypeCreateResponse
from ......types.zero_trust.casb.posture.finding_type_update_response import FindingTypeUpdateResponse
from ......types.zero_trust.casb.posture.finding_type_validate_response import FindingTypeValidateResponse

__all__ = ["FindingTypesResource", "AsyncFindingTypesResource"]


class FindingTypesResource(SyncAPIResource):
    @cached_property
    def remediation_types(self) -> RemediationTypesResource:
        return RemediationTypesResource(self._client)

    @cached_property
    def with_raw_response(self) -> FindingTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return FindingTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FindingTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return FindingTypesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        applies_to_all_integrations: bool,
        asset_class: str,
        asset_vendor: Literal[
            "ANTHROPIC",
            "AWS",
            "BITBUCKET",
            "BOX",
            "CONFLUENCE",
            "DROPBOX",
            "GITHUB",
            "GOOGLE_CLOUD_PLATFORM",
            "GOOGLE_WORKSPACE",
            "JIRA",
            "MICROSOFT",
            "OPENAI",
            "SALESFORCE",
            "SERVICENOW",
            "SLACK",
            "ZOOM",
        ],
        description: str,
        expression: str,
        name: str,
        severity: Literal["Critical", "High", "Medium", "Low"],
        integration_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[FindingTypeCreateResponse]:
        """
        Create a new custom finding type with policy definition.

        Args:
          applies_to_all_integrations: When true, this finding type applies to every current and future integration of
              the vendor.

          asset_class: Asset class this finding type applies to (PascalCase, e.g. GoogleWorkspaceFile)

          asset_vendor: Canonical vendor enum for the platform whose assets this finding type evaluates.

          description: Human-readable description of the finding type. Cannot be empty. Maximum 4096
              characters.

          expression: Rego expression body for the policy. `package cloudflare.casb.custom` and
              `import rego.v1` are added automatically. Do not include package or import
              declarations. This field cannot be changed after creation. Maximum 4096
              characters.

          name: Human-readable name for the finding type. Maximum 256 characters.

          severity: Default severity used when no integration-specific severity override exists.

          integration_ids: Required and non-empty when applies_to_all_integrations is false; omit when it
              is true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/data-security/posture/finding_types", account_id=account_id),
            body=maybe_transform(
                {
                    "applies_to_all_integrations": applies_to_all_integrations,
                    "asset_class": asset_class,
                    "asset_vendor": asset_vendor,
                    "description": description,
                    "expression": expression,
                    "name": name,
                    "severity": severity,
                    "integration_ids": integration_ids,
                },
                finding_type_create_params.FindingTypeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FindingTypeCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FindingTypeCreateResponse]], ResultWrapper[FindingTypeCreateResponse]),
        )

    def update(
        self,
        finding_type_id: str,
        *,
        account_id: str,
        applies_to_all_integrations: bool,
        description: str | Omit = omit,
        integration_ids: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        severity: Literal["Critical", "High", "Medium", "Low"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[FindingTypeUpdateResponse]:
        """
        Update an existing custom finding type.

        **Immutable fields**: asset_vendor, asset_class, expression, and category cannot
        be changed after creation.

        **Security**: Only custom finding types (not system-managed) can be updated.

        Args:
          applies_to_all_integrations: When true, this finding type applies to every current and future integration of
              the vendor.

          description: Optional description of the finding type. Cannot be empty if provided. Maximum
              4096 characters.

          integration_ids: Required and non-empty when applies_to_all_integrations is false; omit when it
              is true.

          name: Human-readable name for the finding type. Cannot be empty if provided. Maximum
              256 characters.

          severity: Default severity used when no integration-specific severity override exists.
              Changing it reclassifies existing and future findings that do not have an
              override.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not finding_type_id:
            raise ValueError(f"Expected a non-empty value for `finding_type_id` but received {finding_type_id!r}")
        return self._put(
            path_template(
                "/accounts/{account_id}/data-security/posture/finding_types/{finding_type_id}",
                account_id=account_id,
                finding_type_id=finding_type_id,
            ),
            body=maybe_transform(
                {
                    "applies_to_all_integrations": applies_to_all_integrations,
                    "description": description,
                    "integration_ids": integration_ids,
                    "name": name,
                    "severity": severity,
                },
                finding_type_update_params.FindingTypeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FindingTypeUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FindingTypeUpdateResponse]], ResultWrapper[FindingTypeUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | Omit = omit,
        max_updated_at: Union[str, datetime] | Omit = omit,
        min_updated_at: Union[str, datetime] | Omit = omit,
        order: Literal["created", "updated", "match_count", "name", "vendor", "type", "origin", "severity"]
        | Omit = omit,
        origins: List[Literal["custom", "system"]] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        quarantined: bool | Omit = omit,
        search: str | Omit = omit,
        severities: List[Literal["critical", "high", "medium", "low"]] | Omit = omit,
        types: List[Literal["Content", "Posture"]] | Omit = omit,
        vendors: List[
            Literal[
                "ANTHROPIC",
                "AWS",
                "BITBUCKET",
                "BOX",
                "CONFLUENCE",
                "DROPBOX",
                "GITHUB",
                "GOOGLE_CLOUD_PLATFORM",
                "GOOGLE_WORKSPACE",
                "JIRA",
                "MICROSOFT",
                "OPENAI",
                "SALESFORCE",
                "SERVICENOW",
                "SLACK",
                "ZOOM",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[FindingTypeListResponse]:
        """
        List all available finding types with pagination support.

        Args:
          direction: Sort direction for the primary field. Defaults to 'desc'. Ties are resolved by
              case-insensitive name, then ID, both ascending regardless of direction.

          max_updated_at: Return only finding types updated at or before this RFC 3339 timestamp
              (inclusive).

          min_updated_at: Return only finding types updated at or after this RFC 3339 timestamp
              (inclusive).

          order: Field to sort by (case-insensitive). Defaults to 'created'. Name and vendor
              sorting is case-insensitive; vendor uses friendly provider names. Ascending
              order: type Content then Posture; origin custom then system; severity Low,
              Medium, High, Critical.

          origins: Filter finding types by origin. Supports multiple comma-separated,
              case-insensitive values.

          page: A page number within the paginated result set.

          per_page: Number of results to return per page.

          quarantined: When true, return only quarantined finding types; when false, return only
              non-quarantined finding types. Omit to return both.

          search: Filter finding types by name or ID (case-insensitive substring match).

          severities: Filter finding types by severity. Supports multiple comma-separated,
              case-insensitive values.

          types: Filter finding types by category type. Supports multiple comma-separated,
              case-insensitive values.

          vendors: Filter finding types by vendor. Supports multiple comma-separated values. Each
              value may be either the vendor enum (GOOGLE_WORKSPACE) or the friendly name
              returned by the read routes (Google Workspace).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/data-security/posture/finding_types", account_id=account_id),
            page=SyncV4PagePaginationArray[FindingTypeListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "max_updated_at": max_updated_at,
                        "min_updated_at": min_updated_at,
                        "order": order,
                        "origins": origins,
                        "page": page,
                        "per_page": per_page,
                        "quarantined": quarantined,
                        "search": search,
                        "severities": severities,
                        "types": types,
                        "vendors": vendors,
                    },
                    finding_type_list_params.FindingTypeListParams,
                ),
            ),
            model=FindingTypeListResponse,
        )

    def delete(
        self,
        finding_type_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an existing custom finding type.

        **Security**: Only custom finding types (not system-managed) can be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not finding_type_id:
            raise ValueError(f"Expected a non-empty value for `finding_type_id` but received {finding_type_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/accounts/{account_id}/data-security/posture/finding_types/{finding_type_id}",
                account_id=account_id,
                finding_type_id=finding_type_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        finding_type_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[FindingTypeGetResponse]:
        """
        Retrieve a specific finding type by its unique identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not finding_type_id:
            raise ValueError(f"Expected a non-empty value for `finding_type_id` but received {finding_type_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/data-security/posture/finding_types/{finding_type_id}",
                account_id=account_id,
                finding_type_id=finding_type_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FindingTypeGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FindingTypeGetResponse]], ResultWrapper[FindingTypeGetResponse]),
        )

    def validate(
        self,
        *,
        account_id: str,
        applies_to_all_integrations: bool,
        asset_class: str,
        asset_vendor: Literal[
            "ANTHROPIC",
            "AWS",
            "BITBUCKET",
            "BOX",
            "CONFLUENCE",
            "DROPBOX",
            "GITHUB",
            "GOOGLE_CLOUD_PLATFORM",
            "GOOGLE_WORKSPACE",
            "JIRA",
            "MICROSOFT",
            "OPENAI",
            "SALESFORCE",
            "SERVICENOW",
            "SLACK",
            "ZOOM",
        ],
        description: str,
        expression: str,
        name: str,
        severity: Literal["Critical", "High", "Medium", "Low"],
        integration_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[FindingTypeValidateResponse]:
        """
        Check a candidate custom finding type without creating it, so problems can be
        corrected before publishing. The request body is the same shape as
        `CreateFindingType`, and the candidate is checked against the same rules, so a
        valid result means the definition itself is sound. It is not a reservation: a
        create can still be rejected for a reason that does not belong to the
        definition, such as the account already holding the maximum number of custom
        finding types.

        A candidate that fails validation is still a **200** with `result.valid: false`
        and one entry in `result.errors` per problem — that is the answer this endpoint
        exists to give. `4xx` is reserved for a request that could not be processed at
        all, such as a body that will not parse.

        Args:
          applies_to_all_integrations: When true, this finding type applies to every current and future integration of
              the vendor.

          asset_class: Asset class this finding type applies to (PascalCase, e.g. GoogleWorkspaceFile)

          asset_vendor: Canonical vendor enum for the platform whose assets this finding type evaluates.

          description: Human-readable description of the finding type. Cannot be empty. Maximum 4096
              characters.

          expression: Rego expression body for the policy. `package cloudflare.casb.custom` and
              `import rego.v1` are added automatically. Do not include package or import
              declarations. This field cannot be changed after creation. Maximum 4096
              characters.

          name: Human-readable name for the finding type. Maximum 256 characters.

          severity: Default severity used when no integration-specific severity override exists.

          integration_ids: Required and non-empty when applies_to_all_integrations is false; omit when it
              is true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/data-security/posture/finding_types/validate", account_id=account_id),
            body=maybe_transform(
                {
                    "applies_to_all_integrations": applies_to_all_integrations,
                    "asset_class": asset_class,
                    "asset_vendor": asset_vendor,
                    "description": description,
                    "expression": expression,
                    "name": name,
                    "severity": severity,
                    "integration_ids": integration_ids,
                },
                finding_type_validate_params.FindingTypeValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FindingTypeValidateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FindingTypeValidateResponse]], ResultWrapper[FindingTypeValidateResponse]),
        )


class AsyncFindingTypesResource(AsyncAPIResource):
    @cached_property
    def remediation_types(self) -> AsyncRemediationTypesResource:
        return AsyncRemediationTypesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFindingTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFindingTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFindingTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncFindingTypesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        applies_to_all_integrations: bool,
        asset_class: str,
        asset_vendor: Literal[
            "ANTHROPIC",
            "AWS",
            "BITBUCKET",
            "BOX",
            "CONFLUENCE",
            "DROPBOX",
            "GITHUB",
            "GOOGLE_CLOUD_PLATFORM",
            "GOOGLE_WORKSPACE",
            "JIRA",
            "MICROSOFT",
            "OPENAI",
            "SALESFORCE",
            "SERVICENOW",
            "SLACK",
            "ZOOM",
        ],
        description: str,
        expression: str,
        name: str,
        severity: Literal["Critical", "High", "Medium", "Low"],
        integration_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[FindingTypeCreateResponse]:
        """
        Create a new custom finding type with policy definition.

        Args:
          applies_to_all_integrations: When true, this finding type applies to every current and future integration of
              the vendor.

          asset_class: Asset class this finding type applies to (PascalCase, e.g. GoogleWorkspaceFile)

          asset_vendor: Canonical vendor enum for the platform whose assets this finding type evaluates.

          description: Human-readable description of the finding type. Cannot be empty. Maximum 4096
              characters.

          expression: Rego expression body for the policy. `package cloudflare.casb.custom` and
              `import rego.v1` are added automatically. Do not include package or import
              declarations. This field cannot be changed after creation. Maximum 4096
              characters.

          name: Human-readable name for the finding type. Maximum 256 characters.

          severity: Default severity used when no integration-specific severity override exists.

          integration_ids: Required and non-empty when applies_to_all_integrations is false; omit when it
              is true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/data-security/posture/finding_types", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "applies_to_all_integrations": applies_to_all_integrations,
                    "asset_class": asset_class,
                    "asset_vendor": asset_vendor,
                    "description": description,
                    "expression": expression,
                    "name": name,
                    "severity": severity,
                    "integration_ids": integration_ids,
                },
                finding_type_create_params.FindingTypeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FindingTypeCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FindingTypeCreateResponse]], ResultWrapper[FindingTypeCreateResponse]),
        )

    async def update(
        self,
        finding_type_id: str,
        *,
        account_id: str,
        applies_to_all_integrations: bool,
        description: str | Omit = omit,
        integration_ids: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        severity: Literal["Critical", "High", "Medium", "Low"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[FindingTypeUpdateResponse]:
        """
        Update an existing custom finding type.

        **Immutable fields**: asset_vendor, asset_class, expression, and category cannot
        be changed after creation.

        **Security**: Only custom finding types (not system-managed) can be updated.

        Args:
          applies_to_all_integrations: When true, this finding type applies to every current and future integration of
              the vendor.

          description: Optional description of the finding type. Cannot be empty if provided. Maximum
              4096 characters.

          integration_ids: Required and non-empty when applies_to_all_integrations is false; omit when it
              is true.

          name: Human-readable name for the finding type. Cannot be empty if provided. Maximum
              256 characters.

          severity: Default severity used when no integration-specific severity override exists.
              Changing it reclassifies existing and future findings that do not have an
              override.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not finding_type_id:
            raise ValueError(f"Expected a non-empty value for `finding_type_id` but received {finding_type_id!r}")
        return await self._put(
            path_template(
                "/accounts/{account_id}/data-security/posture/finding_types/{finding_type_id}",
                account_id=account_id,
                finding_type_id=finding_type_id,
            ),
            body=await async_maybe_transform(
                {
                    "applies_to_all_integrations": applies_to_all_integrations,
                    "description": description,
                    "integration_ids": integration_ids,
                    "name": name,
                    "severity": severity,
                },
                finding_type_update_params.FindingTypeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FindingTypeUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FindingTypeUpdateResponse]], ResultWrapper[FindingTypeUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | Omit = omit,
        max_updated_at: Union[str, datetime] | Omit = omit,
        min_updated_at: Union[str, datetime] | Omit = omit,
        order: Literal["created", "updated", "match_count", "name", "vendor", "type", "origin", "severity"]
        | Omit = omit,
        origins: List[Literal["custom", "system"]] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        quarantined: bool | Omit = omit,
        search: str | Omit = omit,
        severities: List[Literal["critical", "high", "medium", "low"]] | Omit = omit,
        types: List[Literal["Content", "Posture"]] | Omit = omit,
        vendors: List[
            Literal[
                "ANTHROPIC",
                "AWS",
                "BITBUCKET",
                "BOX",
                "CONFLUENCE",
                "DROPBOX",
                "GITHUB",
                "GOOGLE_CLOUD_PLATFORM",
                "GOOGLE_WORKSPACE",
                "JIRA",
                "MICROSOFT",
                "OPENAI",
                "SALESFORCE",
                "SERVICENOW",
                "SLACK",
                "ZOOM",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[FindingTypeListResponse, AsyncV4PagePaginationArray[FindingTypeListResponse]]:
        """
        List all available finding types with pagination support.

        Args:
          direction: Sort direction for the primary field. Defaults to 'desc'. Ties are resolved by
              case-insensitive name, then ID, both ascending regardless of direction.

          max_updated_at: Return only finding types updated at or before this RFC 3339 timestamp
              (inclusive).

          min_updated_at: Return only finding types updated at or after this RFC 3339 timestamp
              (inclusive).

          order: Field to sort by (case-insensitive). Defaults to 'created'. Name and vendor
              sorting is case-insensitive; vendor uses friendly provider names. Ascending
              order: type Content then Posture; origin custom then system; severity Low,
              Medium, High, Critical.

          origins: Filter finding types by origin. Supports multiple comma-separated,
              case-insensitive values.

          page: A page number within the paginated result set.

          per_page: Number of results to return per page.

          quarantined: When true, return only quarantined finding types; when false, return only
              non-quarantined finding types. Omit to return both.

          search: Filter finding types by name or ID (case-insensitive substring match).

          severities: Filter finding types by severity. Supports multiple comma-separated,
              case-insensitive values.

          types: Filter finding types by category type. Supports multiple comma-separated,
              case-insensitive values.

          vendors: Filter finding types by vendor. Supports multiple comma-separated values. Each
              value may be either the vendor enum (GOOGLE_WORKSPACE) or the friendly name
              returned by the read routes (Google Workspace).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/data-security/posture/finding_types", account_id=account_id),
            page=AsyncV4PagePaginationArray[FindingTypeListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "max_updated_at": max_updated_at,
                        "min_updated_at": min_updated_at,
                        "order": order,
                        "origins": origins,
                        "page": page,
                        "per_page": per_page,
                        "quarantined": quarantined,
                        "search": search,
                        "severities": severities,
                        "types": types,
                        "vendors": vendors,
                    },
                    finding_type_list_params.FindingTypeListParams,
                ),
            ),
            model=FindingTypeListResponse,
        )

    async def delete(
        self,
        finding_type_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an existing custom finding type.

        **Security**: Only custom finding types (not system-managed) can be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not finding_type_id:
            raise ValueError(f"Expected a non-empty value for `finding_type_id` but received {finding_type_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/accounts/{account_id}/data-security/posture/finding_types/{finding_type_id}",
                account_id=account_id,
                finding_type_id=finding_type_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        finding_type_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[FindingTypeGetResponse]:
        """
        Retrieve a specific finding type by its unique identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not finding_type_id:
            raise ValueError(f"Expected a non-empty value for `finding_type_id` but received {finding_type_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/data-security/posture/finding_types/{finding_type_id}",
                account_id=account_id,
                finding_type_id=finding_type_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FindingTypeGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FindingTypeGetResponse]], ResultWrapper[FindingTypeGetResponse]),
        )

    async def validate(
        self,
        *,
        account_id: str,
        applies_to_all_integrations: bool,
        asset_class: str,
        asset_vendor: Literal[
            "ANTHROPIC",
            "AWS",
            "BITBUCKET",
            "BOX",
            "CONFLUENCE",
            "DROPBOX",
            "GITHUB",
            "GOOGLE_CLOUD_PLATFORM",
            "GOOGLE_WORKSPACE",
            "JIRA",
            "MICROSOFT",
            "OPENAI",
            "SALESFORCE",
            "SERVICENOW",
            "SLACK",
            "ZOOM",
        ],
        description: str,
        expression: str,
        name: str,
        severity: Literal["Critical", "High", "Medium", "Low"],
        integration_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[FindingTypeValidateResponse]:
        """
        Check a candidate custom finding type without creating it, so problems can be
        corrected before publishing. The request body is the same shape as
        `CreateFindingType`, and the candidate is checked against the same rules, so a
        valid result means the definition itself is sound. It is not a reservation: a
        create can still be rejected for a reason that does not belong to the
        definition, such as the account already holding the maximum number of custom
        finding types.

        A candidate that fails validation is still a **200** with `result.valid: false`
        and one entry in `result.errors` per problem — that is the answer this endpoint
        exists to give. `4xx` is reserved for a request that could not be processed at
        all, such as a body that will not parse.

        Args:
          applies_to_all_integrations: When true, this finding type applies to every current and future integration of
              the vendor.

          asset_class: Asset class this finding type applies to (PascalCase, e.g. GoogleWorkspaceFile)

          asset_vendor: Canonical vendor enum for the platform whose assets this finding type evaluates.

          description: Human-readable description of the finding type. Cannot be empty. Maximum 4096
              characters.

          expression: Rego expression body for the policy. `package cloudflare.casb.custom` and
              `import rego.v1` are added automatically. Do not include package or import
              declarations. This field cannot be changed after creation. Maximum 4096
              characters.

          name: Human-readable name for the finding type. Maximum 256 characters.

          severity: Default severity used when no integration-specific severity override exists.

          integration_ids: Required and non-empty when applies_to_all_integrations is false; omit when it
              is true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/data-security/posture/finding_types/validate", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "applies_to_all_integrations": applies_to_all_integrations,
                    "asset_class": asset_class,
                    "asset_vendor": asset_vendor,
                    "description": description,
                    "expression": expression,
                    "name": name,
                    "severity": severity,
                    "integration_ids": integration_ids,
                },
                finding_type_validate_params.FindingTypeValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FindingTypeValidateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FindingTypeValidateResponse]], ResultWrapper[FindingTypeValidateResponse]),
        )


class FindingTypesResourceWithRawResponse:
    def __init__(self, finding_types: FindingTypesResource) -> None:
        self._finding_types = finding_types

        self.create = to_raw_response_wrapper(
            finding_types.create,
        )
        self.update = to_raw_response_wrapper(
            finding_types.update,
        )
        self.list = to_raw_response_wrapper(
            finding_types.list,
        )
        self.delete = to_raw_response_wrapper(
            finding_types.delete,
        )
        self.get = to_raw_response_wrapper(
            finding_types.get,
        )
        self.validate = to_raw_response_wrapper(
            finding_types.validate,
        )

    @cached_property
    def remediation_types(self) -> RemediationTypesResourceWithRawResponse:
        return RemediationTypesResourceWithRawResponse(self._finding_types.remediation_types)


class AsyncFindingTypesResourceWithRawResponse:
    def __init__(self, finding_types: AsyncFindingTypesResource) -> None:
        self._finding_types = finding_types

        self.create = async_to_raw_response_wrapper(
            finding_types.create,
        )
        self.update = async_to_raw_response_wrapper(
            finding_types.update,
        )
        self.list = async_to_raw_response_wrapper(
            finding_types.list,
        )
        self.delete = async_to_raw_response_wrapper(
            finding_types.delete,
        )
        self.get = async_to_raw_response_wrapper(
            finding_types.get,
        )
        self.validate = async_to_raw_response_wrapper(
            finding_types.validate,
        )

    @cached_property
    def remediation_types(self) -> AsyncRemediationTypesResourceWithRawResponse:
        return AsyncRemediationTypesResourceWithRawResponse(self._finding_types.remediation_types)


class FindingTypesResourceWithStreamingResponse:
    def __init__(self, finding_types: FindingTypesResource) -> None:
        self._finding_types = finding_types

        self.create = to_streamed_response_wrapper(
            finding_types.create,
        )
        self.update = to_streamed_response_wrapper(
            finding_types.update,
        )
        self.list = to_streamed_response_wrapper(
            finding_types.list,
        )
        self.delete = to_streamed_response_wrapper(
            finding_types.delete,
        )
        self.get = to_streamed_response_wrapper(
            finding_types.get,
        )
        self.validate = to_streamed_response_wrapper(
            finding_types.validate,
        )

    @cached_property
    def remediation_types(self) -> RemediationTypesResourceWithStreamingResponse:
        return RemediationTypesResourceWithStreamingResponse(self._finding_types.remediation_types)


class AsyncFindingTypesResourceWithStreamingResponse:
    def __init__(self, finding_types: AsyncFindingTypesResource) -> None:
        self._finding_types = finding_types

        self.create = async_to_streamed_response_wrapper(
            finding_types.create,
        )
        self.update = async_to_streamed_response_wrapper(
            finding_types.update,
        )
        self.list = async_to_streamed_response_wrapper(
            finding_types.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            finding_types.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            finding_types.get,
        )
        self.validate = async_to_streamed_response_wrapper(
            finding_types.validate,
        )

    @cached_property
    def remediation_types(self) -> AsyncRemediationTypesResourceWithStreamingResponse:
        return AsyncRemediationTypesResourceWithStreamingResponse(self._finding_types.remediation_types)
