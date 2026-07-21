# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.cloudforce_one.threat_events import IndicatorListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIndicators:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        indicator = client.cloudforce_one.threat_events.indicators.list(
            account_id="account_id",
        )
        assert_matches_type(IndicatorListResponse, indicator, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        indicator = client.cloudforce_one.threat_events.indicators.list(
            account_id="account_id",
            cache="from-graph",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            dataset_ids=["string"],
            format="json",
            include_tags=True,
            include_total_count=True,
            indicator_type="indicatorType",
            name="name",
            page=0,
            page_size=0,
            related_events=["string"],
            related_events_limit=2,
            search=[
                {
                    "field": "value",
                    "op": "contains",
                    "value": "malicious",
                }
            ],
            source="do",
            tags=["string"],
            tag_search=[
                {
                    "field": "originCountryISO",
                    "op": "in",
                    "value": "IR",
                }
            ],
        )
        assert_matches_type(IndicatorListResponse, indicator, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.indicators.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator = response.parse()
        assert_matches_type(IndicatorListResponse, indicator, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.indicators.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator = response.parse()
            assert_matches_type(IndicatorListResponse, indicator, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_events.indicators.with_raw_response.list(
                account_id="",
            )


class TestAsyncIndicators:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        indicator = await async_client.cloudforce_one.threat_events.indicators.list(
            account_id="account_id",
        )
        assert_matches_type(IndicatorListResponse, indicator, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        indicator = await async_client.cloudforce_one.threat_events.indicators.list(
            account_id="account_id",
            cache="from-graph",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            dataset_ids=["string"],
            format="json",
            include_tags=True,
            include_total_count=True,
            indicator_type="indicatorType",
            name="name",
            page=0,
            page_size=0,
            related_events=["string"],
            related_events_limit=2,
            search=[
                {
                    "field": "value",
                    "op": "contains",
                    "value": "malicious",
                }
            ],
            source="do",
            tags=["string"],
            tag_search=[
                {
                    "field": "originCountryISO",
                    "op": "in",
                    "value": "IR",
                }
            ],
        )
        assert_matches_type(IndicatorListResponse, indicator, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.indicators.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator = await response.parse()
        assert_matches_type(IndicatorListResponse, indicator, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.indicators.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator = await response.parse()
            assert_matches_type(IndicatorListResponse, indicator, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_events.indicators.with_raw_response.list(
                account_id="",
            )
