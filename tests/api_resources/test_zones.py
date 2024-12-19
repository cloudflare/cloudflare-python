# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.zones import (
    Zone,
    ZoneDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestZones:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        zone = client.zones.create(
            account={},
            name="example.com",
        )
        assert_matches_type(Optional[Zone], zone, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        zone = client.zones.create(
            account={"id": "023e105f4ecef8ad9ca31a8372d0c353"},
            name="example.com",
            type="full",
        )
        assert_matches_type(Optional[Zone], zone, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zones.with_raw_response.create(
            account={},
            name="example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = response.parse()
        assert_matches_type(Optional[Zone], zone, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zones.with_streaming_response.create(
            account={},
            name="example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = response.parse()
            assert_matches_type(Optional[Zone], zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        zone = client.zones.list()
        assert_matches_type(SyncV4PagePaginationArray[Zone], zone, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        zone = client.zones.list(
            account={
                "id": "id",
                "name": "name",
            },
            direction="asc",
            match="any",
            name="name",
            order="name",
            page=1,
            per_page=5,
            status="initializing",
        )
        assert_matches_type(SyncV4PagePaginationArray[Zone], zone, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zones.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[Zone], zone, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zones.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[Zone], zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="body parameter is required")
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        zone = client.zones.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ZoneDeleteResponse], zone, path=["response"])

    @pytest.mark.skip(reason="body parameter is required")
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zones.with_raw_response.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = response.parse()
        assert_matches_type(Optional[ZoneDeleteResponse], zone, path=["response"])

    @pytest.mark.skip(reason="body parameter is required")
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zones.with_streaming_response.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = response.parse()
            assert_matches_type(Optional[ZoneDeleteResponse], zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="body parameter is required")
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.with_raw_response.delete(
                zone_id="",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        zone = client.zones.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Zone], zone, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        zone = client.zones.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="full",
            vanity_name_servers=["ns1.example.com", "ns2.example.com"],
        )
        assert_matches_type(Optional[Zone], zone, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.zones.with_raw_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = response.parse()
        assert_matches_type(Optional[Zone], zone, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.zones.with_streaming_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = response.parse()
            assert_matches_type(Optional[Zone], zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.with_raw_response.edit(
                zone_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        zone = client.zones.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Zone], zone, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zones.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = response.parse()
        assert_matches_type(Optional[Zone], zone, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zones.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = response.parse()
            assert_matches_type(Optional[Zone], zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.with_raw_response.get(
                zone_id="",
            )


class TestAsyncZones:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        zone = await async_client.zones.create(
            account={},
            name="example.com",
        )
        assert_matches_type(Optional[Zone], zone, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        zone = await async_client.zones.create(
            account={"id": "023e105f4ecef8ad9ca31a8372d0c353"},
            name="example.com",
            type="full",
        )
        assert_matches_type(Optional[Zone], zone, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.with_raw_response.create(
            account={},
            name="example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = await response.parse()
        assert_matches_type(Optional[Zone], zone, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.with_streaming_response.create(
            account={},
            name="example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = await response.parse()
            assert_matches_type(Optional[Zone], zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        zone = await async_client.zones.list()
        assert_matches_type(AsyncV4PagePaginationArray[Zone], zone, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        zone = await async_client.zones.list(
            account={
                "id": "id",
                "name": "name",
            },
            direction="asc",
            match="any",
            name="name",
            order="name",
            page=1,
            per_page=5,
            status="initializing",
        )
        assert_matches_type(AsyncV4PagePaginationArray[Zone], zone, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[Zone], zone, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[Zone], zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="body parameter is required")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        zone = await async_client.zones.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ZoneDeleteResponse], zone, path=["response"])

    @pytest.mark.skip(reason="body parameter is required")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.with_raw_response.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = await response.parse()
        assert_matches_type(Optional[ZoneDeleteResponse], zone, path=["response"])

    @pytest.mark.skip(reason="body parameter is required")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.with_streaming_response.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = await response.parse()
            assert_matches_type(Optional[ZoneDeleteResponse], zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="body parameter is required")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.with_raw_response.delete(
                zone_id="",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        zone = await async_client.zones.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Zone], zone, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        zone = await async_client.zones.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="full",
            vanity_name_servers=["ns1.example.com", "ns2.example.com"],
        )
        assert_matches_type(Optional[Zone], zone, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.with_raw_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = await response.parse()
        assert_matches_type(Optional[Zone], zone, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.with_streaming_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = await response.parse()
            assert_matches_type(Optional[Zone], zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.with_raw_response.edit(
                zone_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        zone = await async_client.zones.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Zone], zone, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = await response.parse()
        assert_matches_type(Optional[Zone], zone, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = await response.parse()
            assert_matches_type(Optional[Zone], zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.with_raw_response.get(
                zone_id="",
            )
