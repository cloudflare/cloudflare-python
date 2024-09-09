# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.radar.entities import (
    LocationGetResponse,
    LocationListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLocations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        location = client.radar.entities.locations.list()
        assert_matches_type(LocationListResponse, location, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        location = client.radar.entities.locations.list(
            format="JSON",
            limit=5,
            location="US,CA",
            offset=0,
        )
        assert_matches_type(LocationListResponse, location, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.radar.entities.locations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = response.parse()
        assert_matches_type(LocationListResponse, location, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.radar.entities.locations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = response.parse()
            assert_matches_type(LocationListResponse, location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        location = client.radar.entities.locations.get(
            location="US",
        )
        assert_matches_type(LocationGetResponse, location, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        location = client.radar.entities.locations.get(
            location="US",
            format="JSON",
        )
        assert_matches_type(LocationGetResponse, location, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.radar.entities.locations.with_raw_response.get(
            location="US",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = response.parse()
        assert_matches_type(LocationGetResponse, location, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.radar.entities.locations.with_streaming_response.get(
            location="US",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = response.parse()
            assert_matches_type(LocationGetResponse, location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `location` but received ''"):
            client.radar.entities.locations.with_raw_response.get(
                location="",
            )


class TestAsyncLocations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        location = await async_client.radar.entities.locations.list()
        assert_matches_type(LocationListResponse, location, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        location = await async_client.radar.entities.locations.list(
            format="JSON",
            limit=5,
            location="US,CA",
            offset=0,
        )
        assert_matches_type(LocationListResponse, location, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.entities.locations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = await response.parse()
        assert_matches_type(LocationListResponse, location, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.entities.locations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = await response.parse()
            assert_matches_type(LocationListResponse, location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        location = await async_client.radar.entities.locations.get(
            location="US",
        )
        assert_matches_type(LocationGetResponse, location, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        location = await async_client.radar.entities.locations.get(
            location="US",
            format="JSON",
        )
        assert_matches_type(LocationGetResponse, location, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.entities.locations.with_raw_response.get(
            location="US",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = await response.parse()
        assert_matches_type(LocationGetResponse, location, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.entities.locations.with_streaming_response.get(
            location="US",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = await response.parse()
            assert_matches_type(LocationGetResponse, location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `location` but received ''"):
            await async_client.radar.entities.locations.with_raw_response.get(
                location="",
            )
