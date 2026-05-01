# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.zero_trust.devices import (
    DeploymentGroup,
    DeploymentGroupDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeploymentGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        deployment_group = client.zero_trust.devices.deployment_groups.create(
            account_id="account_id",
            name="Engineering Ring 0",
            version_config=[
                {
                    "target_environment": "windows",
                    "version": "2026.5.234.0",
                }
            ],
        )
        assert_matches_type(DeploymentGroup, deployment_group, path=["response"])

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        deployment_group = client.zero_trust.devices.deployment_groups.create(
            account_id="account_id",
            name="Engineering Ring 0",
            version_config=[
                {
                    "target_environment": "windows",
                    "version": "2026.5.234.0",
                }
            ],
            policy_ids=["string"],
        )
        assert_matches_type(DeploymentGroup, deployment_group, path=["response"])

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.deployment_groups.with_raw_response.create(
            account_id="account_id",
            name="Engineering Ring 0",
            version_config=[
                {
                    "target_environment": "windows",
                    "version": "2026.5.234.0",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment_group = response.parse()
        assert_matches_type(DeploymentGroup, deployment_group, path=["response"])

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.deployment_groups.with_streaming_response.create(
            account_id="account_id",
            name="Engineering Ring 0",
            version_config=[
                {
                    "target_environment": "windows",
                    "version": "2026.5.234.0",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment_group = response.parse()
            assert_matches_type(DeploymentGroup, deployment_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.deployment_groups.with_raw_response.create(
                account_id="",
                name="Engineering Ring 0",
                version_config=[
                    {
                        "target_environment": "windows",
                        "version": "2026.5.234.0",
                    }
                ],
            )

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        deployment_group = client.zero_trust.devices.deployment_groups.list(
            account_id="account_id",
        )
        assert_matches_type(SyncV4PagePaginationArray[DeploymentGroup], deployment_group, path=["response"])

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        deployment_group = client.zero_trust.devices.deployment_groups.list(
            account_id="account_id",
            page=1,
            per_page=1,
        )
        assert_matches_type(SyncV4PagePaginationArray[DeploymentGroup], deployment_group, path=["response"])

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.deployment_groups.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment_group = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[DeploymentGroup], deployment_group, path=["response"])

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.deployment_groups.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment_group = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[DeploymentGroup], deployment_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.deployment_groups.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        deployment_group = client.zero_trust.devices.deployment_groups.delete(
            group_id="group_id",
            account_id="account_id",
        )
        assert_matches_type(DeploymentGroupDeleteResponse, deployment_group, path=["response"])

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.deployment_groups.with_raw_response.delete(
            group_id="group_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment_group = response.parse()
        assert_matches_type(DeploymentGroupDeleteResponse, deployment_group, path=["response"])

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.deployment_groups.with_streaming_response.delete(
            group_id="group_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment_group = response.parse()
            assert_matches_type(DeploymentGroupDeleteResponse, deployment_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.deployment_groups.with_raw_response.delete(
                group_id="group_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.zero_trust.devices.deployment_groups.with_raw_response.delete(
                group_id="",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        deployment_group = client.zero_trust.devices.deployment_groups.edit(
            group_id="group_id",
            account_id="account_id",
        )
        assert_matches_type(DeploymentGroup, deployment_group, path=["response"])

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        deployment_group = client.zero_trust.devices.deployment_groups.edit(
            group_id="group_id",
            account_id="account_id",
            name="Engineering Ring 0",
            policy_ids=["string"],
            version_config=[
                {
                    "target_environment": "windows",
                    "version": "2026.5.234.0",
                }
            ],
        )
        assert_matches_type(DeploymentGroup, deployment_group, path=["response"])

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.deployment_groups.with_raw_response.edit(
            group_id="group_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment_group = response.parse()
        assert_matches_type(DeploymentGroup, deployment_group, path=["response"])

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.deployment_groups.with_streaming_response.edit(
            group_id="group_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment_group = response.parse()
            assert_matches_type(DeploymentGroup, deployment_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.deployment_groups.with_raw_response.edit(
                group_id="group_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.zero_trust.devices.deployment_groups.with_raw_response.edit(
                group_id="",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        deployment_group = client.zero_trust.devices.deployment_groups.get(
            group_id="group_id",
            account_id="account_id",
        )
        assert_matches_type(DeploymentGroup, deployment_group, path=["response"])

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.deployment_groups.with_raw_response.get(
            group_id="group_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment_group = response.parse()
        assert_matches_type(DeploymentGroup, deployment_group, path=["response"])

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.deployment_groups.with_streaming_response.get(
            group_id="group_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment_group = response.parse()
            assert_matches_type(DeploymentGroup, deployment_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.deployment_groups.with_raw_response.get(
                group_id="group_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.zero_trust.devices.deployment_groups.with_raw_response.get(
                group_id="",
                account_id="account_id",
            )


class TestAsyncDeploymentGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        deployment_group = await async_client.zero_trust.devices.deployment_groups.create(
            account_id="account_id",
            name="Engineering Ring 0",
            version_config=[
                {
                    "target_environment": "windows",
                    "version": "2026.5.234.0",
                }
            ],
        )
        assert_matches_type(DeploymentGroup, deployment_group, path=["response"])

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        deployment_group = await async_client.zero_trust.devices.deployment_groups.create(
            account_id="account_id",
            name="Engineering Ring 0",
            version_config=[
                {
                    "target_environment": "windows",
                    "version": "2026.5.234.0",
                }
            ],
            policy_ids=["string"],
        )
        assert_matches_type(DeploymentGroup, deployment_group, path=["response"])

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.deployment_groups.with_raw_response.create(
            account_id="account_id",
            name="Engineering Ring 0",
            version_config=[
                {
                    "target_environment": "windows",
                    "version": "2026.5.234.0",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment_group = await response.parse()
        assert_matches_type(DeploymentGroup, deployment_group, path=["response"])

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.deployment_groups.with_streaming_response.create(
            account_id="account_id",
            name="Engineering Ring 0",
            version_config=[
                {
                    "target_environment": "windows",
                    "version": "2026.5.234.0",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment_group = await response.parse()
            assert_matches_type(DeploymentGroup, deployment_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.deployment_groups.with_raw_response.create(
                account_id="",
                name="Engineering Ring 0",
                version_config=[
                    {
                        "target_environment": "windows",
                        "version": "2026.5.234.0",
                    }
                ],
            )

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        deployment_group = await async_client.zero_trust.devices.deployment_groups.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncV4PagePaginationArray[DeploymentGroup], deployment_group, path=["response"])

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        deployment_group = await async_client.zero_trust.devices.deployment_groups.list(
            account_id="account_id",
            page=1,
            per_page=1,
        )
        assert_matches_type(AsyncV4PagePaginationArray[DeploymentGroup], deployment_group, path=["response"])

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.deployment_groups.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment_group = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[DeploymentGroup], deployment_group, path=["response"])

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.deployment_groups.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment_group = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[DeploymentGroup], deployment_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.deployment_groups.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        deployment_group = await async_client.zero_trust.devices.deployment_groups.delete(
            group_id="group_id",
            account_id="account_id",
        )
        assert_matches_type(DeploymentGroupDeleteResponse, deployment_group, path=["response"])

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.deployment_groups.with_raw_response.delete(
            group_id="group_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment_group = await response.parse()
        assert_matches_type(DeploymentGroupDeleteResponse, deployment_group, path=["response"])

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.deployment_groups.with_streaming_response.delete(
            group_id="group_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment_group = await response.parse()
            assert_matches_type(DeploymentGroupDeleteResponse, deployment_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.deployment_groups.with_raw_response.delete(
                group_id="group_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.zero_trust.devices.deployment_groups.with_raw_response.delete(
                group_id="",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        deployment_group = await async_client.zero_trust.devices.deployment_groups.edit(
            group_id="group_id",
            account_id="account_id",
        )
        assert_matches_type(DeploymentGroup, deployment_group, path=["response"])

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        deployment_group = await async_client.zero_trust.devices.deployment_groups.edit(
            group_id="group_id",
            account_id="account_id",
            name="Engineering Ring 0",
            policy_ids=["string"],
            version_config=[
                {
                    "target_environment": "windows",
                    "version": "2026.5.234.0",
                }
            ],
        )
        assert_matches_type(DeploymentGroup, deployment_group, path=["response"])

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.deployment_groups.with_raw_response.edit(
            group_id="group_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment_group = await response.parse()
        assert_matches_type(DeploymentGroup, deployment_group, path=["response"])

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.deployment_groups.with_streaming_response.edit(
            group_id="group_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment_group = await response.parse()
            assert_matches_type(DeploymentGroup, deployment_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.deployment_groups.with_raw_response.edit(
                group_id="group_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.zero_trust.devices.deployment_groups.with_raw_response.edit(
                group_id="",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        deployment_group = await async_client.zero_trust.devices.deployment_groups.get(
            group_id="group_id",
            account_id="account_id",
        )
        assert_matches_type(DeploymentGroup, deployment_group, path=["response"])

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.deployment_groups.with_raw_response.get(
            group_id="group_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment_group = await response.parse()
        assert_matches_type(DeploymentGroup, deployment_group, path=["response"])

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.deployment_groups.with_streaming_response.get(
            group_id="group_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment_group = await response.parse()
            assert_matches_type(DeploymentGroup, deployment_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 401 error from prism")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.deployment_groups.with_raw_response.get(
                group_id="group_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.zero_trust.devices.deployment_groups.with_raw_response.get(
                group_id="",
                account_id="account_id",
            )
