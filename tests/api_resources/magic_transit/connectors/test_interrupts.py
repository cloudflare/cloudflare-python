# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.magic_transit.connectors import (
    InterruptListResponse,
    InterruptCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInterrupts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        interrupt = client.magic_transit.connectors.interrupts.create(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(InterruptCreateResponse, interrupt, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        interrupt = client.magic_transit.connectors.interrupts.create(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            reboot={"purge": True},
            restart={"purge": True},
            shutdown={"purge": True},
        )
        assert_matches_type(InterruptCreateResponse, interrupt, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.magic_transit.connectors.interrupts.with_raw_response.create(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interrupt = response.parse()
        assert_matches_type(InterruptCreateResponse, interrupt, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.magic_transit.connectors.interrupts.with_streaming_response.create(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interrupt = response.parse()
            assert_matches_type(InterruptCreateResponse, interrupt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.connectors.interrupts.with_raw_response.create(
                connector_id="connector_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            client.magic_transit.connectors.interrupts.with_raw_response.create(
                connector_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        interrupt = client.magic_transit.connectors.interrupts.list(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[InterruptListResponse], interrupt, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.magic_transit.connectors.interrupts.with_raw_response.list(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interrupt = response.parse()
        assert_matches_type(SyncSinglePage[InterruptListResponse], interrupt, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.magic_transit.connectors.interrupts.with_streaming_response.list(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interrupt = response.parse()
            assert_matches_type(SyncSinglePage[InterruptListResponse], interrupt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.connectors.interrupts.with_raw_response.list(
                connector_id="connector_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            client.magic_transit.connectors.interrupts.with_raw_response.list(
                connector_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncInterrupts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        interrupt = await async_client.magic_transit.connectors.interrupts.create(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(InterruptCreateResponse, interrupt, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        interrupt = await async_client.magic_transit.connectors.interrupts.create(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            reboot={"purge": True},
            restart={"purge": True},
            shutdown={"purge": True},
        )
        assert_matches_type(InterruptCreateResponse, interrupt, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.connectors.interrupts.with_raw_response.create(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interrupt = await response.parse()
        assert_matches_type(InterruptCreateResponse, interrupt, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.connectors.interrupts.with_streaming_response.create(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interrupt = await response.parse()
            assert_matches_type(InterruptCreateResponse, interrupt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.connectors.interrupts.with_raw_response.create(
                connector_id="connector_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            await async_client.magic_transit.connectors.interrupts.with_raw_response.create(
                connector_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        interrupt = await async_client.magic_transit.connectors.interrupts.list(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[InterruptListResponse], interrupt, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.connectors.interrupts.with_raw_response.list(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interrupt = await response.parse()
        assert_matches_type(AsyncSinglePage[InterruptListResponse], interrupt, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.connectors.interrupts.with_streaming_response.list(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interrupt = await response.parse()
            assert_matches_type(AsyncSinglePage[InterruptListResponse], interrupt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.connectors.interrupts.with_raw_response.list(
                connector_id="connector_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            await async_client.magic_transit.connectors.interrupts.with_raw_response.list(
                connector_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
