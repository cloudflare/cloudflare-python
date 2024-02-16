# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import (
    FilterGetResponse,
    FilterDeleteResponse,
    FilterUpdateResponse,
    FilterFiltersListFiltersResponse,
    FilterFiltersCreateFiltersResponse,
    FilterFiltersUpdateFiltersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFilters:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        filter = client.filters.update(
            "372e67954025e0ba6aaa6d586b9e0b61",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[FilterUpdateResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.filters.with_raw_response.update(
            "372e67954025e0ba6aaa6d586b9e0b61",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = response.parse()
        assert_matches_type(Optional[FilterUpdateResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.filters.with_streaming_response.update(
            "372e67954025e0ba6aaa6d586b9e0b61",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter = response.parse()
            assert_matches_type(Optional[FilterUpdateResponse], filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.filters.with_raw_response.update(
                "372e67954025e0ba6aaa6d586b9e0b61",
                zone_identifier="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.filters.with_raw_response.update(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        filter = client.filters.delete(
            "372e67954025e0ba6aaa6d586b9e0b61",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[FilterDeleteResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.filters.with_raw_response.delete(
            "372e67954025e0ba6aaa6d586b9e0b61",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = response.parse()
        assert_matches_type(Optional[FilterDeleteResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.filters.with_streaming_response.delete(
            "372e67954025e0ba6aaa6d586b9e0b61",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter = response.parse()
            assert_matches_type(Optional[FilterDeleteResponse], filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.filters.with_raw_response.delete(
                "372e67954025e0ba6aaa6d586b9e0b61",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.filters.with_raw_response.delete(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_filters_create_filters(self, client: Cloudflare) -> None:
        filter = client.filters.filters_create_filters(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[FilterFiltersCreateFiltersResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_filters_create_filters(self, client: Cloudflare) -> None:
        response = client.filters.with_raw_response.filters_create_filters(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = response.parse()
        assert_matches_type(Optional[FilterFiltersCreateFiltersResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_filters_create_filters(self, client: Cloudflare) -> None:
        with client.filters.with_streaming_response.filters_create_filters(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter = response.parse()
            assert_matches_type(Optional[FilterFiltersCreateFiltersResponse], filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_filters_create_filters(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.filters.with_raw_response.filters_create_filters(
                "",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_filters_list_filters(self, client: Cloudflare) -> None:
        filter = client.filters.filters_list_filters(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[FilterFiltersListFiltersResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_filters_list_filters_with_all_params(self, client: Cloudflare) -> None:
        filter = client.filters.filters_list_filters(
            "023e105f4ecef8ad9ca31a8372d0c353",
            description="browsers",
            expression="php",
            page=1,
            paused=False,
            per_page=5,
            ref="FIL-100",
        )
        assert_matches_type(Optional[FilterFiltersListFiltersResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_filters_list_filters(self, client: Cloudflare) -> None:
        response = client.filters.with_raw_response.filters_list_filters(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = response.parse()
        assert_matches_type(Optional[FilterFiltersListFiltersResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_filters_list_filters(self, client: Cloudflare) -> None:
        with client.filters.with_streaming_response.filters_list_filters(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter = response.parse()
            assert_matches_type(Optional[FilterFiltersListFiltersResponse], filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_filters_list_filters(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.filters.with_raw_response.filters_list_filters(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_filters_update_filters(self, client: Cloudflare) -> None:
        filter = client.filters.filters_update_filters(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[FilterFiltersUpdateFiltersResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_filters_update_filters(self, client: Cloudflare) -> None:
        response = client.filters.with_raw_response.filters_update_filters(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = response.parse()
        assert_matches_type(Optional[FilterFiltersUpdateFiltersResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_filters_update_filters(self, client: Cloudflare) -> None:
        with client.filters.with_streaming_response.filters_update_filters(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter = response.parse()
            assert_matches_type(Optional[FilterFiltersUpdateFiltersResponse], filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_filters_update_filters(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.filters.with_raw_response.filters_update_filters(
                "",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        filter = client.filters.get(
            "372e67954025e0ba6aaa6d586b9e0b61",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[FilterGetResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.filters.with_raw_response.get(
            "372e67954025e0ba6aaa6d586b9e0b61",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = response.parse()
        assert_matches_type(Optional[FilterGetResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.filters.with_streaming_response.get(
            "372e67954025e0ba6aaa6d586b9e0b61",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter = response.parse()
            assert_matches_type(Optional[FilterGetResponse], filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.filters.with_raw_response.get(
                "372e67954025e0ba6aaa6d586b9e0b61",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.filters.with_raw_response.get(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncFilters:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        filter = await async_client.filters.update(
            "372e67954025e0ba6aaa6d586b9e0b61",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[FilterUpdateResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.filters.with_raw_response.update(
            "372e67954025e0ba6aaa6d586b9e0b61",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = await response.parse()
        assert_matches_type(Optional[FilterUpdateResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.filters.with_streaming_response.update(
            "372e67954025e0ba6aaa6d586b9e0b61",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter = await response.parse()
            assert_matches_type(Optional[FilterUpdateResponse], filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.filters.with_raw_response.update(
                "372e67954025e0ba6aaa6d586b9e0b61",
                zone_identifier="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.filters.with_raw_response.update(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        filter = await async_client.filters.delete(
            "372e67954025e0ba6aaa6d586b9e0b61",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[FilterDeleteResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.filters.with_raw_response.delete(
            "372e67954025e0ba6aaa6d586b9e0b61",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = await response.parse()
        assert_matches_type(Optional[FilterDeleteResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.filters.with_streaming_response.delete(
            "372e67954025e0ba6aaa6d586b9e0b61",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter = await response.parse()
            assert_matches_type(Optional[FilterDeleteResponse], filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.filters.with_raw_response.delete(
                "372e67954025e0ba6aaa6d586b9e0b61",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.filters.with_raw_response.delete(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_filters_create_filters(self, async_client: AsyncCloudflare) -> None:
        filter = await async_client.filters.filters_create_filters(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[FilterFiltersCreateFiltersResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_filters_create_filters(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.filters.with_raw_response.filters_create_filters(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = await response.parse()
        assert_matches_type(Optional[FilterFiltersCreateFiltersResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_filters_create_filters(self, async_client: AsyncCloudflare) -> None:
        async with async_client.filters.with_streaming_response.filters_create_filters(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter = await response.parse()
            assert_matches_type(Optional[FilterFiltersCreateFiltersResponse], filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_filters_create_filters(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.filters.with_raw_response.filters_create_filters(
                "",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_filters_list_filters(self, async_client: AsyncCloudflare) -> None:
        filter = await async_client.filters.filters_list_filters(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[FilterFiltersListFiltersResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_filters_list_filters_with_all_params(self, async_client: AsyncCloudflare) -> None:
        filter = await async_client.filters.filters_list_filters(
            "023e105f4ecef8ad9ca31a8372d0c353",
            description="browsers",
            expression="php",
            page=1,
            paused=False,
            per_page=5,
            ref="FIL-100",
        )
        assert_matches_type(Optional[FilterFiltersListFiltersResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_filters_list_filters(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.filters.with_raw_response.filters_list_filters(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = await response.parse()
        assert_matches_type(Optional[FilterFiltersListFiltersResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_filters_list_filters(self, async_client: AsyncCloudflare) -> None:
        async with async_client.filters.with_streaming_response.filters_list_filters(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter = await response.parse()
            assert_matches_type(Optional[FilterFiltersListFiltersResponse], filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_filters_list_filters(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.filters.with_raw_response.filters_list_filters(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_filters_update_filters(self, async_client: AsyncCloudflare) -> None:
        filter = await async_client.filters.filters_update_filters(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[FilterFiltersUpdateFiltersResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_filters_update_filters(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.filters.with_raw_response.filters_update_filters(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = await response.parse()
        assert_matches_type(Optional[FilterFiltersUpdateFiltersResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_filters_update_filters(self, async_client: AsyncCloudflare) -> None:
        async with async_client.filters.with_streaming_response.filters_update_filters(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter = await response.parse()
            assert_matches_type(Optional[FilterFiltersUpdateFiltersResponse], filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_filters_update_filters(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.filters.with_raw_response.filters_update_filters(
                "",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        filter = await async_client.filters.get(
            "372e67954025e0ba6aaa6d586b9e0b61",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[FilterGetResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.filters.with_raw_response.get(
            "372e67954025e0ba6aaa6d586b9e0b61",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = await response.parse()
        assert_matches_type(Optional[FilterGetResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.filters.with_streaming_response.get(
            "372e67954025e0ba6aaa6d586b9e0b61",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter = await response.parse()
            assert_matches_type(Optional[FilterGetResponse], filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.filters.with_raw_response.get(
                "372e67954025e0ba6aaa6d586b9e0b61",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.filters.with_raw_response.get(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )
