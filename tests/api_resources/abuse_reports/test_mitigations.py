# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage, SyncV4PagePagination, AsyncV4PagePagination
from cloudflare.types.abuse_reports import (
    MitigationListResponse,
    MitigationReviewResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMitigations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: support api token auth scheme")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        mitigation = client.abuse_reports.mitigations.list(
            report_id="report_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePagination[Optional[MitigationListResponse]], mitigation, path=["response"])

    @pytest.mark.skip(reason="TODO: support api token auth scheme")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        mitigation = client.abuse_reports.mitigations.list(
            report_id="report_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            effective_after="2009-11-10T23:00:00Z",
            effective_before="2009-11-10T23:00:00Z",
            entity_type="url_pattern",
            page=0,
            per_page=0,
            sort="type,asc",
            status="pending",
            type="account_suspend",
        )
        assert_matches_type(SyncV4PagePagination[Optional[MitigationListResponse]], mitigation, path=["response"])

    @pytest.mark.skip(reason="TODO: support api token auth scheme")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.abuse_reports.mitigations.with_raw_response.list(
            report_id="report_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mitigation = response.parse()
        assert_matches_type(SyncV4PagePagination[Optional[MitigationListResponse]], mitigation, path=["response"])

    @pytest.mark.skip(reason="TODO: support api token auth scheme")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.abuse_reports.mitigations.with_streaming_response.list(
            report_id="report_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mitigation = response.parse()
            assert_matches_type(SyncV4PagePagination[Optional[MitigationListResponse]], mitigation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: support api token auth scheme")
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.abuse_reports.mitigations.with_raw_response.list(
                report_id="report_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            client.abuse_reports.mitigations.with_raw_response.list(
                report_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: support api token auth scheme")
    @parametrize
    def test_method_review(self, client: Cloudflare) -> None:
        mitigation = client.abuse_reports.mitigations.review(
            report_id="report_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[MitigationReviewResponse], mitigation, path=["response"])

    @pytest.mark.skip(reason="TODO: support api token auth scheme")
    @parametrize
    def test_method_review_with_all_params(self, client: Cloudflare) -> None:
        mitigation = client.abuse_reports.mitigations.review(
            report_id="report_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            appeals=[
                {
                    "id": "id",
                    "reason": "misclassified",
                }
            ],
            data={
                "city": "city",
                "country": "country",
                "email": "dev@stainless.com",
                "full_name": "full_name",
                "jurisdiction_consent": True,
                "perjury_attestation": True,
                "phone_number": "phone_number",
                "signature": "signature",
                "state": "state",
                "street_address": "street_address",
                "urls": ["https://example.com"],
                "zip_code": "zip_code",
                "company": "company",
                "counter_notice_response": "counter_notice_response",
            },
            type="counter_notice",
        )
        assert_matches_type(SyncSinglePage[MitigationReviewResponse], mitigation, path=["response"])

    @pytest.mark.skip(reason="TODO: support api token auth scheme")
    @parametrize
    def test_raw_response_review(self, client: Cloudflare) -> None:
        response = client.abuse_reports.mitigations.with_raw_response.review(
            report_id="report_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mitigation = response.parse()
        assert_matches_type(SyncSinglePage[MitigationReviewResponse], mitigation, path=["response"])

    @pytest.mark.skip(reason="TODO: support api token auth scheme")
    @parametrize
    def test_streaming_response_review(self, client: Cloudflare) -> None:
        with client.abuse_reports.mitigations.with_streaming_response.review(
            report_id="report_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mitigation = response.parse()
            assert_matches_type(SyncSinglePage[MitigationReviewResponse], mitigation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: support api token auth scheme")
    @parametrize
    def test_path_params_review(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.abuse_reports.mitigations.with_raw_response.review(
                report_id="report_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            client.abuse_reports.mitigations.with_raw_response.review(
                report_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncMitigations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="TODO: support api token auth scheme")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        mitigation = await async_client.abuse_reports.mitigations.list(
            report_id="report_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePagination[Optional[MitigationListResponse]], mitigation, path=["response"])

    @pytest.mark.skip(reason="TODO: support api token auth scheme")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        mitigation = await async_client.abuse_reports.mitigations.list(
            report_id="report_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            effective_after="2009-11-10T23:00:00Z",
            effective_before="2009-11-10T23:00:00Z",
            entity_type="url_pattern",
            page=0,
            per_page=0,
            sort="type,asc",
            status="pending",
            type="account_suspend",
        )
        assert_matches_type(AsyncV4PagePagination[Optional[MitigationListResponse]], mitigation, path=["response"])

    @pytest.mark.skip(reason="TODO: support api token auth scheme")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.abuse_reports.mitigations.with_raw_response.list(
            report_id="report_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mitigation = await response.parse()
        assert_matches_type(AsyncV4PagePagination[Optional[MitigationListResponse]], mitigation, path=["response"])

    @pytest.mark.skip(reason="TODO: support api token auth scheme")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.abuse_reports.mitigations.with_streaming_response.list(
            report_id="report_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mitigation = await response.parse()
            assert_matches_type(AsyncV4PagePagination[Optional[MitigationListResponse]], mitigation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: support api token auth scheme")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.abuse_reports.mitigations.with_raw_response.list(
                report_id="report_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            await async_client.abuse_reports.mitigations.with_raw_response.list(
                report_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: support api token auth scheme")
    @parametrize
    async def test_method_review(self, async_client: AsyncCloudflare) -> None:
        mitigation = await async_client.abuse_reports.mitigations.review(
            report_id="report_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[MitigationReviewResponse], mitigation, path=["response"])

    @pytest.mark.skip(reason="TODO: support api token auth scheme")
    @parametrize
    async def test_method_review_with_all_params(self, async_client: AsyncCloudflare) -> None:
        mitigation = await async_client.abuse_reports.mitigations.review(
            report_id="report_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            appeals=[
                {
                    "id": "id",
                    "reason": "misclassified",
                }
            ],
            data={
                "city": "city",
                "country": "country",
                "email": "dev@stainless.com",
                "full_name": "full_name",
                "jurisdiction_consent": True,
                "perjury_attestation": True,
                "phone_number": "phone_number",
                "signature": "signature",
                "state": "state",
                "street_address": "street_address",
                "urls": ["https://example.com"],
                "zip_code": "zip_code",
                "company": "company",
                "counter_notice_response": "counter_notice_response",
            },
            type="counter_notice",
        )
        assert_matches_type(AsyncSinglePage[MitigationReviewResponse], mitigation, path=["response"])

    @pytest.mark.skip(reason="TODO: support api token auth scheme")
    @parametrize
    async def test_raw_response_review(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.abuse_reports.mitigations.with_raw_response.review(
            report_id="report_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mitigation = await response.parse()
        assert_matches_type(AsyncSinglePage[MitigationReviewResponse], mitigation, path=["response"])

    @pytest.mark.skip(reason="TODO: support api token auth scheme")
    @parametrize
    async def test_streaming_response_review(self, async_client: AsyncCloudflare) -> None:
        async with async_client.abuse_reports.mitigations.with_streaming_response.review(
            report_id="report_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mitigation = await response.parse()
            assert_matches_type(AsyncSinglePage[MitigationReviewResponse], mitigation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: support api token auth scheme")
    @parametrize
    async def test_path_params_review(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.abuse_reports.mitigations.with_raw_response.review(
                report_id="report_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            await async_client.abuse_reports.mitigations.with_raw_response.review(
                report_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
