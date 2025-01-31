# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.zero_trust.access import (
    GroupGetResponse,
    GroupListResponse,
    GroupCreateResponse,
    GroupDeleteResponse,
    GroupUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        group = client.zero_trust.access.groups.create(
            include=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
            name="Allow devs",
            account_id="account_id",
        )
        assert_matches_type(Optional[GroupCreateResponse], group, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        group = client.zero_trust.access.groups.create(
            include=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
            name="Allow devs",
            account_id="account_id",
            exclude=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
            is_default=True,
            require=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
        )
        assert_matches_type(Optional[GroupCreateResponse], group, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.groups.with_raw_response.create(
            include=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
            name="Allow devs",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(Optional[GroupCreateResponse], group, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.access.groups.with_streaming_response.create(
            include=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
            name="Allow devs",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(Optional[GroupCreateResponse], group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.groups.with_raw_response.create(
                include=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
                name="Allow devs",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.groups.with_raw_response.create(
                include=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
                name="Allow devs",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        group = client.zero_trust.access.groups.update(
            group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            include=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
            name="Allow devs",
            account_id="account_id",
        )
        assert_matches_type(Optional[GroupUpdateResponse], group, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        group = client.zero_trust.access.groups.update(
            group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            include=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
            name="Allow devs",
            account_id="account_id",
            exclude=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
            is_default=True,
            require=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
        )
        assert_matches_type(Optional[GroupUpdateResponse], group, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.groups.with_raw_response.update(
            group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            include=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
            name="Allow devs",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(Optional[GroupUpdateResponse], group, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.access.groups.with_streaming_response.update(
            group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            include=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
            name="Allow devs",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(Optional[GroupUpdateResponse], group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.zero_trust.access.groups.with_raw_response.update(
                group_id="",
                include=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
                name="Allow devs",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.groups.with_raw_response.update(
                group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                include=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
                name="Allow devs",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.groups.with_raw_response.update(
                group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                include=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
                name="Allow devs",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        group = client.zero_trust.access.groups.list(
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[GroupListResponse], group, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        group = client.zero_trust.access.groups.list(
            account_id="account_id",
            name="name",
            search="search",
        )
        assert_matches_type(SyncSinglePage[GroupListResponse], group, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.groups.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(SyncSinglePage[GroupListResponse], group, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.access.groups.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(SyncSinglePage[GroupListResponse], group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.groups.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.groups.with_raw_response.list(
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        group = client.zero_trust.access.groups.delete(
            group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[GroupDeleteResponse], group, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        group = client.zero_trust.access.groups.delete(
            group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[GroupDeleteResponse], group, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.groups.with_raw_response.delete(
            group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(Optional[GroupDeleteResponse], group, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.access.groups.with_streaming_response.delete(
            group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(Optional[GroupDeleteResponse], group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.zero_trust.access.groups.with_raw_response.delete(
                group_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.groups.with_raw_response.delete(
                group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.groups.with_raw_response.delete(
                group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        group = client.zero_trust.access.groups.get(
            group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[GroupGetResponse], group, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        group = client.zero_trust.access.groups.get(
            group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[GroupGetResponse], group, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.groups.with_raw_response.get(
            group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(Optional[GroupGetResponse], group, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.access.groups.with_streaming_response.get(
            group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(Optional[GroupGetResponse], group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.zero_trust.access.groups.with_raw_response.get(
                group_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.groups.with_raw_response.get(
                group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.groups.with_raw_response.get(
                group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="account_id",
            )


class TestAsyncGroups:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        group = await async_client.zero_trust.access.groups.create(
            include=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
            name="Allow devs",
            account_id="account_id",
        )
        assert_matches_type(Optional[GroupCreateResponse], group, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        group = await async_client.zero_trust.access.groups.create(
            include=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
            name="Allow devs",
            account_id="account_id",
            exclude=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
            is_default=True,
            require=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
        )
        assert_matches_type(Optional[GroupCreateResponse], group, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.groups.with_raw_response.create(
            include=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
            name="Allow devs",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(Optional[GroupCreateResponse], group, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.groups.with_streaming_response.create(
            include=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
            name="Allow devs",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(Optional[GroupCreateResponse], group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.groups.with_raw_response.create(
                include=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
                name="Allow devs",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.groups.with_raw_response.create(
                include=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
                name="Allow devs",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        group = await async_client.zero_trust.access.groups.update(
            group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            include=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
            name="Allow devs",
            account_id="account_id",
        )
        assert_matches_type(Optional[GroupUpdateResponse], group, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        group = await async_client.zero_trust.access.groups.update(
            group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            include=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
            name="Allow devs",
            account_id="account_id",
            exclude=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
            is_default=True,
            require=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
        )
        assert_matches_type(Optional[GroupUpdateResponse], group, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.groups.with_raw_response.update(
            group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            include=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
            name="Allow devs",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(Optional[GroupUpdateResponse], group, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.groups.with_streaming_response.update(
            group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            include=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
            name="Allow devs",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(Optional[GroupUpdateResponse], group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.zero_trust.access.groups.with_raw_response.update(
                group_id="",
                include=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
                name="Allow devs",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.groups.with_raw_response.update(
                group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                include=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
                name="Allow devs",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.groups.with_raw_response.update(
                group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                include=[{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
                name="Allow devs",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        group = await async_client.zero_trust.access.groups.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[GroupListResponse], group, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        group = await async_client.zero_trust.access.groups.list(
            account_id="account_id",
            name="name",
            search="search",
        )
        assert_matches_type(AsyncSinglePage[GroupListResponse], group, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.groups.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(AsyncSinglePage[GroupListResponse], group, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.groups.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(AsyncSinglePage[GroupListResponse], group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.groups.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.groups.with_raw_response.list(
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        group = await async_client.zero_trust.access.groups.delete(
            group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[GroupDeleteResponse], group, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        group = await async_client.zero_trust.access.groups.delete(
            group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[GroupDeleteResponse], group, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.groups.with_raw_response.delete(
            group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(Optional[GroupDeleteResponse], group, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.groups.with_streaming_response.delete(
            group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(Optional[GroupDeleteResponse], group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.zero_trust.access.groups.with_raw_response.delete(
                group_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.groups.with_raw_response.delete(
                group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.groups.with_raw_response.delete(
                group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        group = await async_client.zero_trust.access.groups.get(
            group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[GroupGetResponse], group, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        group = await async_client.zero_trust.access.groups.get(
            group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[GroupGetResponse], group, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.groups.with_raw_response.get(
            group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(Optional[GroupGetResponse], group, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.groups.with_streaming_response.get(
            group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(Optional[GroupGetResponse], group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.zero_trust.access.groups.with_raw_response.get(
                group_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.groups.with_raw_response.get(
                group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.groups.with_raw_response.get(
                group_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="account_id",
            )
