# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncCursorPagination, AsyncCursorPagination
from cloudflare.types.zero_trust.cws import (
    Deployment,
    DeploymentDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeployments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        deployment = client.zero_trust.cws.deployments.create(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            basic_auth_credential_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            default_mode="ALLOW",
            name="x",
            policy_set_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(Deployment, deployment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        deployment = client.zero_trust.cws.deployments.create(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            basic_auth_credential_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            default_mode="ALLOW",
            name="x",
            policy_set_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            description="description",
            domain_acl_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            on_error_action="BLOCK",
            rego_raise_error=True,
            tags={"foo": "string"},
        )
        assert_matches_type(Deployment, deployment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.cws.deployments.with_raw_response.create(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            basic_auth_credential_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            default_mode="ALLOW",
            name="x",
            policy_set_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(Deployment, deployment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.cws.deployments.with_streaming_response.create(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            basic_auth_credential_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            default_mode="ALLOW",
            name="x",
            policy_set_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(Deployment, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.cws.deployments.with_raw_response.create(
                account_id="",
                basic_auth_credential_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                default_mode="ALLOW",
                name="x",
                policy_set_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        deployment = client.zero_trust.cws.deployments.update(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            basic_auth_credential_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            default_mode="ALLOW",
            name="x",
            policy_set_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(Deployment, deployment, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        deployment = client.zero_trust.cws.deployments.update(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            basic_auth_credential_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            default_mode="ALLOW",
            name="x",
            policy_set_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            description="description",
            domain_acl_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            on_error_action="BLOCK",
            rego_raise_error=True,
            tags={"foo": "string"},
        )
        assert_matches_type(Deployment, deployment, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.cws.deployments.with_raw_response.update(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            basic_auth_credential_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            default_mode="ALLOW",
            name="x",
            policy_set_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(Deployment, deployment, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.cws.deployments.with_streaming_response.update(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            basic_auth_credential_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            default_mode="ALLOW",
            name="x",
            policy_set_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(Deployment, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.cws.deployments.with_raw_response.update(
                deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                basic_auth_credential_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                default_mode="ALLOW",
                name="x",
                policy_set_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            client.zero_trust.cws.deployments.with_raw_response.update(
                deployment_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                basic_auth_credential_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                default_mode="ALLOW",
                name="x",
                policy_set_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        deployment = client.zero_trust.cws.deployments.list(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(SyncCursorPagination[Deployment], deployment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        deployment = client.zero_trust.cws.deployments.list(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            cursor="cursor",
            direction="asc",
            name="name",
            order="name",
            per_page=1,
        )
        assert_matches_type(SyncCursorPagination[Deployment], deployment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.cws.deployments.with_raw_response.list(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(SyncCursorPagination[Deployment], deployment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.cws.deployments.with_streaming_response.list(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(SyncCursorPagination[Deployment], deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.cws.deployments.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        deployment = client.zero_trust.cws.deployments.delete(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(DeploymentDeleteResponse, deployment, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.cws.deployments.with_raw_response.delete(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(DeploymentDeleteResponse, deployment, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.cws.deployments.with_streaming_response.delete(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(DeploymentDeleteResponse, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.cws.deployments.with_raw_response.delete(
                deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            client.zero_trust.cws.deployments.with_raw_response.delete(
                deployment_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        deployment = client.zero_trust.cws.deployments.get(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(Deployment, deployment, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.cws.deployments.with_raw_response.get(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(Deployment, deployment, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.cws.deployments.with_streaming_response.get(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(Deployment, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.cws.deployments.with_raw_response.get(
                deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            client.zero_trust.cws.deployments.with_raw_response.get(
                deployment_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            )


class TestAsyncDeployments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        deployment = await async_client.zero_trust.cws.deployments.create(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            basic_auth_credential_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            default_mode="ALLOW",
            name="x",
            policy_set_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(Deployment, deployment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        deployment = await async_client.zero_trust.cws.deployments.create(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            basic_auth_credential_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            default_mode="ALLOW",
            name="x",
            policy_set_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            description="description",
            domain_acl_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            on_error_action="BLOCK",
            rego_raise_error=True,
            tags={"foo": "string"},
        )
        assert_matches_type(Deployment, deployment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.cws.deployments.with_raw_response.create(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            basic_auth_credential_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            default_mode="ALLOW",
            name="x",
            policy_set_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(Deployment, deployment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.cws.deployments.with_streaming_response.create(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            basic_auth_credential_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            default_mode="ALLOW",
            name="x",
            policy_set_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(Deployment, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.cws.deployments.with_raw_response.create(
                account_id="",
                basic_auth_credential_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                default_mode="ALLOW",
                name="x",
                policy_set_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        deployment = await async_client.zero_trust.cws.deployments.update(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            basic_auth_credential_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            default_mode="ALLOW",
            name="x",
            policy_set_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(Deployment, deployment, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        deployment = await async_client.zero_trust.cws.deployments.update(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            basic_auth_credential_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            default_mode="ALLOW",
            name="x",
            policy_set_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            description="description",
            domain_acl_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            on_error_action="BLOCK",
            rego_raise_error=True,
            tags={"foo": "string"},
        )
        assert_matches_type(Deployment, deployment, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.cws.deployments.with_raw_response.update(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            basic_auth_credential_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            default_mode="ALLOW",
            name="x",
            policy_set_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(Deployment, deployment, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.cws.deployments.with_streaming_response.update(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            basic_auth_credential_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            default_mode="ALLOW",
            name="x",
            policy_set_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(Deployment, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.cws.deployments.with_raw_response.update(
                deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                basic_auth_credential_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                default_mode="ALLOW",
                name="x",
                policy_set_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            await async_client.zero_trust.cws.deployments.with_raw_response.update(
                deployment_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                basic_auth_credential_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                default_mode="ALLOW",
                name="x",
                policy_set_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        deployment = await async_client.zero_trust.cws.deployments.list(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(AsyncCursorPagination[Deployment], deployment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        deployment = await async_client.zero_trust.cws.deployments.list(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            cursor="cursor",
            direction="asc",
            name="name",
            order="name",
            per_page=1,
        )
        assert_matches_type(AsyncCursorPagination[Deployment], deployment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.cws.deployments.with_raw_response.list(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(AsyncCursorPagination[Deployment], deployment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.cws.deployments.with_streaming_response.list(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(AsyncCursorPagination[Deployment], deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.cws.deployments.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        deployment = await async_client.zero_trust.cws.deployments.delete(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(DeploymentDeleteResponse, deployment, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.cws.deployments.with_raw_response.delete(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(DeploymentDeleteResponse, deployment, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.cws.deployments.with_streaming_response.delete(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(DeploymentDeleteResponse, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.cws.deployments.with_raw_response.delete(
                deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            await async_client.zero_trust.cws.deployments.with_raw_response.delete(
                deployment_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        deployment = await async_client.zero_trust.cws.deployments.get(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(Deployment, deployment, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.cws.deployments.with_raw_response.get(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(Deployment, deployment, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.cws.deployments.with_streaming_response.get(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(Deployment, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.cws.deployments.with_raw_response.get(
                deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            await async_client.zero_trust.cws.deployments.with_raw_response.get(
                deployment_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            )
