# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.iam import (
    ResourceGroupGetResponse,
    ResourceGroupListResponse,
    ResourceGroupCreateResponse,
    ResourceGroupDeleteResponse,
    ResourceGroupUpdateResponse,
)
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResourceGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        resource_group = client.iam.resource_groups.create(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            scope={
                "key": "com.cloudflare.api.account.eb78d65290b24279ba6f44721b3ea3c4",
                "objects": [{"key": "com.cloudflare.api.account.zone.23f8d65290b24279ba6f44721b3eaad5"}],
            },
        )
        assert_matches_type(ResourceGroupCreateResponse, resource_group, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        resource_group = client.iam.resource_groups.create(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            scope={
                "key": "com.cloudflare.api.account.eb78d65290b24279ba6f44721b3ea3c4",
                "objects": [{"key": "com.cloudflare.api.account.zone.23f8d65290b24279ba6f44721b3eaad5"}],
            },
            meta={"editable": "false"},
        )
        assert_matches_type(ResourceGroupCreateResponse, resource_group, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.iam.resource_groups.with_raw_response.create(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            scope={
                "key": "com.cloudflare.api.account.eb78d65290b24279ba6f44721b3ea3c4",
                "objects": [{"key": "com.cloudflare.api.account.zone.23f8d65290b24279ba6f44721b3eaad5"}],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_group = response.parse()
        assert_matches_type(ResourceGroupCreateResponse, resource_group, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.iam.resource_groups.with_streaming_response.create(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            scope={
                "key": "com.cloudflare.api.account.eb78d65290b24279ba6f44721b3ea3c4",
                "objects": [{"key": "com.cloudflare.api.account.zone.23f8d65290b24279ba6f44721b3eaad5"}],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_group = response.parse()
            assert_matches_type(ResourceGroupCreateResponse, resource_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.iam.resource_groups.with_raw_response.create(
                account_id="",
                scope={
                    "key": "com.cloudflare.api.account.eb78d65290b24279ba6f44721b3ea3c4",
                    "objects": [{"key": "com.cloudflare.api.account.zone.23f8d65290b24279ba6f44721b3eaad5"}],
                },
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        resource_group = client.iam.resource_groups.update(
            resource_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            scope={
                "key": "com.cloudflare.api.account.eb78d65290b24279ba6f44721b3ea3c4",
                "objects": [{"key": "com.cloudflare.api.account.zone.23f8d65290b24279ba6f44721b3eaad5"}],
            },
        )
        assert_matches_type(ResourceGroupUpdateResponse, resource_group, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        resource_group = client.iam.resource_groups.update(
            resource_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            scope={
                "key": "com.cloudflare.api.account.eb78d65290b24279ba6f44721b3ea3c4",
                "objects": [{"key": "com.cloudflare.api.account.zone.23f8d65290b24279ba6f44721b3eaad5"}],
            },
            meta={"editable": "false"},
        )
        assert_matches_type(ResourceGroupUpdateResponse, resource_group, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.iam.resource_groups.with_raw_response.update(
            resource_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            scope={
                "key": "com.cloudflare.api.account.eb78d65290b24279ba6f44721b3ea3c4",
                "objects": [{"key": "com.cloudflare.api.account.zone.23f8d65290b24279ba6f44721b3eaad5"}],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_group = response.parse()
        assert_matches_type(ResourceGroupUpdateResponse, resource_group, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.iam.resource_groups.with_streaming_response.update(
            resource_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            scope={
                "key": "com.cloudflare.api.account.eb78d65290b24279ba6f44721b3ea3c4",
                "objects": [{"key": "com.cloudflare.api.account.zone.23f8d65290b24279ba6f44721b3eaad5"}],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_group = response.parse()
            assert_matches_type(ResourceGroupUpdateResponse, resource_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.iam.resource_groups.with_raw_response.update(
                resource_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
                account_id="",
                scope={
                    "key": "com.cloudflare.api.account.eb78d65290b24279ba6f44721b3ea3c4",
                    "objects": [{"key": "com.cloudflare.api.account.zone.23f8d65290b24279ba6f44721b3eaad5"}],
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource_group_id` but received ''"):
            client.iam.resource_groups.with_raw_response.update(
                resource_group_id="",
                account_id="eb78d65290b24279ba6f44721b3ea3c4",
                scope={
                    "key": "com.cloudflare.api.account.eb78d65290b24279ba6f44721b3ea3c4",
                    "objects": [{"key": "com.cloudflare.api.account.zone.23f8d65290b24279ba6f44721b3eaad5"}],
                },
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        resource_group = client.iam.resource_groups.list(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )
        assert_matches_type(SyncV4PagePaginationArray[ResourceGroupListResponse], resource_group, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        resource_group = client.iam.resource_groups.list(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
            name="NameOfTheResourceGroup",
            page=1,
            per_page=5,
        )
        assert_matches_type(SyncV4PagePaginationArray[ResourceGroupListResponse], resource_group, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.iam.resource_groups.with_raw_response.list(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_group = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[ResourceGroupListResponse], resource_group, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.iam.resource_groups.with_streaming_response.list(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_group = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[ResourceGroupListResponse], resource_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.iam.resource_groups.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        resource_group = client.iam.resource_groups.delete(
            resource_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )
        assert_matches_type(Optional[ResourceGroupDeleteResponse], resource_group, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.iam.resource_groups.with_raw_response.delete(
            resource_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_group = response.parse()
        assert_matches_type(Optional[ResourceGroupDeleteResponse], resource_group, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.iam.resource_groups.with_streaming_response.delete(
            resource_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_group = response.parse()
            assert_matches_type(Optional[ResourceGroupDeleteResponse], resource_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.iam.resource_groups.with_raw_response.delete(
                resource_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource_group_id` but received ''"):
            client.iam.resource_groups.with_raw_response.delete(
                resource_group_id="",
                account_id="eb78d65290b24279ba6f44721b3ea3c4",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        resource_group = client.iam.resource_groups.get(
            resource_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )
        assert_matches_type(ResourceGroupGetResponse, resource_group, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.iam.resource_groups.with_raw_response.get(
            resource_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_group = response.parse()
        assert_matches_type(ResourceGroupGetResponse, resource_group, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.iam.resource_groups.with_streaming_response.get(
            resource_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_group = response.parse()
            assert_matches_type(ResourceGroupGetResponse, resource_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.iam.resource_groups.with_raw_response.get(
                resource_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource_group_id` but received ''"):
            client.iam.resource_groups.with_raw_response.get(
                resource_group_id="",
                account_id="eb78d65290b24279ba6f44721b3ea3c4",
            )


class TestAsyncResourceGroups:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        resource_group = await async_client.iam.resource_groups.create(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            scope={
                "key": "com.cloudflare.api.account.eb78d65290b24279ba6f44721b3ea3c4",
                "objects": [{"key": "com.cloudflare.api.account.zone.23f8d65290b24279ba6f44721b3eaad5"}],
            },
        )
        assert_matches_type(ResourceGroupCreateResponse, resource_group, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        resource_group = await async_client.iam.resource_groups.create(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            scope={
                "key": "com.cloudflare.api.account.eb78d65290b24279ba6f44721b3ea3c4",
                "objects": [{"key": "com.cloudflare.api.account.zone.23f8d65290b24279ba6f44721b3eaad5"}],
            },
            meta={"editable": "false"},
        )
        assert_matches_type(ResourceGroupCreateResponse, resource_group, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.iam.resource_groups.with_raw_response.create(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            scope={
                "key": "com.cloudflare.api.account.eb78d65290b24279ba6f44721b3ea3c4",
                "objects": [{"key": "com.cloudflare.api.account.zone.23f8d65290b24279ba6f44721b3eaad5"}],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_group = await response.parse()
        assert_matches_type(ResourceGroupCreateResponse, resource_group, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.iam.resource_groups.with_streaming_response.create(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            scope={
                "key": "com.cloudflare.api.account.eb78d65290b24279ba6f44721b3ea3c4",
                "objects": [{"key": "com.cloudflare.api.account.zone.23f8d65290b24279ba6f44721b3eaad5"}],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_group = await response.parse()
            assert_matches_type(ResourceGroupCreateResponse, resource_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.iam.resource_groups.with_raw_response.create(
                account_id="",
                scope={
                    "key": "com.cloudflare.api.account.eb78d65290b24279ba6f44721b3ea3c4",
                    "objects": [{"key": "com.cloudflare.api.account.zone.23f8d65290b24279ba6f44721b3eaad5"}],
                },
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        resource_group = await async_client.iam.resource_groups.update(
            resource_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            scope={
                "key": "com.cloudflare.api.account.eb78d65290b24279ba6f44721b3ea3c4",
                "objects": [{"key": "com.cloudflare.api.account.zone.23f8d65290b24279ba6f44721b3eaad5"}],
            },
        )
        assert_matches_type(ResourceGroupUpdateResponse, resource_group, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        resource_group = await async_client.iam.resource_groups.update(
            resource_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            scope={
                "key": "com.cloudflare.api.account.eb78d65290b24279ba6f44721b3ea3c4",
                "objects": [{"key": "com.cloudflare.api.account.zone.23f8d65290b24279ba6f44721b3eaad5"}],
            },
            meta={"editable": "false"},
        )
        assert_matches_type(ResourceGroupUpdateResponse, resource_group, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.iam.resource_groups.with_raw_response.update(
            resource_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            scope={
                "key": "com.cloudflare.api.account.eb78d65290b24279ba6f44721b3ea3c4",
                "objects": [{"key": "com.cloudflare.api.account.zone.23f8d65290b24279ba6f44721b3eaad5"}],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_group = await response.parse()
        assert_matches_type(ResourceGroupUpdateResponse, resource_group, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.iam.resource_groups.with_streaming_response.update(
            resource_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            scope={
                "key": "com.cloudflare.api.account.eb78d65290b24279ba6f44721b3ea3c4",
                "objects": [{"key": "com.cloudflare.api.account.zone.23f8d65290b24279ba6f44721b3eaad5"}],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_group = await response.parse()
            assert_matches_type(ResourceGroupUpdateResponse, resource_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.iam.resource_groups.with_raw_response.update(
                resource_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
                account_id="",
                scope={
                    "key": "com.cloudflare.api.account.eb78d65290b24279ba6f44721b3ea3c4",
                    "objects": [{"key": "com.cloudflare.api.account.zone.23f8d65290b24279ba6f44721b3eaad5"}],
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource_group_id` but received ''"):
            await async_client.iam.resource_groups.with_raw_response.update(
                resource_group_id="",
                account_id="eb78d65290b24279ba6f44721b3ea3c4",
                scope={
                    "key": "com.cloudflare.api.account.eb78d65290b24279ba6f44721b3ea3c4",
                    "objects": [{"key": "com.cloudflare.api.account.zone.23f8d65290b24279ba6f44721b3eaad5"}],
                },
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        resource_group = await async_client.iam.resource_groups.list(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )
        assert_matches_type(AsyncV4PagePaginationArray[ResourceGroupListResponse], resource_group, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        resource_group = await async_client.iam.resource_groups.list(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
            name="NameOfTheResourceGroup",
            page=1,
            per_page=5,
        )
        assert_matches_type(AsyncV4PagePaginationArray[ResourceGroupListResponse], resource_group, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.iam.resource_groups.with_raw_response.list(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_group = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[ResourceGroupListResponse], resource_group, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.iam.resource_groups.with_streaming_response.list(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_group = await response.parse()
            assert_matches_type(
                AsyncV4PagePaginationArray[ResourceGroupListResponse], resource_group, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.iam.resource_groups.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        resource_group = await async_client.iam.resource_groups.delete(
            resource_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )
        assert_matches_type(Optional[ResourceGroupDeleteResponse], resource_group, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.iam.resource_groups.with_raw_response.delete(
            resource_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_group = await response.parse()
        assert_matches_type(Optional[ResourceGroupDeleteResponse], resource_group, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.iam.resource_groups.with_streaming_response.delete(
            resource_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_group = await response.parse()
            assert_matches_type(Optional[ResourceGroupDeleteResponse], resource_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.iam.resource_groups.with_raw_response.delete(
                resource_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource_group_id` but received ''"):
            await async_client.iam.resource_groups.with_raw_response.delete(
                resource_group_id="",
                account_id="eb78d65290b24279ba6f44721b3ea3c4",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        resource_group = await async_client.iam.resource_groups.get(
            resource_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )
        assert_matches_type(ResourceGroupGetResponse, resource_group, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.iam.resource_groups.with_raw_response.get(
            resource_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_group = await response.parse()
        assert_matches_type(ResourceGroupGetResponse, resource_group, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.iam.resource_groups.with_streaming_response.get(
            resource_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_group = await response.parse()
            assert_matches_type(ResourceGroupGetResponse, resource_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.iam.resource_groups.with_raw_response.get(
                resource_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource_group_id` but received ''"):
            await async_client.iam.resource_groups.with_raw_response.get(
                resource_group_id="",
                account_id="eb78d65290b24279ba6f44721b3ea3c4",
            )
