# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_date
from cloudflare.types.radar.ranking import DomainGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDomain:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        domain = client.radar.ranking.domain.get(
            domain="google.com",
        )
        assert_matches_type(DomainGetResponse, domain, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        domain = client.radar.ranking.domain.get(
            domain="google.com",
            date=[parse_date("2019-12-27")],
            format="JSON",
            include_top_locations=True,
            limit=5,
            name=["main_series"],
            ranking_type="POPULAR",
        )
        assert_matches_type(DomainGetResponse, domain, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.radar.ranking.domain.with_raw_response.get(
            domain="google.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainGetResponse, domain, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.radar.ranking.domain.with_streaming_response.get(
            domain="google.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainGetResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain` but received ''"):
            client.radar.ranking.domain.with_raw_response.get(
                domain="",
            )


class TestAsyncDomain:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        domain = await async_client.radar.ranking.domain.get(
            domain="google.com",
        )
        assert_matches_type(DomainGetResponse, domain, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        domain = await async_client.radar.ranking.domain.get(
            domain="google.com",
            date=[parse_date("2019-12-27")],
            format="JSON",
            include_top_locations=True,
            limit=5,
            name=["main_series"],
            ranking_type="POPULAR",
        )
        assert_matches_type(DomainGetResponse, domain, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.ranking.domain.with_raw_response.get(
            domain="google.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainGetResponse, domain, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.ranking.domain.with_streaming_response.get(
            domain="google.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainGetResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain` but received ''"):
            await async_client.radar.ranking.domain.with_raw_response.get(
                domain="",
            )
