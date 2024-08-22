# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.zero_trust.risk_scoring import (
    IntegrationGetResponse,
    IntegrationListResponse,
    IntegrationCreateResponse,
    IntegrationUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIntegrations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        integration = client.zero_trust.risk_scoring.integrations.create(
            account_id="account_id",
            integration_type="Okta",
            tenant_url="https://example.com",
        )
        assert_matches_type(Optional[IntegrationCreateResponse], integration, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        integration = client.zero_trust.risk_scoring.integrations.create(
            account_id="account_id",
            integration_type="Okta",
            tenant_url="https://example.com",
            reference_id="reference_id",
        )
        assert_matches_type(Optional[IntegrationCreateResponse], integration, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.risk_scoring.integrations.with_raw_response.create(
            account_id="account_id",
            integration_type="Okta",
            tenant_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(Optional[IntegrationCreateResponse], integration, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.risk_scoring.integrations.with_streaming_response.create(
            account_id="account_id",
            integration_type="Okta",
            tenant_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(Optional[IntegrationCreateResponse], integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.risk_scoring.integrations.with_raw_response.create(
                account_id="",
                integration_type="Okta",
                tenant_url="https://example.com",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        integration = client.zero_trust.risk_scoring.integrations.update(
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            active=True,
            tenant_url="https://example.com",
        )
        assert_matches_type(Optional[IntegrationUpdateResponse], integration, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        integration = client.zero_trust.risk_scoring.integrations.update(
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            active=True,
            tenant_url="https://example.com",
            reference_id="reference_id",
        )
        assert_matches_type(Optional[IntegrationUpdateResponse], integration, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.risk_scoring.integrations.with_raw_response.update(
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            active=True,
            tenant_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(Optional[IntegrationUpdateResponse], integration, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.risk_scoring.integrations.with_streaming_response.update(
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            active=True,
            tenant_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(Optional[IntegrationUpdateResponse], integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.risk_scoring.integrations.with_raw_response.update(
                integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                active=True,
                tenant_url="https://example.com",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            client.zero_trust.risk_scoring.integrations.with_raw_response.update(
                integration_id="",
                account_id="account_id",
                active=True,
                tenant_url="https://example.com",
            )

    @pytest.mark.skip(reason="bug in prism where it confuses this method with /zt_risk_scoring/{user_id}")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        integration = client.zero_trust.risk_scoring.integrations.list(
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[IntegrationListResponse], integration, path=["response"])

    @pytest.mark.skip(reason="bug in prism where it confuses this method with /zt_risk_scoring/{user_id}")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.risk_scoring.integrations.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(SyncSinglePage[IntegrationListResponse], integration, path=["response"])

    @pytest.mark.skip(reason="bug in prism where it confuses this method with /zt_risk_scoring/{user_id}")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.risk_scoring.integrations.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(SyncSinglePage[IntegrationListResponse], integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="bug in prism where it confuses this method with /zt_risk_scoring/{user_id}")
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.risk_scoring.integrations.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        integration = client.zero_trust.risk_scoring.integrations.delete(
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(object, integration, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.risk_scoring.integrations.with_raw_response.delete(
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(object, integration, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.risk_scoring.integrations.with_streaming_response.delete(
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
            client.zero_trust.risk_scoring.integrations.with_raw_response.delete(
                integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            client.zero_trust.risk_scoring.integrations.with_raw_response.delete(
                integration_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        integration = client.zero_trust.risk_scoring.integrations.get(
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(Optional[IntegrationGetResponse], integration, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.risk_scoring.integrations.with_raw_response.get(
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(Optional[IntegrationGetResponse], integration, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.risk_scoring.integrations.with_streaming_response.get(
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
            client.zero_trust.risk_scoring.integrations.with_raw_response.get(
                integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            client.zero_trust.risk_scoring.integrations.with_raw_response.get(
                integration_id="",
                account_id="account_id",
            )


class TestAsyncIntegrations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        integration = await async_client.zero_trust.risk_scoring.integrations.create(
            account_id="account_id",
            integration_type="Okta",
            tenant_url="https://example.com",
        )
        assert_matches_type(Optional[IntegrationCreateResponse], integration, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        integration = await async_client.zero_trust.risk_scoring.integrations.create(
            account_id="account_id",
            integration_type="Okta",
            tenant_url="https://example.com",
            reference_id="reference_id",
        )
        assert_matches_type(Optional[IntegrationCreateResponse], integration, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.risk_scoring.integrations.with_raw_response.create(
            account_id="account_id",
            integration_type="Okta",
            tenant_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(Optional[IntegrationCreateResponse], integration, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.risk_scoring.integrations.with_streaming_response.create(
            account_id="account_id",
            integration_type="Okta",
            tenant_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(Optional[IntegrationCreateResponse], integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.risk_scoring.integrations.with_raw_response.create(
                account_id="",
                integration_type="Okta",
                tenant_url="https://example.com",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        integration = await async_client.zero_trust.risk_scoring.integrations.update(
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            active=True,
            tenant_url="https://example.com",
        )
        assert_matches_type(Optional[IntegrationUpdateResponse], integration, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        integration = await async_client.zero_trust.risk_scoring.integrations.update(
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            active=True,
            tenant_url="https://example.com",
            reference_id="reference_id",
        )
        assert_matches_type(Optional[IntegrationUpdateResponse], integration, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.risk_scoring.integrations.with_raw_response.update(
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            active=True,
            tenant_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(Optional[IntegrationUpdateResponse], integration, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.risk_scoring.integrations.with_streaming_response.update(
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            active=True,
            tenant_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(Optional[IntegrationUpdateResponse], integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.risk_scoring.integrations.with_raw_response.update(
                integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                active=True,
                tenant_url="https://example.com",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            await async_client.zero_trust.risk_scoring.integrations.with_raw_response.update(
                integration_id="",
                account_id="account_id",
                active=True,
                tenant_url="https://example.com",
            )

    @pytest.mark.skip(reason="bug in prism where it confuses this method with /zt_risk_scoring/{user_id}")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        integration = await async_client.zero_trust.risk_scoring.integrations.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[IntegrationListResponse], integration, path=["response"])

    @pytest.mark.skip(reason="bug in prism where it confuses this method with /zt_risk_scoring/{user_id}")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.risk_scoring.integrations.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(AsyncSinglePage[IntegrationListResponse], integration, path=["response"])

    @pytest.mark.skip(reason="bug in prism where it confuses this method with /zt_risk_scoring/{user_id}")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.risk_scoring.integrations.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(AsyncSinglePage[IntegrationListResponse], integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="bug in prism where it confuses this method with /zt_risk_scoring/{user_id}")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.risk_scoring.integrations.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        integration = await async_client.zero_trust.risk_scoring.integrations.delete(
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(object, integration, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.risk_scoring.integrations.with_raw_response.delete(
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(object, integration, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.risk_scoring.integrations.with_streaming_response.delete(
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
            await async_client.zero_trust.risk_scoring.integrations.with_raw_response.delete(
                integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            await async_client.zero_trust.risk_scoring.integrations.with_raw_response.delete(
                integration_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        integration = await async_client.zero_trust.risk_scoring.integrations.get(
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(Optional[IntegrationGetResponse], integration, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.risk_scoring.integrations.with_raw_response.get(
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(Optional[IntegrationGetResponse], integration, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.risk_scoring.integrations.with_streaming_response.get(
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
            await async_client.zero_trust.risk_scoring.integrations.with_raw_response.get(
                integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            await async_client.zero_trust.risk_scoring.integrations.with_raw_response.get(
                integration_id="",
                account_id="account_id",
            )
