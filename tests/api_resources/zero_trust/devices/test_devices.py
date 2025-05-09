# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncCursorPagination, AsyncCursorPagination
from cloudflare.types.zero_trust.devices import DeviceGetResponse, DeviceListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDevices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        device = client.zero_trust.devices.devices.list(
            account_id="account_id",
        )
        assert_matches_type(SyncCursorPagination[DeviceListResponse], device, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        device = client.zero_trust.devices.devices.list(
            account_id="account_id",
            id=["string"],
            active_registrations="include",
            cursor="cursor",
            include="include",
            last_seen_user={"email": "email"},
            per_page=0,
            search="search",
            seen_after="seen_after",
            seen_before="seen_before",
            sort_by="name",
            sort_order="asc",
        )
        assert_matches_type(SyncCursorPagination[DeviceListResponse], device, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.devices.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert_matches_type(SyncCursorPagination[DeviceListResponse], device, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.devices.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert_matches_type(SyncCursorPagination[DeviceListResponse], device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.devices.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        device = client.zero_trust.devices.devices.delete(
            device_id="device_id",
            account_id="account_id",
        )
        assert_matches_type(object, device, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.devices.with_raw_response.delete(
            device_id="device_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert_matches_type(object, device, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.devices.with_streaming_response.delete(
            device_id="device_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert_matches_type(object, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.devices.with_raw_response.delete(
                device_id="device_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.zero_trust.devices.devices.with_raw_response.delete(
                device_id="",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        device = client.zero_trust.devices.devices.get(
            device_id="device_id",
            account_id="account_id",
        )
        assert_matches_type(DeviceGetResponse, device, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.devices.with_raw_response.get(
            device_id="device_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert_matches_type(DeviceGetResponse, device, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.devices.with_streaming_response.get(
            device_id="device_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert_matches_type(DeviceGetResponse, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.devices.with_raw_response.get(
                device_id="device_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.zero_trust.devices.devices.with_raw_response.get(
                device_id="",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_method_revoke(self, client: Cloudflare) -> None:
        device = client.zero_trust.devices.devices.revoke(
            device_id="device_id",
            account_id="account_id",
        )
        assert_matches_type(object, device, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_raw_response_revoke(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.devices.with_raw_response.revoke(
            device_id="device_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert_matches_type(object, device, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_streaming_response_revoke(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.devices.with_streaming_response.revoke(
            device_id="device_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert_matches_type(object, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_path_params_revoke(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.devices.with_raw_response.revoke(
                device_id="device_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.zero_trust.devices.devices.with_raw_response.revoke(
                device_id="",
                account_id="account_id",
            )


class TestAsyncDevices:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        device = await async_client.zero_trust.devices.devices.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncCursorPagination[DeviceListResponse], device, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        device = await async_client.zero_trust.devices.devices.list(
            account_id="account_id",
            id=["string"],
            active_registrations="include",
            cursor="cursor",
            include="include",
            last_seen_user={"email": "email"},
            per_page=0,
            search="search",
            seen_after="seen_after",
            seen_before="seen_before",
            sort_by="name",
            sort_order="asc",
        )
        assert_matches_type(AsyncCursorPagination[DeviceListResponse], device, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.devices.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert_matches_type(AsyncCursorPagination[DeviceListResponse], device, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.devices.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert_matches_type(AsyncCursorPagination[DeviceListResponse], device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.devices.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        device = await async_client.zero_trust.devices.devices.delete(
            device_id="device_id",
            account_id="account_id",
        )
        assert_matches_type(object, device, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.devices.with_raw_response.delete(
            device_id="device_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert_matches_type(object, device, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.devices.with_streaming_response.delete(
            device_id="device_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert_matches_type(object, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.devices.with_raw_response.delete(
                device_id="device_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.zero_trust.devices.devices.with_raw_response.delete(
                device_id="",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        device = await async_client.zero_trust.devices.devices.get(
            device_id="device_id",
            account_id="account_id",
        )
        assert_matches_type(DeviceGetResponse, device, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.devices.with_raw_response.get(
            device_id="device_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert_matches_type(DeviceGetResponse, device, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.devices.with_streaming_response.get(
            device_id="device_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert_matches_type(DeviceGetResponse, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.devices.with_raw_response.get(
                device_id="device_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.zero_trust.devices.devices.with_raw_response.get(
                device_id="",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_method_revoke(self, async_client: AsyncCloudflare) -> None:
        device = await async_client.zero_trust.devices.devices.revoke(
            device_id="device_id",
            account_id="account_id",
        )
        assert_matches_type(object, device, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_raw_response_revoke(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.devices.with_raw_response.revoke(
            device_id="device_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert_matches_type(object, device, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_streaming_response_revoke(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.devices.with_streaming_response.revoke(
            device_id="device_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert_matches_type(object, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_path_params_revoke(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.devices.with_raw_response.revoke(
                device_id="device_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.zero_trust.devices.devices.with_raw_response.revoke(
                device_id="",
                account_id="account_id",
            )
