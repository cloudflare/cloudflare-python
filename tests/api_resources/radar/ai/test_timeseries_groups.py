# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar.ai import (
    TimeseriesGroupSummaryResponse,
    TimeseriesGroupUserAgentResponse,
    TimeseriesGroupTimeseriesResponse,
    TimeseriesGroupTimeseriesGroupsResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTimeseriesGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_summary(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.ai.timeseries_groups.summary(
            dimension="USER_AGENT",
        )
        assert_matches_type(TimeseriesGroupSummaryResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_summary_with_all_params(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.ai.timeseries_groups.summary(
            dimension="USER_AGENT",
            asn=["string"],
            continent=["string"],
            crawl_purpose=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            industry=["string"],
            limit_per_group=10,
            location=["string"],
            name=["main_series"],
            vertical=["string"],
        )
        assert_matches_type(TimeseriesGroupSummaryResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_summary(self, client: Cloudflare) -> None:
        response = client.radar.ai.timeseries_groups.with_raw_response.summary(
            dimension="USER_AGENT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupSummaryResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_summary(self, client: Cloudflare) -> None:
        with client.radar.ai.timeseries_groups.with_streaming_response.summary(
            dimension="USER_AGENT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupSummaryResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_timeseries(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.ai.timeseries_groups.timeseries()
        assert_matches_type(TimeseriesGroupTimeseriesResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_timeseries_with_all_params(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.ai.timeseries_groups.timeseries(
            agg_interval="1h",
            asn=["string"],
            continent=["string"],
            crawl_purpose=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            industry=["string"],
            limit_per_group=10,
            location=["string"],
            name=["main_series"],
            user_agent=["string"],
            vertical=["string"],
        )
        assert_matches_type(TimeseriesGroupTimeseriesResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_timeseries(self, client: Cloudflare) -> None:
        response = client.radar.ai.timeseries_groups.with_raw_response.timeseries()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupTimeseriesResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_timeseries(self, client: Cloudflare) -> None:
        with client.radar.ai.timeseries_groups.with_streaming_response.timeseries() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupTimeseriesResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_timeseries_groups(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.ai.timeseries_groups.timeseries_groups(
            dimension="USER_AGENT",
        )
        assert_matches_type(TimeseriesGroupTimeseriesGroupsResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_timeseries_groups_with_all_params(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.ai.timeseries_groups.timeseries_groups(
            dimension="USER_AGENT",
            agg_interval="1h",
            asn=["string"],
            continent=["string"],
            crawl_purpose=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            industry=["string"],
            limit_per_group=10,
            location=["string"],
            name=["main_series"],
            normalization="MIN0_MAX",
            vertical=["string"],
        )
        assert_matches_type(TimeseriesGroupTimeseriesGroupsResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_timeseries_groups(self, client: Cloudflare) -> None:
        response = client.radar.ai.timeseries_groups.with_raw_response.timeseries_groups(
            dimension="USER_AGENT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupTimeseriesGroupsResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_timeseries_groups(self, client: Cloudflare) -> None:
        with client.radar.ai.timeseries_groups.with_streaming_response.timeseries_groups(
            dimension="USER_AGENT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupTimeseriesGroupsResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_user_agent(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            timeseries_group = client.radar.ai.timeseries_groups.user_agent()

        assert_matches_type(TimeseriesGroupUserAgentResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_user_agent_with_all_params(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            timeseries_group = client.radar.ai.timeseries_groups.user_agent(
                agg_interval="1h",
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
        with pytest.warns(DeprecationWarning):
            response = client.radar.ai.timeseries_groups.with_raw_response.user_agent()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupUserAgentResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_user_agent(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.radar.ai.timeseries_groups.with_streaming_response.user_agent() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                timeseries_group = response.parse()
                assert_matches_type(TimeseriesGroupUserAgentResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTimeseriesGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_summary(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.ai.timeseries_groups.summary(
            dimension="USER_AGENT",
        )
        assert_matches_type(TimeseriesGroupSummaryResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_summary_with_all_params(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.ai.timeseries_groups.summary(
            dimension="USER_AGENT",
            asn=["string"],
            continent=["string"],
            crawl_purpose=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            industry=["string"],
            limit_per_group=10,
            location=["string"],
            name=["main_series"],
            vertical=["string"],
        )
        assert_matches_type(TimeseriesGroupSummaryResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_summary(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.ai.timeseries_groups.with_raw_response.summary(
            dimension="USER_AGENT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupSummaryResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_summary(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.ai.timeseries_groups.with_streaming_response.summary(
            dimension="USER_AGENT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupSummaryResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_timeseries(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.ai.timeseries_groups.timeseries()
        assert_matches_type(TimeseriesGroupTimeseriesResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_timeseries_with_all_params(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.ai.timeseries_groups.timeseries(
            agg_interval="1h",
            asn=["string"],
            continent=["string"],
            crawl_purpose=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            industry=["string"],
            limit_per_group=10,
            location=["string"],
            name=["main_series"],
            user_agent=["string"],
            vertical=["string"],
        )
        assert_matches_type(TimeseriesGroupTimeseriesResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_timeseries(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.ai.timeseries_groups.with_raw_response.timeseries()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupTimeseriesResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_timeseries(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.ai.timeseries_groups.with_streaming_response.timeseries() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupTimeseriesResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_timeseries_groups(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.ai.timeseries_groups.timeseries_groups(
            dimension="USER_AGENT",
        )
        assert_matches_type(TimeseriesGroupTimeseriesGroupsResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_timeseries_groups_with_all_params(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.ai.timeseries_groups.timeseries_groups(
            dimension="USER_AGENT",
            agg_interval="1h",
            asn=["string"],
            continent=["string"],
            crawl_purpose=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            industry=["string"],
            limit_per_group=10,
            location=["string"],
            name=["main_series"],
            normalization="MIN0_MAX",
            vertical=["string"],
        )
        assert_matches_type(TimeseriesGroupTimeseriesGroupsResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_timeseries_groups(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.ai.timeseries_groups.with_raw_response.timeseries_groups(
            dimension="USER_AGENT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupTimeseriesGroupsResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_timeseries_groups(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.ai.timeseries_groups.with_streaming_response.timeseries_groups(
            dimension="USER_AGENT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupTimeseriesGroupsResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_user_agent(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            timeseries_group = await async_client.radar.ai.timeseries_groups.user_agent()

        assert_matches_type(TimeseriesGroupUserAgentResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_user_agent_with_all_params(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            timeseries_group = await async_client.radar.ai.timeseries_groups.user_agent(
                agg_interval="1h",
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
        with pytest.warns(DeprecationWarning):
            response = await async_client.radar.ai.timeseries_groups.with_raw_response.user_agent()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupUserAgentResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_user_agent(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.radar.ai.timeseries_groups.with_streaming_response.user_agent() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                timeseries_group = await response.parse()
                assert_matches_type(TimeseriesGroupUserAgentResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True
