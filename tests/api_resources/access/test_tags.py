# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.access import (
    TagGetResponse,
    TagListResponse,
    TagCreateResponse,
    TagDeleteResponse,
    TagUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        tag = client.access.tags.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            name="engineers",
        )
        assert_matches_type(TagCreateResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.access.tags.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            name="engineers",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagCreateResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.access.tags.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            name="engineers",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagCreateResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.access.tags.with_raw_response.create(
                "",
                name="engineers",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        tag = client.access.tags.update(
            "engineers",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            name="engineers",
        )
        assert_matches_type(TagUpdateResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.access.tags.with_raw_response.update(
            "engineers",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            name="engineers",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagUpdateResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.access.tags.with_streaming_response.update(
            "engineers",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            name="engineers",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagUpdateResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.access.tags.with_raw_response.update(
                "engineers",
                identifier="",
                name="engineers",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_name` but received ''"):
            client.access.tags.with_raw_response.update(
                "",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
                name="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        tag = client.access.tags.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[TagListResponse], tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.access.tags.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(Optional[TagListResponse], tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.access.tags.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(Optional[TagListResponse], tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.access.tags.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        tag = client.access.tags.delete(
            "engineers",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(TagDeleteResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.access.tags.with_raw_response.delete(
            "engineers",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagDeleteResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.access.tags.with_streaming_response.delete(
            "engineers",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagDeleteResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.access.tags.with_raw_response.delete(
                "engineers",
                identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.access.tags.with_raw_response.delete(
                "",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        tag = client.access.tags.get(
            "engineers",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(TagGetResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.access.tags.with_raw_response.get(
            "engineers",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagGetResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.access.tags.with_streaming_response.get(
            "engineers",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagGetResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.access.tags.with_raw_response.get(
                "engineers",
                identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.access.tags.with_raw_response.get(
                "",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncTags:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        tag = await async_client.access.tags.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            name="engineers",
        )
        assert_matches_type(TagCreateResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.tags.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            name="engineers",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagCreateResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.tags.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            name="engineers",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagCreateResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.access.tags.with_raw_response.create(
                "",
                name="engineers",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        tag = await async_client.access.tags.update(
            "engineers",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            name="engineers",
        )
        assert_matches_type(TagUpdateResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.tags.with_raw_response.update(
            "engineers",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            name="engineers",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagUpdateResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.tags.with_streaming_response.update(
            "engineers",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            name="engineers",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagUpdateResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.access.tags.with_raw_response.update(
                "engineers",
                identifier="",
                name="engineers",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_name` but received ''"):
            await async_client.access.tags.with_raw_response.update(
                "",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
                name="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        tag = await async_client.access.tags.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[TagListResponse], tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.tags.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(Optional[TagListResponse], tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.tags.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(Optional[TagListResponse], tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.access.tags.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        tag = await async_client.access.tags.delete(
            "engineers",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(TagDeleteResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.tags.with_raw_response.delete(
            "engineers",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagDeleteResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.tags.with_streaming_response.delete(
            "engineers",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagDeleteResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.access.tags.with_raw_response.delete(
                "engineers",
                identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.access.tags.with_raw_response.delete(
                "",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        tag = await async_client.access.tags.get(
            "engineers",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(TagGetResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.tags.with_raw_response.get(
            "engineers",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagGetResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.tags.with_streaming_response.get(
            "engineers",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagGetResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.access.tags.with_raw_response.get(
                "engineers",
                identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.access.tags.with_raw_response.get(
                "",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )
