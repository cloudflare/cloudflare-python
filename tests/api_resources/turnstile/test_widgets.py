# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.turnstile import (
    Widget,
    WidgetListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWidgets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        widget = client.turnstile.widgets.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="non-interactive",
            name="blog.cloudflare.com login form",
        )
        assert_matches_type(Optional[Widget], widget, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        widget = client.turnstile.widgets.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="non-interactive",
            name="blog.cloudflare.com login form",
            direction="asc",
            order="id",
            page=1,
            per_page=5,
            bot_fight_mode=False,
            clearance_level="no_clearance",
            ephemeral_id=False,
            offlabel=False,
            region="world",
        )
        assert_matches_type(Optional[Widget], widget, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.turnstile.widgets.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="non-interactive",
            name="blog.cloudflare.com login form",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget = response.parse()
        assert_matches_type(Optional[Widget], widget, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.turnstile.widgets.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="non-interactive",
            name="blog.cloudflare.com login form",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget = response.parse()
            assert_matches_type(Optional[Widget], widget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.turnstile.widgets.with_raw_response.create(
                account_id="",
                domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
                mode="non-interactive",
                name="blog.cloudflare.com login form",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        widget = client.turnstile.widgets.update(
            sitekey="0x4AAF00AAAABn0R22HWm-YUc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="non-interactive",
            name="blog.cloudflare.com login form",
        )
        assert_matches_type(Optional[Widget], widget, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        widget = client.turnstile.widgets.update(
            sitekey="0x4AAF00AAAABn0R22HWm-YUc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="non-interactive",
            name="blog.cloudflare.com login form",
            bot_fight_mode=False,
            clearance_level="no_clearance",
            ephemeral_id=False,
            offlabel=False,
        )
        assert_matches_type(Optional[Widget], widget, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.turnstile.widgets.with_raw_response.update(
            sitekey="0x4AAF00AAAABn0R22HWm-YUc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="non-interactive",
            name="blog.cloudflare.com login form",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget = response.parse()
        assert_matches_type(Optional[Widget], widget, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.turnstile.widgets.with_streaming_response.update(
            sitekey="0x4AAF00AAAABn0R22HWm-YUc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="non-interactive",
            name="blog.cloudflare.com login form",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget = response.parse()
            assert_matches_type(Optional[Widget], widget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.turnstile.widgets.with_raw_response.update(
                sitekey="0x4AAF00AAAABn0R22HWm-YUc",
                account_id="",
                domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
                mode="non-interactive",
                name="blog.cloudflare.com login form",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sitekey` but received ''"):
            client.turnstile.widgets.with_raw_response.update(
                sitekey="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
                mode="non-interactive",
                name="blog.cloudflare.com login form",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        widget = client.turnstile.widgets.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[WidgetListResponse], widget, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        widget = client.turnstile.widgets.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            order="id",
            page=1,
            per_page=5,
        )
        assert_matches_type(SyncV4PagePaginationArray[WidgetListResponse], widget, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.turnstile.widgets.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[WidgetListResponse], widget, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.turnstile.widgets.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[WidgetListResponse], widget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.turnstile.widgets.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        widget = client.turnstile.widgets.delete(
            sitekey="0x4AAF00AAAABn0R22HWm-YUc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Widget], widget, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.turnstile.widgets.with_raw_response.delete(
            sitekey="0x4AAF00AAAABn0R22HWm-YUc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget = response.parse()
        assert_matches_type(Optional[Widget], widget, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.turnstile.widgets.with_streaming_response.delete(
            sitekey="0x4AAF00AAAABn0R22HWm-YUc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget = response.parse()
            assert_matches_type(Optional[Widget], widget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.turnstile.widgets.with_raw_response.delete(
                sitekey="0x4AAF00AAAABn0R22HWm-YUc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sitekey` but received ''"):
            client.turnstile.widgets.with_raw_response.delete(
                sitekey="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        widget = client.turnstile.widgets.get(
            sitekey="0x4AAF00AAAABn0R22HWm-YUc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Widget], widget, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.turnstile.widgets.with_raw_response.get(
            sitekey="0x4AAF00AAAABn0R22HWm-YUc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget = response.parse()
        assert_matches_type(Optional[Widget], widget, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.turnstile.widgets.with_streaming_response.get(
            sitekey="0x4AAF00AAAABn0R22HWm-YUc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget = response.parse()
            assert_matches_type(Optional[Widget], widget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.turnstile.widgets.with_raw_response.get(
                sitekey="0x4AAF00AAAABn0R22HWm-YUc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sitekey` but received ''"):
            client.turnstile.widgets.with_raw_response.get(
                sitekey="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_rotate_secret(self, client: Cloudflare) -> None:
        widget = client.turnstile.widgets.rotate_secret(
            sitekey="0x4AAF00AAAABn0R22HWm-YUc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Widget], widget, path=["response"])

    @parametrize
    def test_method_rotate_secret_with_all_params(self, client: Cloudflare) -> None:
        widget = client.turnstile.widgets.rotate_secret(
            sitekey="0x4AAF00AAAABn0R22HWm-YUc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            invalidate_immediately=True,
        )
        assert_matches_type(Optional[Widget], widget, path=["response"])

    @parametrize
    def test_raw_response_rotate_secret(self, client: Cloudflare) -> None:
        response = client.turnstile.widgets.with_raw_response.rotate_secret(
            sitekey="0x4AAF00AAAABn0R22HWm-YUc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget = response.parse()
        assert_matches_type(Optional[Widget], widget, path=["response"])

    @parametrize
    def test_streaming_response_rotate_secret(self, client: Cloudflare) -> None:
        with client.turnstile.widgets.with_streaming_response.rotate_secret(
            sitekey="0x4AAF00AAAABn0R22HWm-YUc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget = response.parse()
            assert_matches_type(Optional[Widget], widget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_rotate_secret(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.turnstile.widgets.with_raw_response.rotate_secret(
                sitekey="0x4AAF00AAAABn0R22HWm-YUc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sitekey` but received ''"):
            client.turnstile.widgets.with_raw_response.rotate_secret(
                sitekey="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncWidgets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        widget = await async_client.turnstile.widgets.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="non-interactive",
            name="blog.cloudflare.com login form",
        )
        assert_matches_type(Optional[Widget], widget, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        widget = await async_client.turnstile.widgets.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="non-interactive",
            name="blog.cloudflare.com login form",
            direction="asc",
            order="id",
            page=1,
            per_page=5,
            bot_fight_mode=False,
            clearance_level="no_clearance",
            ephemeral_id=False,
            offlabel=False,
            region="world",
        )
        assert_matches_type(Optional[Widget], widget, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.turnstile.widgets.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="non-interactive",
            name="blog.cloudflare.com login form",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget = await response.parse()
        assert_matches_type(Optional[Widget], widget, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.turnstile.widgets.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="non-interactive",
            name="blog.cloudflare.com login form",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget = await response.parse()
            assert_matches_type(Optional[Widget], widget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.turnstile.widgets.with_raw_response.create(
                account_id="",
                domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
                mode="non-interactive",
                name="blog.cloudflare.com login form",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        widget = await async_client.turnstile.widgets.update(
            sitekey="0x4AAF00AAAABn0R22HWm-YUc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="non-interactive",
            name="blog.cloudflare.com login form",
        )
        assert_matches_type(Optional[Widget], widget, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        widget = await async_client.turnstile.widgets.update(
            sitekey="0x4AAF00AAAABn0R22HWm-YUc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="non-interactive",
            name="blog.cloudflare.com login form",
            bot_fight_mode=False,
            clearance_level="no_clearance",
            ephemeral_id=False,
            offlabel=False,
        )
        assert_matches_type(Optional[Widget], widget, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.turnstile.widgets.with_raw_response.update(
            sitekey="0x4AAF00AAAABn0R22HWm-YUc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="non-interactive",
            name="blog.cloudflare.com login form",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget = await response.parse()
        assert_matches_type(Optional[Widget], widget, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.turnstile.widgets.with_streaming_response.update(
            sitekey="0x4AAF00AAAABn0R22HWm-YUc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="non-interactive",
            name="blog.cloudflare.com login form",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget = await response.parse()
            assert_matches_type(Optional[Widget], widget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.turnstile.widgets.with_raw_response.update(
                sitekey="0x4AAF00AAAABn0R22HWm-YUc",
                account_id="",
                domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
                mode="non-interactive",
                name="blog.cloudflare.com login form",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sitekey` but received ''"):
            await async_client.turnstile.widgets.with_raw_response.update(
                sitekey="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
                mode="non-interactive",
                name="blog.cloudflare.com login form",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        widget = await async_client.turnstile.widgets.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[WidgetListResponse], widget, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        widget = await async_client.turnstile.widgets.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            order="id",
            page=1,
            per_page=5,
        )
        assert_matches_type(AsyncV4PagePaginationArray[WidgetListResponse], widget, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.turnstile.widgets.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[WidgetListResponse], widget, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.turnstile.widgets.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[WidgetListResponse], widget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.turnstile.widgets.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        widget = await async_client.turnstile.widgets.delete(
            sitekey="0x4AAF00AAAABn0R22HWm-YUc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Widget], widget, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.turnstile.widgets.with_raw_response.delete(
            sitekey="0x4AAF00AAAABn0R22HWm-YUc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget = await response.parse()
        assert_matches_type(Optional[Widget], widget, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.turnstile.widgets.with_streaming_response.delete(
            sitekey="0x4AAF00AAAABn0R22HWm-YUc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget = await response.parse()
            assert_matches_type(Optional[Widget], widget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.turnstile.widgets.with_raw_response.delete(
                sitekey="0x4AAF00AAAABn0R22HWm-YUc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sitekey` but received ''"):
            await async_client.turnstile.widgets.with_raw_response.delete(
                sitekey="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        widget = await async_client.turnstile.widgets.get(
            sitekey="0x4AAF00AAAABn0R22HWm-YUc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Widget], widget, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.turnstile.widgets.with_raw_response.get(
            sitekey="0x4AAF00AAAABn0R22HWm-YUc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget = await response.parse()
        assert_matches_type(Optional[Widget], widget, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.turnstile.widgets.with_streaming_response.get(
            sitekey="0x4AAF00AAAABn0R22HWm-YUc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget = await response.parse()
            assert_matches_type(Optional[Widget], widget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.turnstile.widgets.with_raw_response.get(
                sitekey="0x4AAF00AAAABn0R22HWm-YUc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sitekey` but received ''"):
            await async_client.turnstile.widgets.with_raw_response.get(
                sitekey="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_rotate_secret(self, async_client: AsyncCloudflare) -> None:
        widget = await async_client.turnstile.widgets.rotate_secret(
            sitekey="0x4AAF00AAAABn0R22HWm-YUc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Widget], widget, path=["response"])

    @parametrize
    async def test_method_rotate_secret_with_all_params(self, async_client: AsyncCloudflare) -> None:
        widget = await async_client.turnstile.widgets.rotate_secret(
            sitekey="0x4AAF00AAAABn0R22HWm-YUc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            invalidate_immediately=True,
        )
        assert_matches_type(Optional[Widget], widget, path=["response"])

    @parametrize
    async def test_raw_response_rotate_secret(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.turnstile.widgets.with_raw_response.rotate_secret(
            sitekey="0x4AAF00AAAABn0R22HWm-YUc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget = await response.parse()
        assert_matches_type(Optional[Widget], widget, path=["response"])

    @parametrize
    async def test_streaming_response_rotate_secret(self, async_client: AsyncCloudflare) -> None:
        async with async_client.turnstile.widgets.with_streaming_response.rotate_secret(
            sitekey="0x4AAF00AAAABn0R22HWm-YUc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget = await response.parse()
            assert_matches_type(Optional[Widget], widget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_rotate_secret(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.turnstile.widgets.with_raw_response.rotate_secret(
                sitekey="0x4AAF00AAAABn0R22HWm-YUc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sitekey` but received ''"):
            await async_client.turnstile.widgets.with_raw_response.rotate_secret(
                sitekey="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
