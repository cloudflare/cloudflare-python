# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.dlp import Profile
from cloudflare.types.zero_trust.dlp.profiles import CustomCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustom:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Cloudflare) -> None:
        custom = client.zero_trust.dlp.profiles.custom.create(
            account_id="account_id",
            profiles=[
                {
                    "entries": [
                        {
                            "enabled": True,
                            "name": "name",
                            "pattern": {"regex": "regex"},
                        }
                    ],
                    "name": "name",
                }
            ],
        )
        assert_matches_type(Optional[CustomCreateResponse], custom, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.profiles.custom.with_raw_response.create(
            account_id="account_id",
            profiles=[
                {
                    "entries": [
                        {
                            "enabled": True,
                            "name": "name",
                            "pattern": {"regex": "regex"},
                        }
                    ],
                    "name": "name",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(Optional[CustomCreateResponse], custom, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.profiles.custom.with_streaming_response.create(
            account_id="account_id",
            profiles=[
                {
                    "entries": [
                        {
                            "enabled": True,
                            "name": "name",
                            "pattern": {"regex": "regex"},
                        }
                    ],
                    "name": "name",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(Optional[CustomCreateResponse], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.profiles.custom.with_raw_response.create(
                account_id="",
                profiles=[
                    {
                        "entries": [
                            {
                                "enabled": True,
                                "name": "name",
                                "pattern": {"regex": "regex"},
                            }
                        ],
                        "name": "name",
                    }
                ],
            )

    @parametrize
    def test_method_create_overload_2(self, client: Cloudflare) -> None:
        custom = client.zero_trust.dlp.profiles.custom.create(
            account_id="account_id",
            entries=[
                {
                    "enabled": True,
                    "name": "name",
                    "pattern": {"regex": "regex"},
                }
            ],
            name="name",
        )
        assert_matches_type(Optional[CustomCreateResponse], custom, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Cloudflare) -> None:
        custom = client.zero_trust.dlp.profiles.custom.create(
            account_id="account_id",
            entries=[
                {
                    "enabled": True,
                    "name": "name",
                    "pattern": {
                        "regex": "regex",
                        "validation": "luhn",
                    },
                }
            ],
            name="name",
            ai_context_enabled=True,
            allowed_match_count=5,
            confidence_threshold="confidence_threshold",
            context_awareness={
                "enabled": True,
                "skip": {"files": True},
            },
            description="description",
            ocr_enabled=True,
            shared_entries=[
                {
                    "enabled": True,
                    "entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "entry_type": "custom",
                }
            ],
        )
        assert_matches_type(Optional[CustomCreateResponse], custom, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.profiles.custom.with_raw_response.create(
            account_id="account_id",
            entries=[
                {
                    "enabled": True,
                    "name": "name",
                    "pattern": {"regex": "regex"},
                }
            ],
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(Optional[CustomCreateResponse], custom, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.profiles.custom.with_streaming_response.create(
            account_id="account_id",
            entries=[
                {
                    "enabled": True,
                    "name": "name",
                    "pattern": {"regex": "regex"},
                }
            ],
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(Optional[CustomCreateResponse], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.profiles.custom.with_raw_response.create(
                account_id="",
                entries=[
                    {
                        "enabled": True,
                        "name": "name",
                        "pattern": {"regex": "regex"},
                    }
                ],
                name="name",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        custom = client.zero_trust.dlp.profiles.custom.update(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            name="name",
        )
        assert_matches_type(Optional[Profile], custom, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        custom = client.zero_trust.dlp.profiles.custom.update(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            name="name",
            ai_context_enabled=True,
            allowed_match_count=0,
            confidence_threshold="confidence_threshold",
            context_awareness={
                "enabled": True,
                "skip": {"files": True},
            },
            description="description",
            entries=[
                {
                    "enabled": True,
                    "entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "name": "name",
                    "pattern": {
                        "regex": "regex",
                        "validation": "luhn",
                    },
                }
            ],
            ocr_enabled=True,
            shared_entries=[
                {
                    "enabled": True,
                    "entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "entry_type": "predefined",
                }
            ],
        )
        assert_matches_type(Optional[Profile], custom, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.profiles.custom.with_raw_response.update(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(Optional[Profile], custom, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.profiles.custom.with_streaming_response.update(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(Optional[Profile], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.profiles.custom.with_raw_response.update(
                profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.zero_trust.dlp.profiles.custom.with_raw_response.update(
                profile_id="",
                account_id="account_id",
                name="name",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        custom = client.zero_trust.dlp.profiles.custom.delete(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(object, custom, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.profiles.custom.with_raw_response.delete(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(object, custom, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.profiles.custom.with_streaming_response.delete(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
            client.zero_trust.dlp.profiles.custom.with_raw_response.delete(
                profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.zero_trust.dlp.profiles.custom.with_raw_response.delete(
                profile_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        custom = client.zero_trust.dlp.profiles.custom.get(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(Optional[Profile], custom, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.profiles.custom.with_raw_response.get(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(Optional[Profile], custom, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.profiles.custom.with_streaming_response.get(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(Optional[Profile], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.profiles.custom.with_raw_response.get(
                profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.zero_trust.dlp.profiles.custom.with_raw_response.get(
                profile_id="",
                account_id="account_id",
            )


class TestAsyncCustom:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.zero_trust.dlp.profiles.custom.create(
            account_id="account_id",
            profiles=[
                {
                    "entries": [
                        {
                            "enabled": True,
                            "name": "name",
                            "pattern": {"regex": "regex"},
                        }
                    ],
                    "name": "name",
                }
            ],
        )
        assert_matches_type(Optional[CustomCreateResponse], custom, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.profiles.custom.with_raw_response.create(
            account_id="account_id",
            profiles=[
                {
                    "entries": [
                        {
                            "enabled": True,
                            "name": "name",
                            "pattern": {"regex": "regex"},
                        }
                    ],
                    "name": "name",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(Optional[CustomCreateResponse], custom, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.profiles.custom.with_streaming_response.create(
            account_id="account_id",
            profiles=[
                {
                    "entries": [
                        {
                            "enabled": True,
                            "name": "name",
                            "pattern": {"regex": "regex"},
                        }
                    ],
                    "name": "name",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(Optional[CustomCreateResponse], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.profiles.custom.with_raw_response.create(
                account_id="",
                profiles=[
                    {
                        "entries": [
                            {
                                "enabled": True,
                                "name": "name",
                                "pattern": {"regex": "regex"},
                            }
                        ],
                        "name": "name",
                    }
                ],
            )

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.zero_trust.dlp.profiles.custom.create(
            account_id="account_id",
            entries=[
                {
                    "enabled": True,
                    "name": "name",
                    "pattern": {"regex": "regex"},
                }
            ],
            name="name",
        )
        assert_matches_type(Optional[CustomCreateResponse], custom, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.zero_trust.dlp.profiles.custom.create(
            account_id="account_id",
            entries=[
                {
                    "enabled": True,
                    "name": "name",
                    "pattern": {
                        "regex": "regex",
                        "validation": "luhn",
                    },
                }
            ],
            name="name",
            ai_context_enabled=True,
            allowed_match_count=5,
            confidence_threshold="confidence_threshold",
            context_awareness={
                "enabled": True,
                "skip": {"files": True},
            },
            description="description",
            ocr_enabled=True,
            shared_entries=[
                {
                    "enabled": True,
                    "entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "entry_type": "custom",
                }
            ],
        )
        assert_matches_type(Optional[CustomCreateResponse], custom, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.profiles.custom.with_raw_response.create(
            account_id="account_id",
            entries=[
                {
                    "enabled": True,
                    "name": "name",
                    "pattern": {"regex": "regex"},
                }
            ],
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(Optional[CustomCreateResponse], custom, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.profiles.custom.with_streaming_response.create(
            account_id="account_id",
            entries=[
                {
                    "enabled": True,
                    "name": "name",
                    "pattern": {"regex": "regex"},
                }
            ],
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(Optional[CustomCreateResponse], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.profiles.custom.with_raw_response.create(
                account_id="",
                entries=[
                    {
                        "enabled": True,
                        "name": "name",
                        "pattern": {"regex": "regex"},
                    }
                ],
                name="name",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.zero_trust.dlp.profiles.custom.update(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            name="name",
        )
        assert_matches_type(Optional[Profile], custom, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.zero_trust.dlp.profiles.custom.update(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            name="name",
            ai_context_enabled=True,
            allowed_match_count=0,
            confidence_threshold="confidence_threshold",
            context_awareness={
                "enabled": True,
                "skip": {"files": True},
            },
            description="description",
            entries=[
                {
                    "enabled": True,
                    "entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "name": "name",
                    "pattern": {
                        "regex": "regex",
                        "validation": "luhn",
                    },
                }
            ],
            ocr_enabled=True,
            shared_entries=[
                {
                    "enabled": True,
                    "entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "entry_type": "predefined",
                }
            ],
        )
        assert_matches_type(Optional[Profile], custom, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.profiles.custom.with_raw_response.update(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(Optional[Profile], custom, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.profiles.custom.with_streaming_response.update(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(Optional[Profile], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.profiles.custom.with_raw_response.update(
                profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.zero_trust.dlp.profiles.custom.with_raw_response.update(
                profile_id="",
                account_id="account_id",
                name="name",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.zero_trust.dlp.profiles.custom.delete(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(object, custom, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.profiles.custom.with_raw_response.delete(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(object, custom, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.profiles.custom.with_streaming_response.delete(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
            await async_client.zero_trust.dlp.profiles.custom.with_raw_response.delete(
                profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.zero_trust.dlp.profiles.custom.with_raw_response.delete(
                profile_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.zero_trust.dlp.profiles.custom.get(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(Optional[Profile], custom, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.profiles.custom.with_raw_response.get(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(Optional[Profile], custom, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.profiles.custom.with_streaming_response.get(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(Optional[Profile], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.profiles.custom.with_raw_response.get(
                profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.zero_trust.dlp.profiles.custom.with_raw_response.get(
                profile_id="",
                account_id="account_id",
            )
