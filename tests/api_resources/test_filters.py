# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage, SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.filters import FirewallFilter

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFilters:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            filter = client.filters.create(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                expression='(http.request.uri.path ~ ".*wp-login.php" or http.request.uri.path ~ ".*xmlrpc.php") and ip.addr ne 172.16.22.155',
            )

        assert_matches_type(SyncSinglePage[FirewallFilter], filter, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.filters.with_raw_response.create(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                expression='(http.request.uri.path ~ ".*wp-login.php" or http.request.uri.path ~ ".*xmlrpc.php") and ip.addr ne 172.16.22.155',
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = response.parse()
        assert_matches_type(SyncSinglePage[FirewallFilter], filter, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.filters.with_streaming_response.create(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                expression='(http.request.uri.path ~ ".*wp-login.php" or http.request.uri.path ~ ".*xmlrpc.php") and ip.addr ne 172.16.22.155',
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                filter = response.parse()
                assert_matches_type(SyncSinglePage[FirewallFilter], filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                client.filters.with_raw_response.create(
                    zone_id="",
                    expression='(http.request.uri.path ~ ".*wp-login.php" or http.request.uri.path ~ ".*xmlrpc.php") and ip.addr ne 172.16.22.155',
                )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            filter = client.filters.update(
                filter_id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert_matches_type(FirewallFilter, filter, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.filters.with_raw_response.update(
                filter_id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = response.parse()
        assert_matches_type(FirewallFilter, filter, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.filters.with_streaming_response.update(
                filter_id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                filter = response.parse()
                assert_matches_type(FirewallFilter, filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                client.filters.with_raw_response.update(
                    filter_id="372e67954025e0ba6aaa6d586b9e0b61",
                    zone_id="",
                    body={},
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `filter_id` but received ''"):
                client.filters.with_raw_response.update(
                    filter_id="",
                    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                    body={},
                )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            filter = client.filters.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(SyncV4PagePaginationArray[FirewallFilter], filter, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            filter = client.filters.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="372e67954025e0ba6aaa6d586b9e0b61",
                description="browsers",
                expression="php",
                page=1,
                paused=False,
                per_page=5,
                ref="FIL-100",
            )

        assert_matches_type(SyncV4PagePaginationArray[FirewallFilter], filter, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.filters.with_raw_response.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[FirewallFilter], filter, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.filters.with_streaming_response.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                filter = response.parse()
                assert_matches_type(SyncV4PagePaginationArray[FirewallFilter], filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                client.filters.with_raw_response.list(
                    zone_id="",
                )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            filter = client.filters.delete(
                filter_id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(FirewallFilter, filter, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.filters.with_raw_response.delete(
                filter_id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = response.parse()
        assert_matches_type(FirewallFilter, filter, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.filters.with_streaming_response.delete(
                filter_id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                filter = response.parse()
                assert_matches_type(FirewallFilter, filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                client.filters.with_raw_response.delete(
                    filter_id="372e67954025e0ba6aaa6d586b9e0b61",
                    zone_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `filter_id` but received ''"):
                client.filters.with_raw_response.delete(
                    filter_id="",
                    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                )

    @parametrize
    def test_method_bulk_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            filter = client.filters.bulk_delete(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(SyncSinglePage[FirewallFilter], filter, path=["response"])

    @parametrize
    def test_raw_response_bulk_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.filters.with_raw_response.bulk_delete(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = response.parse()
        assert_matches_type(SyncSinglePage[FirewallFilter], filter, path=["response"])

    @parametrize
    def test_streaming_response_bulk_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.filters.with_streaming_response.bulk_delete(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                filter = response.parse()
                assert_matches_type(SyncSinglePage[FirewallFilter], filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_bulk_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                client.filters.with_raw_response.bulk_delete(
                    zone_id="",
                )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_bulk_update(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            filter = client.filters.bulk_update(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(SyncSinglePage[FirewallFilter], filter, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_bulk_update(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.filters.with_raw_response.bulk_update(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = response.parse()
        assert_matches_type(SyncSinglePage[FirewallFilter], filter, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_bulk_update(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.filters.with_streaming_response.bulk_update(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                filter = response.parse()
                assert_matches_type(SyncSinglePage[FirewallFilter], filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_bulk_update(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                client.filters.with_raw_response.bulk_update(
                    zone_id="",
                )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            filter = client.filters.get(
                filter_id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(FirewallFilter, filter, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.filters.with_raw_response.get(
                filter_id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = response.parse()
        assert_matches_type(FirewallFilter, filter, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.filters.with_streaming_response.get(
                filter_id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                filter = response.parse()
                assert_matches_type(FirewallFilter, filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                client.filters.with_raw_response.get(
                    filter_id="372e67954025e0ba6aaa6d586b9e0b61",
                    zone_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `filter_id` but received ''"):
                client.filters.with_raw_response.get(
                    filter_id="",
                    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                )


class TestAsyncFilters:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            filter = await async_client.filters.create(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                expression='(http.request.uri.path ~ ".*wp-login.php" or http.request.uri.path ~ ".*xmlrpc.php") and ip.addr ne 172.16.22.155',
            )

        assert_matches_type(AsyncSinglePage[FirewallFilter], filter, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.filters.with_raw_response.create(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                expression='(http.request.uri.path ~ ".*wp-login.php" or http.request.uri.path ~ ".*xmlrpc.php") and ip.addr ne 172.16.22.155',
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = await response.parse()
        assert_matches_type(AsyncSinglePage[FirewallFilter], filter, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.filters.with_streaming_response.create(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                expression='(http.request.uri.path ~ ".*wp-login.php" or http.request.uri.path ~ ".*xmlrpc.php") and ip.addr ne 172.16.22.155',
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                filter = await response.parse()
                assert_matches_type(AsyncSinglePage[FirewallFilter], filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                await async_client.filters.with_raw_response.create(
                    zone_id="",
                    expression='(http.request.uri.path ~ ".*wp-login.php" or http.request.uri.path ~ ".*xmlrpc.php") and ip.addr ne 172.16.22.155',
                )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            filter = await async_client.filters.update(
                filter_id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert_matches_type(FirewallFilter, filter, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.filters.with_raw_response.update(
                filter_id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = await response.parse()
        assert_matches_type(FirewallFilter, filter, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.filters.with_streaming_response.update(
                filter_id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                filter = await response.parse()
                assert_matches_type(FirewallFilter, filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                await async_client.filters.with_raw_response.update(
                    filter_id="372e67954025e0ba6aaa6d586b9e0b61",
                    zone_id="",
                    body={},
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `filter_id` but received ''"):
                await async_client.filters.with_raw_response.update(
                    filter_id="",
                    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                    body={},
                )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            filter = await async_client.filters.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(AsyncV4PagePaginationArray[FirewallFilter], filter, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            filter = await async_client.filters.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="372e67954025e0ba6aaa6d586b9e0b61",
                description="browsers",
                expression="php",
                page=1,
                paused=False,
                per_page=5,
                ref="FIL-100",
            )

        assert_matches_type(AsyncV4PagePaginationArray[FirewallFilter], filter, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.filters.with_raw_response.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[FirewallFilter], filter, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.filters.with_streaming_response.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                filter = await response.parse()
                assert_matches_type(AsyncV4PagePaginationArray[FirewallFilter], filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                await async_client.filters.with_raw_response.list(
                    zone_id="",
                )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            filter = await async_client.filters.delete(
                filter_id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(FirewallFilter, filter, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.filters.with_raw_response.delete(
                filter_id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = await response.parse()
        assert_matches_type(FirewallFilter, filter, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.filters.with_streaming_response.delete(
                filter_id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                filter = await response.parse()
                assert_matches_type(FirewallFilter, filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                await async_client.filters.with_raw_response.delete(
                    filter_id="372e67954025e0ba6aaa6d586b9e0b61",
                    zone_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `filter_id` but received ''"):
                await async_client.filters.with_raw_response.delete(
                    filter_id="",
                    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                )

    @parametrize
    async def test_method_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            filter = await async_client.filters.bulk_delete(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(AsyncSinglePage[FirewallFilter], filter, path=["response"])

    @parametrize
    async def test_raw_response_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.filters.with_raw_response.bulk_delete(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = await response.parse()
        assert_matches_type(AsyncSinglePage[FirewallFilter], filter, path=["response"])

    @parametrize
    async def test_streaming_response_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.filters.with_streaming_response.bulk_delete(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                filter = await response.parse()
                assert_matches_type(AsyncSinglePage[FirewallFilter], filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                await async_client.filters.with_raw_response.bulk_delete(
                    zone_id="",
                )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_bulk_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            filter = await async_client.filters.bulk_update(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(AsyncSinglePage[FirewallFilter], filter, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_bulk_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.filters.with_raw_response.bulk_update(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = await response.parse()
        assert_matches_type(AsyncSinglePage[FirewallFilter], filter, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_bulk_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.filters.with_streaming_response.bulk_update(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                filter = await response.parse()
                assert_matches_type(AsyncSinglePage[FirewallFilter], filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_bulk_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                await async_client.filters.with_raw_response.bulk_update(
                    zone_id="",
                )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            filter = await async_client.filters.get(
                filter_id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(FirewallFilter, filter, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.filters.with_raw_response.get(
                filter_id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = await response.parse()
        assert_matches_type(FirewallFilter, filter, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.filters.with_streaming_response.get(
                filter_id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                filter = await response.parse()
                assert_matches_type(FirewallFilter, filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                await async_client.filters.with_raw_response.get(
                    filter_id="372e67954025e0ba6aaa6d586b9e0b61",
                    zone_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `filter_id` but received ''"):
                await async_client.filters.with_raw_response.get(
                    filter_id="",
                    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                )
