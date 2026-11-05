# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.zero_trust.dlp.validators import (
    ProximityWordValidator,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProximityWords:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        proximity_word = client.zero_trust.dlp.validators.proximity_words.create(
            account_id="account_id",
            name="HIPAA context words",
            words=[
                {
                    "weight": "strong",
                    "word": "social security number",
                }
            ],
        )
        assert_matches_type(Optional[ProximityWordValidator], proximity_word, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.validators.proximity_words.with_raw_response.create(
            account_id="account_id",
            name="HIPAA context words",
            words=[
                {
                    "weight": "strong",
                    "word": "social security number",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proximity_word = response.parse()
        assert_matches_type(Optional[ProximityWordValidator], proximity_word, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.validators.proximity_words.with_streaming_response.create(
            account_id="account_id",
            name="HIPAA context words",
            words=[
                {
                    "weight": "strong",
                    "word": "social security number",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proximity_word = response.parse()
            assert_matches_type(Optional[ProximityWordValidator], proximity_word, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.validators.proximity_words.with_raw_response.create(
                account_id="",
                name="HIPAA context words",
                words=[
                    {
                        "weight": "strong",
                        "word": "social security number",
                    }
                ],
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        proximity_word = client.zero_trust.dlp.validators.proximity_words.update(
            validator_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            name="HIPAA context words",
            words=[
                {
                    "weight": "strong",
                    "word": "social security number",
                }
            ],
        )
        assert_matches_type(Optional[ProximityWordValidator], proximity_word, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.validators.proximity_words.with_raw_response.update(
            validator_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            name="HIPAA context words",
            words=[
                {
                    "weight": "strong",
                    "word": "social security number",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proximity_word = response.parse()
        assert_matches_type(Optional[ProximityWordValidator], proximity_word, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.validators.proximity_words.with_streaming_response.update(
            validator_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            name="HIPAA context words",
            words=[
                {
                    "weight": "strong",
                    "word": "social security number",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proximity_word = response.parse()
            assert_matches_type(Optional[ProximityWordValidator], proximity_word, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.validators.proximity_words.with_raw_response.update(
                validator_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                name="HIPAA context words",
                words=[
                    {
                        "weight": "strong",
                        "word": "social security number",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `validator_id` but received ''"):
            client.zero_trust.dlp.validators.proximity_words.with_raw_response.update(
                validator_id="",
                account_id="account_id",
                name="HIPAA context words",
                words=[
                    {
                        "weight": "strong",
                        "word": "social security number",
                    }
                ],
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        proximity_word = client.zero_trust.dlp.validators.proximity_words.list(
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[ProximityWordValidator], proximity_word, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.validators.proximity_words.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proximity_word = response.parse()
        assert_matches_type(SyncSinglePage[ProximityWordValidator], proximity_word, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.validators.proximity_words.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proximity_word = response.parse()
            assert_matches_type(SyncSinglePage[ProximityWordValidator], proximity_word, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.validators.proximity_words.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        proximity_word = client.zero_trust.dlp.validators.proximity_words.delete(
            validator_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(object, proximity_word, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.validators.proximity_words.with_raw_response.delete(
            validator_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proximity_word = response.parse()
        assert_matches_type(object, proximity_word, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.validators.proximity_words.with_streaming_response.delete(
            validator_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proximity_word = response.parse()
            assert_matches_type(object, proximity_word, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.validators.proximity_words.with_raw_response.delete(
                validator_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `validator_id` but received ''"):
            client.zero_trust.dlp.validators.proximity_words.with_raw_response.delete(
                validator_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        proximity_word = client.zero_trust.dlp.validators.proximity_words.get(
            validator_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(Optional[ProximityWordValidator], proximity_word, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.validators.proximity_words.with_raw_response.get(
            validator_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proximity_word = response.parse()
        assert_matches_type(Optional[ProximityWordValidator], proximity_word, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.validators.proximity_words.with_streaming_response.get(
            validator_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proximity_word = response.parse()
            assert_matches_type(Optional[ProximityWordValidator], proximity_word, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.validators.proximity_words.with_raw_response.get(
                validator_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `validator_id` but received ''"):
            client.zero_trust.dlp.validators.proximity_words.with_raw_response.get(
                validator_id="",
                account_id="account_id",
            )


class TestAsyncProximityWords:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        proximity_word = await async_client.zero_trust.dlp.validators.proximity_words.create(
            account_id="account_id",
            name="HIPAA context words",
            words=[
                {
                    "weight": "strong",
                    "word": "social security number",
                }
            ],
        )
        assert_matches_type(Optional[ProximityWordValidator], proximity_word, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.validators.proximity_words.with_raw_response.create(
            account_id="account_id",
            name="HIPAA context words",
            words=[
                {
                    "weight": "strong",
                    "word": "social security number",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proximity_word = await response.parse()
        assert_matches_type(Optional[ProximityWordValidator], proximity_word, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.validators.proximity_words.with_streaming_response.create(
            account_id="account_id",
            name="HIPAA context words",
            words=[
                {
                    "weight": "strong",
                    "word": "social security number",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proximity_word = await response.parse()
            assert_matches_type(Optional[ProximityWordValidator], proximity_word, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.validators.proximity_words.with_raw_response.create(
                account_id="",
                name="HIPAA context words",
                words=[
                    {
                        "weight": "strong",
                        "word": "social security number",
                    }
                ],
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        proximity_word = await async_client.zero_trust.dlp.validators.proximity_words.update(
            validator_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            name="HIPAA context words",
            words=[
                {
                    "weight": "strong",
                    "word": "social security number",
                }
            ],
        )
        assert_matches_type(Optional[ProximityWordValidator], proximity_word, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.validators.proximity_words.with_raw_response.update(
            validator_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            name="HIPAA context words",
            words=[
                {
                    "weight": "strong",
                    "word": "social security number",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proximity_word = await response.parse()
        assert_matches_type(Optional[ProximityWordValidator], proximity_word, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.validators.proximity_words.with_streaming_response.update(
            validator_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            name="HIPAA context words",
            words=[
                {
                    "weight": "strong",
                    "word": "social security number",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proximity_word = await response.parse()
            assert_matches_type(Optional[ProximityWordValidator], proximity_word, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.validators.proximity_words.with_raw_response.update(
                validator_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                name="HIPAA context words",
                words=[
                    {
                        "weight": "strong",
                        "word": "social security number",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `validator_id` but received ''"):
            await async_client.zero_trust.dlp.validators.proximity_words.with_raw_response.update(
                validator_id="",
                account_id="account_id",
                name="HIPAA context words",
                words=[
                    {
                        "weight": "strong",
                        "word": "social security number",
                    }
                ],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        proximity_word = await async_client.zero_trust.dlp.validators.proximity_words.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[ProximityWordValidator], proximity_word, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.validators.proximity_words.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proximity_word = await response.parse()
        assert_matches_type(AsyncSinglePage[ProximityWordValidator], proximity_word, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.validators.proximity_words.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proximity_word = await response.parse()
            assert_matches_type(AsyncSinglePage[ProximityWordValidator], proximity_word, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.validators.proximity_words.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        proximity_word = await async_client.zero_trust.dlp.validators.proximity_words.delete(
            validator_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(object, proximity_word, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.validators.proximity_words.with_raw_response.delete(
            validator_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proximity_word = await response.parse()
        assert_matches_type(object, proximity_word, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.validators.proximity_words.with_streaming_response.delete(
            validator_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proximity_word = await response.parse()
            assert_matches_type(object, proximity_word, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.validators.proximity_words.with_raw_response.delete(
                validator_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `validator_id` but received ''"):
            await async_client.zero_trust.dlp.validators.proximity_words.with_raw_response.delete(
                validator_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        proximity_word = await async_client.zero_trust.dlp.validators.proximity_words.get(
            validator_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(Optional[ProximityWordValidator], proximity_word, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.validators.proximity_words.with_raw_response.get(
            validator_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proximity_word = await response.parse()
        assert_matches_type(Optional[ProximityWordValidator], proximity_word, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.validators.proximity_words.with_streaming_response.get(
            validator_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proximity_word = await response.parse()
            assert_matches_type(Optional[ProximityWordValidator], proximity_word, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.validators.proximity_words.with_raw_response.get(
                validator_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `validator_id` but received ''"):
            await async_client.zero_trust.dlp.validators.proximity_words.with_raw_response.get(
                validator_id="",
                account_id="account_id",
            )
