# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.api_gateway.labels import (
    UserGetResponse,
    UserEditResponse,
    UserDeleteResponse,
    UserUpdateResponse,
    UserBulkCreateResponse,
    UserBulkDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUser:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        user = client.api_gateway.labels.user.update(
            name="login",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        user = client.api_gateway.labels.user.update(
            name="login",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            description="All endpoints that deal with logins",
            metadata={"foo": "bar"},
        )
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.api_gateway.labels.user.with_raw_response.update(
            name="login",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.api_gateway.labels.user.with_streaming_response.update(
            name="login",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserUpdateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateway.labels.user.with_raw_response.update(
                name="login",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.api_gateway.labels.user.with_raw_response.update(
                name="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        user = client.api_gateway.labels.user.delete(
            name="login",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(UserDeleteResponse, user, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.api_gateway.labels.user.with_raw_response.delete(
            name="login",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserDeleteResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.api_gateway.labels.user.with_streaming_response.delete(
            name="login",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserDeleteResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateway.labels.user.with_raw_response.delete(
                name="login",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.api_gateway.labels.user.with_raw_response.delete(
                name="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_bulk_create(self, client: Cloudflare) -> None:
        user = client.api_gateway.labels.user.bulk_create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{"name": "login"}],
        )
        assert_matches_type(SyncSinglePage[UserBulkCreateResponse], user, path=["response"])

    @parametrize
    def test_raw_response_bulk_create(self, client: Cloudflare) -> None:
        response = client.api_gateway.labels.user.with_raw_response.bulk_create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{"name": "login"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(SyncSinglePage[UserBulkCreateResponse], user, path=["response"])

    @parametrize
    def test_streaming_response_bulk_create(self, client: Cloudflare) -> None:
        with client.api_gateway.labels.user.with_streaming_response.bulk_create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{"name": "login"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(SyncSinglePage[UserBulkCreateResponse], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_bulk_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateway.labels.user.with_raw_response.bulk_create(
                zone_id="",
                body=[{"name": "login"}],
            )

    @parametrize
    def test_method_bulk_delete(self, client: Cloudflare) -> None:
        user = client.api_gateway.labels.user.bulk_delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[UserBulkDeleteResponse], user, path=["response"])

    @parametrize
    def test_raw_response_bulk_delete(self, client: Cloudflare) -> None:
        response = client.api_gateway.labels.user.with_raw_response.bulk_delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(SyncSinglePage[UserBulkDeleteResponse], user, path=["response"])

    @parametrize
    def test_streaming_response_bulk_delete(self, client: Cloudflare) -> None:
        with client.api_gateway.labels.user.with_streaming_response.bulk_delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(SyncSinglePage[UserBulkDeleteResponse], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_bulk_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateway.labels.user.with_raw_response.bulk_delete(
                zone_id="",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        user = client.api_gateway.labels.user.edit(
            name="login",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(UserEditResponse, user, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        user = client.api_gateway.labels.user.edit(
            name="login",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            description="All endpoints that deal with logins",
            metadata={"foo": "bar"},
        )
        assert_matches_type(UserEditResponse, user, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.api_gateway.labels.user.with_raw_response.edit(
            name="login",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserEditResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.api_gateway.labels.user.with_streaming_response.edit(
            name="login",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserEditResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateway.labels.user.with_raw_response.edit(
                name="login",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.api_gateway.labels.user.with_raw_response.edit(
                name="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        user = client.api_gateway.labels.user.get(
            name="login",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(UserGetResponse, user, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        user = client.api_gateway.labels.user.get(
            name="login",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            with_mapped_resource_counts=True,
        )
        assert_matches_type(UserGetResponse, user, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.api_gateway.labels.user.with_raw_response.get(
            name="login",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserGetResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.api_gateway.labels.user.with_streaming_response.get(
            name="login",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserGetResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateway.labels.user.with_raw_response.get(
                name="login",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.api_gateway.labels.user.with_raw_response.get(
                name="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncUser:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        user = await async_client.api_gateway.labels.user.update(
            name="login",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        user = await async_client.api_gateway.labels.user.update(
            name="login",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            description="All endpoints that deal with logins",
            metadata={"foo": "bar"},
        )
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateway.labels.user.with_raw_response.update(
            name="login",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateway.labels.user.with_streaming_response.update(
            name="login",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserUpdateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateway.labels.user.with_raw_response.update(
                name="login",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.api_gateway.labels.user.with_raw_response.update(
                name="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        user = await async_client.api_gateway.labels.user.delete(
            name="login",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(UserDeleteResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateway.labels.user.with_raw_response.delete(
            name="login",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserDeleteResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateway.labels.user.with_streaming_response.delete(
            name="login",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserDeleteResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateway.labels.user.with_raw_response.delete(
                name="login",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.api_gateway.labels.user.with_raw_response.delete(
                name="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_bulk_create(self, async_client: AsyncCloudflare) -> None:
        user = await async_client.api_gateway.labels.user.bulk_create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{"name": "login"}],
        )
        assert_matches_type(AsyncSinglePage[UserBulkCreateResponse], user, path=["response"])

    @parametrize
    async def test_raw_response_bulk_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateway.labels.user.with_raw_response.bulk_create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{"name": "login"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(AsyncSinglePage[UserBulkCreateResponse], user, path=["response"])

    @parametrize
    async def test_streaming_response_bulk_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateway.labels.user.with_streaming_response.bulk_create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{"name": "login"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(AsyncSinglePage[UserBulkCreateResponse], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_bulk_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateway.labels.user.with_raw_response.bulk_create(
                zone_id="",
                body=[{"name": "login"}],
            )

    @parametrize
    async def test_method_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        user = await async_client.api_gateway.labels.user.bulk_delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[UserBulkDeleteResponse], user, path=["response"])

    @parametrize
    async def test_raw_response_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateway.labels.user.with_raw_response.bulk_delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(AsyncSinglePage[UserBulkDeleteResponse], user, path=["response"])

    @parametrize
    async def test_streaming_response_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateway.labels.user.with_streaming_response.bulk_delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(AsyncSinglePage[UserBulkDeleteResponse], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateway.labels.user.with_raw_response.bulk_delete(
                zone_id="",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        user = await async_client.api_gateway.labels.user.edit(
            name="login",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(UserEditResponse, user, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        user = await async_client.api_gateway.labels.user.edit(
            name="login",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            description="All endpoints that deal with logins",
            metadata={"foo": "bar"},
        )
        assert_matches_type(UserEditResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateway.labels.user.with_raw_response.edit(
            name="login",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserEditResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateway.labels.user.with_streaming_response.edit(
            name="login",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserEditResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateway.labels.user.with_raw_response.edit(
                name="login",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.api_gateway.labels.user.with_raw_response.edit(
                name="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        user = await async_client.api_gateway.labels.user.get(
            name="login",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(UserGetResponse, user, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        user = await async_client.api_gateway.labels.user.get(
            name="login",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            with_mapped_resource_counts=True,
        )
        assert_matches_type(UserGetResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateway.labels.user.with_raw_response.get(
            name="login",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserGetResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateway.labels.user.with_streaming_response.get(
            name="login",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserGetResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateway.labels.user.with_raw_response.get(
                name="login",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.api_gateway.labels.user.with_raw_response.get(
                name="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
