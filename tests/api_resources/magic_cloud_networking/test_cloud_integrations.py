# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.magic_cloud_networking import (
    CloudIntegrationGetResponse,
    CloudIntegrationEditResponse,
    CloudIntegrationListResponse,
    CloudIntegrationCreateResponse,
    CloudIntegrationDeleteResponse,
    CloudIntegrationUpdateResponse,
    CloudIntegrationDiscoverResponse,
    CloudIntegrationDiscoverAllResponse,
    CloudIntegrationInitialSetupResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCloudIntegrations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        cloud_integration = client.magic_cloud_networking.cloud_integrations.create(
            account_id="account_id",
            cloud_type="AWS",
            friendly_name="friendly_name",
        )
        assert_matches_type(CloudIntegrationCreateResponse, cloud_integration, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        cloud_integration = client.magic_cloud_networking.cloud_integrations.create(
            account_id="account_id",
            cloud_type="AWS",
            friendly_name="friendly_name",
            description="description",
            forwarded="forwarded",
        )
        assert_matches_type(CloudIntegrationCreateResponse, cloud_integration, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.cloud_integrations.with_raw_response.create(
            account_id="account_id",
            cloud_type="AWS",
            friendly_name="friendly_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cloud_integration = response.parse()
        assert_matches_type(CloudIntegrationCreateResponse, cloud_integration, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.cloud_integrations.with_streaming_response.create(
            account_id="account_id",
            cloud_type="AWS",
            friendly_name="friendly_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cloud_integration = response.parse()
            assert_matches_type(CloudIntegrationCreateResponse, cloud_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.cloud_integrations.with_raw_response.create(
                account_id="",
                cloud_type="AWS",
                friendly_name="friendly_name",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        cloud_integration = client.magic_cloud_networking.cloud_integrations.update(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(CloudIntegrationUpdateResponse, cloud_integration, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        cloud_integration = client.magic_cloud_networking.cloud_integrations.update(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            aws_arn="aws_arn",
            azure_subscription_id="azure_subscription_id",
            azure_tenant_id="azure_tenant_id",
            description="description",
            friendly_name="friendly_name",
            gcp_project_id="gcp_project_id",
            gcp_service_account_email="gcp_service_account_email",
        )
        assert_matches_type(CloudIntegrationUpdateResponse, cloud_integration, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.cloud_integrations.with_raw_response.update(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cloud_integration = response.parse()
        assert_matches_type(CloudIntegrationUpdateResponse, cloud_integration, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.cloud_integrations.with_streaming_response.update(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cloud_integration = response.parse()
            assert_matches_type(CloudIntegrationUpdateResponse, cloud_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.cloud_integrations.with_raw_response.update(
                provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            client.magic_cloud_networking.cloud_integrations.with_raw_response.update(
                provider_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        cloud_integration = client.magic_cloud_networking.cloud_integrations.list(
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[CloudIntegrationListResponse], cloud_integration, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        cloud_integration = client.magic_cloud_networking.cloud_integrations.list(
            account_id="account_id",
            cloudflare=True,
            desc=True,
            order_by="order_by",
            status=True,
        )
        assert_matches_type(SyncSinglePage[CloudIntegrationListResponse], cloud_integration, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.cloud_integrations.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cloud_integration = response.parse()
        assert_matches_type(SyncSinglePage[CloudIntegrationListResponse], cloud_integration, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.cloud_integrations.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cloud_integration = response.parse()
            assert_matches_type(SyncSinglePage[CloudIntegrationListResponse], cloud_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.cloud_integrations.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        cloud_integration = client.magic_cloud_networking.cloud_integrations.delete(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(CloudIntegrationDeleteResponse, cloud_integration, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.cloud_integrations.with_raw_response.delete(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cloud_integration = response.parse()
        assert_matches_type(CloudIntegrationDeleteResponse, cloud_integration, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.cloud_integrations.with_streaming_response.delete(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cloud_integration = response.parse()
            assert_matches_type(CloudIntegrationDeleteResponse, cloud_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.cloud_integrations.with_raw_response.delete(
                provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            client.magic_cloud_networking.cloud_integrations.with_raw_response.delete(
                provider_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_discover(self, client: Cloudflare) -> None:
        cloud_integration = client.magic_cloud_networking.cloud_integrations.discover(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(CloudIntegrationDiscoverResponse, cloud_integration, path=["response"])

    @parametrize
    def test_method_discover_with_all_params(self, client: Cloudflare) -> None:
        cloud_integration = client.magic_cloud_networking.cloud_integrations.discover(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            v2=True,
        )
        assert_matches_type(CloudIntegrationDiscoverResponse, cloud_integration, path=["response"])

    @parametrize
    def test_raw_response_discover(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.cloud_integrations.with_raw_response.discover(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cloud_integration = response.parse()
        assert_matches_type(CloudIntegrationDiscoverResponse, cloud_integration, path=["response"])

    @parametrize
    def test_streaming_response_discover(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.cloud_integrations.with_streaming_response.discover(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cloud_integration = response.parse()
            assert_matches_type(CloudIntegrationDiscoverResponse, cloud_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_discover(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.cloud_integrations.with_raw_response.discover(
                provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            client.magic_cloud_networking.cloud_integrations.with_raw_response.discover(
                provider_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_discover_all(self, client: Cloudflare) -> None:
        cloud_integration = client.magic_cloud_networking.cloud_integrations.discover_all(
            account_id="account_id",
        )
        assert_matches_type(CloudIntegrationDiscoverAllResponse, cloud_integration, path=["response"])

    @parametrize
    def test_raw_response_discover_all(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.cloud_integrations.with_raw_response.discover_all(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cloud_integration = response.parse()
        assert_matches_type(CloudIntegrationDiscoverAllResponse, cloud_integration, path=["response"])

    @parametrize
    def test_streaming_response_discover_all(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.cloud_integrations.with_streaming_response.discover_all(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cloud_integration = response.parse()
            assert_matches_type(CloudIntegrationDiscoverAllResponse, cloud_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_discover_all(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.cloud_integrations.with_raw_response.discover_all(
                account_id="",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        cloud_integration = client.magic_cloud_networking.cloud_integrations.edit(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(CloudIntegrationEditResponse, cloud_integration, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        cloud_integration = client.magic_cloud_networking.cloud_integrations.edit(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            aws_arn="aws_arn",
            azure_subscription_id="azure_subscription_id",
            azure_tenant_id="azure_tenant_id",
            description="description",
            friendly_name="friendly_name",
            gcp_project_id="gcp_project_id",
            gcp_service_account_email="gcp_service_account_email",
        )
        assert_matches_type(CloudIntegrationEditResponse, cloud_integration, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.cloud_integrations.with_raw_response.edit(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cloud_integration = response.parse()
        assert_matches_type(CloudIntegrationEditResponse, cloud_integration, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.cloud_integrations.with_streaming_response.edit(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cloud_integration = response.parse()
            assert_matches_type(CloudIntegrationEditResponse, cloud_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.cloud_integrations.with_raw_response.edit(
                provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            client.magic_cloud_networking.cloud_integrations.with_raw_response.edit(
                provider_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        cloud_integration = client.magic_cloud_networking.cloud_integrations.get(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(CloudIntegrationGetResponse, cloud_integration, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        cloud_integration = client.magic_cloud_networking.cloud_integrations.get(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            status=True,
        )
        assert_matches_type(CloudIntegrationGetResponse, cloud_integration, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.cloud_integrations.with_raw_response.get(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cloud_integration = response.parse()
        assert_matches_type(CloudIntegrationGetResponse, cloud_integration, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.cloud_integrations.with_streaming_response.get(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cloud_integration = response.parse()
            assert_matches_type(CloudIntegrationGetResponse, cloud_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.cloud_integrations.with_raw_response.get(
                provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            client.magic_cloud_networking.cloud_integrations.with_raw_response.get(
                provider_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_initial_setup(self, client: Cloudflare) -> None:
        cloud_integration = client.magic_cloud_networking.cloud_integrations.initial_setup(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(CloudIntegrationInitialSetupResponse, cloud_integration, path=["response"])

    @parametrize
    def test_raw_response_initial_setup(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.cloud_integrations.with_raw_response.initial_setup(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cloud_integration = response.parse()
        assert_matches_type(CloudIntegrationInitialSetupResponse, cloud_integration, path=["response"])

    @parametrize
    def test_streaming_response_initial_setup(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.cloud_integrations.with_streaming_response.initial_setup(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cloud_integration = response.parse()
            assert_matches_type(CloudIntegrationInitialSetupResponse, cloud_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_initial_setup(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.cloud_integrations.with_raw_response.initial_setup(
                provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            client.magic_cloud_networking.cloud_integrations.with_raw_response.initial_setup(
                provider_id="",
                account_id="account_id",
            )


class TestAsyncCloudIntegrations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        cloud_integration = await async_client.magic_cloud_networking.cloud_integrations.create(
            account_id="account_id",
            cloud_type="AWS",
            friendly_name="friendly_name",
        )
        assert_matches_type(CloudIntegrationCreateResponse, cloud_integration, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        cloud_integration = await async_client.magic_cloud_networking.cloud_integrations.create(
            account_id="account_id",
            cloud_type="AWS",
            friendly_name="friendly_name",
            description="description",
            forwarded="forwarded",
        )
        assert_matches_type(CloudIntegrationCreateResponse, cloud_integration, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.cloud_integrations.with_raw_response.create(
            account_id="account_id",
            cloud_type="AWS",
            friendly_name="friendly_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cloud_integration = await response.parse()
        assert_matches_type(CloudIntegrationCreateResponse, cloud_integration, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.cloud_integrations.with_streaming_response.create(
            account_id="account_id",
            cloud_type="AWS",
            friendly_name="friendly_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cloud_integration = await response.parse()
            assert_matches_type(CloudIntegrationCreateResponse, cloud_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.cloud_integrations.with_raw_response.create(
                account_id="",
                cloud_type="AWS",
                friendly_name="friendly_name",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        cloud_integration = await async_client.magic_cloud_networking.cloud_integrations.update(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(CloudIntegrationUpdateResponse, cloud_integration, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        cloud_integration = await async_client.magic_cloud_networking.cloud_integrations.update(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            aws_arn="aws_arn",
            azure_subscription_id="azure_subscription_id",
            azure_tenant_id="azure_tenant_id",
            description="description",
            friendly_name="friendly_name",
            gcp_project_id="gcp_project_id",
            gcp_service_account_email="gcp_service_account_email",
        )
        assert_matches_type(CloudIntegrationUpdateResponse, cloud_integration, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.cloud_integrations.with_raw_response.update(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cloud_integration = await response.parse()
        assert_matches_type(CloudIntegrationUpdateResponse, cloud_integration, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.cloud_integrations.with_streaming_response.update(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cloud_integration = await response.parse()
            assert_matches_type(CloudIntegrationUpdateResponse, cloud_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.cloud_integrations.with_raw_response.update(
                provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            await async_client.magic_cloud_networking.cloud_integrations.with_raw_response.update(
                provider_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        cloud_integration = await async_client.magic_cloud_networking.cloud_integrations.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[CloudIntegrationListResponse], cloud_integration, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        cloud_integration = await async_client.magic_cloud_networking.cloud_integrations.list(
            account_id="account_id",
            cloudflare=True,
            desc=True,
            order_by="order_by",
            status=True,
        )
        assert_matches_type(AsyncSinglePage[CloudIntegrationListResponse], cloud_integration, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.cloud_integrations.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cloud_integration = await response.parse()
        assert_matches_type(AsyncSinglePage[CloudIntegrationListResponse], cloud_integration, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.cloud_integrations.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cloud_integration = await response.parse()
            assert_matches_type(AsyncSinglePage[CloudIntegrationListResponse], cloud_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.cloud_integrations.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        cloud_integration = await async_client.magic_cloud_networking.cloud_integrations.delete(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(CloudIntegrationDeleteResponse, cloud_integration, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.cloud_integrations.with_raw_response.delete(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cloud_integration = await response.parse()
        assert_matches_type(CloudIntegrationDeleteResponse, cloud_integration, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.cloud_integrations.with_streaming_response.delete(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cloud_integration = await response.parse()
            assert_matches_type(CloudIntegrationDeleteResponse, cloud_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.cloud_integrations.with_raw_response.delete(
                provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            await async_client.magic_cloud_networking.cloud_integrations.with_raw_response.delete(
                provider_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_discover(self, async_client: AsyncCloudflare) -> None:
        cloud_integration = await async_client.magic_cloud_networking.cloud_integrations.discover(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(CloudIntegrationDiscoverResponse, cloud_integration, path=["response"])

    @parametrize
    async def test_method_discover_with_all_params(self, async_client: AsyncCloudflare) -> None:
        cloud_integration = await async_client.magic_cloud_networking.cloud_integrations.discover(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            v2=True,
        )
        assert_matches_type(CloudIntegrationDiscoverResponse, cloud_integration, path=["response"])

    @parametrize
    async def test_raw_response_discover(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.cloud_integrations.with_raw_response.discover(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cloud_integration = await response.parse()
        assert_matches_type(CloudIntegrationDiscoverResponse, cloud_integration, path=["response"])

    @parametrize
    async def test_streaming_response_discover(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.cloud_integrations.with_streaming_response.discover(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cloud_integration = await response.parse()
            assert_matches_type(CloudIntegrationDiscoverResponse, cloud_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_discover(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.cloud_integrations.with_raw_response.discover(
                provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            await async_client.magic_cloud_networking.cloud_integrations.with_raw_response.discover(
                provider_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_discover_all(self, async_client: AsyncCloudflare) -> None:
        cloud_integration = await async_client.magic_cloud_networking.cloud_integrations.discover_all(
            account_id="account_id",
        )
        assert_matches_type(CloudIntegrationDiscoverAllResponse, cloud_integration, path=["response"])

    @parametrize
    async def test_raw_response_discover_all(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.cloud_integrations.with_raw_response.discover_all(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cloud_integration = await response.parse()
        assert_matches_type(CloudIntegrationDiscoverAllResponse, cloud_integration, path=["response"])

    @parametrize
    async def test_streaming_response_discover_all(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.cloud_integrations.with_streaming_response.discover_all(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cloud_integration = await response.parse()
            assert_matches_type(CloudIntegrationDiscoverAllResponse, cloud_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_discover_all(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.cloud_integrations.with_raw_response.discover_all(
                account_id="",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        cloud_integration = await async_client.magic_cloud_networking.cloud_integrations.edit(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(CloudIntegrationEditResponse, cloud_integration, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        cloud_integration = await async_client.magic_cloud_networking.cloud_integrations.edit(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            aws_arn="aws_arn",
            azure_subscription_id="azure_subscription_id",
            azure_tenant_id="azure_tenant_id",
            description="description",
            friendly_name="friendly_name",
            gcp_project_id="gcp_project_id",
            gcp_service_account_email="gcp_service_account_email",
        )
        assert_matches_type(CloudIntegrationEditResponse, cloud_integration, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.cloud_integrations.with_raw_response.edit(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cloud_integration = await response.parse()
        assert_matches_type(CloudIntegrationEditResponse, cloud_integration, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.cloud_integrations.with_streaming_response.edit(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cloud_integration = await response.parse()
            assert_matches_type(CloudIntegrationEditResponse, cloud_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.cloud_integrations.with_raw_response.edit(
                provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            await async_client.magic_cloud_networking.cloud_integrations.with_raw_response.edit(
                provider_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        cloud_integration = await async_client.magic_cloud_networking.cloud_integrations.get(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(CloudIntegrationGetResponse, cloud_integration, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        cloud_integration = await async_client.magic_cloud_networking.cloud_integrations.get(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            status=True,
        )
        assert_matches_type(CloudIntegrationGetResponse, cloud_integration, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.cloud_integrations.with_raw_response.get(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cloud_integration = await response.parse()
        assert_matches_type(CloudIntegrationGetResponse, cloud_integration, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.cloud_integrations.with_streaming_response.get(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cloud_integration = await response.parse()
            assert_matches_type(CloudIntegrationGetResponse, cloud_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.cloud_integrations.with_raw_response.get(
                provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            await async_client.magic_cloud_networking.cloud_integrations.with_raw_response.get(
                provider_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_initial_setup(self, async_client: AsyncCloudflare) -> None:
        cloud_integration = await async_client.magic_cloud_networking.cloud_integrations.initial_setup(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(CloudIntegrationInitialSetupResponse, cloud_integration, path=["response"])

    @parametrize
    async def test_raw_response_initial_setup(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.cloud_integrations.with_raw_response.initial_setup(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cloud_integration = await response.parse()
        assert_matches_type(CloudIntegrationInitialSetupResponse, cloud_integration, path=["response"])

    @parametrize
    async def test_streaming_response_initial_setup(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.cloud_integrations.with_streaming_response.initial_setup(
            provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cloud_integration = await response.parse()
            assert_matches_type(CloudIntegrationInitialSetupResponse, cloud_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_initial_setup(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.cloud_integrations.with_raw_response.initial_setup(
                provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            await async_client.magic_cloud_networking.cloud_integrations.with_raw_response.initial_setup(
                provider_id="",
                account_id="account_id",
            )
