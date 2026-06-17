# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.moq import (
    RelayGetResponse,
    RelayListResponse,
    RelayCreateResponse,
    RelayUpdateResponse,
)
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRelays:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        relay = client.moq.relays.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="Production Live Stream",
        )
        assert_matches_type(Optional[RelayCreateResponse], relay, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.moq.relays.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="Production Live Stream",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        relay = response.parse()
        assert_matches_type(Optional[RelayCreateResponse], relay, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.moq.relays.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="Production Live Stream",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            relay = response.parse()
            assert_matches_type(Optional[RelayCreateResponse], relay, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.moq.relays.with_raw_response.create(
                account_id="",
                name="Production Live Stream",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        relay = client.moq.relays.update(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RelayUpdateResponse], relay, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        relay = client.moq.relays.update(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "lingering_subscribe": {
                    "enabled": True,
                    "max_timeout_ms": 0,
                },
                "origin_fallback": {
                    "enabled": True,
                    "origins": [{"url": "url"}],
                },
            },
            name="name",
        )
        assert_matches_type(Optional[RelayUpdateResponse], relay, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.moq.relays.with_raw_response.update(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        relay = response.parse()
        assert_matches_type(Optional[RelayUpdateResponse], relay, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.moq.relays.with_streaming_response.update(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            relay = response.parse()
            assert_matches_type(Optional[RelayUpdateResponse], relay, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.moq.relays.with_raw_response.update(
                relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `relay_id` but received ''"):
            client.moq.relays.with_raw_response.update(
                relay_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        relay = client.moq.relays.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[RelayListResponse], relay, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        relay = client.moq.relays.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            asc=True,
            created_after=parse_datetime("2026-03-27T15:00:00Z"),
            created_before=parse_datetime("2026-03-27T15:00:00Z"),
            per_page=50,
        )
        assert_matches_type(SyncSinglePage[RelayListResponse], relay, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.moq.relays.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        relay = response.parse()
        assert_matches_type(SyncSinglePage[RelayListResponse], relay, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.moq.relays.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            relay = response.parse()
            assert_matches_type(SyncSinglePage[RelayListResponse], relay, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.moq.relays.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        relay = client.moq.relays.delete(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, relay, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.moq.relays.with_raw_response.delete(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        relay = response.parse()
        assert_matches_type(object, relay, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.moq.relays.with_streaming_response.delete(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            relay = response.parse()
            assert_matches_type(object, relay, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.moq.relays.with_raw_response.delete(
                relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `relay_id` but received ''"):
            client.moq.relays.with_raw_response.delete(
                relay_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        relay = client.moq.relays.get(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RelayGetResponse], relay, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.moq.relays.with_raw_response.get(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        relay = response.parse()
        assert_matches_type(Optional[RelayGetResponse], relay, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.moq.relays.with_streaming_response.get(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            relay = response.parse()
            assert_matches_type(Optional[RelayGetResponse], relay, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.moq.relays.with_raw_response.get(
                relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `relay_id` but received ''"):
            client.moq.relays.with_raw_response.get(
                relay_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncRelays:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        relay = await async_client.moq.relays.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="Production Live Stream",
        )
        assert_matches_type(Optional[RelayCreateResponse], relay, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.moq.relays.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="Production Live Stream",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        relay = await response.parse()
        assert_matches_type(Optional[RelayCreateResponse], relay, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.moq.relays.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="Production Live Stream",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            relay = await response.parse()
            assert_matches_type(Optional[RelayCreateResponse], relay, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.moq.relays.with_raw_response.create(
                account_id="",
                name="Production Live Stream",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        relay = await async_client.moq.relays.update(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RelayUpdateResponse], relay, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        relay = await async_client.moq.relays.update(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "lingering_subscribe": {
                    "enabled": True,
                    "max_timeout_ms": 0,
                },
                "origin_fallback": {
                    "enabled": True,
                    "origins": [{"url": "url"}],
                },
            },
            name="name",
        )
        assert_matches_type(Optional[RelayUpdateResponse], relay, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.moq.relays.with_raw_response.update(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        relay = await response.parse()
        assert_matches_type(Optional[RelayUpdateResponse], relay, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.moq.relays.with_streaming_response.update(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            relay = await response.parse()
            assert_matches_type(Optional[RelayUpdateResponse], relay, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.moq.relays.with_raw_response.update(
                relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `relay_id` but received ''"):
            await async_client.moq.relays.with_raw_response.update(
                relay_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        relay = await async_client.moq.relays.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[RelayListResponse], relay, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        relay = await async_client.moq.relays.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            asc=True,
            created_after=parse_datetime("2026-03-27T15:00:00Z"),
            created_before=parse_datetime("2026-03-27T15:00:00Z"),
            per_page=50,
        )
        assert_matches_type(AsyncSinglePage[RelayListResponse], relay, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.moq.relays.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        relay = await response.parse()
        assert_matches_type(AsyncSinglePage[RelayListResponse], relay, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.moq.relays.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            relay = await response.parse()
            assert_matches_type(AsyncSinglePage[RelayListResponse], relay, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.moq.relays.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        relay = await async_client.moq.relays.delete(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, relay, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.moq.relays.with_raw_response.delete(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        relay = await response.parse()
        assert_matches_type(object, relay, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.moq.relays.with_streaming_response.delete(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            relay = await response.parse()
            assert_matches_type(object, relay, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.moq.relays.with_raw_response.delete(
                relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `relay_id` but received ''"):
            await async_client.moq.relays.with_raw_response.delete(
                relay_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        relay = await async_client.moq.relays.get(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RelayGetResponse], relay, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.moq.relays.with_raw_response.get(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        relay = await response.parse()
        assert_matches_type(Optional[RelayGetResponse], relay, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.moq.relays.with_streaming_response.get(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            relay = await response.parse()
            assert_matches_type(Optional[RelayGetResponse], relay, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.moq.relays.with_raw_response.get(
                relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `relay_id` but received ''"):
            await async_client.moq.relays.with_raw_response.get(
                relay_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
