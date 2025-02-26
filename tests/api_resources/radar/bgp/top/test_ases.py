# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar.bgp.top import AseGetResponse, AsePrefixesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        ase = client.radar.bgp.top.ases.get()
        assert_matches_type(AseGetResponse, ase, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        ase = client.radar.bgp.top.ases.get(
            asn=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit=5,
            name=["main_series"],
            prefix=["1.1.1.0/24"],
            update_type=["ANNOUNCEMENT"],
        )
        assert_matches_type(AseGetResponse, ase, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.radar.bgp.top.ases.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ase = response.parse()
        assert_matches_type(AseGetResponse, ase, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.radar.bgp.top.ases.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ase = response.parse()
            assert_matches_type(AseGetResponse, ase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_prefixes(self, client: Cloudflare) -> None:
        ase = client.radar.bgp.top.ases.prefixes()
        assert_matches_type(AsePrefixesResponse, ase, path=["response"])

    @parametrize
    def test_method_prefixes_with_all_params(self, client: Cloudflare) -> None:
        ase = client.radar.bgp.top.ases.prefixes(
            country="NZ",
            format="JSON",
            limit=10,
        )
        assert_matches_type(AsePrefixesResponse, ase, path=["response"])

    @parametrize
    def test_raw_response_prefixes(self, client: Cloudflare) -> None:
        response = client.radar.bgp.top.ases.with_raw_response.prefixes()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ase = response.parse()
        assert_matches_type(AsePrefixesResponse, ase, path=["response"])

    @parametrize
    def test_streaming_response_prefixes(self, client: Cloudflare) -> None:
        with client.radar.bgp.top.ases.with_streaming_response.prefixes() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ase = response.parse()
            assert_matches_type(AsePrefixesResponse, ase, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAses:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        ase = await async_client.radar.bgp.top.ases.get()
        assert_matches_type(AseGetResponse, ase, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ase = await async_client.radar.bgp.top.ases.get(
            asn=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit=5,
            name=["main_series"],
            prefix=["1.1.1.0/24"],
            update_type=["ANNOUNCEMENT"],
        )
        assert_matches_type(AseGetResponse, ase, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.bgp.top.ases.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ase = await response.parse()
        assert_matches_type(AseGetResponse, ase, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.bgp.top.ases.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ase = await response.parse()
            assert_matches_type(AseGetResponse, ase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_prefixes(self, async_client: AsyncCloudflare) -> None:
        ase = await async_client.radar.bgp.top.ases.prefixes()
        assert_matches_type(AsePrefixesResponse, ase, path=["response"])

    @parametrize
    async def test_method_prefixes_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ase = await async_client.radar.bgp.top.ases.prefixes(
            country="NZ",
            format="JSON",
            limit=10,
        )
        assert_matches_type(AsePrefixesResponse, ase, path=["response"])

    @parametrize
    async def test_raw_response_prefixes(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.bgp.top.ases.with_raw_response.prefixes()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ase = await response.parse()
        assert_matches_type(AsePrefixesResponse, ase, path=["response"])

    @parametrize
    async def test_streaming_response_prefixes(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.bgp.top.ases.with_streaming_response.prefixes() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ase = await response.parse()
            assert_matches_type(AsePrefixesResponse, ase, path=["response"])

        assert cast(Any, response.is_closed) is True
