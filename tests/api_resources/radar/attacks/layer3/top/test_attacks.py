# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar.attacks.layer3.top import AttackListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAttacks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        attack = client.radar.attacks.layer3.top.attacks.list()
        assert_matches_type(AttackListResponse, attack, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        attack = client.radar.attacks.layer3.top.attacks.list(
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["1d", "2d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            format="JSON",
            ip_version=["IPv4", "IPv6"],
            limit=5,
            limit_direction="ORIGIN",
            limit_per_location=10,
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            protocol=["UDP", "TCP", "ICMP"],
        )
        assert_matches_type(AttackListResponse, attack, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.radar.attacks.layer3.top.attacks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attack = response.parse()
        assert_matches_type(AttackListResponse, attack, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.radar.attacks.layer3.top.attacks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attack = response.parse()
            assert_matches_type(AttackListResponse, attack, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAttacks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        attack = await async_client.radar.attacks.layer3.top.attacks.list()
        assert_matches_type(AttackListResponse, attack, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        attack = await async_client.radar.attacks.layer3.top.attacks.list(
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["1d", "2d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            format="JSON",
            ip_version=["IPv4", "IPv6"],
            limit=5,
            limit_direction="ORIGIN",
            limit_per_location=10,
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            protocol=["UDP", "TCP", "ICMP"],
        )
        assert_matches_type(AttackListResponse, attack, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.attacks.layer3.top.attacks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attack = await response.parse()
        assert_matches_type(AttackListResponse, attack, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.attacks.layer3.top.attacks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attack = await response.parse()
            assert_matches_type(AttackListResponse, attack, path=["response"])

        assert cast(Any, response.is_closed) is True
