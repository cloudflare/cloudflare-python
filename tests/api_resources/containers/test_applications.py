# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncPageTokenPagination, AsyncPageTokenPagination
from cloudflare.types.containers import (
    ApplicationGetResponse,
    ApplicationEditResponse,
    ApplicationListResponse,
    ApplicationCreateResponse,
    ApplicationDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApplications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Cloudflare) -> None:
        application = client.containers.applications.create(
            account_id="account-123",
            configuration={"image": "image"},
            instances=0,
            max_instances=0,
            name="name",
            scheduling_policy="default",
        )
        assert_matches_type(ApplicationCreateResponse, application, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Cloudflare) -> None:
        application = client.containers.applications.create(
            account_id="account-123",
            configuration={
                "image": "image",
                "authorized_keys": [
                    {
                        "public_key": "public_key",
                        "name": "name",
                    }
                ],
                "command": ["myapp", "--default-option"],
                "entrypoint": ["/bin/bash"],
                "environment_variables": [
                    {
                        "name": "name",
                        "value": "value",
                    }
                ],
                "instance_type": "lite",
                "observability": {"logs": {"enabled": True}},
            },
            instances=0,
            max_instances=0,
            name="name",
            scheduling_policy="default",
            constraints={
                "jurisdiction": "jurisdiction",
                "regions": ["WNAM"],
            },
            durable_objects={"namespace_id": "14758f1afd44c09b7992073ccf00b43d"},
            observability={"logs": {"enabled": True}},
            rollout_active_grace_period=0,
        )
        assert_matches_type(ApplicationCreateResponse, application, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Cloudflare) -> None:
        response = client.containers.applications.with_raw_response.create(
            account_id="account-123",
            configuration={"image": "image"},
            instances=0,
            max_instances=0,
            name="name",
            scheduling_policy="default",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(ApplicationCreateResponse, application, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Cloudflare) -> None:
        with client.containers.applications.with_streaming_response.create(
            account_id="account-123",
            configuration={"image": "image"},
            instances=0,
            max_instances=0,
            name="name",
            scheduling_policy="default",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(ApplicationCreateResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.containers.applications.with_raw_response.create(
                account_id="",
                configuration={"image": "image"},
                instances=0,
                max_instances=0,
                name="name",
                scheduling_policy="default",
            )

    @parametrize
    def test_method_create_overload_2(self, client: Cloudflare) -> None:
        application = client.containers.applications.create(
            account_id="account-123",
            durable_objects={"namespace_id": "14758f1afd44c09b7992073ccf00b43d"},
            name="name",
            scheduling_policy="durable_object",
        )
        assert_matches_type(ApplicationCreateResponse, application, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Cloudflare) -> None:
        application = client.containers.applications.create(
            account_id="account-123",
            durable_objects={"namespace_id": "14758f1afd44c09b7992073ccf00b43d"},
            name="name",
            scheduling_policy="durable_object",
            configuration={
                "authorized_keys": [
                    {
                        "public_key": "public_key",
                        "name": "name",
                    }
                ],
                "wrangler_ssh": {
                    "enabled": True,
                    "port": 1,
                },
            },
            observability={"logs": {"enabled": True}},
        )
        assert_matches_type(ApplicationCreateResponse, application, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Cloudflare) -> None:
        response = client.containers.applications.with_raw_response.create(
            account_id="account-123",
            durable_objects={"namespace_id": "14758f1afd44c09b7992073ccf00b43d"},
            name="name",
            scheduling_policy="durable_object",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(ApplicationCreateResponse, application, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Cloudflare) -> None:
        with client.containers.applications.with_streaming_response.create(
            account_id="account-123",
            durable_objects={"namespace_id": "14758f1afd44c09b7992073ccf00b43d"},
            name="name",
            scheduling_policy="durable_object",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(ApplicationCreateResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.containers.applications.with_raw_response.create(
                account_id="",
                durable_objects={"namespace_id": "14758f1afd44c09b7992073ccf00b43d"},
                name="name",
                scheduling_policy="durable_object",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        application = client.containers.applications.list(
            account_id="account-123",
        )
        assert_matches_type(SyncPageTokenPagination[ApplicationListResponse], application, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        application = client.containers.applications.list(
            account_id="account-123",
            image="image",
            name="name",
            page_token="page_token",
            per_page=1,
        )
        assert_matches_type(SyncPageTokenPagination[ApplicationListResponse], application, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.containers.applications.with_raw_response.list(
            account_id="account-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(SyncPageTokenPagination[ApplicationListResponse], application, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.containers.applications.with_streaming_response.list(
            account_id="account-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(SyncPageTokenPagination[ApplicationListResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.containers.applications.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        application = client.containers.applications.delete(
            application_id="application_id",
            account_id="account-123",
        )
        assert_matches_type(ApplicationDeleteResponse, application, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.containers.applications.with_raw_response.delete(
            application_id="application_id",
            account_id="account-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(ApplicationDeleteResponse, application, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.containers.applications.with_streaming_response.delete(
            application_id="application_id",
            account_id="account-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(ApplicationDeleteResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.containers.applications.with_raw_response.delete(
                application_id="application_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.containers.applications.with_raw_response.delete(
                application_id="",
                account_id="account-123",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        application = client.containers.applications.edit(
            application_id="application_id",
            account_id="account-123",
        )
        assert_matches_type(ApplicationEditResponse, application, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        application = client.containers.applications.edit(
            application_id="application_id",
            account_id="account-123",
            configuration={
                "authorized_keys": [
                    {
                        "public_key": "public_key",
                        "name": "name",
                    }
                ],
                "wrangler_ssh": {
                    "enabled": True,
                    "port": 1,
                },
            },
            constraints={
                "jurisdiction": "jurisdiction",
                "regions": ["WNAM"],
            },
            max_instances=0,
            observability={"logs": {"enabled": True}},
            rollout_active_grace_period=0,
        )
        assert_matches_type(ApplicationEditResponse, application, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.containers.applications.with_raw_response.edit(
            application_id="application_id",
            account_id="account-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(ApplicationEditResponse, application, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.containers.applications.with_streaming_response.edit(
            application_id="application_id",
            account_id="account-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(ApplicationEditResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.containers.applications.with_raw_response.edit(
                application_id="application_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.containers.applications.with_raw_response.edit(
                application_id="",
                account_id="account-123",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        application = client.containers.applications.get(
            application_id="application_id",
            account_id="account-123",
        )
        assert_matches_type(ApplicationGetResponse, application, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.containers.applications.with_raw_response.get(
            application_id="application_id",
            account_id="account-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(ApplicationGetResponse, application, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.containers.applications.with_streaming_response.get(
            application_id="application_id",
            account_id="account-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(ApplicationGetResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.containers.applications.with_raw_response.get(
                application_id="application_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.containers.applications.with_raw_response.get(
                application_id="",
                account_id="account-123",
            )


class TestAsyncApplications:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.containers.applications.create(
            account_id="account-123",
            configuration={"image": "image"},
            instances=0,
            max_instances=0,
            name="name",
            scheduling_policy="default",
        )
        assert_matches_type(ApplicationCreateResponse, application, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.containers.applications.create(
            account_id="account-123",
            configuration={
                "image": "image",
                "authorized_keys": [
                    {
                        "public_key": "public_key",
                        "name": "name",
                    }
                ],
                "command": ["myapp", "--default-option"],
                "entrypoint": ["/bin/bash"],
                "environment_variables": [
                    {
                        "name": "name",
                        "value": "value",
                    }
                ],
                "instance_type": "lite",
                "observability": {"logs": {"enabled": True}},
            },
            instances=0,
            max_instances=0,
            name="name",
            scheduling_policy="default",
            constraints={
                "jurisdiction": "jurisdiction",
                "regions": ["WNAM"],
            },
            durable_objects={"namespace_id": "14758f1afd44c09b7992073ccf00b43d"},
            observability={"logs": {"enabled": True}},
            rollout_active_grace_period=0,
        )
        assert_matches_type(ApplicationCreateResponse, application, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.containers.applications.with_raw_response.create(
            account_id="account-123",
            configuration={"image": "image"},
            instances=0,
            max_instances=0,
            name="name",
            scheduling_policy="default",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(ApplicationCreateResponse, application, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.containers.applications.with_streaming_response.create(
            account_id="account-123",
            configuration={"image": "image"},
            instances=0,
            max_instances=0,
            name="name",
            scheduling_policy="default",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(ApplicationCreateResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.containers.applications.with_raw_response.create(
                account_id="",
                configuration={"image": "image"},
                instances=0,
                max_instances=0,
                name="name",
                scheduling_policy="default",
            )

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.containers.applications.create(
            account_id="account-123",
            durable_objects={"namespace_id": "14758f1afd44c09b7992073ccf00b43d"},
            name="name",
            scheduling_policy="durable_object",
        )
        assert_matches_type(ApplicationCreateResponse, application, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.containers.applications.create(
            account_id="account-123",
            durable_objects={"namespace_id": "14758f1afd44c09b7992073ccf00b43d"},
            name="name",
            scheduling_policy="durable_object",
            configuration={
                "authorized_keys": [
                    {
                        "public_key": "public_key",
                        "name": "name",
                    }
                ],
                "wrangler_ssh": {
                    "enabled": True,
                    "port": 1,
                },
            },
            observability={"logs": {"enabled": True}},
        )
        assert_matches_type(ApplicationCreateResponse, application, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.containers.applications.with_raw_response.create(
            account_id="account-123",
            durable_objects={"namespace_id": "14758f1afd44c09b7992073ccf00b43d"},
            name="name",
            scheduling_policy="durable_object",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(ApplicationCreateResponse, application, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.containers.applications.with_streaming_response.create(
            account_id="account-123",
            durable_objects={"namespace_id": "14758f1afd44c09b7992073ccf00b43d"},
            name="name",
            scheduling_policy="durable_object",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(ApplicationCreateResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.containers.applications.with_raw_response.create(
                account_id="",
                durable_objects={"namespace_id": "14758f1afd44c09b7992073ccf00b43d"},
                name="name",
                scheduling_policy="durable_object",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.containers.applications.list(
            account_id="account-123",
        )
        assert_matches_type(AsyncPageTokenPagination[ApplicationListResponse], application, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.containers.applications.list(
            account_id="account-123",
            image="image",
            name="name",
            page_token="page_token",
            per_page=1,
        )
        assert_matches_type(AsyncPageTokenPagination[ApplicationListResponse], application, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.containers.applications.with_raw_response.list(
            account_id="account-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(AsyncPageTokenPagination[ApplicationListResponse], application, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.containers.applications.with_streaming_response.list(
            account_id="account-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(AsyncPageTokenPagination[ApplicationListResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.containers.applications.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.containers.applications.delete(
            application_id="application_id",
            account_id="account-123",
        )
        assert_matches_type(ApplicationDeleteResponse, application, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.containers.applications.with_raw_response.delete(
            application_id="application_id",
            account_id="account-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(ApplicationDeleteResponse, application, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.containers.applications.with_streaming_response.delete(
            application_id="application_id",
            account_id="account-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(ApplicationDeleteResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.containers.applications.with_raw_response.delete(
                application_id="application_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.containers.applications.with_raw_response.delete(
                application_id="",
                account_id="account-123",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.containers.applications.edit(
            application_id="application_id",
            account_id="account-123",
        )
        assert_matches_type(ApplicationEditResponse, application, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.containers.applications.edit(
            application_id="application_id",
            account_id="account-123",
            configuration={
                "authorized_keys": [
                    {
                        "public_key": "public_key",
                        "name": "name",
                    }
                ],
                "wrangler_ssh": {
                    "enabled": True,
                    "port": 1,
                },
            },
            constraints={
                "jurisdiction": "jurisdiction",
                "regions": ["WNAM"],
            },
            max_instances=0,
            observability={"logs": {"enabled": True}},
            rollout_active_grace_period=0,
        )
        assert_matches_type(ApplicationEditResponse, application, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.containers.applications.with_raw_response.edit(
            application_id="application_id",
            account_id="account-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(ApplicationEditResponse, application, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.containers.applications.with_streaming_response.edit(
            application_id="application_id",
            account_id="account-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(ApplicationEditResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.containers.applications.with_raw_response.edit(
                application_id="application_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.containers.applications.with_raw_response.edit(
                application_id="",
                account_id="account-123",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.containers.applications.get(
            application_id="application_id",
            account_id="account-123",
        )
        assert_matches_type(ApplicationGetResponse, application, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.containers.applications.with_raw_response.get(
            application_id="application_id",
            account_id="account-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(ApplicationGetResponse, application, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.containers.applications.with_streaming_response.get(
            application_id="application_id",
            account_id="account-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(ApplicationGetResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.containers.applications.with_raw_response.get(
                application_id="application_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.containers.applications.with_raw_response.get(
                application_id="",
                account_id="account-123",
            )
