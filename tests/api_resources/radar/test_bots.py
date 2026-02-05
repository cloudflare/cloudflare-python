# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar import (
    BotGetResponse,
    BotListResponse,
    BotSummaryResponse,
    BotTimeseriesResponse,
    BotTimeseriesGroupsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBots:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        bot = client.radar.bots.list()
        assert_matches_type(BotListResponse, bot, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        bot = client.radar.bots.list(
            bot_category="SEARCH_ENGINE_CRAWLER",
            bot_operator="botOperator",
            bot_verification_status="VERIFIED",
            format="JSON",
            kind="AGENT",
            limit=1,
            offset=0,
        )
        assert_matches_type(BotListResponse, bot, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.radar.bots.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot = response.parse()
        assert_matches_type(BotListResponse, bot, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.radar.bots.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot = response.parse()
            assert_matches_type(BotListResponse, bot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        bot = client.radar.bots.get(
            bot_slug="gptbot",
        )
        assert_matches_type(BotGetResponse, bot, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        bot = client.radar.bots.get(
            bot_slug="gptbot",
            format="JSON",
        )
        assert_matches_type(BotGetResponse, bot, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.radar.bots.with_raw_response.get(
            bot_slug="gptbot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot = response.parse()
        assert_matches_type(BotGetResponse, bot, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.radar.bots.with_streaming_response.get(
            bot_slug="gptbot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot = response.parse()
            assert_matches_type(BotGetResponse, bot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bot_slug` but received ''"):
            client.radar.bots.with_raw_response.get(
                bot_slug="",
            )

    @parametrize
    def test_method_summary(self, client: Cloudflare) -> None:
        bot = client.radar.bots.summary(
            dimension="BOT",
        )
        assert_matches_type(BotSummaryResponse, bot, path=["response"])

    @parametrize
    def test_method_summary_with_all_params(self, client: Cloudflare) -> None:
        bot = client.radar.bots.summary(
            dimension="BOT",
            asn=["string"],
            bot=["string"],
            bot_category=["SEARCH_ENGINE_CRAWLER"],
            bot_kind=["AGENT"],
            bot_operator=["string"],
            bot_verification_status=["VERIFIED"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit_per_group=10,
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(BotSummaryResponse, bot, path=["response"])

    @parametrize
    def test_raw_response_summary(self, client: Cloudflare) -> None:
        response = client.radar.bots.with_raw_response.summary(
            dimension="BOT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot = response.parse()
        assert_matches_type(BotSummaryResponse, bot, path=["response"])

    @parametrize
    def test_streaming_response_summary(self, client: Cloudflare) -> None:
        with client.radar.bots.with_streaming_response.summary(
            dimension="BOT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot = response.parse()
            assert_matches_type(BotSummaryResponse, bot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_timeseries(self, client: Cloudflare) -> None:
        bot = client.radar.bots.timeseries()
        assert_matches_type(BotTimeseriesResponse, bot, path=["response"])

    @parametrize
    def test_method_timeseries_with_all_params(self, client: Cloudflare) -> None:
        bot = client.radar.bots.timeseries(
            agg_interval="1h",
            asn=["string"],
            bot=["string"],
            bot_category=["SEARCH_ENGINE_CRAWLER"],
            bot_kind=["AGENT"],
            bot_operator=["string"],
            bot_verification_status=["VERIFIED"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(BotTimeseriesResponse, bot, path=["response"])

    @parametrize
    def test_raw_response_timeseries(self, client: Cloudflare) -> None:
        response = client.radar.bots.with_raw_response.timeseries()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot = response.parse()
        assert_matches_type(BotTimeseriesResponse, bot, path=["response"])

    @parametrize
    def test_streaming_response_timeseries(self, client: Cloudflare) -> None:
        with client.radar.bots.with_streaming_response.timeseries() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot = response.parse()
            assert_matches_type(BotTimeseriesResponse, bot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_timeseries_groups(self, client: Cloudflare) -> None:
        bot = client.radar.bots.timeseries_groups(
            dimension="BOT",
        )
        assert_matches_type(BotTimeseriesGroupsResponse, bot, path=["response"])

    @parametrize
    def test_method_timeseries_groups_with_all_params(self, client: Cloudflare) -> None:
        bot = client.radar.bots.timeseries_groups(
            dimension="BOT",
            agg_interval="1h",
            asn=["string"],
            bot=["string"],
            bot_category=["SEARCH_ENGINE_CRAWLER"],
            bot_kind=["AGENT"],
            bot_operator=["string"],
            bot_verification_status=["VERIFIED"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit_per_group=10,
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(BotTimeseriesGroupsResponse, bot, path=["response"])

    @parametrize
    def test_raw_response_timeseries_groups(self, client: Cloudflare) -> None:
        response = client.radar.bots.with_raw_response.timeseries_groups(
            dimension="BOT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot = response.parse()
        assert_matches_type(BotTimeseriesGroupsResponse, bot, path=["response"])

    @parametrize
    def test_streaming_response_timeseries_groups(self, client: Cloudflare) -> None:
        with client.radar.bots.with_streaming_response.timeseries_groups(
            dimension="BOT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot = response.parse()
            assert_matches_type(BotTimeseriesGroupsResponse, bot, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBots:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        bot = await async_client.radar.bots.list()
        assert_matches_type(BotListResponse, bot, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        bot = await async_client.radar.bots.list(
            bot_category="SEARCH_ENGINE_CRAWLER",
            bot_operator="botOperator",
            bot_verification_status="VERIFIED",
            format="JSON",
            kind="AGENT",
            limit=1,
            offset=0,
        )
        assert_matches_type(BotListResponse, bot, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.bots.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot = await response.parse()
        assert_matches_type(BotListResponse, bot, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.bots.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot = await response.parse()
            assert_matches_type(BotListResponse, bot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        bot = await async_client.radar.bots.get(
            bot_slug="gptbot",
        )
        assert_matches_type(BotGetResponse, bot, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        bot = await async_client.radar.bots.get(
            bot_slug="gptbot",
            format="JSON",
        )
        assert_matches_type(BotGetResponse, bot, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.bots.with_raw_response.get(
            bot_slug="gptbot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot = await response.parse()
        assert_matches_type(BotGetResponse, bot, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.bots.with_streaming_response.get(
            bot_slug="gptbot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot = await response.parse()
            assert_matches_type(BotGetResponse, bot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bot_slug` but received ''"):
            await async_client.radar.bots.with_raw_response.get(
                bot_slug="",
            )

    @parametrize
    async def test_method_summary(self, async_client: AsyncCloudflare) -> None:
        bot = await async_client.radar.bots.summary(
            dimension="BOT",
        )
        assert_matches_type(BotSummaryResponse, bot, path=["response"])

    @parametrize
    async def test_method_summary_with_all_params(self, async_client: AsyncCloudflare) -> None:
        bot = await async_client.radar.bots.summary(
            dimension="BOT",
            asn=["string"],
            bot=["string"],
            bot_category=["SEARCH_ENGINE_CRAWLER"],
            bot_kind=["AGENT"],
            bot_operator=["string"],
            bot_verification_status=["VERIFIED"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit_per_group=10,
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(BotSummaryResponse, bot, path=["response"])

    @parametrize
    async def test_raw_response_summary(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.bots.with_raw_response.summary(
            dimension="BOT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot = await response.parse()
        assert_matches_type(BotSummaryResponse, bot, path=["response"])

    @parametrize
    async def test_streaming_response_summary(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.bots.with_streaming_response.summary(
            dimension="BOT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot = await response.parse()
            assert_matches_type(BotSummaryResponse, bot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_timeseries(self, async_client: AsyncCloudflare) -> None:
        bot = await async_client.radar.bots.timeseries()
        assert_matches_type(BotTimeseriesResponse, bot, path=["response"])

    @parametrize
    async def test_method_timeseries_with_all_params(self, async_client: AsyncCloudflare) -> None:
        bot = await async_client.radar.bots.timeseries(
            agg_interval="1h",
            asn=["string"],
            bot=["string"],
            bot_category=["SEARCH_ENGINE_CRAWLER"],
            bot_kind=["AGENT"],
            bot_operator=["string"],
            bot_verification_status=["VERIFIED"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(BotTimeseriesResponse, bot, path=["response"])

    @parametrize
    async def test_raw_response_timeseries(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.bots.with_raw_response.timeseries()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot = await response.parse()
        assert_matches_type(BotTimeseriesResponse, bot, path=["response"])

    @parametrize
    async def test_streaming_response_timeseries(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.bots.with_streaming_response.timeseries() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot = await response.parse()
            assert_matches_type(BotTimeseriesResponse, bot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_timeseries_groups(self, async_client: AsyncCloudflare) -> None:
        bot = await async_client.radar.bots.timeseries_groups(
            dimension="BOT",
        )
        assert_matches_type(BotTimeseriesGroupsResponse, bot, path=["response"])

    @parametrize
    async def test_method_timeseries_groups_with_all_params(self, async_client: AsyncCloudflare) -> None:
        bot = await async_client.radar.bots.timeseries_groups(
            dimension="BOT",
            agg_interval="1h",
            asn=["string"],
            bot=["string"],
            bot_category=["SEARCH_ENGINE_CRAWLER"],
            bot_kind=["AGENT"],
            bot_operator=["string"],
            bot_verification_status=["VERIFIED"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit_per_group=10,
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(BotTimeseriesGroupsResponse, bot, path=["response"])

    @parametrize
    async def test_raw_response_timeseries_groups(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.bots.with_raw_response.timeseries_groups(
            dimension="BOT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot = await response.parse()
        assert_matches_type(BotTimeseriesGroupsResponse, bot, path=["response"])

    @parametrize
    async def test_streaming_response_timeseries_groups(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.bots.with_streaming_response.timeseries_groups(
            dimension="BOT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot = await response.parse()
            assert_matches_type(BotTimeseriesGroupsResponse, bot, path=["response"])

        assert cast(Any, response.is_closed) is True
