# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar.bgp import TopPrefixesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTop:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_prefixes(self, client: Cloudflare) -> None:
        top = client.radar.bgp.top.prefixes()
        assert_matches_type(TopPrefixesResponse, top, path=["response"])

    @parametrize
    def test_method_prefixes_with_all_params(self, client: Cloudflare) -> None:
        top = client.radar.bgp.top.prefixes(
            asn=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            format="JSON",
            limit=5,
            name=["string", "string", "string"],
            update_type=["ANNOUNCEMENT", "WITHDRAWAL"],
        )
        assert_matches_type(TopPrefixesResponse, top, path=["response"])

    @parametrize
    def test_raw_response_prefixes(self, client: Cloudflare) -> None:
        response = client.radar.bgp.top.with_raw_response.prefixes()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = response.parse()
        assert_matches_type(TopPrefixesResponse, top, path=["response"])

    @parametrize
    def test_streaming_response_prefixes(self, client: Cloudflare) -> None:
        with client.radar.bgp.top.with_streaming_response.prefixes() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = response.parse()
            assert_matches_type(TopPrefixesResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTop:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_prefixes(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.bgp.top.prefixes()
        assert_matches_type(TopPrefixesResponse, top, path=["response"])

    @parametrize
    async def test_method_prefixes_with_all_params(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.bgp.top.prefixes(
            asn=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            format="JSON",
            limit=5,
            name=["string", "string", "string"],
            update_type=["ANNOUNCEMENT", "WITHDRAWAL"],
        )
        assert_matches_type(TopPrefixesResponse, top, path=["response"])

    @parametrize
    async def test_raw_response_prefixes(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.bgp.top.with_raw_response.prefixes()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = await response.parse()
        assert_matches_type(TopPrefixesResponse, top, path=["response"])

    @parametrize
    async def test_streaming_response_prefixes(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.bgp.top.with_streaming_response.prefixes() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = await response.parse()
            assert_matches_type(TopPrefixesResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True
