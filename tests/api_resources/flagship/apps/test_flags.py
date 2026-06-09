# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncCursorPaginationAfter, AsyncCursorPaginationAfter
from cloudflare.types.flagship.apps import (
    FlagGetResponse,
    FlagListResponse,
    FlagCreateResponse,
    FlagDeleteResponse,
    FlagUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFlags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        flag = client.flagship.apps.flags.create(
            app_id="app_id",
            account_id="account_id",
            default_variation="x",
            enabled=True,
            key="x",
            rules=[
                {
                    "conditions": [
                        {
                            "attribute": "x",
                            "operator": "equals",
                            "value": {},
                        }
                    ],
                    "priority": 1,
                    "serve_variation": "x",
                }
            ],
            variations={"foo": "string"},
        )
        assert_matches_type(FlagCreateResponse, flag, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        flag = client.flagship.apps.flags.create(
            app_id="app_id",
            account_id="account_id",
            default_variation="x",
            enabled=True,
            key="x",
            rules=[
                {
                    "conditions": [
                        {
                            "attribute": "x",
                            "operator": "equals",
                            "value": {},
                        }
                    ],
                    "priority": 1,
                    "serve_variation": "x",
                    "rollout": {
                        "percentage": 0,
                        "attribute": "x",
                    },
                }
            ],
            variations={"foo": "string"},
            description="description",
            type="boolean",
        )
        assert_matches_type(FlagCreateResponse, flag, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.flagship.apps.flags.with_raw_response.create(
            app_id="app_id",
            account_id="account_id",
            default_variation="x",
            enabled=True,
            key="x",
            rules=[
                {
                    "conditions": [
                        {
                            "attribute": "x",
                            "operator": "equals",
                            "value": {},
                        }
                    ],
                    "priority": 1,
                    "serve_variation": "x",
                }
            ],
            variations={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flag = response.parse()
        assert_matches_type(FlagCreateResponse, flag, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.flagship.apps.flags.with_streaming_response.create(
            app_id="app_id",
            account_id="account_id",
            default_variation="x",
            enabled=True,
            key="x",
            rules=[
                {
                    "conditions": [
                        {
                            "attribute": "x",
                            "operator": "equals",
                            "value": {},
                        }
                    ],
                    "priority": 1,
                    "serve_variation": "x",
                }
            ],
            variations={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flag = response.parse()
            assert_matches_type(FlagCreateResponse, flag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.flagship.apps.flags.with_raw_response.create(
                app_id="app_id",
                account_id="",
                default_variation="x",
                enabled=True,
                key="x",
                rules=[
                    {
                        "conditions": [
                            {
                                "attribute": "x",
                                "operator": "equals",
                                "value": {},
                            }
                        ],
                        "priority": 1,
                        "serve_variation": "x",
                    }
                ],
                variations={"foo": "string"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.flagship.apps.flags.with_raw_response.create(
                app_id="",
                account_id="account_id",
                default_variation="x",
                enabled=True,
                key="x",
                rules=[
                    {
                        "conditions": [
                            {
                                "attribute": "x",
                                "operator": "equals",
                                "value": {},
                            }
                        ],
                        "priority": 1,
                        "serve_variation": "x",
                    }
                ],
                variations={"foo": "string"},
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        flag = client.flagship.apps.flags.update(
            flag_key="flag_key",
            account_id="account_id",
            app_id="app_id",
            default_variation="x",
            enabled=True,
            key="x",
            rules=[
                {
                    "conditions": [
                        {
                            "attribute": "x",
                            "operator": "equals",
                            "value": {},
                        }
                    ],
                    "priority": 1,
                    "serve_variation": "x",
                }
            ],
            variations={"foo": "string"},
        )
        assert_matches_type(FlagUpdateResponse, flag, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        flag = client.flagship.apps.flags.update(
            flag_key="flag_key",
            account_id="account_id",
            app_id="app_id",
            default_variation="x",
            enabled=True,
            key="x",
            rules=[
                {
                    "conditions": [
                        {
                            "attribute": "x",
                            "operator": "equals",
                            "value": {},
                        }
                    ],
                    "priority": 1,
                    "serve_variation": "x",
                    "rollout": {
                        "percentage": 0,
                        "attribute": "x",
                    },
                }
            ],
            variations={"foo": "string"},
            description="description",
            type="boolean",
        )
        assert_matches_type(FlagUpdateResponse, flag, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.flagship.apps.flags.with_raw_response.update(
            flag_key="flag_key",
            account_id="account_id",
            app_id="app_id",
            default_variation="x",
            enabled=True,
            key="x",
            rules=[
                {
                    "conditions": [
                        {
                            "attribute": "x",
                            "operator": "equals",
                            "value": {},
                        }
                    ],
                    "priority": 1,
                    "serve_variation": "x",
                }
            ],
            variations={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flag = response.parse()
        assert_matches_type(FlagUpdateResponse, flag, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.flagship.apps.flags.with_streaming_response.update(
            flag_key="flag_key",
            account_id="account_id",
            app_id="app_id",
            default_variation="x",
            enabled=True,
            key="x",
            rules=[
                {
                    "conditions": [
                        {
                            "attribute": "x",
                            "operator": "equals",
                            "value": {},
                        }
                    ],
                    "priority": 1,
                    "serve_variation": "x",
                }
            ],
            variations={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flag = response.parse()
            assert_matches_type(FlagUpdateResponse, flag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.flagship.apps.flags.with_raw_response.update(
                flag_key="flag_key",
                account_id="",
                app_id="app_id",
                default_variation="x",
                enabled=True,
                key="x",
                rules=[
                    {
                        "conditions": [
                            {
                                "attribute": "x",
                                "operator": "equals",
                                "value": {},
                            }
                        ],
                        "priority": 1,
                        "serve_variation": "x",
                    }
                ],
                variations={"foo": "string"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.flagship.apps.flags.with_raw_response.update(
                flag_key="flag_key",
                account_id="account_id",
                app_id="",
                default_variation="x",
                enabled=True,
                key="x",
                rules=[
                    {
                        "conditions": [
                            {
                                "attribute": "x",
                                "operator": "equals",
                                "value": {},
                            }
                        ],
                        "priority": 1,
                        "serve_variation": "x",
                    }
                ],
                variations={"foo": "string"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flag_key` but received ''"):
            client.flagship.apps.flags.with_raw_response.update(
                flag_key="",
                account_id="account_id",
                app_id="app_id",
                default_variation="x",
                enabled=True,
                key="x",
                rules=[
                    {
                        "conditions": [
                            {
                                "attribute": "x",
                                "operator": "equals",
                                "value": {},
                            }
                        ],
                        "priority": 1,
                        "serve_variation": "x",
                    }
                ],
                variations={"foo": "string"},
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        flag = client.flagship.apps.flags.list(
            app_id="app_id",
            account_id="account_id",
        )
        assert_matches_type(SyncCursorPaginationAfter[FlagListResponse], flag, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        flag = client.flagship.apps.flags.list(
            app_id="app_id",
            account_id="account_id",
            cursor="cursor",
            limit="limit",
        )
        assert_matches_type(SyncCursorPaginationAfter[FlagListResponse], flag, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.flagship.apps.flags.with_raw_response.list(
            app_id="app_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flag = response.parse()
        assert_matches_type(SyncCursorPaginationAfter[FlagListResponse], flag, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.flagship.apps.flags.with_streaming_response.list(
            app_id="app_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flag = response.parse()
            assert_matches_type(SyncCursorPaginationAfter[FlagListResponse], flag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.flagship.apps.flags.with_raw_response.list(
                app_id="app_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.flagship.apps.flags.with_raw_response.list(
                app_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        flag = client.flagship.apps.flags.delete(
            flag_key="flag_key",
            account_id="account_id",
            app_id="app_id",
        )
        assert_matches_type(FlagDeleteResponse, flag, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.flagship.apps.flags.with_raw_response.delete(
            flag_key="flag_key",
            account_id="account_id",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flag = response.parse()
        assert_matches_type(FlagDeleteResponse, flag, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.flagship.apps.flags.with_streaming_response.delete(
            flag_key="flag_key",
            account_id="account_id",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flag = response.parse()
            assert_matches_type(FlagDeleteResponse, flag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.flagship.apps.flags.with_raw_response.delete(
                flag_key="flag_key",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.flagship.apps.flags.with_raw_response.delete(
                flag_key="flag_key",
                account_id="account_id",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flag_key` but received ''"):
            client.flagship.apps.flags.with_raw_response.delete(
                flag_key="",
                account_id="account_id",
                app_id="app_id",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        flag = client.flagship.apps.flags.get(
            flag_key="flag_key",
            account_id="account_id",
            app_id="app_id",
        )
        assert_matches_type(FlagGetResponse, flag, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.flagship.apps.flags.with_raw_response.get(
            flag_key="flag_key",
            account_id="account_id",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flag = response.parse()
        assert_matches_type(FlagGetResponse, flag, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.flagship.apps.flags.with_streaming_response.get(
            flag_key="flag_key",
            account_id="account_id",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flag = response.parse()
            assert_matches_type(FlagGetResponse, flag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.flagship.apps.flags.with_raw_response.get(
                flag_key="flag_key",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.flagship.apps.flags.with_raw_response.get(
                flag_key="flag_key",
                account_id="account_id",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flag_key` but received ''"):
            client.flagship.apps.flags.with_raw_response.get(
                flag_key="",
                account_id="account_id",
                app_id="app_id",
            )


class TestAsyncFlags:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        flag = await async_client.flagship.apps.flags.create(
            app_id="app_id",
            account_id="account_id",
            default_variation="x",
            enabled=True,
            key="x",
            rules=[
                {
                    "conditions": [
                        {
                            "attribute": "x",
                            "operator": "equals",
                            "value": {},
                        }
                    ],
                    "priority": 1,
                    "serve_variation": "x",
                }
            ],
            variations={"foo": "string"},
        )
        assert_matches_type(FlagCreateResponse, flag, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        flag = await async_client.flagship.apps.flags.create(
            app_id="app_id",
            account_id="account_id",
            default_variation="x",
            enabled=True,
            key="x",
            rules=[
                {
                    "conditions": [
                        {
                            "attribute": "x",
                            "operator": "equals",
                            "value": {},
                        }
                    ],
                    "priority": 1,
                    "serve_variation": "x",
                    "rollout": {
                        "percentage": 0,
                        "attribute": "x",
                    },
                }
            ],
            variations={"foo": "string"},
            description="description",
            type="boolean",
        )
        assert_matches_type(FlagCreateResponse, flag, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.flagship.apps.flags.with_raw_response.create(
            app_id="app_id",
            account_id="account_id",
            default_variation="x",
            enabled=True,
            key="x",
            rules=[
                {
                    "conditions": [
                        {
                            "attribute": "x",
                            "operator": "equals",
                            "value": {},
                        }
                    ],
                    "priority": 1,
                    "serve_variation": "x",
                }
            ],
            variations={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flag = await response.parse()
        assert_matches_type(FlagCreateResponse, flag, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.flagship.apps.flags.with_streaming_response.create(
            app_id="app_id",
            account_id="account_id",
            default_variation="x",
            enabled=True,
            key="x",
            rules=[
                {
                    "conditions": [
                        {
                            "attribute": "x",
                            "operator": "equals",
                            "value": {},
                        }
                    ],
                    "priority": 1,
                    "serve_variation": "x",
                }
            ],
            variations={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flag = await response.parse()
            assert_matches_type(FlagCreateResponse, flag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.flagship.apps.flags.with_raw_response.create(
                app_id="app_id",
                account_id="",
                default_variation="x",
                enabled=True,
                key="x",
                rules=[
                    {
                        "conditions": [
                            {
                                "attribute": "x",
                                "operator": "equals",
                                "value": {},
                            }
                        ],
                        "priority": 1,
                        "serve_variation": "x",
                    }
                ],
                variations={"foo": "string"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.flagship.apps.flags.with_raw_response.create(
                app_id="",
                account_id="account_id",
                default_variation="x",
                enabled=True,
                key="x",
                rules=[
                    {
                        "conditions": [
                            {
                                "attribute": "x",
                                "operator": "equals",
                                "value": {},
                            }
                        ],
                        "priority": 1,
                        "serve_variation": "x",
                    }
                ],
                variations={"foo": "string"},
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        flag = await async_client.flagship.apps.flags.update(
            flag_key="flag_key",
            account_id="account_id",
            app_id="app_id",
            default_variation="x",
            enabled=True,
            key="x",
            rules=[
                {
                    "conditions": [
                        {
                            "attribute": "x",
                            "operator": "equals",
                            "value": {},
                        }
                    ],
                    "priority": 1,
                    "serve_variation": "x",
                }
            ],
            variations={"foo": "string"},
        )
        assert_matches_type(FlagUpdateResponse, flag, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        flag = await async_client.flagship.apps.flags.update(
            flag_key="flag_key",
            account_id="account_id",
            app_id="app_id",
            default_variation="x",
            enabled=True,
            key="x",
            rules=[
                {
                    "conditions": [
                        {
                            "attribute": "x",
                            "operator": "equals",
                            "value": {},
                        }
                    ],
                    "priority": 1,
                    "serve_variation": "x",
                    "rollout": {
                        "percentage": 0,
                        "attribute": "x",
                    },
                }
            ],
            variations={"foo": "string"},
            description="description",
            type="boolean",
        )
        assert_matches_type(FlagUpdateResponse, flag, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.flagship.apps.flags.with_raw_response.update(
            flag_key="flag_key",
            account_id="account_id",
            app_id="app_id",
            default_variation="x",
            enabled=True,
            key="x",
            rules=[
                {
                    "conditions": [
                        {
                            "attribute": "x",
                            "operator": "equals",
                            "value": {},
                        }
                    ],
                    "priority": 1,
                    "serve_variation": "x",
                }
            ],
            variations={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flag = await response.parse()
        assert_matches_type(FlagUpdateResponse, flag, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.flagship.apps.flags.with_streaming_response.update(
            flag_key="flag_key",
            account_id="account_id",
            app_id="app_id",
            default_variation="x",
            enabled=True,
            key="x",
            rules=[
                {
                    "conditions": [
                        {
                            "attribute": "x",
                            "operator": "equals",
                            "value": {},
                        }
                    ],
                    "priority": 1,
                    "serve_variation": "x",
                }
            ],
            variations={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flag = await response.parse()
            assert_matches_type(FlagUpdateResponse, flag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.flagship.apps.flags.with_raw_response.update(
                flag_key="flag_key",
                account_id="",
                app_id="app_id",
                default_variation="x",
                enabled=True,
                key="x",
                rules=[
                    {
                        "conditions": [
                            {
                                "attribute": "x",
                                "operator": "equals",
                                "value": {},
                            }
                        ],
                        "priority": 1,
                        "serve_variation": "x",
                    }
                ],
                variations={"foo": "string"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.flagship.apps.flags.with_raw_response.update(
                flag_key="flag_key",
                account_id="account_id",
                app_id="",
                default_variation="x",
                enabled=True,
                key="x",
                rules=[
                    {
                        "conditions": [
                            {
                                "attribute": "x",
                                "operator": "equals",
                                "value": {},
                            }
                        ],
                        "priority": 1,
                        "serve_variation": "x",
                    }
                ],
                variations={"foo": "string"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flag_key` but received ''"):
            await async_client.flagship.apps.flags.with_raw_response.update(
                flag_key="",
                account_id="account_id",
                app_id="app_id",
                default_variation="x",
                enabled=True,
                key="x",
                rules=[
                    {
                        "conditions": [
                            {
                                "attribute": "x",
                                "operator": "equals",
                                "value": {},
                            }
                        ],
                        "priority": 1,
                        "serve_variation": "x",
                    }
                ],
                variations={"foo": "string"},
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        flag = await async_client.flagship.apps.flags.list(
            app_id="app_id",
            account_id="account_id",
        )
        assert_matches_type(AsyncCursorPaginationAfter[FlagListResponse], flag, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        flag = await async_client.flagship.apps.flags.list(
            app_id="app_id",
            account_id="account_id",
            cursor="cursor",
            limit="limit",
        )
        assert_matches_type(AsyncCursorPaginationAfter[FlagListResponse], flag, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.flagship.apps.flags.with_raw_response.list(
            app_id="app_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flag = await response.parse()
        assert_matches_type(AsyncCursorPaginationAfter[FlagListResponse], flag, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.flagship.apps.flags.with_streaming_response.list(
            app_id="app_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flag = await response.parse()
            assert_matches_type(AsyncCursorPaginationAfter[FlagListResponse], flag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.flagship.apps.flags.with_raw_response.list(
                app_id="app_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.flagship.apps.flags.with_raw_response.list(
                app_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        flag = await async_client.flagship.apps.flags.delete(
            flag_key="flag_key",
            account_id="account_id",
            app_id="app_id",
        )
        assert_matches_type(FlagDeleteResponse, flag, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.flagship.apps.flags.with_raw_response.delete(
            flag_key="flag_key",
            account_id="account_id",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flag = await response.parse()
        assert_matches_type(FlagDeleteResponse, flag, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.flagship.apps.flags.with_streaming_response.delete(
            flag_key="flag_key",
            account_id="account_id",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flag = await response.parse()
            assert_matches_type(FlagDeleteResponse, flag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.flagship.apps.flags.with_raw_response.delete(
                flag_key="flag_key",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.flagship.apps.flags.with_raw_response.delete(
                flag_key="flag_key",
                account_id="account_id",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flag_key` but received ''"):
            await async_client.flagship.apps.flags.with_raw_response.delete(
                flag_key="",
                account_id="account_id",
                app_id="app_id",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        flag = await async_client.flagship.apps.flags.get(
            flag_key="flag_key",
            account_id="account_id",
            app_id="app_id",
        )
        assert_matches_type(FlagGetResponse, flag, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.flagship.apps.flags.with_raw_response.get(
            flag_key="flag_key",
            account_id="account_id",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flag = await response.parse()
        assert_matches_type(FlagGetResponse, flag, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.flagship.apps.flags.with_streaming_response.get(
            flag_key="flag_key",
            account_id="account_id",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flag = await response.parse()
            assert_matches_type(FlagGetResponse, flag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.flagship.apps.flags.with_raw_response.get(
                flag_key="flag_key",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.flagship.apps.flags.with_raw_response.get(
                flag_key="flag_key",
                account_id="account_id",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flag_key` but received ''"):
            await async_client.flagship.apps.flags.with_raw_response.get(
                flag_key="",
                account_id="account_id",
                app_id="app_id",
            )
