# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar.http.locations import BotClassGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBotClass:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        bot_class = client.radar.http.locations.bot_class.get(
            bot_class="LIKELY_AUTOMATED",
        )
        assert_matches_type(BotClassGetResponse, bot_class, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        bot_class = client.radar.http.locations.bot_class.get(
            bot_class="LIKELY_AUTOMATED",
            asn=["string"],
            browser_family=["CHROME"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            device_type=["DESKTOP"],
            format="JSON",
            http_protocol=["HTTP"],
            http_version=["HTTPv1"],
            ip_version=["IPv4"],
            limit=5,
            location=["string"],
            name=["main_series"],
            os=["WINDOWS"],
            tls_version=["TLSv1_0"],
        )
        assert_matches_type(BotClassGetResponse, bot_class, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.radar.http.locations.bot_class.with_raw_response.get(
            bot_class="LIKELY_AUTOMATED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot_class = response.parse()
        assert_matches_type(BotClassGetResponse, bot_class, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.radar.http.locations.bot_class.with_streaming_response.get(
            bot_class="LIKELY_AUTOMATED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot_class = response.parse()
            assert_matches_type(BotClassGetResponse, bot_class, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBotClass:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        bot_class = await async_client.radar.http.locations.bot_class.get(
            bot_class="LIKELY_AUTOMATED",
        )
        assert_matches_type(BotClassGetResponse, bot_class, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        bot_class = await async_client.radar.http.locations.bot_class.get(
            bot_class="LIKELY_AUTOMATED",
            asn=["string"],
            browser_family=["CHROME"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            device_type=["DESKTOP"],
            format="JSON",
            http_protocol=["HTTP"],
            http_version=["HTTPv1"],
            ip_version=["IPv4"],
            limit=5,
            location=["string"],
            name=["main_series"],
            os=["WINDOWS"],
            tls_version=["TLSv1_0"],
        )
        assert_matches_type(BotClassGetResponse, bot_class, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.http.locations.bot_class.with_raw_response.get(
            bot_class="LIKELY_AUTOMATED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot_class = await response.parse()
        assert_matches_type(BotClassGetResponse, bot_class, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.http.locations.bot_class.with_streaming_response.get(
            bot_class="LIKELY_AUTOMATED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot_class = await response.parse()
            assert_matches_type(BotClassGetResponse, bot_class, path=["response"])

        assert cast(Any, response.is_closed) is True
