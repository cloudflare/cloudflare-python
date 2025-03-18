# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.cloudforce_one.scans import (
    ConfigEditResponse,
    ConfigListResponse,
    ConfigCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfig:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        config = client.cloudforce_one.scans.config.create(
            account_id="account_id",
            ips=["1.1.1.1", "2606:4700:4700::1111"],
        )
        assert_matches_type(Optional[ConfigCreateResponse], config, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        config = client.cloudforce_one.scans.config.create(
            account_id="account_id",
            ips=["1.1.1.1", "2606:4700:4700::1111"],
            frequency=7,
            ports=["default"],
        )
        assert_matches_type(Optional[ConfigCreateResponse], config, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.scans.config.with_raw_response.create(
            account_id="account_id",
            ips=["1.1.1.1", "2606:4700:4700::1111"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(Optional[ConfigCreateResponse], config, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.cloudforce_one.scans.config.with_streaming_response.create(
            account_id="account_id",
            ips=["1.1.1.1", "2606:4700:4700::1111"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(Optional[ConfigCreateResponse], config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.scans.config.with_raw_response.create(
                account_id="",
                ips=["1.1.1.1", "2606:4700:4700::1111"],
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        config = client.cloudforce_one.scans.config.list(
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[ConfigListResponse], config, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.scans.config.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(SyncSinglePage[ConfigListResponse], config, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.cloudforce_one.scans.config.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(SyncSinglePage[ConfigListResponse], config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.scans.config.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        config = client.cloudforce_one.scans.config.delete(
            config_id="config_id",
            account_id="account_id",
        )
        assert_matches_type(object, config, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.scans.config.with_raw_response.delete(
            config_id="config_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.cloudforce_one.scans.config.with_streaming_response.delete(
            config_id="config_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.scans.config.with_raw_response.delete(
                config_id="config_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            client.cloudforce_one.scans.config.with_raw_response.delete(
                config_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        config = client.cloudforce_one.scans.config.edit(
            config_id="config_id",
            account_id="account_id",
        )
        assert_matches_type(Optional[ConfigEditResponse], config, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        config = client.cloudforce_one.scans.config.edit(
            config_id="config_id",
            account_id="account_id",
            frequency=7,
            ips=["1.1.1.1", "2606:4700:4700::1111"],
            ports=["default"],
        )
        assert_matches_type(Optional[ConfigEditResponse], config, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.scans.config.with_raw_response.edit(
            config_id="config_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(Optional[ConfigEditResponse], config, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.cloudforce_one.scans.config.with_streaming_response.edit(
            config_id="config_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(Optional[ConfigEditResponse], config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.scans.config.with_raw_response.edit(
                config_id="config_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            client.cloudforce_one.scans.config.with_raw_response.edit(
                config_id="",
                account_id="account_id",
            )


class TestAsyncConfig:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.cloudforce_one.scans.config.create(
            account_id="account_id",
            ips=["1.1.1.1", "2606:4700:4700::1111"],
        )
        assert_matches_type(Optional[ConfigCreateResponse], config, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.cloudforce_one.scans.config.create(
            account_id="account_id",
            ips=["1.1.1.1", "2606:4700:4700::1111"],
            frequency=7,
            ports=["default"],
        )
        assert_matches_type(Optional[ConfigCreateResponse], config, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.scans.config.with_raw_response.create(
            account_id="account_id",
            ips=["1.1.1.1", "2606:4700:4700::1111"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(Optional[ConfigCreateResponse], config, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.scans.config.with_streaming_response.create(
            account_id="account_id",
            ips=["1.1.1.1", "2606:4700:4700::1111"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(Optional[ConfigCreateResponse], config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.scans.config.with_raw_response.create(
                account_id="",
                ips=["1.1.1.1", "2606:4700:4700::1111"],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.cloudforce_one.scans.config.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[ConfigListResponse], config, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.scans.config.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(AsyncSinglePage[ConfigListResponse], config, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.scans.config.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(AsyncSinglePage[ConfigListResponse], config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.scans.config.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.cloudforce_one.scans.config.delete(
            config_id="config_id",
            account_id="account_id",
        )
        assert_matches_type(object, config, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.scans.config.with_raw_response.delete(
            config_id="config_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.scans.config.with_streaming_response.delete(
            config_id="config_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.scans.config.with_raw_response.delete(
                config_id="config_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            await async_client.cloudforce_one.scans.config.with_raw_response.delete(
                config_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.cloudforce_one.scans.config.edit(
            config_id="config_id",
            account_id="account_id",
        )
        assert_matches_type(Optional[ConfigEditResponse], config, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.cloudforce_one.scans.config.edit(
            config_id="config_id",
            account_id="account_id",
            frequency=7,
            ips=["1.1.1.1", "2606:4700:4700::1111"],
            ports=["default"],
        )
        assert_matches_type(Optional[ConfigEditResponse], config, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.scans.config.with_raw_response.edit(
            config_id="config_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(Optional[ConfigEditResponse], config, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.scans.config.with_streaming_response.edit(
            config_id="config_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(Optional[ConfigEditResponse], config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.scans.config.with_raw_response.edit(
                config_id="config_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            await async_client.cloudforce_one.scans.config.with_raw_response.edit(
                config_id="",
                account_id="account_id",
            )
