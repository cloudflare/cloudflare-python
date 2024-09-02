# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.intel.attack_surface_report.issue_list_response import IssueListResponse

from ....pagination import SyncV4PagePagination, AsyncV4PagePagination

from ...._utils import maybe_transform, async_maybe_transform

from ...._base_client import make_request_options, AsyncPaginator

from typing import List, Optional, Type

from ....types.intel.attack_surface_report.issue_type import IssueType

from ....types.intel.attack_surface_report.severity_query_param import SeverityQueryParam

from ....types.intel.attack_surface_report.issue_class_response import IssueClassResponse

from ...._wrappers import ResultWrapper

from ....types.intel.attack_surface_report.issue_dismiss_response import IssueDismissResponse

from ....types.intel.attack_surface_report.issue_severity_response import IssueSeverityResponse

from ....types.intel.attack_surface_report.issue_type_response import IssueTypeResponse

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
from ....types.intel.attack_surface_report import issue_list_params
from ....types.intel.attack_surface_report import issue_class_params
from ....types.intel.attack_surface_report import issue_dismiss_params
from ....types.intel.attack_surface_report import issue_severity_params
from ....types.intel.attack_surface_report import issue_type_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["IssuesResource", "AsyncIssuesResource"]


class IssuesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IssuesResourceWithRawResponse:
        return IssuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IssuesResourceWithStreamingResponse:
        return IssuesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        dismissed: bool | NotGiven = NOT_GIVEN,
        issue_class: List[str] | NotGiven = NOT_GIVEN,
        issue_class_neq: List[str] | NotGiven = NOT_GIVEN,
        issue_type: List[IssueType] | NotGiven = NOT_GIVEN,
        issue_type_neq: List[IssueType] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        product: List[str] | NotGiven = NOT_GIVEN,
        product_neq: List[str] | NotGiven = NOT_GIVEN,
        severity: List[SeverityQueryParam] | NotGiven = NOT_GIVEN,
        severity_neq: List[SeverityQueryParam] | NotGiven = NOT_GIVEN,
        subject: List[str] | NotGiven = NOT_GIVEN,
        subject_neq: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePagination[IssueListResponse]:
        """
        Get Security Center Issues

        Args:
          account_id: Identifier

          page: Current page within paginated list of results

          per_page: Number of results per page of results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/intel/attack-surface-report/issues",
            page=SyncV4PagePagination[IssueListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dismissed": dismissed,
                        "issue_class": issue_class,
                        "issue_class_neq": issue_class_neq,
                        "issue_type": issue_type,
                        "issue_type_neq": issue_type_neq,
                        "page": page,
                        "per_page": per_page,
                        "product": product,
                        "product_neq": product_neq,
                        "severity": severity,
                        "severity_neq": severity_neq,
                        "subject": subject,
                        "subject_neq": subject_neq,
                    },
                    issue_list_params.IssueListParams,
                ),
            ),
            model=IssueListResponse,
        )

    def class_(
        self,
        *,
        account_id: str,
        dismissed: bool | NotGiven = NOT_GIVEN,
        issue_class: List[str] | NotGiven = NOT_GIVEN,
        issue_class_neq: List[str] | NotGiven = NOT_GIVEN,
        issue_type: List[IssueType] | NotGiven = NOT_GIVEN,
        issue_type_neq: List[IssueType] | NotGiven = NOT_GIVEN,
        product: List[str] | NotGiven = NOT_GIVEN,
        product_neq: List[str] | NotGiven = NOT_GIVEN,
        severity: List[SeverityQueryParam] | NotGiven = NOT_GIVEN,
        severity_neq: List[SeverityQueryParam] | NotGiven = NOT_GIVEN,
        subject: List[str] | NotGiven = NOT_GIVEN,
        subject_neq: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IssueClassResponse]:
        """
        Get Security Center Issue Counts by Class

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/intel/attack-surface-report/issues/class",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dismissed": dismissed,
                        "issue_class": issue_class,
                        "issue_class_neq": issue_class_neq,
                        "issue_type": issue_type,
                        "issue_type_neq": issue_type_neq,
                        "product": product,
                        "product_neq": product_neq,
                        "severity": severity,
                        "severity_neq": severity_neq,
                        "subject": subject,
                        "subject_neq": subject_neq,
                    },
                    issue_class_params.IssueClassParams,
                ),
                post_parser=ResultWrapper[Optional[IssueClassResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IssueClassResponse]], ResultWrapper[IssueClassResponse]),
        )

    def dismiss(
        self,
        issue_id: str,
        *,
        account_id: str,
        dismiss: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IssueDismissResponse]:
        """
        Archive Security Center Insight

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not issue_id:
            raise ValueError(f"Expected a non-empty value for `issue_id` but received {issue_id!r}")
        return cast(
            Optional[IssueDismissResponse],
            self._put(
                f"/accounts/{account_id}/intel/attack-surface-report/{issue_id}/dismiss",
                body=maybe_transform({"dismiss": dismiss}, issue_dismiss_params.IssueDismissParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[IssueDismissResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[IssueDismissResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def severity(
        self,
        *,
        account_id: str,
        dismissed: bool | NotGiven = NOT_GIVEN,
        issue_class: List[str] | NotGiven = NOT_GIVEN,
        issue_class_neq: List[str] | NotGiven = NOT_GIVEN,
        issue_type: List[IssueType] | NotGiven = NOT_GIVEN,
        issue_type_neq: List[IssueType] | NotGiven = NOT_GIVEN,
        product: List[str] | NotGiven = NOT_GIVEN,
        product_neq: List[str] | NotGiven = NOT_GIVEN,
        severity: List[SeverityQueryParam] | NotGiven = NOT_GIVEN,
        severity_neq: List[SeverityQueryParam] | NotGiven = NOT_GIVEN,
        subject: List[str] | NotGiven = NOT_GIVEN,
        subject_neq: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IssueSeverityResponse]:
        """
        Get Security Center Issue Counts by Severity

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/intel/attack-surface-report/issues/severity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dismissed": dismissed,
                        "issue_class": issue_class,
                        "issue_class_neq": issue_class_neq,
                        "issue_type": issue_type,
                        "issue_type_neq": issue_type_neq,
                        "product": product,
                        "product_neq": product_neq,
                        "severity": severity,
                        "severity_neq": severity_neq,
                        "subject": subject,
                        "subject_neq": subject_neq,
                    },
                    issue_severity_params.IssueSeverityParams,
                ),
                post_parser=ResultWrapper[Optional[IssueSeverityResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IssueSeverityResponse]], ResultWrapper[IssueSeverityResponse]),
        )

    def type(
        self,
        *,
        account_id: str,
        dismissed: bool | NotGiven = NOT_GIVEN,
        issue_class: List[str] | NotGiven = NOT_GIVEN,
        issue_class_neq: List[str] | NotGiven = NOT_GIVEN,
        issue_type: List[IssueType] | NotGiven = NOT_GIVEN,
        issue_type_neq: List[IssueType] | NotGiven = NOT_GIVEN,
        product: List[str] | NotGiven = NOT_GIVEN,
        product_neq: List[str] | NotGiven = NOT_GIVEN,
        severity: List[SeverityQueryParam] | NotGiven = NOT_GIVEN,
        severity_neq: List[SeverityQueryParam] | NotGiven = NOT_GIVEN,
        subject: List[str] | NotGiven = NOT_GIVEN,
        subject_neq: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IssueTypeResponse]:
        """
        Get Security Center Issue Counts by Type

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/intel/attack-surface-report/issues/type",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dismissed": dismissed,
                        "issue_class": issue_class,
                        "issue_class_neq": issue_class_neq,
                        "issue_type": issue_type,
                        "issue_type_neq": issue_type_neq,
                        "product": product,
                        "product_neq": product_neq,
                        "severity": severity,
                        "severity_neq": severity_neq,
                        "subject": subject,
                        "subject_neq": subject_neq,
                    },
                    issue_type_params.IssueTypeParams,
                ),
                post_parser=ResultWrapper[Optional[IssueTypeResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IssueTypeResponse]], ResultWrapper[IssueTypeResponse]),
        )


class AsyncIssuesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIssuesResourceWithRawResponse:
        return AsyncIssuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIssuesResourceWithStreamingResponse:
        return AsyncIssuesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        dismissed: bool | NotGiven = NOT_GIVEN,
        issue_class: List[str] | NotGiven = NOT_GIVEN,
        issue_class_neq: List[str] | NotGiven = NOT_GIVEN,
        issue_type: List[IssueType] | NotGiven = NOT_GIVEN,
        issue_type_neq: List[IssueType] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        product: List[str] | NotGiven = NOT_GIVEN,
        product_neq: List[str] | NotGiven = NOT_GIVEN,
        severity: List[SeverityQueryParam] | NotGiven = NOT_GIVEN,
        severity_neq: List[SeverityQueryParam] | NotGiven = NOT_GIVEN,
        subject: List[str] | NotGiven = NOT_GIVEN,
        subject_neq: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[IssueListResponse, AsyncV4PagePagination[IssueListResponse]]:
        """
        Get Security Center Issues

        Args:
          account_id: Identifier

          page: Current page within paginated list of results

          per_page: Number of results per page of results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/intel/attack-surface-report/issues",
            page=AsyncV4PagePagination[IssueListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dismissed": dismissed,
                        "issue_class": issue_class,
                        "issue_class_neq": issue_class_neq,
                        "issue_type": issue_type,
                        "issue_type_neq": issue_type_neq,
                        "page": page,
                        "per_page": per_page,
                        "product": product,
                        "product_neq": product_neq,
                        "severity": severity,
                        "severity_neq": severity_neq,
                        "subject": subject,
                        "subject_neq": subject_neq,
                    },
                    issue_list_params.IssueListParams,
                ),
            ),
            model=IssueListResponse,
        )

    async def class_(
        self,
        *,
        account_id: str,
        dismissed: bool | NotGiven = NOT_GIVEN,
        issue_class: List[str] | NotGiven = NOT_GIVEN,
        issue_class_neq: List[str] | NotGiven = NOT_GIVEN,
        issue_type: List[IssueType] | NotGiven = NOT_GIVEN,
        issue_type_neq: List[IssueType] | NotGiven = NOT_GIVEN,
        product: List[str] | NotGiven = NOT_GIVEN,
        product_neq: List[str] | NotGiven = NOT_GIVEN,
        severity: List[SeverityQueryParam] | NotGiven = NOT_GIVEN,
        severity_neq: List[SeverityQueryParam] | NotGiven = NOT_GIVEN,
        subject: List[str] | NotGiven = NOT_GIVEN,
        subject_neq: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IssueClassResponse]:
        """
        Get Security Center Issue Counts by Class

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/intel/attack-surface-report/issues/class",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "dismissed": dismissed,
                        "issue_class": issue_class,
                        "issue_class_neq": issue_class_neq,
                        "issue_type": issue_type,
                        "issue_type_neq": issue_type_neq,
                        "product": product,
                        "product_neq": product_neq,
                        "severity": severity,
                        "severity_neq": severity_neq,
                        "subject": subject,
                        "subject_neq": subject_neq,
                    },
                    issue_class_params.IssueClassParams,
                ),
                post_parser=ResultWrapper[Optional[IssueClassResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IssueClassResponse]], ResultWrapper[IssueClassResponse]),
        )

    async def dismiss(
        self,
        issue_id: str,
        *,
        account_id: str,
        dismiss: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IssueDismissResponse]:
        """
        Archive Security Center Insight

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not issue_id:
            raise ValueError(f"Expected a non-empty value for `issue_id` but received {issue_id!r}")
        return cast(
            Optional[IssueDismissResponse],
            await self._put(
                f"/accounts/{account_id}/intel/attack-surface-report/{issue_id}/dismiss",
                body=await async_maybe_transform({"dismiss": dismiss}, issue_dismiss_params.IssueDismissParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[IssueDismissResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[IssueDismissResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def severity(
        self,
        *,
        account_id: str,
        dismissed: bool | NotGiven = NOT_GIVEN,
        issue_class: List[str] | NotGiven = NOT_GIVEN,
        issue_class_neq: List[str] | NotGiven = NOT_GIVEN,
        issue_type: List[IssueType] | NotGiven = NOT_GIVEN,
        issue_type_neq: List[IssueType] | NotGiven = NOT_GIVEN,
        product: List[str] | NotGiven = NOT_GIVEN,
        product_neq: List[str] | NotGiven = NOT_GIVEN,
        severity: List[SeverityQueryParam] | NotGiven = NOT_GIVEN,
        severity_neq: List[SeverityQueryParam] | NotGiven = NOT_GIVEN,
        subject: List[str] | NotGiven = NOT_GIVEN,
        subject_neq: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IssueSeverityResponse]:
        """
        Get Security Center Issue Counts by Severity

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/intel/attack-surface-report/issues/severity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "dismissed": dismissed,
                        "issue_class": issue_class,
                        "issue_class_neq": issue_class_neq,
                        "issue_type": issue_type,
                        "issue_type_neq": issue_type_neq,
                        "product": product,
                        "product_neq": product_neq,
                        "severity": severity,
                        "severity_neq": severity_neq,
                        "subject": subject,
                        "subject_neq": subject_neq,
                    },
                    issue_severity_params.IssueSeverityParams,
                ),
                post_parser=ResultWrapper[Optional[IssueSeverityResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IssueSeverityResponse]], ResultWrapper[IssueSeverityResponse]),
        )

    async def type(
        self,
        *,
        account_id: str,
        dismissed: bool | NotGiven = NOT_GIVEN,
        issue_class: List[str] | NotGiven = NOT_GIVEN,
        issue_class_neq: List[str] | NotGiven = NOT_GIVEN,
        issue_type: List[IssueType] | NotGiven = NOT_GIVEN,
        issue_type_neq: List[IssueType] | NotGiven = NOT_GIVEN,
        product: List[str] | NotGiven = NOT_GIVEN,
        product_neq: List[str] | NotGiven = NOT_GIVEN,
        severity: List[SeverityQueryParam] | NotGiven = NOT_GIVEN,
        severity_neq: List[SeverityQueryParam] | NotGiven = NOT_GIVEN,
        subject: List[str] | NotGiven = NOT_GIVEN,
        subject_neq: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IssueTypeResponse]:
        """
        Get Security Center Issue Counts by Type

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/intel/attack-surface-report/issues/type",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "dismissed": dismissed,
                        "issue_class": issue_class,
                        "issue_class_neq": issue_class_neq,
                        "issue_type": issue_type,
                        "issue_type_neq": issue_type_neq,
                        "product": product,
                        "product_neq": product_neq,
                        "severity": severity,
                        "severity_neq": severity_neq,
                        "subject": subject,
                        "subject_neq": subject_neq,
                    },
                    issue_type_params.IssueTypeParams,
                ),
                post_parser=ResultWrapper[Optional[IssueTypeResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IssueTypeResponse]], ResultWrapper[IssueTypeResponse]),
        )


class IssuesResourceWithRawResponse:
    def __init__(self, issues: IssuesResource) -> None:
        self._issues = issues

        self.list = to_raw_response_wrapper(
            issues.list,
        )
        self.class_ = to_raw_response_wrapper(
            issues.class_,
        )
        self.dismiss = to_raw_response_wrapper(
            issues.dismiss,
        )
        self.severity = to_raw_response_wrapper(
            issues.severity,
        )
        self.type = to_raw_response_wrapper(
            issues.type,
        )


class AsyncIssuesResourceWithRawResponse:
    def __init__(self, issues: AsyncIssuesResource) -> None:
        self._issues = issues

        self.list = async_to_raw_response_wrapper(
            issues.list,
        )
        self.class_ = async_to_raw_response_wrapper(
            issues.class_,
        )
        self.dismiss = async_to_raw_response_wrapper(
            issues.dismiss,
        )
        self.severity = async_to_raw_response_wrapper(
            issues.severity,
        )
        self.type = async_to_raw_response_wrapper(
            issues.type,
        )


class IssuesResourceWithStreamingResponse:
    def __init__(self, issues: IssuesResource) -> None:
        self._issues = issues

        self.list = to_streamed_response_wrapper(
            issues.list,
        )
        self.class_ = to_streamed_response_wrapper(
            issues.class_,
        )
        self.dismiss = to_streamed_response_wrapper(
            issues.dismiss,
        )
        self.severity = to_streamed_response_wrapper(
            issues.severity,
        )
        self.type = to_streamed_response_wrapper(
            issues.type,
        )


class AsyncIssuesResourceWithStreamingResponse:
    def __init__(self, issues: AsyncIssuesResource) -> None:
        self._issues = issues

        self.list = async_to_streamed_response_wrapper(
            issues.list,
        )
        self.class_ = async_to_streamed_response_wrapper(
            issues.class_,
        )
        self.dismiss = async_to_streamed_response_wrapper(
            issues.dismiss,
        )
        self.severity = async_to_streamed_response_wrapper(
            issues.severity,
        )
        self.type = async_to_streamed_response_wrapper(
            issues.type,
        )
