# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.security_center import (
    InsightGetResponse,
    InsightDismissResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInsights:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_dismiss(self, client: Cloudflare) -> None:
        insight = client.security_center.insights.dismiss(
            issue_id="issue_id",
            account_id="account_id",
        )
        assert_matches_type(InsightDismissResponse, insight, path=["response"])

    @parametrize
    def test_method_dismiss_with_all_params(self, client: Cloudflare) -> None:
        insight = client.security_center.insights.dismiss(
            issue_id="issue_id",
            account_id="account_id",
            dismiss=True,
        )
        assert_matches_type(InsightDismissResponse, insight, path=["response"])

    @parametrize
    def test_raw_response_dismiss(self, client: Cloudflare) -> None:
        response = client.security_center.insights.with_raw_response.dismiss(
            issue_id="issue_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = response.parse()
        assert_matches_type(InsightDismissResponse, insight, path=["response"])

    @parametrize
    def test_streaming_response_dismiss(self, client: Cloudflare) -> None:
        with client.security_center.insights.with_streaming_response.dismiss(
            issue_id="issue_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = response.parse()
            assert_matches_type(InsightDismissResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_dismiss(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `issue_id` but received ''"):
            client.security_center.insights.with_raw_response.dismiss(
                issue_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.security_center.insights.with_raw_response.dismiss(
                issue_id="issue_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.security_center.insights.with_raw_response.dismiss(
                issue_id="issue_id",
                account_id="account_id",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        insight = client.security_center.insights.get(
            account_id="account_id",
        )
        assert_matches_type(Optional[InsightGetResponse], insight, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        insight = client.security_center.insights.get(
            account_id="account_id",
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
        assert_matches_type(Optional[InsightGetResponse], insight, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.security_center.insights.with_raw_response.get(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = response.parse()
        assert_matches_type(Optional[InsightGetResponse], insight, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.security_center.insights.with_streaming_response.get(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = response.parse()
            assert_matches_type(Optional[InsightGetResponse], insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.security_center.insights.with_raw_response.get(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.security_center.insights.with_raw_response.get(
                account_id="account_id",
            )


class TestAsyncInsights:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_dismiss(self, async_client: AsyncCloudflare) -> None:
        insight = await async_client.security_center.insights.dismiss(
            issue_id="issue_id",
            account_id="account_id",
        )
        assert_matches_type(InsightDismissResponse, insight, path=["response"])

    @parametrize
    async def test_method_dismiss_with_all_params(self, async_client: AsyncCloudflare) -> None:
        insight = await async_client.security_center.insights.dismiss(
            issue_id="issue_id",
            account_id="account_id",
            dismiss=True,
        )
        assert_matches_type(InsightDismissResponse, insight, path=["response"])

    @parametrize
    async def test_raw_response_dismiss(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.security_center.insights.with_raw_response.dismiss(
            issue_id="issue_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = await response.parse()
        assert_matches_type(InsightDismissResponse, insight, path=["response"])

    @parametrize
    async def test_streaming_response_dismiss(self, async_client: AsyncCloudflare) -> None:
        async with async_client.security_center.insights.with_streaming_response.dismiss(
            issue_id="issue_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = await response.parse()
            assert_matches_type(InsightDismissResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_dismiss(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `issue_id` but received ''"):
            await async_client.security_center.insights.with_raw_response.dismiss(
                issue_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.security_center.insights.with_raw_response.dismiss(
                issue_id="issue_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.security_center.insights.with_raw_response.dismiss(
                issue_id="issue_id",
                account_id="account_id",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        insight = await async_client.security_center.insights.get(
            account_id="account_id",
        )
        assert_matches_type(Optional[InsightGetResponse], insight, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        insight = await async_client.security_center.insights.get(
            account_id="account_id",
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
        assert_matches_type(Optional[InsightGetResponse], insight, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.security_center.insights.with_raw_response.get(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = await response.parse()
        assert_matches_type(Optional[InsightGetResponse], insight, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.security_center.insights.with_streaming_response.get(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = await response.parse()
            assert_matches_type(Optional[InsightGetResponse], insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.security_center.insights.with_raw_response.get(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.security_center.insights.with_raw_response.get(
                account_id="account_id",
            )
