# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncCursorPagination, AsyncCursorPagination
from cloudflare.types.zero_trust.cws import (
    PolicySet,
    PolicySetDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolicySets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        policy_set = client.zero_trust.cws.policy_sets.create(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            policies=[{"policy_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )
        assert_matches_type(PolicySet, policy_set, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        policy_set = client.zero_trust.cws.policy_sets.create(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            policies=[
                {
                    "policy_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "enforce": True,
                }
            ],
            description="description",
            exclude_workload_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            include_workload_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            tags={"foo": "string"},
        )
        assert_matches_type(PolicySet, policy_set, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.cws.policy_sets.with_raw_response.create(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            policies=[{"policy_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_set = response.parse()
        assert_matches_type(PolicySet, policy_set, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.cws.policy_sets.with_streaming_response.create(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            policies=[{"policy_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_set = response.parse()
            assert_matches_type(PolicySet, policy_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.cws.policy_sets.with_raw_response.create(
                account_id="",
                name="x",
                policies=[{"policy_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        policy_set = client.zero_trust.cws.policy_sets.update(
            policy_set_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            policies=[{"policy_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )
        assert_matches_type(PolicySet, policy_set, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        policy_set = client.zero_trust.cws.policy_sets.update(
            policy_set_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            policies=[
                {
                    "policy_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "enforce": True,
                }
            ],
            description="description",
            exclude_workload_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            include_workload_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            tags={"foo": "string"},
        )
        assert_matches_type(PolicySet, policy_set, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.cws.policy_sets.with_raw_response.update(
            policy_set_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            policies=[{"policy_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_set = response.parse()
        assert_matches_type(PolicySet, policy_set, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.cws.policy_sets.with_streaming_response.update(
            policy_set_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            policies=[{"policy_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_set = response.parse()
            assert_matches_type(PolicySet, policy_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.cws.policy_sets.with_raw_response.update(
                policy_set_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                name="x",
                policies=[{"policy_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_set_id` but received ''"):
            client.zero_trust.cws.policy_sets.with_raw_response.update(
                policy_set_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                name="x",
                policies=[{"policy_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        policy_set = client.zero_trust.cws.policy_sets.list(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(SyncCursorPagination[PolicySet], policy_set, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        policy_set = client.zero_trust.cws.policy_sets.list(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            cursor="cursor",
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="asc",
            name="name",
            order="name",
            per_page=1,
        )
        assert_matches_type(SyncCursorPagination[PolicySet], policy_set, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.cws.policy_sets.with_raw_response.list(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_set = response.parse()
        assert_matches_type(SyncCursorPagination[PolicySet], policy_set, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.cws.policy_sets.with_streaming_response.list(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_set = response.parse()
            assert_matches_type(SyncCursorPagination[PolicySet], policy_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.cws.policy_sets.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        policy_set = client.zero_trust.cws.policy_sets.delete(
            policy_set_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(PolicySetDeleteResponse, policy_set, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.cws.policy_sets.with_raw_response.delete(
            policy_set_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_set = response.parse()
        assert_matches_type(PolicySetDeleteResponse, policy_set, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.cws.policy_sets.with_streaming_response.delete(
            policy_set_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_set = response.parse()
            assert_matches_type(PolicySetDeleteResponse, policy_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.cws.policy_sets.with_raw_response.delete(
                policy_set_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_set_id` but received ''"):
            client.zero_trust.cws.policy_sets.with_raw_response.delete(
                policy_set_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        policy_set = client.zero_trust.cws.policy_sets.get(
            policy_set_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(PolicySet, policy_set, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.cws.policy_sets.with_raw_response.get(
            policy_set_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_set = response.parse()
        assert_matches_type(PolicySet, policy_set, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.cws.policy_sets.with_streaming_response.get(
            policy_set_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_set = response.parse()
            assert_matches_type(PolicySet, policy_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.cws.policy_sets.with_raw_response.get(
                policy_set_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_set_id` but received ''"):
            client.zero_trust.cws.policy_sets.with_raw_response.get(
                policy_set_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            )


class TestAsyncPolicySets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        policy_set = await async_client.zero_trust.cws.policy_sets.create(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            policies=[{"policy_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )
        assert_matches_type(PolicySet, policy_set, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        policy_set = await async_client.zero_trust.cws.policy_sets.create(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            policies=[
                {
                    "policy_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "enforce": True,
                }
            ],
            description="description",
            exclude_workload_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            include_workload_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            tags={"foo": "string"},
        )
        assert_matches_type(PolicySet, policy_set, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.cws.policy_sets.with_raw_response.create(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            policies=[{"policy_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_set = await response.parse()
        assert_matches_type(PolicySet, policy_set, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.cws.policy_sets.with_streaming_response.create(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            policies=[{"policy_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_set = await response.parse()
            assert_matches_type(PolicySet, policy_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.cws.policy_sets.with_raw_response.create(
                account_id="",
                name="x",
                policies=[{"policy_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        policy_set = await async_client.zero_trust.cws.policy_sets.update(
            policy_set_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            policies=[{"policy_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )
        assert_matches_type(PolicySet, policy_set, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        policy_set = await async_client.zero_trust.cws.policy_sets.update(
            policy_set_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            policies=[
                {
                    "policy_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "enforce": True,
                }
            ],
            description="description",
            exclude_workload_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            include_workload_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            tags={"foo": "string"},
        )
        assert_matches_type(PolicySet, policy_set, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.cws.policy_sets.with_raw_response.update(
            policy_set_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            policies=[{"policy_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_set = await response.parse()
        assert_matches_type(PolicySet, policy_set, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.cws.policy_sets.with_streaming_response.update(
            policy_set_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            policies=[{"policy_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_set = await response.parse()
            assert_matches_type(PolicySet, policy_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.cws.policy_sets.with_raw_response.update(
                policy_set_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                name="x",
                policies=[{"policy_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_set_id` but received ''"):
            await async_client.zero_trust.cws.policy_sets.with_raw_response.update(
                policy_set_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                name="x",
                policies=[{"policy_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        policy_set = await async_client.zero_trust.cws.policy_sets.list(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(AsyncCursorPagination[PolicySet], policy_set, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        policy_set = await async_client.zero_trust.cws.policy_sets.list(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            cursor="cursor",
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="asc",
            name="name",
            order="name",
            per_page=1,
        )
        assert_matches_type(AsyncCursorPagination[PolicySet], policy_set, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.cws.policy_sets.with_raw_response.list(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_set = await response.parse()
        assert_matches_type(AsyncCursorPagination[PolicySet], policy_set, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.cws.policy_sets.with_streaming_response.list(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_set = await response.parse()
            assert_matches_type(AsyncCursorPagination[PolicySet], policy_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.cws.policy_sets.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        policy_set = await async_client.zero_trust.cws.policy_sets.delete(
            policy_set_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(PolicySetDeleteResponse, policy_set, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.cws.policy_sets.with_raw_response.delete(
            policy_set_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_set = await response.parse()
        assert_matches_type(PolicySetDeleteResponse, policy_set, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.cws.policy_sets.with_streaming_response.delete(
            policy_set_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_set = await response.parse()
            assert_matches_type(PolicySetDeleteResponse, policy_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.cws.policy_sets.with_raw_response.delete(
                policy_set_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_set_id` but received ''"):
            await async_client.zero_trust.cws.policy_sets.with_raw_response.delete(
                policy_set_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        policy_set = await async_client.zero_trust.cws.policy_sets.get(
            policy_set_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(PolicySet, policy_set, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.cws.policy_sets.with_raw_response.get(
            policy_set_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_set = await response.parse()
        assert_matches_type(PolicySet, policy_set, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.cws.policy_sets.with_streaming_response.get(
            policy_set_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_set = await response.parse()
            assert_matches_type(PolicySet, policy_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.cws.policy_sets.with_raw_response.get(
                policy_set_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_set_id` but received ''"):
            await async_client.zero_trust.cws.policy_sets.with_raw_response.get(
                policy_set_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            )
