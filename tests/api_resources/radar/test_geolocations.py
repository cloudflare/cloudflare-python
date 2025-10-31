# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.radar import (
    GeolocationGetResponse,
    GeolocationListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGeolocations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        geolocation = client.radar.geolocations.list()
        assert_matches_type(GeolocationListResponse, geolocation, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        geolocation = client.radar.geolocations.list(
            format="JSON",
            geo_id="3190509,360689",
            limit=1,
            location="US,CA",
            offset=0,
        )
        assert_matches_type(GeolocationListResponse, geolocation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.radar.geolocations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geolocation = response.parse()
        assert_matches_type(GeolocationListResponse, geolocation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.radar.geolocations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geolocation = response.parse()
            assert_matches_type(GeolocationListResponse, geolocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        geolocation = client.radar.geolocations.get(
            geo_id="3190509",
        )
        assert_matches_type(GeolocationGetResponse, geolocation, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        geolocation = client.radar.geolocations.get(
            geo_id="3190509",
            format="JSON",
        )
        assert_matches_type(GeolocationGetResponse, geolocation, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.radar.geolocations.with_raw_response.get(
            geo_id="3190509",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geolocation = response.parse()
        assert_matches_type(GeolocationGetResponse, geolocation, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.radar.geolocations.with_streaming_response.get(
            geo_id="3190509",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geolocation = response.parse()
            assert_matches_type(GeolocationGetResponse, geolocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `geo_id` but received ''"):
            client.radar.geolocations.with_raw_response.get(
                geo_id="",
            )


class TestAsyncGeolocations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        geolocation = await async_client.radar.geolocations.list()
        assert_matches_type(GeolocationListResponse, geolocation, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        geolocation = await async_client.radar.geolocations.list(
            format="JSON",
            geo_id="3190509,360689",
            limit=1,
            location="US,CA",
            offset=0,
        )
        assert_matches_type(GeolocationListResponse, geolocation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.geolocations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geolocation = await response.parse()
        assert_matches_type(GeolocationListResponse, geolocation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.geolocations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geolocation = await response.parse()
            assert_matches_type(GeolocationListResponse, geolocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        geolocation = await async_client.radar.geolocations.get(
            geo_id="3190509",
        )
        assert_matches_type(GeolocationGetResponse, geolocation, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        geolocation = await async_client.radar.geolocations.get(
            geo_id="3190509",
            format="JSON",
        )
        assert_matches_type(GeolocationGetResponse, geolocation, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.geolocations.with_raw_response.get(
            geo_id="3190509",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geolocation = await response.parse()
        assert_matches_type(GeolocationGetResponse, geolocation, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.geolocations.with_streaming_response.get(
            geo_id="3190509",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geolocation = await response.parse()
            assert_matches_type(GeolocationGetResponse, geolocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `geo_id` but received ''"):
            await async_client.radar.geolocations.with_raw_response.get(
                geo_id="",
            )
