# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.radar.entities.asn_ip_response import ASNIPResponse
from cloudflare.types.radar.entities.asn_get_response import ASNGetResponse
from cloudflare.types.radar.entities.asn_rel_response import ASNRelResponse
from cloudflare.types.radar.entities.asn_list_response import ASNListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestASNs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        asn = client.radar.entities.asns.list()
        assert_matches_type(ASNListResponse, asn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        asn = client.radar.entities.asns.list(
            asn="174,7922",
            format="JSON",
            limit=5,
            location="US",
            offset=0,
            order_by="ASN",
        )
        assert_matches_type(ASNListResponse, asn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.radar.entities.asns.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asn = response.parse()
        assert_matches_type(ASNListResponse, asn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.radar.entities.asns.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asn = response.parse()
            assert_matches_type(ASNListResponse, asn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        asn = client.radar.entities.asns.get(
            3,
        )
        assert_matches_type(ASNGetResponse, asn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        asn = client.radar.entities.asns.get(
            3,
            format="JSON",
        )
        assert_matches_type(ASNGetResponse, asn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.radar.entities.asns.with_raw_response.get(
            3,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asn = response.parse()
        assert_matches_type(ASNGetResponse, asn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.radar.entities.asns.with_streaming_response.get(
            3,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asn = response.parse()
            assert_matches_type(ASNGetResponse, asn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_ip(self, client: Cloudflare) -> None:
        asn = client.radar.entities.asns.ip(
            ip="8.8.8.8",
        )
        assert_matches_type(ASNIPResponse, asn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_ip_with_all_params(self, client: Cloudflare) -> None:
        asn = client.radar.entities.asns.ip(
            ip="8.8.8.8",
            format="JSON",
        )
        assert_matches_type(ASNIPResponse, asn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_ip(self, client: Cloudflare) -> None:
        response = client.radar.entities.asns.with_raw_response.ip(
            ip="8.8.8.8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asn = response.parse()
        assert_matches_type(ASNIPResponse, asn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_ip(self, client: Cloudflare) -> None:
        with client.radar.entities.asns.with_streaming_response.ip(
            ip="8.8.8.8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asn = response.parse()
            assert_matches_type(ASNIPResponse, asn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_rel(self, client: Cloudflare) -> None:
        asn = client.radar.entities.asns.rel(
            3,
        )
        assert_matches_type(ASNRelResponse, asn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_rel_with_all_params(self, client: Cloudflare) -> None:
        asn = client.radar.entities.asns.rel(
            3,
            asn2=0,
            format="JSON",
        )
        assert_matches_type(ASNRelResponse, asn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_rel(self, client: Cloudflare) -> None:
        response = client.radar.entities.asns.with_raw_response.rel(
            3,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asn = response.parse()
        assert_matches_type(ASNRelResponse, asn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_rel(self, client: Cloudflare) -> None:
        with client.radar.entities.asns.with_streaming_response.rel(
            3,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asn = response.parse()
            assert_matches_type(ASNRelResponse, asn, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncASNs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        asn = await async_client.radar.entities.asns.list()
        assert_matches_type(ASNListResponse, asn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        asn = await async_client.radar.entities.asns.list(
            asn="174,7922",
            format="JSON",
            limit=5,
            location="US",
            offset=0,
            order_by="ASN",
        )
        assert_matches_type(ASNListResponse, asn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.entities.asns.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asn = await response.parse()
        assert_matches_type(ASNListResponse, asn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.entities.asns.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asn = await response.parse()
            assert_matches_type(ASNListResponse, asn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        asn = await async_client.radar.entities.asns.get(
            3,
        )
        assert_matches_type(ASNGetResponse, asn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        asn = await async_client.radar.entities.asns.get(
            3,
            format="JSON",
        )
        assert_matches_type(ASNGetResponse, asn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.entities.asns.with_raw_response.get(
            3,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asn = await response.parse()
        assert_matches_type(ASNGetResponse, asn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.entities.asns.with_streaming_response.get(
            3,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asn = await response.parse()
            assert_matches_type(ASNGetResponse, asn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_ip(self, async_client: AsyncCloudflare) -> None:
        asn = await async_client.radar.entities.asns.ip(
            ip="8.8.8.8",
        )
        assert_matches_type(ASNIPResponse, asn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_ip_with_all_params(self, async_client: AsyncCloudflare) -> None:
        asn = await async_client.radar.entities.asns.ip(
            ip="8.8.8.8",
            format="JSON",
        )
        assert_matches_type(ASNIPResponse, asn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_ip(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.entities.asns.with_raw_response.ip(
            ip="8.8.8.8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asn = await response.parse()
        assert_matches_type(ASNIPResponse, asn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_ip(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.entities.asns.with_streaming_response.ip(
            ip="8.8.8.8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asn = await response.parse()
            assert_matches_type(ASNIPResponse, asn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_rel(self, async_client: AsyncCloudflare) -> None:
        asn = await async_client.radar.entities.asns.rel(
            3,
        )
        assert_matches_type(ASNRelResponse, asn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_rel_with_all_params(self, async_client: AsyncCloudflare) -> None:
        asn = await async_client.radar.entities.asns.rel(
            3,
            asn2=0,
            format="JSON",
        )
        assert_matches_type(ASNRelResponse, asn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_rel(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.entities.asns.with_raw_response.rel(
            3,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asn = await response.parse()
        assert_matches_type(ASNRelResponse, asn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_rel(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.entities.asns.with_streaming_response.rel(
            3,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asn = await response.parse()
            assert_matches_type(ASNRelResponse, asn, path=["response"])

        assert cast(Any, response.is_closed) is True
