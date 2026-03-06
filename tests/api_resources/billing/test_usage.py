# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_date
from cloudflare.types.billing import UsagePaygoResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_paygo(self, client: Cloudflare) -> None:
        usage = client.billing.usage.paygo(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(UsagePaygoResponse, usage, path=["response"])

    @parametrize
    def test_method_paygo_with_all_params(self, client: Cloudflare) -> None:
        usage = client.billing.usage.paygo(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            from_=parse_date("2025-02-01"),
            last_month_period_start=6,
            last_year_period_start=2025,
            to=parse_date("2025-03-01"),
        )
        assert_matches_type(UsagePaygoResponse, usage, path=["response"])

    @parametrize
    def test_raw_response_paygo(self, client: Cloudflare) -> None:
        response = client.billing.usage.with_raw_response.paygo(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsagePaygoResponse, usage, path=["response"])

    @parametrize
    def test_streaming_response_paygo(self, client: Cloudflare) -> None:
        with client.billing.usage.with_streaming_response.paygo(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsagePaygoResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_paygo(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.billing.usage.with_raw_response.paygo(
                account_id="",
            )


class TestAsyncUsage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_paygo(self, async_client: AsyncCloudflare) -> None:
        usage = await async_client.billing.usage.paygo(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(UsagePaygoResponse, usage, path=["response"])

    @parametrize
    async def test_method_paygo_with_all_params(self, async_client: AsyncCloudflare) -> None:
        usage = await async_client.billing.usage.paygo(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            from_=parse_date("2025-02-01"),
            last_month_period_start=6,
            last_year_period_start=2025,
            to=parse_date("2025-03-01"),
        )
        assert_matches_type(UsagePaygoResponse, usage, path=["response"])

    @parametrize
    async def test_raw_response_paygo(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.billing.usage.with_raw_response.paygo(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsagePaygoResponse, usage, path=["response"])

    @parametrize
    async def test_streaming_response_paygo(self, async_client: AsyncCloudflare) -> None:
        async with async_client.billing.usage.with_streaming_response.paygo(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsagePaygoResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_paygo(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.billing.usage.with_raw_response.paygo(
                account_id="",
            )
