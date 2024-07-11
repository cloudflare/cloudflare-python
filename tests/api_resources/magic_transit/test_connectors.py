# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.magic_transit import (
    ConnectorGetResponse,
    ConnectorEditResponse,
    ConnectorListResponse,
    ConnectorUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnectors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        connector = client.magic_transit.connectors.update(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ConnectorUpdateResponse, connector, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        connector = client.magic_transit.connectors.update(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            activated=True,
            interrupt_window_duration_hours=0,
            interrupt_window_hour_of_day=0,
            notes="notes",
            timezone="timezone",
        )
        assert_matches_type(ConnectorUpdateResponse, connector, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.magic_transit.connectors.with_raw_response.update(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = response.parse()
        assert_matches_type(ConnectorUpdateResponse, connector, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.magic_transit.connectors.with_streaming_response.update(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = response.parse()
            assert_matches_type(ConnectorUpdateResponse, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.connectors.with_raw_response.update(
                connector_id="connector_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            client.magic_transit.connectors.with_raw_response.update(
                connector_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        connector = client.magic_transit.connectors.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[ConnectorListResponse], connector, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.magic_transit.connectors.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = response.parse()
        assert_matches_type(SyncSinglePage[ConnectorListResponse], connector, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.magic_transit.connectors.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = response.parse()
            assert_matches_type(SyncSinglePage[ConnectorListResponse], connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.connectors.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        connector = client.magic_transit.connectors.edit(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ConnectorEditResponse, connector, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        connector = client.magic_transit.connectors.edit(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            activated=True,
            interrupt_window_duration_hours=0,
            interrupt_window_hour_of_day=0,
            notes="notes",
            timezone="timezone",
        )
        assert_matches_type(ConnectorEditResponse, connector, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.magic_transit.connectors.with_raw_response.edit(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = response.parse()
        assert_matches_type(ConnectorEditResponse, connector, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.magic_transit.connectors.with_streaming_response.edit(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = response.parse()
            assert_matches_type(ConnectorEditResponse, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.connectors.with_raw_response.edit(
                connector_id="connector_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            client.magic_transit.connectors.with_raw_response.edit(
                connector_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        connector = client.magic_transit.connectors.get(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ConnectorGetResponse, connector, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.magic_transit.connectors.with_raw_response.get(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = response.parse()
        assert_matches_type(ConnectorGetResponse, connector, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.magic_transit.connectors.with_streaming_response.get(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = response.parse()
            assert_matches_type(ConnectorGetResponse, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.connectors.with_raw_response.get(
                connector_id="connector_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            client.magic_transit.connectors.with_raw_response.get(
                connector_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncConnectors:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        connector = await async_client.magic_transit.connectors.update(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ConnectorUpdateResponse, connector, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        connector = await async_client.magic_transit.connectors.update(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            activated=True,
            interrupt_window_duration_hours=0,
            interrupt_window_hour_of_day=0,
            notes="notes",
            timezone="timezone",
        )
        assert_matches_type(ConnectorUpdateResponse, connector, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.connectors.with_raw_response.update(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = await response.parse()
        assert_matches_type(ConnectorUpdateResponse, connector, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.connectors.with_streaming_response.update(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = await response.parse()
            assert_matches_type(ConnectorUpdateResponse, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.connectors.with_raw_response.update(
                connector_id="connector_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            await async_client.magic_transit.connectors.with_raw_response.update(
                connector_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        connector = await async_client.magic_transit.connectors.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[ConnectorListResponse], connector, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.connectors.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = await response.parse()
        assert_matches_type(AsyncSinglePage[ConnectorListResponse], connector, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.connectors.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = await response.parse()
            assert_matches_type(AsyncSinglePage[ConnectorListResponse], connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.connectors.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        connector = await async_client.magic_transit.connectors.edit(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ConnectorEditResponse, connector, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        connector = await async_client.magic_transit.connectors.edit(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            activated=True,
            interrupt_window_duration_hours=0,
            interrupt_window_hour_of_day=0,
            notes="notes",
            timezone="timezone",
        )
        assert_matches_type(ConnectorEditResponse, connector, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.connectors.with_raw_response.edit(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = await response.parse()
        assert_matches_type(ConnectorEditResponse, connector, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.connectors.with_streaming_response.edit(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = await response.parse()
            assert_matches_type(ConnectorEditResponse, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.connectors.with_raw_response.edit(
                connector_id="connector_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            await async_client.magic_transit.connectors.with_raw_response.edit(
                connector_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        connector = await async_client.magic_transit.connectors.get(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ConnectorGetResponse, connector, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.connectors.with_raw_response.get(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = await response.parse()
        assert_matches_type(ConnectorGetResponse, connector, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.connectors.with_streaming_response.get(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = await response.parse()
            assert_matches_type(ConnectorGetResponse, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.connectors.with_raw_response.get(
                connector_id="connector_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            await async_client.magic_transit.connectors.with_raw_response.get(
                connector_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
