# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar.ai import TimeseriesGroupUserAgentResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTimeseriesGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_user_agent(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.ai.timeseries_groups.user_agent()
        assert_matches_type(TimeseriesGroupUserAgentResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_user_agent_with_all_params(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.ai.timeseries_groups.user_agent(
            agg_interval="15m",
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit_per_group=10,
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(TimeseriesGroupUserAgentResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_user_agent(self, client: Cloudflare) -> None:
        response = client.radar.ai.timeseries_groups.with_raw_response.user_agent()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupUserAgentResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_user_agent(self, client: Cloudflare) -> None:
        with client.radar.ai.timeseries_groups.with_streaming_response.user_agent() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupUserAgentResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTimeseriesGroups:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_user_agent(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.ai.timeseries_groups.user_agent()
        assert_matches_type(TimeseriesGroupUserAgentResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_user_agent_with_all_params(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.ai.timeseries_groups.user_agent(
            agg_interval="15m",
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit_per_group=10,
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(TimeseriesGroupUserAgentResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_user_agent(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.ai.timeseries_groups.with_raw_response.user_agent()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupUserAgentResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_user_agent(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.ai.timeseries_groups.with_streaming_response.user_agent() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupUserAgentResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True
