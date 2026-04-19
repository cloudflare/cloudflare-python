# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.zero_trust.dlp.entries import (
    IntegrationGetResponse,
    IntegrationListResponse,
    IntegrationCreateResponse,
    IntegrationUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIntegration:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        integration = client.zero_trust.dlp.entries.integration.create(
            account_id="account_id",
            enabled=True,
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Optional[IntegrationCreateResponse], integration, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        integration = client.zero_trust.dlp.entries.integration.create(
            account_id="account_id",
            enabled=True,
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Optional[IntegrationCreateResponse], integration, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.entries.integration.with_raw_response.create(
            account_id="account_id",
            enabled=True,
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(Optional[IntegrationCreateResponse], integration, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.entries.integration.with_streaming_response.create(
            account_id="account_id",
            enabled=True,
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(Optional[IntegrationCreateResponse], integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.entries.integration.with_raw_response.create(
                account_id="",
                enabled=True,
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        integration = client.zero_trust.dlp.entries.integration.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            enabled=True,
        )
        assert_matches_type(Optional[IntegrationUpdateResponse], integration, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.entries.integration.with_raw_response.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(Optional[IntegrationUpdateResponse], integration, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.entries.integration.with_streaming_response.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(Optional[IntegrationUpdateResponse], integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.entries.integration.with_raw_response.update(
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                enabled=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            client.zero_trust.dlp.entries.integration.with_raw_response.update(
                entry_id="",
                account_id="account_id",
                enabled=True,
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        integration = client.zero_trust.dlp.entries.integration.list(
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[IntegrationListResponse], integration, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.entries.integration.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(SyncSinglePage[IntegrationListResponse], integration, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.entries.integration.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(SyncSinglePage[IntegrationListResponse], integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.entries.integration.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        integration = client.zero_trust.dlp.entries.integration.delete(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(object, integration, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.entries.integration.with_raw_response.delete(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(object, integration, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.entries.integration.with_streaming_response.delete(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(object, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.entries.integration.with_raw_response.delete(
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            client.zero_trust.dlp.entries.integration.with_raw_response.delete(
                entry_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        integration = client.zero_trust.dlp.entries.integration.get(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(Optional[IntegrationGetResponse], integration, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.entries.integration.with_raw_response.get(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(Optional[IntegrationGetResponse], integration, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.entries.integration.with_streaming_response.get(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(Optional[IntegrationGetResponse], integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.entries.integration.with_raw_response.get(
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            client.zero_trust.dlp.entries.integration.with_raw_response.get(
                entry_id="",
                account_id="account_id",
            )


class TestAsyncIntegration:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        integration = await async_client.zero_trust.dlp.entries.integration.create(
            account_id="account_id",
            enabled=True,
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Optional[IntegrationCreateResponse], integration, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        integration = await async_client.zero_trust.dlp.entries.integration.create(
            account_id="account_id",
            enabled=True,
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Optional[IntegrationCreateResponse], integration, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.entries.integration.with_raw_response.create(
            account_id="account_id",
            enabled=True,
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(Optional[IntegrationCreateResponse], integration, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.entries.integration.with_streaming_response.create(
            account_id="account_id",
            enabled=True,
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(Optional[IntegrationCreateResponse], integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.entries.integration.with_raw_response.create(
                account_id="",
                enabled=True,
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        integration = await async_client.zero_trust.dlp.entries.integration.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            enabled=True,
        )
        assert_matches_type(Optional[IntegrationUpdateResponse], integration, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.entries.integration.with_raw_response.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(Optional[IntegrationUpdateResponse], integration, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.entries.integration.with_streaming_response.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(Optional[IntegrationUpdateResponse], integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.entries.integration.with_raw_response.update(
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                enabled=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            await async_client.zero_trust.dlp.entries.integration.with_raw_response.update(
                entry_id="",
                account_id="account_id",
                enabled=True,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        integration = await async_client.zero_trust.dlp.entries.integration.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[IntegrationListResponse], integration, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.entries.integration.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(AsyncSinglePage[IntegrationListResponse], integration, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.entries.integration.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(AsyncSinglePage[IntegrationListResponse], integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.entries.integration.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        integration = await async_client.zero_trust.dlp.entries.integration.delete(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(object, integration, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.entries.integration.with_raw_response.delete(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(object, integration, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.entries.integration.with_streaming_response.delete(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(object, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.entries.integration.with_raw_response.delete(
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            await async_client.zero_trust.dlp.entries.integration.with_raw_response.delete(
                entry_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        integration = await async_client.zero_trust.dlp.entries.integration.get(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(Optional[IntegrationGetResponse], integration, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.entries.integration.with_raw_response.get(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(Optional[IntegrationGetResponse], integration, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.entries.integration.with_streaming_response.get(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(Optional[IntegrationGetResponse], integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.entries.integration.with_raw_response.get(
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            await async_client.zero_trust.dlp.entries.integration.with_raw_response.get(
                entry_id="",
                account_id="account_id",
            )
