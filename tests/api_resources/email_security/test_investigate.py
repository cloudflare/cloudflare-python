# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.email_security import InvestigateGetResponse, InvestigateListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvestigate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        investigate = client.email_security.investigate.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[InvestigateListResponse], investigate, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        investigate = client.email_security.investigate.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action_log=True,
            alert_id="alert_id",
            detections_only=True,
            domain="domain",
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            final_disposition="MALICIOUS",
            message_action="PREVIEW",
            message_id="message_id",
            metric="metric",
            page=1,
            per_page=1,
            query="query",
            recipient="recipient",
            sender="sender",
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncV4PagePaginationArray[InvestigateListResponse], investigate, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.email_security.investigate.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        investigate = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[InvestigateListResponse], investigate, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.email_security.investigate.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            investigate = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[InvestigateListResponse], investigate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.investigate.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        investigate = client.email_security.investigate.get(
            postfix_id="4Njp3P0STMz2c02Q",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(InvestigateGetResponse, investigate, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.email_security.investigate.with_raw_response.get(
            postfix_id="4Njp3P0STMz2c02Q",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        investigate = response.parse()
        assert_matches_type(InvestigateGetResponse, investigate, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.email_security.investigate.with_streaming_response.get(
            postfix_id="4Njp3P0STMz2c02Q",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            investigate = response.parse()
            assert_matches_type(InvestigateGetResponse, investigate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.investigate.with_raw_response.get(
                postfix_id="4Njp3P0STMz2c02Q",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `postfix_id` but received ''"):
            client.email_security.investigate.with_raw_response.get(
                postfix_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncInvestigate:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        investigate = await async_client.email_security.investigate.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[InvestigateListResponse], investigate, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        investigate = await async_client.email_security.investigate.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action_log=True,
            alert_id="alert_id",
            detections_only=True,
            domain="domain",
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            final_disposition="MALICIOUS",
            message_action="PREVIEW",
            message_id="message_id",
            metric="metric",
            page=1,
            per_page=1,
            query="query",
            recipient="recipient",
            sender="sender",
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncV4PagePaginationArray[InvestigateListResponse], investigate, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.investigate.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        investigate = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[InvestigateListResponse], investigate, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.investigate.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            investigate = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[InvestigateListResponse], investigate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.investigate.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        investigate = await async_client.email_security.investigate.get(
            postfix_id="4Njp3P0STMz2c02Q",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(InvestigateGetResponse, investigate, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.investigate.with_raw_response.get(
            postfix_id="4Njp3P0STMz2c02Q",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        investigate = await response.parse()
        assert_matches_type(InvestigateGetResponse, investigate, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.investigate.with_streaming_response.get(
            postfix_id="4Njp3P0STMz2c02Q",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            investigate = await response.parse()
            assert_matches_type(InvestigateGetResponse, investigate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.investigate.with_raw_response.get(
                postfix_id="4Njp3P0STMz2c02Q",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `postfix_id` but received ''"):
            await async_client.email_security.investigate.with_raw_response.get(
                postfix_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
