# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.dlp.entries import (
    CustomCreateResponse,
    CustomUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustom:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        custom = client.zero_trust.dlp.entries.custom.create(
            account_id="account_id",
            enabled=True,
            name="name",
            pattern={"regex": "regex"},
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Optional[CustomCreateResponse], custom, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        custom = client.zero_trust.dlp.entries.custom.create(
            account_id="account_id",
            enabled=True,
            name="name",
            pattern={
                "regex": "regex",
                "validation": "luhn",
            },
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Optional[CustomCreateResponse], custom, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.entries.custom.with_raw_response.create(
            account_id="account_id",
            enabled=True,
            name="name",
            pattern={"regex": "regex"},
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(Optional[CustomCreateResponse], custom, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.entries.custom.with_streaming_response.create(
            account_id="account_id",
            enabled=True,
            name="name",
            pattern={"regex": "regex"},
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(Optional[CustomCreateResponse], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.entries.custom.with_raw_response.create(
                account_id="",
                enabled=True,
                name="name",
                pattern={"regex": "regex"},
                profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_update_overload_1(self, client: Cloudflare) -> None:
        custom = client.zero_trust.dlp.entries.custom.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            name="name",
            pattern={"regex": "regex"},
            type="custom",
        )
        assert_matches_type(Optional[CustomUpdateResponse], custom, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Cloudflare) -> None:
        custom = client.zero_trust.dlp.entries.custom.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            name="name",
            pattern={
                "regex": "regex",
                "validation": "luhn",
            },
            type="custom",
            enabled=True,
        )
        assert_matches_type(Optional[CustomUpdateResponse], custom, path=["response"])

    @parametrize
    def test_raw_response_update_overload_1(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.entries.custom.with_raw_response.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            name="name",
            pattern={"regex": "regex"},
            type="custom",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(Optional[CustomUpdateResponse], custom, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_1(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.entries.custom.with_streaming_response.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            name="name",
            pattern={"regex": "regex"},
            type="custom",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(Optional[CustomUpdateResponse], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.entries.custom.with_raw_response.update(
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                name="name",
                pattern={"regex": "regex"},
                type="custom",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            client.zero_trust.dlp.entries.custom.with_raw_response.update(
                entry_id="",
                account_id="account_id",
                name="name",
                pattern={"regex": "regex"},
                type="custom",
            )

    @parametrize
    def test_method_update_overload_2(self, client: Cloudflare) -> None:
        custom = client.zero_trust.dlp.entries.custom.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            type="predefined",
        )
        assert_matches_type(Optional[CustomUpdateResponse], custom, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: Cloudflare) -> None:
        custom = client.zero_trust.dlp.entries.custom.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            type="predefined",
            enabled=True,
        )
        assert_matches_type(Optional[CustomUpdateResponse], custom, path=["response"])

    @parametrize
    def test_raw_response_update_overload_2(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.entries.custom.with_raw_response.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            type="predefined",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(Optional[CustomUpdateResponse], custom, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_2(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.entries.custom.with_streaming_response.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            type="predefined",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(Optional[CustomUpdateResponse], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.entries.custom.with_raw_response.update(
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                type="predefined",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            client.zero_trust.dlp.entries.custom.with_raw_response.update(
                entry_id="",
                account_id="account_id",
                type="predefined",
            )

    @parametrize
    def test_method_update_overload_3(self, client: Cloudflare) -> None:
        custom = client.zero_trust.dlp.entries.custom.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            type="integration",
        )
        assert_matches_type(Optional[CustomUpdateResponse], custom, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_3(self, client: Cloudflare) -> None:
        custom = client.zero_trust.dlp.entries.custom.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            type="integration",
            enabled=True,
        )
        assert_matches_type(Optional[CustomUpdateResponse], custom, path=["response"])

    @parametrize
    def test_raw_response_update_overload_3(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.entries.custom.with_raw_response.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            type="integration",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(Optional[CustomUpdateResponse], custom, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_3(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.entries.custom.with_streaming_response.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            type="integration",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(Optional[CustomUpdateResponse], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.entries.custom.with_raw_response.update(
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                type="integration",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            client.zero_trust.dlp.entries.custom.with_raw_response.update(
                entry_id="",
                account_id="account_id",
                type="integration",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        custom = client.zero_trust.dlp.entries.custom.delete(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(object, custom, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.entries.custom.with_raw_response.delete(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(object, custom, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.entries.custom.with_streaming_response.delete(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(object, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.entries.custom.with_raw_response.delete(
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            client.zero_trust.dlp.entries.custom.with_raw_response.delete(
                entry_id="",
                account_id="account_id",
            )


class TestAsyncCustom:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.zero_trust.dlp.entries.custom.create(
            account_id="account_id",
            enabled=True,
            name="name",
            pattern={"regex": "regex"},
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Optional[CustomCreateResponse], custom, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.zero_trust.dlp.entries.custom.create(
            account_id="account_id",
            enabled=True,
            name="name",
            pattern={
                "regex": "regex",
                "validation": "luhn",
            },
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Optional[CustomCreateResponse], custom, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.entries.custom.with_raw_response.create(
            account_id="account_id",
            enabled=True,
            name="name",
            pattern={"regex": "regex"},
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(Optional[CustomCreateResponse], custom, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.entries.custom.with_streaming_response.create(
            account_id="account_id",
            enabled=True,
            name="name",
            pattern={"regex": "regex"},
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(Optional[CustomCreateResponse], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.entries.custom.with_raw_response.create(
                account_id="",
                enabled=True,
                name="name",
                pattern={"regex": "regex"},
                profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.zero_trust.dlp.entries.custom.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            name="name",
            pattern={"regex": "regex"},
            type="custom",
        )
        assert_matches_type(Optional[CustomUpdateResponse], custom, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.zero_trust.dlp.entries.custom.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            name="name",
            pattern={
                "regex": "regex",
                "validation": "luhn",
            },
            type="custom",
            enabled=True,
        )
        assert_matches_type(Optional[CustomUpdateResponse], custom, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.entries.custom.with_raw_response.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            name="name",
            pattern={"regex": "regex"},
            type="custom",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(Optional[CustomUpdateResponse], custom, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.entries.custom.with_streaming_response.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            name="name",
            pattern={"regex": "regex"},
            type="custom",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(Optional[CustomUpdateResponse], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.entries.custom.with_raw_response.update(
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                name="name",
                pattern={"regex": "regex"},
                type="custom",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            await async_client.zero_trust.dlp.entries.custom.with_raw_response.update(
                entry_id="",
                account_id="account_id",
                name="name",
                pattern={"regex": "regex"},
                type="custom",
            )

    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.zero_trust.dlp.entries.custom.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            type="predefined",
        )
        assert_matches_type(Optional[CustomUpdateResponse], custom, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.zero_trust.dlp.entries.custom.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            type="predefined",
            enabled=True,
        )
        assert_matches_type(Optional[CustomUpdateResponse], custom, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.entries.custom.with_raw_response.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            type="predefined",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(Optional[CustomUpdateResponse], custom, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.entries.custom.with_streaming_response.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            type="predefined",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(Optional[CustomUpdateResponse], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.entries.custom.with_raw_response.update(
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                type="predefined",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            await async_client.zero_trust.dlp.entries.custom.with_raw_response.update(
                entry_id="",
                account_id="account_id",
                type="predefined",
            )

    @parametrize
    async def test_method_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.zero_trust.dlp.entries.custom.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            type="integration",
        )
        assert_matches_type(Optional[CustomUpdateResponse], custom, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_3(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.zero_trust.dlp.entries.custom.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            type="integration",
            enabled=True,
        )
        assert_matches_type(Optional[CustomUpdateResponse], custom, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.entries.custom.with_raw_response.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            type="integration",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(Optional[CustomUpdateResponse], custom, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.entries.custom.with_streaming_response.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            type="integration",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(Optional[CustomUpdateResponse], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.entries.custom.with_raw_response.update(
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                type="integration",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            await async_client.zero_trust.dlp.entries.custom.with_raw_response.update(
                entry_id="",
                account_id="account_id",
                type="integration",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.zero_trust.dlp.entries.custom.delete(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(object, custom, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.entries.custom.with_raw_response.delete(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(object, custom, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.entries.custom.with_streaming_response.delete(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(object, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.entries.custom.with_raw_response.delete(
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            await async_client.zero_trust.dlp.entries.custom.with_raw_response.delete(
                entry_id="",
                account_id="account_id",
            )
