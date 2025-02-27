# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.hyperdrive import Hyperdrive

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfigs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        config = client.hyperdrive.configs.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example-hyperdrive",
            origin={
                "database": "postgres",
                "host": "database.example.com",
                "password": "password",
                "port": 5432,
                "scheme": "postgres",
                "user": "postgres",
            },
        )
        assert_matches_type(Hyperdrive, config, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        config = client.hyperdrive.configs.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example-hyperdrive",
            origin={
                "database": "postgres",
                "host": "database.example.com",
                "password": "password",
                "port": 5432,
                "scheme": "postgres",
                "user": "postgres",
            },
            caching={"disabled": True},
        )
        assert_matches_type(Hyperdrive, config, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.hyperdrive.configs.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example-hyperdrive",
            origin={
                "database": "postgres",
                "host": "database.example.com",
                "password": "password",
                "port": 5432,
                "scheme": "postgres",
                "user": "postgres",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(Hyperdrive, config, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.hyperdrive.configs.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example-hyperdrive",
            origin={
                "database": "postgres",
                "host": "database.example.com",
                "password": "password",
                "port": 5432,
                "scheme": "postgres",
                "user": "postgres",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(Hyperdrive, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.hyperdrive.configs.with_raw_response.create(
                account_id="",
                name="example-hyperdrive",
                origin={
                    "database": "postgres",
                    "host": "database.example.com",
                    "password": "password",
                    "port": 5432,
                    "scheme": "postgres",
                    "user": "postgres",
                },
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        config = client.hyperdrive.configs.update(
            hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example-hyperdrive",
            origin={
                "database": "postgres",
                "host": "database.example.com",
                "password": "password",
                "port": 5432,
                "scheme": "postgres",
                "user": "postgres",
            },
        )
        assert_matches_type(Hyperdrive, config, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        config = client.hyperdrive.configs.update(
            hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example-hyperdrive",
            origin={
                "database": "postgres",
                "host": "database.example.com",
                "password": "password",
                "port": 5432,
                "scheme": "postgres",
                "user": "postgres",
            },
            caching={"disabled": True},
        )
        assert_matches_type(Hyperdrive, config, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.hyperdrive.configs.with_raw_response.update(
            hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example-hyperdrive",
            origin={
                "database": "postgres",
                "host": "database.example.com",
                "password": "password",
                "port": 5432,
                "scheme": "postgres",
                "user": "postgres",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(Hyperdrive, config, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.hyperdrive.configs.with_streaming_response.update(
            hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example-hyperdrive",
            origin={
                "database": "postgres",
                "host": "database.example.com",
                "password": "password",
                "port": 5432,
                "scheme": "postgres",
                "user": "postgres",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(Hyperdrive, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.hyperdrive.configs.with_raw_response.update(
                hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                name="example-hyperdrive",
                origin={
                    "database": "postgres",
                    "host": "database.example.com",
                    "password": "password",
                    "port": 5432,
                    "scheme": "postgres",
                    "user": "postgres",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hyperdrive_id` but received ''"):
            client.hyperdrive.configs.with_raw_response.update(
                hyperdrive_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example-hyperdrive",
                origin={
                    "database": "postgres",
                    "host": "database.example.com",
                    "password": "password",
                    "port": 5432,
                    "scheme": "postgres",
                    "user": "postgres",
                },
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        config = client.hyperdrive.configs.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[Hyperdrive], config, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.hyperdrive.configs.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(SyncSinglePage[Hyperdrive], config, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.hyperdrive.configs.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(SyncSinglePage[Hyperdrive], config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.hyperdrive.configs.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        config = client.hyperdrive.configs.delete(
            hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, config, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.hyperdrive.configs.with_raw_response.delete(
            hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.hyperdrive.configs.with_streaming_response.delete(
            hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.hyperdrive.configs.with_raw_response.delete(
                hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hyperdrive_id` but received ''"):
            client.hyperdrive.configs.with_raw_response.delete(
                hyperdrive_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        config = client.hyperdrive.configs.edit(
            hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Hyperdrive, config, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        config = client.hyperdrive.configs.edit(
            hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            caching={"disabled": True},
            name="example-hyperdrive",
            origin={
                "database": "postgres",
                "scheme": "postgres",
                "user": "postgres",
            },
        )
        assert_matches_type(Hyperdrive, config, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.hyperdrive.configs.with_raw_response.edit(
            hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(Hyperdrive, config, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.hyperdrive.configs.with_streaming_response.edit(
            hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(Hyperdrive, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.hyperdrive.configs.with_raw_response.edit(
                hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hyperdrive_id` but received ''"):
            client.hyperdrive.configs.with_raw_response.edit(
                hyperdrive_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        config = client.hyperdrive.configs.get(
            hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Hyperdrive, config, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.hyperdrive.configs.with_raw_response.get(
            hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(Hyperdrive, config, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.hyperdrive.configs.with_streaming_response.get(
            hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(Hyperdrive, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.hyperdrive.configs.with_raw_response.get(
                hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hyperdrive_id` but received ''"):
            client.hyperdrive.configs.with_raw_response.get(
                hyperdrive_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncConfigs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.hyperdrive.configs.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example-hyperdrive",
            origin={
                "database": "postgres",
                "host": "database.example.com",
                "password": "password",
                "port": 5432,
                "scheme": "postgres",
                "user": "postgres",
            },
        )
        assert_matches_type(Hyperdrive, config, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.hyperdrive.configs.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example-hyperdrive",
            origin={
                "database": "postgres",
                "host": "database.example.com",
                "password": "password",
                "port": 5432,
                "scheme": "postgres",
                "user": "postgres",
            },
            caching={"disabled": True},
        )
        assert_matches_type(Hyperdrive, config, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.hyperdrive.configs.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example-hyperdrive",
            origin={
                "database": "postgres",
                "host": "database.example.com",
                "password": "password",
                "port": 5432,
                "scheme": "postgres",
                "user": "postgres",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(Hyperdrive, config, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.hyperdrive.configs.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example-hyperdrive",
            origin={
                "database": "postgres",
                "host": "database.example.com",
                "password": "password",
                "port": 5432,
                "scheme": "postgres",
                "user": "postgres",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(Hyperdrive, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.hyperdrive.configs.with_raw_response.create(
                account_id="",
                name="example-hyperdrive",
                origin={
                    "database": "postgres",
                    "host": "database.example.com",
                    "password": "password",
                    "port": 5432,
                    "scheme": "postgres",
                    "user": "postgres",
                },
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.hyperdrive.configs.update(
            hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example-hyperdrive",
            origin={
                "database": "postgres",
                "host": "database.example.com",
                "password": "password",
                "port": 5432,
                "scheme": "postgres",
                "user": "postgres",
            },
        )
        assert_matches_type(Hyperdrive, config, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.hyperdrive.configs.update(
            hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example-hyperdrive",
            origin={
                "database": "postgres",
                "host": "database.example.com",
                "password": "password",
                "port": 5432,
                "scheme": "postgres",
                "user": "postgres",
            },
            caching={"disabled": True},
        )
        assert_matches_type(Hyperdrive, config, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.hyperdrive.configs.with_raw_response.update(
            hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example-hyperdrive",
            origin={
                "database": "postgres",
                "host": "database.example.com",
                "password": "password",
                "port": 5432,
                "scheme": "postgres",
                "user": "postgres",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(Hyperdrive, config, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.hyperdrive.configs.with_streaming_response.update(
            hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example-hyperdrive",
            origin={
                "database": "postgres",
                "host": "database.example.com",
                "password": "password",
                "port": 5432,
                "scheme": "postgres",
                "user": "postgres",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(Hyperdrive, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.hyperdrive.configs.with_raw_response.update(
                hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                name="example-hyperdrive",
                origin={
                    "database": "postgres",
                    "host": "database.example.com",
                    "password": "password",
                    "port": 5432,
                    "scheme": "postgres",
                    "user": "postgres",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hyperdrive_id` but received ''"):
            await async_client.hyperdrive.configs.with_raw_response.update(
                hyperdrive_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example-hyperdrive",
                origin={
                    "database": "postgres",
                    "host": "database.example.com",
                    "password": "password",
                    "port": 5432,
                    "scheme": "postgres",
                    "user": "postgres",
                },
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.hyperdrive.configs.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[Hyperdrive], config, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.hyperdrive.configs.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(AsyncSinglePage[Hyperdrive], config, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.hyperdrive.configs.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(AsyncSinglePage[Hyperdrive], config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.hyperdrive.configs.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.hyperdrive.configs.delete(
            hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, config, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.hyperdrive.configs.with_raw_response.delete(
            hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.hyperdrive.configs.with_streaming_response.delete(
            hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.hyperdrive.configs.with_raw_response.delete(
                hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hyperdrive_id` but received ''"):
            await async_client.hyperdrive.configs.with_raw_response.delete(
                hyperdrive_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.hyperdrive.configs.edit(
            hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Hyperdrive, config, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.hyperdrive.configs.edit(
            hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            caching={"disabled": True},
            name="example-hyperdrive",
            origin={
                "database": "postgres",
                "scheme": "postgres",
                "user": "postgres",
            },
        )
        assert_matches_type(Hyperdrive, config, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.hyperdrive.configs.with_raw_response.edit(
            hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(Hyperdrive, config, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.hyperdrive.configs.with_streaming_response.edit(
            hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(Hyperdrive, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.hyperdrive.configs.with_raw_response.edit(
                hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hyperdrive_id` but received ''"):
            await async_client.hyperdrive.configs.with_raw_response.edit(
                hyperdrive_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.hyperdrive.configs.get(
            hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Hyperdrive, config, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.hyperdrive.configs.with_raw_response.get(
            hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(Hyperdrive, config, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.hyperdrive.configs.with_streaming_response.get(
            hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(Hyperdrive, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.hyperdrive.configs.with_raw_response.get(
                hyperdrive_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hyperdrive_id` but received ''"):
            await async_client.hyperdrive.configs.with_raw_response.get(
                hyperdrive_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
