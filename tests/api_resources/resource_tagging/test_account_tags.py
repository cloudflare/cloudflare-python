# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.resource_tagging import (
    AccountTagGetResponse,
    AccountTagUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccountTags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update_overload_1(self, client: Cloudflare) -> None:
        account_tag = client.resource_tagging.account_tags.update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="worker",
            worker_id="3f72a691-44b3-4c11-8642-c18a88ddaa5e",
        )
        assert_matches_type(Optional[AccountTagUpdateResponse], account_tag, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Cloudflare) -> None:
        account_tag = client.resource_tagging.account_tags.update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="worker",
            worker_id="3f72a691-44b3-4c11-8642-c18a88ddaa5e",
            tags={
                "environment": "production",
                "team": "engineering",
            },
            if_match='"v1:RBNvo1WzZ4oRRq0W9-hkng"',
        )
        assert_matches_type(Optional[AccountTagUpdateResponse], account_tag, path=["response"])

    @parametrize
    def test_raw_response_update_overload_1(self, client: Cloudflare) -> None:
        response = client.resource_tagging.account_tags.with_raw_response.update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="worker",
            worker_id="3f72a691-44b3-4c11-8642-c18a88ddaa5e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_tag = response.parse()
        assert_matches_type(Optional[AccountTagUpdateResponse], account_tag, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_1(self, client: Cloudflare) -> None:
        with client.resource_tagging.account_tags.with_streaming_response.update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="worker",
            worker_id="3f72a691-44b3-4c11-8642-c18a88ddaa5e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_tag = response.parse()
            assert_matches_type(Optional[AccountTagUpdateResponse], account_tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.resource_tagging.account_tags.with_raw_response.update(
                account_id="",
                resource_id="023e105f4ecef8ad9ca31a8372d0c353",
                resource_type="worker",
                worker_id="3f72a691-44b3-4c11-8642-c18a88ddaa5e",
            )

    @parametrize
    def test_method_update_overload_2(self, client: Cloudflare) -> None:
        account_tag = client.resource_tagging.account_tags.update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="worker",
        )
        assert_matches_type(Optional[AccountTagUpdateResponse], account_tag, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: Cloudflare) -> None:
        account_tag = client.resource_tagging.account_tags.update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="worker",
            tags={
                "environment": "production",
                "team": "engineering",
            },
            if_match='"v1:RBNvo1WzZ4oRRq0W9-hkng"',
        )
        assert_matches_type(Optional[AccountTagUpdateResponse], account_tag, path=["response"])

    @parametrize
    def test_raw_response_update_overload_2(self, client: Cloudflare) -> None:
        response = client.resource_tagging.account_tags.with_raw_response.update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="worker",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_tag = response.parse()
        assert_matches_type(Optional[AccountTagUpdateResponse], account_tag, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_2(self, client: Cloudflare) -> None:
        with client.resource_tagging.account_tags.with_streaming_response.update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="worker",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_tag = response.parse()
            assert_matches_type(Optional[AccountTagUpdateResponse], account_tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.resource_tagging.account_tags.with_raw_response.update(
                account_id="",
                resource_id="023e105f4ecef8ad9ca31a8372d0c353",
                resource_type="worker",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        account_tag = client.resource_tagging.account_tags.delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert account_tag is None

    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        account_tag = client.resource_tagging.account_tags.delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            if_match='"v1:RBNvo1WzZ4oRRq0W9-hkng"',
        )
        assert account_tag is None

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.resource_tagging.account_tags.with_raw_response.delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_tag = response.parse()
        assert account_tag is None

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.resource_tagging.account_tags.with_streaming_response.delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_tag = response.parse()
            assert account_tag is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.resource_tagging.account_tags.with_raw_response.delete(
                account_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        account_tag = client.resource_tagging.account_tags.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="worker",
        )
        assert_matches_type(Optional[AccountTagGetResponse], account_tag, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        account_tag = client.resource_tagging.account_tags.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="worker",
            worker_id="3f72a691-44b3-4c11-8642-c18a88ddaa5e",
        )
        assert_matches_type(Optional[AccountTagGetResponse], account_tag, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.resource_tagging.account_tags.with_raw_response.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="worker",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_tag = response.parse()
        assert_matches_type(Optional[AccountTagGetResponse], account_tag, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.resource_tagging.account_tags.with_streaming_response.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="worker",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_tag = response.parse()
            assert_matches_type(Optional[AccountTagGetResponse], account_tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.resource_tagging.account_tags.with_raw_response.get(
                account_id="",
                resource_id="023e105f4ecef8ad9ca31a8372d0c353",
                resource_type="worker",
            )


class TestAsyncAccountTags:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        account_tag = await async_client.resource_tagging.account_tags.update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="worker",
            worker_id="3f72a691-44b3-4c11-8642-c18a88ddaa5e",
        )
        assert_matches_type(Optional[AccountTagUpdateResponse], account_tag, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        account_tag = await async_client.resource_tagging.account_tags.update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="worker",
            worker_id="3f72a691-44b3-4c11-8642-c18a88ddaa5e",
            tags={
                "environment": "production",
                "team": "engineering",
            },
            if_match='"v1:RBNvo1WzZ4oRRq0W9-hkng"',
        )
        assert_matches_type(Optional[AccountTagUpdateResponse], account_tag, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.resource_tagging.account_tags.with_raw_response.update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="worker",
            worker_id="3f72a691-44b3-4c11-8642-c18a88ddaa5e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_tag = await response.parse()
        assert_matches_type(Optional[AccountTagUpdateResponse], account_tag, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.resource_tagging.account_tags.with_streaming_response.update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="worker",
            worker_id="3f72a691-44b3-4c11-8642-c18a88ddaa5e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_tag = await response.parse()
            assert_matches_type(Optional[AccountTagUpdateResponse], account_tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.resource_tagging.account_tags.with_raw_response.update(
                account_id="",
                resource_id="023e105f4ecef8ad9ca31a8372d0c353",
                resource_type="worker",
                worker_id="3f72a691-44b3-4c11-8642-c18a88ddaa5e",
            )

    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        account_tag = await async_client.resource_tagging.account_tags.update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="worker",
        )
        assert_matches_type(Optional[AccountTagUpdateResponse], account_tag, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        account_tag = await async_client.resource_tagging.account_tags.update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="worker",
            tags={
                "environment": "production",
                "team": "engineering",
            },
            if_match='"v1:RBNvo1WzZ4oRRq0W9-hkng"',
        )
        assert_matches_type(Optional[AccountTagUpdateResponse], account_tag, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.resource_tagging.account_tags.with_raw_response.update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="worker",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_tag = await response.parse()
        assert_matches_type(Optional[AccountTagUpdateResponse], account_tag, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.resource_tagging.account_tags.with_streaming_response.update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="worker",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_tag = await response.parse()
            assert_matches_type(Optional[AccountTagUpdateResponse], account_tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.resource_tagging.account_tags.with_raw_response.update(
                account_id="",
                resource_id="023e105f4ecef8ad9ca31a8372d0c353",
                resource_type="worker",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        account_tag = await async_client.resource_tagging.account_tags.delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert account_tag is None

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        account_tag = await async_client.resource_tagging.account_tags.delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            if_match='"v1:RBNvo1WzZ4oRRq0W9-hkng"',
        )
        assert account_tag is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.resource_tagging.account_tags.with_raw_response.delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_tag = await response.parse()
        assert account_tag is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.resource_tagging.account_tags.with_streaming_response.delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_tag = await response.parse()
            assert account_tag is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.resource_tagging.account_tags.with_raw_response.delete(
                account_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        account_tag = await async_client.resource_tagging.account_tags.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="worker",
        )
        assert_matches_type(Optional[AccountTagGetResponse], account_tag, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        account_tag = await async_client.resource_tagging.account_tags.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="worker",
            worker_id="3f72a691-44b3-4c11-8642-c18a88ddaa5e",
        )
        assert_matches_type(Optional[AccountTagGetResponse], account_tag, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.resource_tagging.account_tags.with_raw_response.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="worker",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_tag = await response.parse()
        assert_matches_type(Optional[AccountTagGetResponse], account_tag, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.resource_tagging.account_tags.with_streaming_response.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="worker",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_tag = await response.parse()
            assert_matches_type(Optional[AccountTagGetResponse], account_tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.resource_tagging.account_tags.with_raw_response.get(
                account_id="",
                resource_id="023e105f4ecef8ad9ca31a8372d0c353",
                resource_type="worker",
            )
