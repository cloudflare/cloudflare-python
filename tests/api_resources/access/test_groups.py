# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.access import (
    GroupGetResponse,
    GroupDeleteResponse,
    GroupUpdateResponse,
    GroupAccessGroupsListAccessGroupsResponse,
    GroupAccessGroupsCreateAnAccessGroupResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        group = client.access.groups.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
        )
        assert_matches_type(GroupUpdateResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        group = client.access.groups.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
            exclude=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            is_default=True,
            require=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
        )
        assert_matches_type(GroupUpdateResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.access.groups.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupUpdateResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.access.groups.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupUpdateResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.groups.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.groups.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.access.groups.with_raw_response.update(
                "",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        group = client.access.groups.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(GroupDeleteResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.access.groups.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupDeleteResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.access.groups.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupDeleteResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.groups.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.groups.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.access.groups.with_raw_response.delete(
                "",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_access_groups_create_an_access_group(self, client: Cloudflare) -> None:
        group = client.access.groups.access_groups_create_an_access_group(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
        )
        assert_matches_type(GroupAccessGroupsCreateAnAccessGroupResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_access_groups_create_an_access_group_with_all_params(self, client: Cloudflare) -> None:
        group = client.access.groups.access_groups_create_an_access_group(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
            exclude=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            is_default=True,
            require=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
        )
        assert_matches_type(GroupAccessGroupsCreateAnAccessGroupResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_access_groups_create_an_access_group(self, client: Cloudflare) -> None:
        response = client.access.groups.with_raw_response.access_groups_create_an_access_group(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupAccessGroupsCreateAnAccessGroupResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_access_groups_create_an_access_group(self, client: Cloudflare) -> None:
        with client.access.groups.with_streaming_response.access_groups_create_an_access_group(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupAccessGroupsCreateAnAccessGroupResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_access_groups_create_an_access_group(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.groups.with_raw_response.access_groups_create_an_access_group(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.groups.with_raw_response.access_groups_create_an_access_group(
                "",
                account_or_zone="string",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_access_groups_list_access_groups(self, client: Cloudflare) -> None:
        group = client.access.groups.access_groups_list_access_groups(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        )
        assert_matches_type(Optional[GroupAccessGroupsListAccessGroupsResponse], group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_access_groups_list_access_groups(self, client: Cloudflare) -> None:
        response = client.access.groups.with_raw_response.access_groups_list_access_groups(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(Optional[GroupAccessGroupsListAccessGroupsResponse], group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_access_groups_list_access_groups(self, client: Cloudflare) -> None:
        with client.access.groups.with_streaming_response.access_groups_list_access_groups(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(Optional[GroupAccessGroupsListAccessGroupsResponse], group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_access_groups_list_access_groups(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.groups.with_raw_response.access_groups_list_access_groups(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.groups.with_raw_response.access_groups_list_access_groups(
                "",
                account_or_zone="string",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        group = client.access.groups.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(GroupGetResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.access.groups.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupGetResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.access.groups.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupGetResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.groups.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.groups.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.access.groups.with_raw_response.get(
                "",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncGroups:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        group = await async_client.access.groups.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
        )
        assert_matches_type(GroupUpdateResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        group = await async_client.access.groups.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
            exclude=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            is_default=True,
            require=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
        )
        assert_matches_type(GroupUpdateResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.groups.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupUpdateResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.groups.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupUpdateResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.groups.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.groups.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.access.groups.with_raw_response.update(
                "",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        group = await async_client.access.groups.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(GroupDeleteResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.groups.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupDeleteResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.groups.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupDeleteResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.groups.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.groups.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.access.groups.with_raw_response.delete(
                "",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_access_groups_create_an_access_group(self, async_client: AsyncCloudflare) -> None:
        group = await async_client.access.groups.access_groups_create_an_access_group(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
        )
        assert_matches_type(GroupAccessGroupsCreateAnAccessGroupResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_access_groups_create_an_access_group_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        group = await async_client.access.groups.access_groups_create_an_access_group(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
            exclude=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            is_default=True,
            require=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
        )
        assert_matches_type(GroupAccessGroupsCreateAnAccessGroupResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_access_groups_create_an_access_group(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.groups.with_raw_response.access_groups_create_an_access_group(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupAccessGroupsCreateAnAccessGroupResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_access_groups_create_an_access_group(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.groups.with_streaming_response.access_groups_create_an_access_group(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupAccessGroupsCreateAnAccessGroupResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_access_groups_create_an_access_group(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.groups.with_raw_response.access_groups_create_an_access_group(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.groups.with_raw_response.access_groups_create_an_access_group(
                "",
                account_or_zone="string",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_access_groups_list_access_groups(self, async_client: AsyncCloudflare) -> None:
        group = await async_client.access.groups.access_groups_list_access_groups(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        )
        assert_matches_type(Optional[GroupAccessGroupsListAccessGroupsResponse], group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_access_groups_list_access_groups(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.groups.with_raw_response.access_groups_list_access_groups(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(Optional[GroupAccessGroupsListAccessGroupsResponse], group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_access_groups_list_access_groups(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.groups.with_streaming_response.access_groups_list_access_groups(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(Optional[GroupAccessGroupsListAccessGroupsResponse], group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_access_groups_list_access_groups(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.groups.with_raw_response.access_groups_list_access_groups(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.groups.with_raw_response.access_groups_list_access_groups(
                "",
                account_or_zone="string",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        group = await async_client.access.groups.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(GroupGetResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.groups.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupGetResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.groups.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupGetResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.groups.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.groups.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.access.groups.with_raw_response.get(
                "",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
