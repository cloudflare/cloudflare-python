# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import (
    SyncPageTokenPagination,
    AsyncPageTokenPagination,
    SyncContainersInstancesV1Pagination,
    AsyncContainersInstancesV1Pagination,
)
from cloudflare.types.containers.applications import (
    InstanceGetResponse,
    InstanceListResponse,
    InstanceListV1Response,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInstances:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        instance = client.containers.applications.instances.list(
            application_id="application_id",
            account_id="account-123",
        )
        assert_matches_type(SyncPageTokenPagination[InstanceListResponse], instance, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        instance = client.containers.applications.instances.list(
            application_id="application_id",
            account_id="account-123",
            name_prefix="name_prefix",
            page_token="page_token",
            per_page=1,
            state="active",
        )
        assert_matches_type(SyncPageTokenPagination[InstanceListResponse], instance, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.containers.applications.instances.with_raw_response.list(
            application_id="application_id",
            account_id="account-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(SyncPageTokenPagination[InstanceListResponse], instance, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.containers.applications.instances.with_streaming_response.list(
            application_id="application_id",
            account_id="account-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(SyncPageTokenPagination[InstanceListResponse], instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.containers.applications.instances.with_raw_response.list(
                application_id="application_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.containers.applications.instances.with_raw_response.list(
                application_id="",
                account_id="account-123",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        instance = client.containers.applications.instances.get(
            instance_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            account_id="account-123",
            application_id="application_id",
        )
        assert_matches_type(InstanceGetResponse, instance, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.containers.applications.instances.with_raw_response.get(
            instance_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            account_id="account-123",
            application_id="application_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceGetResponse, instance, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.containers.applications.instances.with_streaming_response.get(
            instance_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            account_id="account-123",
            application_id="application_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceGetResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.containers.applications.instances.with_raw_response.get(
                instance_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                account_id="",
                application_id="application_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.containers.applications.instances.with_raw_response.get(
                instance_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                account_id="account-123",
                application_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.containers.applications.instances.with_raw_response.get(
                instance_id="",
                account_id="account-123",
                application_id="application_id",
            )

    @parametrize
    def test_method_list_v1(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            instance = client.containers.applications.instances.list_v1(
                application_id="application_id",
                account_id="account-123",
            )

        assert_matches_type(SyncContainersInstancesV1Pagination[InstanceListV1Response], instance, path=["response"])

    @parametrize
    def test_method_list_v1_with_all_params(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            instance = client.containers.applications.instances.list_v1(
                application_id="application_id",
                account_id="account-123",
                name_prefix="name_prefix",
                page_token="page_token",
                per_page=1,
                state="active",
            )

        assert_matches_type(SyncContainersInstancesV1Pagination[InstanceListV1Response], instance, path=["response"])

    @parametrize
    def test_raw_response_list_v1(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.containers.applications.instances.with_raw_response.list_v1(
                application_id="application_id",
                account_id="account-123",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(SyncContainersInstancesV1Pagination[InstanceListV1Response], instance, path=["response"])

    @parametrize
    def test_streaming_response_list_v1(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.containers.applications.instances.with_streaming_response.list_v1(
                application_id="application_id",
                account_id="account-123",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                instance = response.parse()
                assert_matches_type(
                    SyncContainersInstancesV1Pagination[InstanceListV1Response], instance, path=["response"]
                )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_v1(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
                client.containers.applications.instances.with_raw_response.list_v1(
                    application_id="application_id",
                    account_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
                client.containers.applications.instances.with_raw_response.list_v1(
                    application_id="",
                    account_id="account-123",
                )


class TestAsyncInstances:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        instance = await async_client.containers.applications.instances.list(
            application_id="application_id",
            account_id="account-123",
        )
        assert_matches_type(AsyncPageTokenPagination[InstanceListResponse], instance, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        instance = await async_client.containers.applications.instances.list(
            application_id="application_id",
            account_id="account-123",
            name_prefix="name_prefix",
            page_token="page_token",
            per_page=1,
            state="active",
        )
        assert_matches_type(AsyncPageTokenPagination[InstanceListResponse], instance, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.containers.applications.instances.with_raw_response.list(
            application_id="application_id",
            account_id="account-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(AsyncPageTokenPagination[InstanceListResponse], instance, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.containers.applications.instances.with_streaming_response.list(
            application_id="application_id",
            account_id="account-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(AsyncPageTokenPagination[InstanceListResponse], instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.containers.applications.instances.with_raw_response.list(
                application_id="application_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.containers.applications.instances.with_raw_response.list(
                application_id="",
                account_id="account-123",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        instance = await async_client.containers.applications.instances.get(
            instance_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            account_id="account-123",
            application_id="application_id",
        )
        assert_matches_type(InstanceGetResponse, instance, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.containers.applications.instances.with_raw_response.get(
            instance_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            account_id="account-123",
            application_id="application_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceGetResponse, instance, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.containers.applications.instances.with_streaming_response.get(
            instance_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            account_id="account-123",
            application_id="application_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceGetResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.containers.applications.instances.with_raw_response.get(
                instance_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                account_id="",
                application_id="application_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.containers.applications.instances.with_raw_response.get(
                instance_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                account_id="account-123",
                application_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.containers.applications.instances.with_raw_response.get(
                instance_id="",
                account_id="account-123",
                application_id="application_id",
            )

    @parametrize
    async def test_method_list_v1(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            instance = await async_client.containers.applications.instances.list_v1(
                application_id="application_id",
                account_id="account-123",
            )

        assert_matches_type(AsyncContainersInstancesV1Pagination[InstanceListV1Response], instance, path=["response"])

    @parametrize
    async def test_method_list_v1_with_all_params(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            instance = await async_client.containers.applications.instances.list_v1(
                application_id="application_id",
                account_id="account-123",
                name_prefix="name_prefix",
                page_token="page_token",
                per_page=1,
                state="active",
            )

        assert_matches_type(AsyncContainersInstancesV1Pagination[InstanceListV1Response], instance, path=["response"])

    @parametrize
    async def test_raw_response_list_v1(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.containers.applications.instances.with_raw_response.list_v1(
                application_id="application_id",
                account_id="account-123",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(AsyncContainersInstancesV1Pagination[InstanceListV1Response], instance, path=["response"])

    @parametrize
    async def test_streaming_response_list_v1(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.containers.applications.instances.with_streaming_response.list_v1(
                application_id="application_id",
                account_id="account-123",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                instance = await response.parse()
                assert_matches_type(
                    AsyncContainersInstancesV1Pagination[InstanceListV1Response], instance, path=["response"]
                )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_v1(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
                await async_client.containers.applications.instances.with_raw_response.list_v1(
                    application_id="application_id",
                    account_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
                await async_client.containers.applications.instances.with_raw_response.list_v1(
                    application_id="",
                    account_id="account-123",
                )
