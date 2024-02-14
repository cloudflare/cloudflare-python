# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.radar.entities import AsnRelResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.radar.entities import asn_rel_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAsns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_rel(self, client: Cloudflare) -> None:
        asn = client.radar.entities.asns.rel(
            3,
        )
        assert_matches_type(AsnRelResponse, asn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_rel_with_all_params(self, client: Cloudflare) -> None:
        asn = client.radar.entities.asns.rel(
            3,
            asn2=0,
            format="JSON",
        )
        assert_matches_type(AsnRelResponse, asn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_rel(self, client: Cloudflare) -> None:
        response = client.radar.entities.asns.with_raw_response.rel(
            3,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asn = response.parse()
        assert_matches_type(AsnRelResponse, asn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_rel(self, client: Cloudflare) -> None:
        with client.radar.entities.asns.with_streaming_response.rel(
            3,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asn = response.parse()
            assert_matches_type(AsnRelResponse, asn, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAsns:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_rel(self, async_client: AsyncCloudflare) -> None:
        asn = await async_client.radar.entities.asns.rel(
            3,
        )
        assert_matches_type(AsnRelResponse, asn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_rel_with_all_params(self, async_client: AsyncCloudflare) -> None:
        asn = await async_client.radar.entities.asns.rel(
            3,
            asn2=0,
            format="JSON",
        )
        assert_matches_type(AsnRelResponse, asn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_rel(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.entities.asns.with_raw_response.rel(
            3,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asn = await response.parse()
        assert_matches_type(AsnRelResponse, asn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_rel(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.entities.asns.with_streaming_response.rel(
            3,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asn = await response.parse()
            assert_matches_type(AsnRelResponse, asn, path=["response"])

        assert cast(Any, response.is_closed) is True
