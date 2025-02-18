# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.network_interconnects import (
    InterconnectGetResponse,
    InterconnectListResponse,
    InterconnectCreateResponse,
    InterconnectStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInterconnects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Cloudflare) -> None:
        interconnect = client.network_interconnects.interconnects.create(
            account_id="account_id",
            account="account",
            slot_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="type",
        )
        assert_matches_type(InterconnectCreateResponse, interconnect, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Cloudflare) -> None:
        interconnect = client.network_interconnects.interconnects.create(
            account_id="account_id",
            account="account",
            slot_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="type",
            speed="speed",
        )
        assert_matches_type(InterconnectCreateResponse, interconnect, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Cloudflare) -> None:
        response = client.network_interconnects.interconnects.with_raw_response.create(
            account_id="account_id",
            account="account",
            slot_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interconnect = response.parse()
        assert_matches_type(InterconnectCreateResponse, interconnect, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Cloudflare) -> None:
        with client.network_interconnects.interconnects.with_streaming_response.create(
            account_id="account_id",
            account="account",
            slot_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interconnect = response.parse()
            assert_matches_type(InterconnectCreateResponse, interconnect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.network_interconnects.interconnects.with_raw_response.create(
                account_id="",
                account="account",
                slot_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                type="type",
            )

    @parametrize
    def test_method_create_overload_2(self, client: Cloudflare) -> None:
        interconnect = client.network_interconnects.interconnects.create(
            account_id="account_id",
            account="account",
            bandwidth="50M",
            pairing_key="pairing_key",
            type="type",
        )
        assert_matches_type(InterconnectCreateResponse, interconnect, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Cloudflare) -> None:
        response = client.network_interconnects.interconnects.with_raw_response.create(
            account_id="account_id",
            account="account",
            bandwidth="50M",
            pairing_key="pairing_key",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interconnect = response.parse()
        assert_matches_type(InterconnectCreateResponse, interconnect, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Cloudflare) -> None:
        with client.network_interconnects.interconnects.with_streaming_response.create(
            account_id="account_id",
            account="account",
            bandwidth="50M",
            pairing_key="pairing_key",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interconnect = response.parse()
            assert_matches_type(InterconnectCreateResponse, interconnect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.network_interconnects.interconnects.with_raw_response.create(
                account_id="",
                account="account",
                bandwidth="50M",
                pairing_key="pairing_key",
                type="type",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        interconnect = client.network_interconnects.interconnects.list(
            account_id="account_id",
        )
        assert_matches_type(InterconnectListResponse, interconnect, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        interconnect = client.network_interconnects.interconnects.list(
            account_id="account_id",
            cursor=0,
            limit=0,
            site="site",
            type="type",
        )
        assert_matches_type(InterconnectListResponse, interconnect, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.network_interconnects.interconnects.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interconnect = response.parse()
        assert_matches_type(InterconnectListResponse, interconnect, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.network_interconnects.interconnects.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interconnect = response.parse()
            assert_matches_type(InterconnectListResponse, interconnect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.network_interconnects.interconnects.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        interconnect = client.network_interconnects.interconnects.delete(
            icon="icon",
            account_id="account_id",
        )
        assert interconnect is None

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.network_interconnects.interconnects.with_raw_response.delete(
            icon="icon",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interconnect = response.parse()
        assert interconnect is None

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.network_interconnects.interconnects.with_streaming_response.delete(
            icon="icon",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interconnect = response.parse()
            assert interconnect is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.network_interconnects.interconnects.with_raw_response.delete(
                icon="icon",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `icon` but received ''"):
            client.network_interconnects.interconnects.with_raw_response.delete(
                icon="",
                account_id="account_id",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        interconnect = client.network_interconnects.interconnects.get(
            icon="icon",
            account_id="account_id",
        )
        assert_matches_type(InterconnectGetResponse, interconnect, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.network_interconnects.interconnects.with_raw_response.get(
            icon="icon",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interconnect = response.parse()
        assert_matches_type(InterconnectGetResponse, interconnect, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.network_interconnects.interconnects.with_streaming_response.get(
            icon="icon",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interconnect = response.parse()
            assert_matches_type(InterconnectGetResponse, interconnect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.network_interconnects.interconnects.with_raw_response.get(
                icon="icon",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `icon` but received ''"):
            client.network_interconnects.interconnects.with_raw_response.get(
                icon="",
                account_id="account_id",
            )

    @parametrize
    def test_method_loa(self, client: Cloudflare) -> None:
        interconnect = client.network_interconnects.interconnects.loa(
            icon="icon",
            account_id="account_id",
        )
        assert interconnect is None

    @parametrize
    def test_raw_response_loa(self, client: Cloudflare) -> None:
        response = client.network_interconnects.interconnects.with_raw_response.loa(
            icon="icon",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interconnect = response.parse()
        assert interconnect is None

    @parametrize
    def test_streaming_response_loa(self, client: Cloudflare) -> None:
        with client.network_interconnects.interconnects.with_streaming_response.loa(
            icon="icon",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interconnect = response.parse()
            assert interconnect is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_loa(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.network_interconnects.interconnects.with_raw_response.loa(
                icon="icon",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `icon` but received ''"):
            client.network_interconnects.interconnects.with_raw_response.loa(
                icon="",
                account_id="account_id",
            )

    @parametrize
    def test_method_status(self, client: Cloudflare) -> None:
        interconnect = client.network_interconnects.interconnects.status(
            icon="icon",
            account_id="account_id",
        )
        assert_matches_type(InterconnectStatusResponse, interconnect, path=["response"])

    @parametrize
    def test_raw_response_status(self, client: Cloudflare) -> None:
        response = client.network_interconnects.interconnects.with_raw_response.status(
            icon="icon",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interconnect = response.parse()
        assert_matches_type(InterconnectStatusResponse, interconnect, path=["response"])

    @parametrize
    def test_streaming_response_status(self, client: Cloudflare) -> None:
        with client.network_interconnects.interconnects.with_streaming_response.status(
            icon="icon",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interconnect = response.parse()
            assert_matches_type(InterconnectStatusResponse, interconnect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_status(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.network_interconnects.interconnects.with_raw_response.status(
                icon="icon",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `icon` but received ''"):
            client.network_interconnects.interconnects.with_raw_response.status(
                icon="",
                account_id="account_id",
            )


class TestAsyncInterconnects:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        interconnect = await async_client.network_interconnects.interconnects.create(
            account_id="account_id",
            account="account",
            slot_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="type",
        )
        assert_matches_type(InterconnectCreateResponse, interconnect, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        interconnect = await async_client.network_interconnects.interconnects.create(
            account_id="account_id",
            account="account",
            slot_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="type",
            speed="speed",
        )
        assert_matches_type(InterconnectCreateResponse, interconnect, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.network_interconnects.interconnects.with_raw_response.create(
            account_id="account_id",
            account="account",
            slot_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interconnect = await response.parse()
        assert_matches_type(InterconnectCreateResponse, interconnect, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.network_interconnects.interconnects.with_streaming_response.create(
            account_id="account_id",
            account="account",
            slot_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interconnect = await response.parse()
            assert_matches_type(InterconnectCreateResponse, interconnect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.network_interconnects.interconnects.with_raw_response.create(
                account_id="",
                account="account",
                slot_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                type="type",
            )

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        interconnect = await async_client.network_interconnects.interconnects.create(
            account_id="account_id",
            account="account",
            bandwidth="50M",
            pairing_key="pairing_key",
            type="type",
        )
        assert_matches_type(InterconnectCreateResponse, interconnect, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.network_interconnects.interconnects.with_raw_response.create(
            account_id="account_id",
            account="account",
            bandwidth="50M",
            pairing_key="pairing_key",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interconnect = await response.parse()
        assert_matches_type(InterconnectCreateResponse, interconnect, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.network_interconnects.interconnects.with_streaming_response.create(
            account_id="account_id",
            account="account",
            bandwidth="50M",
            pairing_key="pairing_key",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interconnect = await response.parse()
            assert_matches_type(InterconnectCreateResponse, interconnect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.network_interconnects.interconnects.with_raw_response.create(
                account_id="",
                account="account",
                bandwidth="50M",
                pairing_key="pairing_key",
                type="type",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        interconnect = await async_client.network_interconnects.interconnects.list(
            account_id="account_id",
        )
        assert_matches_type(InterconnectListResponse, interconnect, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        interconnect = await async_client.network_interconnects.interconnects.list(
            account_id="account_id",
            cursor=0,
            limit=0,
            site="site",
            type="type",
        )
        assert_matches_type(InterconnectListResponse, interconnect, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.network_interconnects.interconnects.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interconnect = await response.parse()
        assert_matches_type(InterconnectListResponse, interconnect, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.network_interconnects.interconnects.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interconnect = await response.parse()
            assert_matches_type(InterconnectListResponse, interconnect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.network_interconnects.interconnects.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        interconnect = await async_client.network_interconnects.interconnects.delete(
            icon="icon",
            account_id="account_id",
        )
        assert interconnect is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.network_interconnects.interconnects.with_raw_response.delete(
            icon="icon",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interconnect = await response.parse()
        assert interconnect is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.network_interconnects.interconnects.with_streaming_response.delete(
            icon="icon",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interconnect = await response.parse()
            assert interconnect is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.network_interconnects.interconnects.with_raw_response.delete(
                icon="icon",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `icon` but received ''"):
            await async_client.network_interconnects.interconnects.with_raw_response.delete(
                icon="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        interconnect = await async_client.network_interconnects.interconnects.get(
            icon="icon",
            account_id="account_id",
        )
        assert_matches_type(InterconnectGetResponse, interconnect, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.network_interconnects.interconnects.with_raw_response.get(
            icon="icon",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interconnect = await response.parse()
        assert_matches_type(InterconnectGetResponse, interconnect, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.network_interconnects.interconnects.with_streaming_response.get(
            icon="icon",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interconnect = await response.parse()
            assert_matches_type(InterconnectGetResponse, interconnect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.network_interconnects.interconnects.with_raw_response.get(
                icon="icon",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `icon` but received ''"):
            await async_client.network_interconnects.interconnects.with_raw_response.get(
                icon="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_loa(self, async_client: AsyncCloudflare) -> None:
        interconnect = await async_client.network_interconnects.interconnects.loa(
            icon="icon",
            account_id="account_id",
        )
        assert interconnect is None

    @parametrize
    async def test_raw_response_loa(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.network_interconnects.interconnects.with_raw_response.loa(
            icon="icon",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interconnect = await response.parse()
        assert interconnect is None

    @parametrize
    async def test_streaming_response_loa(self, async_client: AsyncCloudflare) -> None:
        async with async_client.network_interconnects.interconnects.with_streaming_response.loa(
            icon="icon",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interconnect = await response.parse()
            assert interconnect is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_loa(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.network_interconnects.interconnects.with_raw_response.loa(
                icon="icon",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `icon` but received ''"):
            await async_client.network_interconnects.interconnects.with_raw_response.loa(
                icon="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_status(self, async_client: AsyncCloudflare) -> None:
        interconnect = await async_client.network_interconnects.interconnects.status(
            icon="icon",
            account_id="account_id",
        )
        assert_matches_type(InterconnectStatusResponse, interconnect, path=["response"])

    @parametrize
    async def test_raw_response_status(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.network_interconnects.interconnects.with_raw_response.status(
            icon="icon",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interconnect = await response.parse()
        assert_matches_type(InterconnectStatusResponse, interconnect, path=["response"])

    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncCloudflare) -> None:
        async with async_client.network_interconnects.interconnects.with_streaming_response.status(
            icon="icon",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interconnect = await response.parse()
            assert_matches_type(InterconnectStatusResponse, interconnect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_status(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.network_interconnects.interconnects.with_raw_response.status(
                icon="icon",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `icon` but received ''"):
            await async_client.network_interconnects.interconnects.with_raw_response.status(
                icon="",
                account_id="account_id",
            )
