# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from cloudflare.types.magic_network_monitoring import Configuration

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.magic_network_monitoring import config_create_params
from cloudflare.types.magic_network_monitoring import config_update_params
from cloudflare.types.magic_network_monitoring import config_edit_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfigs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        config = client.magic_network_monitoring.configs.create(
            account_id="6f91088a406011ed95aed352566e8d4c",
            body={},
        )
        assert_matches_type(Configuration, config, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.magic_network_monitoring.configs.with_raw_response.create(
            account_id="6f91088a406011ed95aed352566e8d4c",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(Configuration, config, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.magic_network_monitoring.configs.with_streaming_response.create(
            account_id="6f91088a406011ed95aed352566e8d4c",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(Configuration, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_network_monitoring.configs.with_raw_response.create(
                account_id="",
                body={},
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        config = client.magic_network_monitoring.configs.update(
            account_id="6f91088a406011ed95aed352566e8d4c",
            body={},
        )
        assert_matches_type(Configuration, config, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.magic_network_monitoring.configs.with_raw_response.update(
            account_id="6f91088a406011ed95aed352566e8d4c",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(Configuration, config, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.magic_network_monitoring.configs.with_streaming_response.update(
            account_id="6f91088a406011ed95aed352566e8d4c",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(Configuration, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_network_monitoring.configs.with_raw_response.update(
                account_id="",
                body={},
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        config = client.magic_network_monitoring.configs.delete(
            account_id="6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(Configuration, config, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.magic_network_monitoring.configs.with_raw_response.delete(
            account_id="6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(Configuration, config, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.magic_network_monitoring.configs.with_streaming_response.delete(
            account_id="6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(Configuration, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_network_monitoring.configs.with_raw_response.delete(
                account_id="",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        config = client.magic_network_monitoring.configs.edit(
            account_id="6f91088a406011ed95aed352566e8d4c",
            body={},
        )
        assert_matches_type(Configuration, config, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.magic_network_monitoring.configs.with_raw_response.edit(
            account_id="6f91088a406011ed95aed352566e8d4c",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(Configuration, config, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.magic_network_monitoring.configs.with_streaming_response.edit(
            account_id="6f91088a406011ed95aed352566e8d4c",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(Configuration, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_network_monitoring.configs.with_raw_response.edit(
                account_id="",
                body={},
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        config = client.magic_network_monitoring.configs.get(
            account_id="6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(Configuration, config, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.magic_network_monitoring.configs.with_raw_response.get(
            account_id="6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(Configuration, config, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.magic_network_monitoring.configs.with_streaming_response.get(
            account_id="6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(Configuration, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_network_monitoring.configs.with_raw_response.get(
                account_id="",
            )


class TestAsyncConfigs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.magic_network_monitoring.configs.create(
            account_id="6f91088a406011ed95aed352566e8d4c",
            body={},
        )
        assert_matches_type(Configuration, config, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_network_monitoring.configs.with_raw_response.create(
            account_id="6f91088a406011ed95aed352566e8d4c",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(Configuration, config, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_network_monitoring.configs.with_streaming_response.create(
            account_id="6f91088a406011ed95aed352566e8d4c",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(Configuration, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_network_monitoring.configs.with_raw_response.create(
                account_id="",
                body={},
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.magic_network_monitoring.configs.update(
            account_id="6f91088a406011ed95aed352566e8d4c",
            body={},
        )
        assert_matches_type(Configuration, config, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_network_monitoring.configs.with_raw_response.update(
            account_id="6f91088a406011ed95aed352566e8d4c",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(Configuration, config, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_network_monitoring.configs.with_streaming_response.update(
            account_id="6f91088a406011ed95aed352566e8d4c",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(Configuration, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_network_monitoring.configs.with_raw_response.update(
                account_id="",
                body={},
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.magic_network_monitoring.configs.delete(
            account_id="6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(Configuration, config, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_network_monitoring.configs.with_raw_response.delete(
            account_id="6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(Configuration, config, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_network_monitoring.configs.with_streaming_response.delete(
            account_id="6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(Configuration, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_network_monitoring.configs.with_raw_response.delete(
                account_id="",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.magic_network_monitoring.configs.edit(
            account_id="6f91088a406011ed95aed352566e8d4c",
            body={},
        )
        assert_matches_type(Configuration, config, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_network_monitoring.configs.with_raw_response.edit(
            account_id="6f91088a406011ed95aed352566e8d4c",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(Configuration, config, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_network_monitoring.configs.with_streaming_response.edit(
            account_id="6f91088a406011ed95aed352566e8d4c",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(Configuration, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_network_monitoring.configs.with_raw_response.edit(
                account_id="",
                body={},
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.magic_network_monitoring.configs.get(
            account_id="6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(Configuration, config, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_network_monitoring.configs.with_raw_response.get(
            account_id="6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(Configuration, config, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_network_monitoring.configs.with_streaming_response.get(
            account_id="6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(Configuration, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_network_monitoring.configs.with_raw_response.get(
                account_id="",
            )
