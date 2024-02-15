# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types import (
    ZoneCreateResponse,
    ZoneUpdateResponse,
    ZoneListResponse,
    ZoneDeleteResponse,
    ZoneGetResponse,
)

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import zone_create_params
from cloudflare.types import zone_update_params
from cloudflare.types import zone_list_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestZones:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        zone = client.zones.create(
            account={},
            name="example.com",
        )
        assert_matches_type(Optional[ZoneCreateResponse], zone, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        zone = client.zones.create(
            account={"id": "023e105f4ecef8ad9ca31a8372d0c353"},
            name="example.com",
            type="full",
        )
        assert_matches_type(Optional[ZoneCreateResponse], zone, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zones.with_raw_response.create(
            account={},
            name="example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = response.parse()
        assert_matches_type(Optional[ZoneCreateResponse], zone, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zones.with_streaming_response.create(
            account={},
            name="example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = response.parse()
            assert_matches_type(Optional[ZoneCreateResponse], zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        zone = client.zones.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ZoneUpdateResponse], zone, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        zone = client.zones.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            plan={"id": "023e105f4ecef8ad9ca31a8372d0c353"},
            type="full",
            vanity_name_servers=["ns1.example.com", "ns2.example.com"],
        )
        assert_matches_type(Optional[ZoneUpdateResponse], zone, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zones.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = response.parse()
        assert_matches_type(Optional[ZoneUpdateResponse], zone, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zones.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = response.parse()
            assert_matches_type(Optional[ZoneUpdateResponse], zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.with_raw_response.update(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        zone = client.zones.list()
        assert_matches_type(Optional[ZoneListResponse], zone, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        zone = client.zones.list(
            account={
                "id": "string",
                "name": "string",
            },
            direction="desc",
            match="any",
            name="string",
            order="status",
            page=1,
            per_page=5,
            status="initializing",
        )
        assert_matches_type(Optional[ZoneListResponse], zone, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zones.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = response.parse()
        assert_matches_type(Optional[ZoneListResponse], zone, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zones.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = response.parse()
            assert_matches_type(Optional[ZoneListResponse], zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="body parameter is required")
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        zone = client.zones.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ZoneDeleteResponse], zone, path=["response"])

    @pytest.mark.skip(reason="body parameter is required")
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zones.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = response.parse()
        assert_matches_type(Optional[ZoneDeleteResponse], zone, path=["response"])

    @pytest.mark.skip(reason="body parameter is required")
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zones.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
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
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        zone = client.zones.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ZoneGetResponse], zone, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zones.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = response.parse()
        assert_matches_type(Optional[ZoneGetResponse], zone, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zones.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = response.parse()
            assert_matches_type(Optional[ZoneGetResponse], zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.with_raw_response.get(
                "",
            )


class TestAsyncZones:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        zone = await async_client.zones.create(
            account={},
            name="example.com",
        )
        assert_matches_type(Optional[ZoneCreateResponse], zone, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        zone = await async_client.zones.create(
            account={"id": "023e105f4ecef8ad9ca31a8372d0c353"},
            name="example.com",
            type="full",
        )
        assert_matches_type(Optional[ZoneCreateResponse], zone, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.with_raw_response.create(
            account={},
            name="example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = await response.parse()
        assert_matches_type(Optional[ZoneCreateResponse], zone, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.with_streaming_response.create(
            account={},
            name="example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = await response.parse()
            assert_matches_type(Optional[ZoneCreateResponse], zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        zone = await async_client.zones.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ZoneUpdateResponse], zone, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        zone = await async_client.zones.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            plan={"id": "023e105f4ecef8ad9ca31a8372d0c353"},
            type="full",
            vanity_name_servers=["ns1.example.com", "ns2.example.com"],
        )
        assert_matches_type(Optional[ZoneUpdateResponse], zone, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = await response.parse()
        assert_matches_type(Optional[ZoneUpdateResponse], zone, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = await response.parse()
            assert_matches_type(Optional[ZoneUpdateResponse], zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.with_raw_response.update(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        zone = await async_client.zones.list()
        assert_matches_type(Optional[ZoneListResponse], zone, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        zone = await async_client.zones.list(
            account={
                "id": "string",
                "name": "string",
            },
            direction="desc",
            match="any",
            name="string",
            order="status",
            page=1,
            per_page=5,
            status="initializing",
        )
        assert_matches_type(Optional[ZoneListResponse], zone, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = await response.parse()
        assert_matches_type(Optional[ZoneListResponse], zone, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = await response.parse()
            assert_matches_type(Optional[ZoneListResponse], zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="body parameter is required")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        zone = await async_client.zones.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ZoneDeleteResponse], zone, path=["response"])

    @pytest.mark.skip(reason="body parameter is required")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = await response.parse()
        assert_matches_type(Optional[ZoneDeleteResponse], zone, path=["response"])

    @pytest.mark.skip(reason="body parameter is required")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
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
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        zone = await async_client.zones.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ZoneGetResponse], zone, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = await response.parse()
        assert_matches_type(Optional[ZoneGetResponse], zone, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = await response.parse()
            assert_matches_type(Optional[ZoneGetResponse], zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.with_raw_response.get(
                "",
            )
