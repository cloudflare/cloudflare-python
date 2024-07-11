# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.workers import AIRunResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAI:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_run_overload_1(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_raw_response_run_overload_1(self, client: Cloudflare) -> None:
        response = client.workers.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_streaming_response_run_overload_1(self, client: Cloudflare) -> None:
        with client.workers.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_run_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.workers.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @parametrize
    def test_method_run_overload_2(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="x",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_raw_response_run_overload_2(self, client: Cloudflare) -> None:
        response = client.workers.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_streaming_response_run_overload_2(self, client: Cloudflare) -> None:
        with client.workers.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_run_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                text="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.workers.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                text="x",
            )

    @parametrize
    def test_method_run_overload_3(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_method_run_with_all_params_overload_3(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
            guidance=0,
            image=[0, 0, 0],
            lora_weights=[0, 0, 0],
            loras=["string", "string", "string"],
            mask=[0, 0, 0],
            num_steps=0,
            strength=0,
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_raw_response_run_overload_3(self, client: Cloudflare) -> None:
        response = client.workers.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_streaming_response_run_overload_3(self, client: Cloudflare) -> None:
        with client.workers.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_run_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                prompt="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.workers.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prompt="x",
            )

    @parametrize
    def test_method_run_overload_4(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="x",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_raw_response_run_overload_4(self, client: Cloudflare) -> None:
        response = client.workers.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_streaming_response_run_overload_4(self, client: Cloudflare) -> None:
        with client.workers.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_run_overload_4(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                text="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.workers.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                text="x",
            )

    @parametrize
    def test_method_run_overload_5(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            audio=[0, 0, 0],
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_raw_response_run_overload_5(self, client: Cloudflare) -> None:
        response = client.workers.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            audio=[0, 0, 0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_streaming_response_run_overload_5(self, client: Cloudflare) -> None:
        with client.workers.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            audio=[0, 0, 0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_run_overload_5(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                audio=[0, 0, 0],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.workers.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                audio=[0, 0, 0],
            )

    @parametrize
    def test_method_run_overload_6(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0, 0, 0],
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_raw_response_run_overload_6(self, client: Cloudflare) -> None:
        response = client.workers.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0, 0, 0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_streaming_response_run_overload_6(self, client: Cloudflare) -> None:
        with client.workers.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0, 0, 0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_run_overload_6(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                image=[0, 0, 0],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.workers.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                image=[0, 0, 0],
            )

    @parametrize
    def test_method_run_overload_7(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_method_run_with_all_params_overload_7(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0, 0, 0],
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_raw_response_run_overload_7(self, client: Cloudflare) -> None:
        response = client.workers.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_streaming_response_run_overload_7(self, client: Cloudflare) -> None:
        with client.workers.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_run_overload_7(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.workers.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_run_overload_8(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_method_run_with_all_params_overload_8(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            lora="lora",
            max_tokens=0,
            messages=[
                {
                    "content": "content",
                    "role": "role",
                },
                {
                    "content": "content",
                    "role": "role",
                },
                {
                    "content": "content",
                    "role": "role",
                },
            ],
            prompt="x",
            raw=True,
            stream=True,
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_raw_response_run_overload_8(self, client: Cloudflare) -> None:
        response = client.workers.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_streaming_response_run_overload_8(self, client: Cloudflare) -> None:
        with client.workers.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_run_overload_8(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.workers.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_run_overload_9(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_lang="target_lang",
            text="x",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_method_run_with_all_params_overload_9(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_lang="target_lang",
            text="x",
            source_lang="source_lang",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_raw_response_run_overload_9(self, client: Cloudflare) -> None:
        response = client.workers.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_lang="target_lang",
            text="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_streaming_response_run_overload_9(self, client: Cloudflare) -> None:
        with client.workers.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_lang="target_lang",
            text="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_run_overload_9(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                target_lang="target_lang",
                text="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.workers.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                target_lang="target_lang",
                text="x",
            )

    @parametrize
    def test_method_run_overload_10(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            input_text="x",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_method_run_with_all_params_overload_10(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            input_text="x",
            max_length=0,
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_raw_response_run_overload_10(self, client: Cloudflare) -> None:
        response = client.workers.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            input_text="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_streaming_response_run_overload_10(self, client: Cloudflare) -> None:
        with client.workers.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            input_text="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_run_overload_10(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                input_text="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.workers.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                input_text="x",
            )

    @parametrize
    def test_method_run_overload_11(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0, 0, 0],
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_method_run_with_all_params_overload_11(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0, 0, 0],
            max_tokens=0,
            messages=[
                {
                    "content": "content",
                    "role": "role",
                },
                {
                    "content": "content",
                    "role": "role",
                },
                {
                    "content": "content",
                    "role": "role",
                },
            ],
            prompt="prompt",
            raw=True,
            temperature=0,
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_raw_response_run_overload_11(self, client: Cloudflare) -> None:
        response = client.workers.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0, 0, 0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_streaming_response_run_overload_11(self, client: Cloudflare) -> None:
        with client.workers.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0, 0, 0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_run_overload_11(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                image=[0, 0, 0],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.workers.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                image=[0, 0, 0],
            )


class TestAsyncAI:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_run_overload_1(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_streaming_response_run_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_run_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @parametrize
    async def test_method_run_overload_2(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="x",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_streaming_response_run_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_run_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                text="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                text="x",
            )

    @parametrize
    async def test_method_run_overload_3(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_method_run_with_all_params_overload_3(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
            guidance=0,
            image=[0, 0, 0],
            lora_weights=[0, 0, 0],
            loras=["string", "string", "string"],
            mask=[0, 0, 0],
            num_steps=0,
            strength=0,
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_streaming_response_run_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_run_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                prompt="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prompt="x",
            )

    @parametrize
    async def test_method_run_overload_4(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="x",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_streaming_response_run_overload_4(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_run_overload_4(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                text="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                text="x",
            )

    @parametrize
    async def test_method_run_overload_5(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            audio=[0, 0, 0],
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_5(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            audio=[0, 0, 0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_streaming_response_run_overload_5(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            audio=[0, 0, 0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_run_overload_5(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                audio=[0, 0, 0],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                audio=[0, 0, 0],
            )

    @parametrize
    async def test_method_run_overload_6(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0, 0, 0],
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_6(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0, 0, 0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_streaming_response_run_overload_6(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0, 0, 0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_run_overload_6(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                image=[0, 0, 0],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                image=[0, 0, 0],
            )

    @parametrize
    async def test_method_run_overload_7(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_method_run_with_all_params_overload_7(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0, 0, 0],
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_7(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_streaming_response_run_overload_7(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_run_overload_7(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_run_overload_8(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_method_run_with_all_params_overload_8(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            lora="lora",
            max_tokens=0,
            messages=[
                {
                    "content": "content",
                    "role": "role",
                },
                {
                    "content": "content",
                    "role": "role",
                },
                {
                    "content": "content",
                    "role": "role",
                },
            ],
            prompt="x",
            raw=True,
            stream=True,
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_8(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_streaming_response_run_overload_8(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_run_overload_8(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_run_overload_9(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_lang="target_lang",
            text="x",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_method_run_with_all_params_overload_9(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_lang="target_lang",
            text="x",
            source_lang="source_lang",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_9(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_lang="target_lang",
            text="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_streaming_response_run_overload_9(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_lang="target_lang",
            text="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_run_overload_9(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                target_lang="target_lang",
                text="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                target_lang="target_lang",
                text="x",
            )

    @parametrize
    async def test_method_run_overload_10(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            input_text="x",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_method_run_with_all_params_overload_10(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            input_text="x",
            max_length=0,
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_10(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            input_text="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_streaming_response_run_overload_10(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            input_text="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_run_overload_10(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                input_text="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                input_text="x",
            )

    @parametrize
    async def test_method_run_overload_11(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0, 0, 0],
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_method_run_with_all_params_overload_11(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0, 0, 0],
            max_tokens=0,
            messages=[
                {
                    "content": "content",
                    "role": "role",
                },
                {
                    "content": "content",
                    "role": "role",
                },
                {
                    "content": "content",
                    "role": "role",
                },
            ],
            prompt="prompt",
            raw=True,
            temperature=0,
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_11(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0, 0, 0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_streaming_response_run_overload_11(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0, 0, 0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_run_overload_11(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                image=[0, 0, 0],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                image=[0, 0, 0],
            )
