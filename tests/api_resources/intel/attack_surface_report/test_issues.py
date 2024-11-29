# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePagination, AsyncV4PagePagination
from cloudflare.types.intel.attack_surface_report import (
    IssueListResponse,
    IssueTypeResponse,
    IssueClassResponse,
    IssueDismissResponse,
    IssueSeverityResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIssues:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        issue = client.intel.attack_surface_report.issues.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePagination[Optional[IssueListResponse]], issue, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        issue = client.intel.attack_surface_report.issues.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dismissed=False,
            issue_class=["a_record_dangling", "always_use_https_not_enabled"],
            issue_class_neq=["a_record_dangling", "always_use_https_not_enabled"],
            issue_type=["compliance_violation", "email_security"],
            issue_type_neq=["compliance_violation", "email_security"],
            page=1,
            per_page=25,
            product=["access", "dns"],
            product_neq=["access", "dns"],
            severity=["low", "moderate"],
            severity_neq=["low", "moderate"],
            subject=["example.com"],
            subject_neq=["example.com"],
        )
        assert_matches_type(SyncV4PagePagination[Optional[IssueListResponse]], issue, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.intel.attack_surface_report.issues.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        issue = response.parse()
        assert_matches_type(SyncV4PagePagination[Optional[IssueListResponse]], issue, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.intel.attack_surface_report.issues.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            issue = response.parse()
            assert_matches_type(SyncV4PagePagination[Optional[IssueListResponse]], issue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.intel.attack_surface_report.issues.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_class(self, client: Cloudflare) -> None:
        issue = client.intel.attack_surface_report.issues.class_(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IssueClassResponse], issue, path=["response"])

    @parametrize
    def test_method_class_with_all_params(self, client: Cloudflare) -> None:
        issue = client.intel.attack_surface_report.issues.class_(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dismissed=False,
            issue_class=["a_record_dangling", "always_use_https_not_enabled"],
            issue_class_neq=["a_record_dangling", "always_use_https_not_enabled"],
            issue_type=["compliance_violation", "email_security"],
            issue_type_neq=["compliance_violation", "email_security"],
            product=["access", "dns"],
            product_neq=["access", "dns"],
            severity=["low", "moderate"],
            severity_neq=["low", "moderate"],
            subject=["example.com"],
            subject_neq=["example.com"],
        )
        assert_matches_type(Optional[IssueClassResponse], issue, path=["response"])

    @parametrize
    def test_raw_response_class(self, client: Cloudflare) -> None:
        response = client.intel.attack_surface_report.issues.with_raw_response.class_(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        issue = response.parse()
        assert_matches_type(Optional[IssueClassResponse], issue, path=["response"])

    @parametrize
    def test_streaming_response_class(self, client: Cloudflare) -> None:
        with client.intel.attack_surface_report.issues.with_streaming_response.class_(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            issue = response.parse()
            assert_matches_type(Optional[IssueClassResponse], issue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_class(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.intel.attack_surface_report.issues.with_raw_response.class_(
                account_id="",
            )

    @parametrize
    def test_method_dismiss(self, client: Cloudflare) -> None:
        issue = client.intel.attack_surface_report.issues.dismiss(
            issue_id="issue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IssueDismissResponse, issue, path=["response"])

    @parametrize
    def test_method_dismiss_with_all_params(self, client: Cloudflare) -> None:
        issue = client.intel.attack_surface_report.issues.dismiss(
            issue_id="issue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dismiss=True,
        )
        assert_matches_type(IssueDismissResponse, issue, path=["response"])

    @parametrize
    def test_raw_response_dismiss(self, client: Cloudflare) -> None:
        response = client.intel.attack_surface_report.issues.with_raw_response.dismiss(
            issue_id="issue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        issue = response.parse()
        assert_matches_type(IssueDismissResponse, issue, path=["response"])

    @parametrize
    def test_streaming_response_dismiss(self, client: Cloudflare) -> None:
        with client.intel.attack_surface_report.issues.with_streaming_response.dismiss(
            issue_id="issue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            issue = response.parse()
            assert_matches_type(IssueDismissResponse, issue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_dismiss(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.intel.attack_surface_report.issues.with_raw_response.dismiss(
                issue_id="issue_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `issue_id` but received ''"):
            client.intel.attack_surface_report.issues.with_raw_response.dismiss(
                issue_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_severity(self, client: Cloudflare) -> None:
        issue = client.intel.attack_surface_report.issues.severity(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IssueSeverityResponse], issue, path=["response"])

    @parametrize
    def test_method_severity_with_all_params(self, client: Cloudflare) -> None:
        issue = client.intel.attack_surface_report.issues.severity(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dismissed=False,
            issue_class=["a_record_dangling", "always_use_https_not_enabled"],
            issue_class_neq=["a_record_dangling", "always_use_https_not_enabled"],
            issue_type=["compliance_violation", "email_security"],
            issue_type_neq=["compliance_violation", "email_security"],
            product=["access", "dns"],
            product_neq=["access", "dns"],
            severity=["low", "moderate"],
            severity_neq=["low", "moderate"],
            subject=["example.com"],
            subject_neq=["example.com"],
        )
        assert_matches_type(Optional[IssueSeverityResponse], issue, path=["response"])

    @parametrize
    def test_raw_response_severity(self, client: Cloudflare) -> None:
        response = client.intel.attack_surface_report.issues.with_raw_response.severity(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        issue = response.parse()
        assert_matches_type(Optional[IssueSeverityResponse], issue, path=["response"])

    @parametrize
    def test_streaming_response_severity(self, client: Cloudflare) -> None:
        with client.intel.attack_surface_report.issues.with_streaming_response.severity(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            issue = response.parse()
            assert_matches_type(Optional[IssueSeverityResponse], issue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_severity(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.intel.attack_surface_report.issues.with_raw_response.severity(
                account_id="",
            )

    @parametrize
    def test_method_type(self, client: Cloudflare) -> None:
        issue = client.intel.attack_surface_report.issues.type(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IssueTypeResponse], issue, path=["response"])

    @parametrize
    def test_method_type_with_all_params(self, client: Cloudflare) -> None:
        issue = client.intel.attack_surface_report.issues.type(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dismissed=False,
            issue_class=["a_record_dangling", "always_use_https_not_enabled"],
            issue_class_neq=["a_record_dangling", "always_use_https_not_enabled"],
            issue_type=["compliance_violation", "email_security"],
            issue_type_neq=["compliance_violation", "email_security"],
            product=["access", "dns"],
            product_neq=["access", "dns"],
            severity=["low", "moderate"],
            severity_neq=["low", "moderate"],
            subject=["example.com"],
            subject_neq=["example.com"],
        )
        assert_matches_type(Optional[IssueTypeResponse], issue, path=["response"])

    @parametrize
    def test_raw_response_type(self, client: Cloudflare) -> None:
        response = client.intel.attack_surface_report.issues.with_raw_response.type(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        issue = response.parse()
        assert_matches_type(Optional[IssueTypeResponse], issue, path=["response"])

    @parametrize
    def test_streaming_response_type(self, client: Cloudflare) -> None:
        with client.intel.attack_surface_report.issues.with_streaming_response.type(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            issue = response.parse()
            assert_matches_type(Optional[IssueTypeResponse], issue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_type(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.intel.attack_surface_report.issues.with_raw_response.type(
                account_id="",
            )


class TestAsyncIssues:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        issue = await async_client.intel.attack_surface_report.issues.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePagination[Optional[IssueListResponse]], issue, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        issue = await async_client.intel.attack_surface_report.issues.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dismissed=False,
            issue_class=["a_record_dangling", "always_use_https_not_enabled"],
            issue_class_neq=["a_record_dangling", "always_use_https_not_enabled"],
            issue_type=["compliance_violation", "email_security"],
            issue_type_neq=["compliance_violation", "email_security"],
            page=1,
            per_page=25,
            product=["access", "dns"],
            product_neq=["access", "dns"],
            severity=["low", "moderate"],
            severity_neq=["low", "moderate"],
            subject=["example.com"],
            subject_neq=["example.com"],
        )
        assert_matches_type(AsyncV4PagePagination[Optional[IssueListResponse]], issue, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intel.attack_surface_report.issues.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        issue = await response.parse()
        assert_matches_type(AsyncV4PagePagination[Optional[IssueListResponse]], issue, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intel.attack_surface_report.issues.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            issue = await response.parse()
            assert_matches_type(AsyncV4PagePagination[Optional[IssueListResponse]], issue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.intel.attack_surface_report.issues.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_class(self, async_client: AsyncCloudflare) -> None:
        issue = await async_client.intel.attack_surface_report.issues.class_(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IssueClassResponse], issue, path=["response"])

    @parametrize
    async def test_method_class_with_all_params(self, async_client: AsyncCloudflare) -> None:
        issue = await async_client.intel.attack_surface_report.issues.class_(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dismissed=False,
            issue_class=["a_record_dangling", "always_use_https_not_enabled"],
            issue_class_neq=["a_record_dangling", "always_use_https_not_enabled"],
            issue_type=["compliance_violation", "email_security"],
            issue_type_neq=["compliance_violation", "email_security"],
            product=["access", "dns"],
            product_neq=["access", "dns"],
            severity=["low", "moderate"],
            severity_neq=["low", "moderate"],
            subject=["example.com"],
            subject_neq=["example.com"],
        )
        assert_matches_type(Optional[IssueClassResponse], issue, path=["response"])

    @parametrize
    async def test_raw_response_class(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intel.attack_surface_report.issues.with_raw_response.class_(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        issue = await response.parse()
        assert_matches_type(Optional[IssueClassResponse], issue, path=["response"])

    @parametrize
    async def test_streaming_response_class(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intel.attack_surface_report.issues.with_streaming_response.class_(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            issue = await response.parse()
            assert_matches_type(Optional[IssueClassResponse], issue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_class(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.intel.attack_surface_report.issues.with_raw_response.class_(
                account_id="",
            )

    @parametrize
    async def test_method_dismiss(self, async_client: AsyncCloudflare) -> None:
        issue = await async_client.intel.attack_surface_report.issues.dismiss(
            issue_id="issue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IssueDismissResponse, issue, path=["response"])

    @parametrize
    async def test_method_dismiss_with_all_params(self, async_client: AsyncCloudflare) -> None:
        issue = await async_client.intel.attack_surface_report.issues.dismiss(
            issue_id="issue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dismiss=True,
        )
        assert_matches_type(IssueDismissResponse, issue, path=["response"])

    @parametrize
    async def test_raw_response_dismiss(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intel.attack_surface_report.issues.with_raw_response.dismiss(
            issue_id="issue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        issue = await response.parse()
        assert_matches_type(IssueDismissResponse, issue, path=["response"])

    @parametrize
    async def test_streaming_response_dismiss(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intel.attack_surface_report.issues.with_streaming_response.dismiss(
            issue_id="issue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            issue = await response.parse()
            assert_matches_type(IssueDismissResponse, issue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_dismiss(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.intel.attack_surface_report.issues.with_raw_response.dismiss(
                issue_id="issue_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `issue_id` but received ''"):
            await async_client.intel.attack_surface_report.issues.with_raw_response.dismiss(
                issue_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_severity(self, async_client: AsyncCloudflare) -> None:
        issue = await async_client.intel.attack_surface_report.issues.severity(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IssueSeverityResponse], issue, path=["response"])

    @parametrize
    async def test_method_severity_with_all_params(self, async_client: AsyncCloudflare) -> None:
        issue = await async_client.intel.attack_surface_report.issues.severity(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dismissed=False,
            issue_class=["a_record_dangling", "always_use_https_not_enabled"],
            issue_class_neq=["a_record_dangling", "always_use_https_not_enabled"],
            issue_type=["compliance_violation", "email_security"],
            issue_type_neq=["compliance_violation", "email_security"],
            product=["access", "dns"],
            product_neq=["access", "dns"],
            severity=["low", "moderate"],
            severity_neq=["low", "moderate"],
            subject=["example.com"],
            subject_neq=["example.com"],
        )
        assert_matches_type(Optional[IssueSeverityResponse], issue, path=["response"])

    @parametrize
    async def test_raw_response_severity(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intel.attack_surface_report.issues.with_raw_response.severity(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        issue = await response.parse()
        assert_matches_type(Optional[IssueSeverityResponse], issue, path=["response"])

    @parametrize
    async def test_streaming_response_severity(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intel.attack_surface_report.issues.with_streaming_response.severity(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            issue = await response.parse()
            assert_matches_type(Optional[IssueSeverityResponse], issue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_severity(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.intel.attack_surface_report.issues.with_raw_response.severity(
                account_id="",
            )

    @parametrize
    async def test_method_type(self, async_client: AsyncCloudflare) -> None:
        issue = await async_client.intel.attack_surface_report.issues.type(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IssueTypeResponse], issue, path=["response"])

    @parametrize
    async def test_method_type_with_all_params(self, async_client: AsyncCloudflare) -> None:
        issue = await async_client.intel.attack_surface_report.issues.type(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dismissed=False,
            issue_class=["a_record_dangling", "always_use_https_not_enabled"],
            issue_class_neq=["a_record_dangling", "always_use_https_not_enabled"],
            issue_type=["compliance_violation", "email_security"],
            issue_type_neq=["compliance_violation", "email_security"],
            product=["access", "dns"],
            product_neq=["access", "dns"],
            severity=["low", "moderate"],
            severity_neq=["low", "moderate"],
            subject=["example.com"],
            subject_neq=["example.com"],
        )
        assert_matches_type(Optional[IssueTypeResponse], issue, path=["response"])

    @parametrize
    async def test_raw_response_type(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intel.attack_surface_report.issues.with_raw_response.type(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        issue = await response.parse()
        assert_matches_type(Optional[IssueTypeResponse], issue, path=["response"])

    @parametrize
    async def test_streaming_response_type(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intel.attack_surface_report.issues.with_streaming_response.type(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            issue = await response.parse()
            assert_matches_type(Optional[IssueTypeResponse], issue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_type(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.intel.attack_surface_report.issues.with_raw_response.type(
                account_id="",
            )
