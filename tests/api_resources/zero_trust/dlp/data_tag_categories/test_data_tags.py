# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.zero_trust.dlp.data_tag_categories import (
    DataTagGetResponse,
    DataTagListResponse,
    DataTagCreateResponse,
    DataTagUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDataTags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        data_tag = client.zero_trust.dlp.data_tag_categories.data_tags.create(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            name="name",
        )
        assert_matches_type(Optional[DataTagCreateResponse], data_tag, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        data_tag = client.zero_trust.dlp.data_tag_categories.data_tags.create(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            name="name",
            description="description",
        )
        assert_matches_type(Optional[DataTagCreateResponse], data_tag, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.create(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_tag = response.parse()
        assert_matches_type(Optional[DataTagCreateResponse], data_tag, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.data_tag_categories.data_tags.with_streaming_response.create(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_tag = response.parse()
            assert_matches_type(Optional[DataTagCreateResponse], data_tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.create(
                category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.create(
                category_id="",
                account_id="account_id",
                name="name",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        data_tag = client.zero_trust.dlp.data_tag_categories.data_tags.update(
            tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Optional[DataTagUpdateResponse], data_tag, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        data_tag = client.zero_trust.dlp.data_tag_categories.data_tags.update(
            tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            name="name",
        )
        assert_matches_type(Optional[DataTagUpdateResponse], data_tag, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.update(
            tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_tag = response.parse()
        assert_matches_type(Optional[DataTagUpdateResponse], data_tag, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.data_tag_categories.data_tags.with_streaming_response.update(
            tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_tag = response.parse()
            assert_matches_type(Optional[DataTagUpdateResponse], data_tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.update(
                tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.update(
                tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="account_id",
                category_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_id` but received ''"):
            client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.update(
                tag_id="",
                account_id="account_id",
                category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        data_tag = client.zero_trust.dlp.data_tag_categories.data_tags.list(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[DataTagListResponse], data_tag, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.list(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_tag = response.parse()
        assert_matches_type(SyncSinglePage[DataTagListResponse], data_tag, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.data_tag_categories.data_tags.with_streaming_response.list(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_tag = response.parse()
            assert_matches_type(SyncSinglePage[DataTagListResponse], data_tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.list(
                category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.list(
                category_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        data_tag = client.zero_trust.dlp.data_tag_categories.data_tags.delete(
            tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, data_tag, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.delete(
            tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_tag = response.parse()
        assert_matches_type(object, data_tag, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.data_tag_categories.data_tags.with_streaming_response.delete(
            tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_tag = response.parse()
            assert_matches_type(object, data_tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.delete(
                tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.delete(
                tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="account_id",
                category_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_id` but received ''"):
            client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.delete(
                tag_id="",
                account_id="account_id",
                category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        data_tag = client.zero_trust.dlp.data_tag_categories.data_tags.get(
            tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Optional[DataTagGetResponse], data_tag, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.get(
            tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_tag = response.parse()
        assert_matches_type(Optional[DataTagGetResponse], data_tag, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.data_tag_categories.data_tags.with_streaming_response.get(
            tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_tag = response.parse()
            assert_matches_type(Optional[DataTagGetResponse], data_tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.get(
                tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.get(
                tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="account_id",
                category_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_id` but received ''"):
            client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.get(
                tag_id="",
                account_id="account_id",
                category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncDataTags:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        data_tag = await async_client.zero_trust.dlp.data_tag_categories.data_tags.create(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            name="name",
        )
        assert_matches_type(Optional[DataTagCreateResponse], data_tag, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        data_tag = await async_client.zero_trust.dlp.data_tag_categories.data_tags.create(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            name="name",
            description="description",
        )
        assert_matches_type(Optional[DataTagCreateResponse], data_tag, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.create(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_tag = await response.parse()
        assert_matches_type(Optional[DataTagCreateResponse], data_tag, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.data_tag_categories.data_tags.with_streaming_response.create(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_tag = await response.parse()
            assert_matches_type(Optional[DataTagCreateResponse], data_tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.create(
                category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            await async_client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.create(
                category_id="",
                account_id="account_id",
                name="name",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        data_tag = await async_client.zero_trust.dlp.data_tag_categories.data_tags.update(
            tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Optional[DataTagUpdateResponse], data_tag, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        data_tag = await async_client.zero_trust.dlp.data_tag_categories.data_tags.update(
            tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            name="name",
        )
        assert_matches_type(Optional[DataTagUpdateResponse], data_tag, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.update(
            tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_tag = await response.parse()
        assert_matches_type(Optional[DataTagUpdateResponse], data_tag, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.data_tag_categories.data_tags.with_streaming_response.update(
            tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_tag = await response.parse()
            assert_matches_type(Optional[DataTagUpdateResponse], data_tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.update(
                tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            await async_client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.update(
                tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="account_id",
                category_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_id` but received ''"):
            await async_client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.update(
                tag_id="",
                account_id="account_id",
                category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        data_tag = await async_client.zero_trust.dlp.data_tag_categories.data_tags.list(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[DataTagListResponse], data_tag, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.list(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_tag = await response.parse()
        assert_matches_type(AsyncSinglePage[DataTagListResponse], data_tag, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.data_tag_categories.data_tags.with_streaming_response.list(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_tag = await response.parse()
            assert_matches_type(AsyncSinglePage[DataTagListResponse], data_tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.list(
                category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            await async_client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.list(
                category_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        data_tag = await async_client.zero_trust.dlp.data_tag_categories.data_tags.delete(
            tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, data_tag, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.delete(
            tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_tag = await response.parse()
        assert_matches_type(object, data_tag, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.data_tag_categories.data_tags.with_streaming_response.delete(
            tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_tag = await response.parse()
            assert_matches_type(object, data_tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.delete(
                tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            await async_client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.delete(
                tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="account_id",
                category_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_id` but received ''"):
            await async_client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.delete(
                tag_id="",
                account_id="account_id",
                category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        data_tag = await async_client.zero_trust.dlp.data_tag_categories.data_tags.get(
            tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Optional[DataTagGetResponse], data_tag, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.get(
            tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_tag = await response.parse()
        assert_matches_type(Optional[DataTagGetResponse], data_tag, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.data_tag_categories.data_tags.with_streaming_response.get(
            tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_tag = await response.parse()
            assert_matches_type(Optional[DataTagGetResponse], data_tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.get(
                tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            await async_client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.get(
                tag_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="account_id",
                category_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_id` but received ''"):
            await async_client.zero_trust.dlp.data_tag_categories.data_tags.with_raw_response.get(
                tag_id="",
                account_id="account_id",
                category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
