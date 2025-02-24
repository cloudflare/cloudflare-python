# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "AIRunParams",
    "TextClassification",
    "TextToImage",
    "TextToSpeech",
    "TextEmbeddings",
    "AutomaticSpeechRecognition",
    "ImageClassification",
    "ObjectDetection",
    "Prompt",
    "PromptResponseFormat",
    "Messages",
    "MessagesMessage",
    "MessagesFunction",
    "MessagesResponseFormat",
    "MessagesTool",
    "MessagesToolUnionMember0",
    "MessagesToolUnionMember0Parameters",
    "MessagesToolUnionMember0ParametersProperties",
    "MessagesToolUnionMember1",
    "MessagesToolUnionMember1Function",
    "MessagesToolUnionMember1FunctionParameters",
    "MessagesToolUnionMember1FunctionParametersProperties",
    "Translation",
    "Summarization",
    "ImageToText",
]


class TextClassification(TypedDict, total=False):
    account_id: Required[str]

    text: Required[str]
    """The text that you want to classify"""


class TextToImage(TypedDict, total=False):
    account_id: Required[str]

    prompt: Required[str]
    """A text description of the image you want to generate"""

    guidance: float
    """
    Controls how closely the generated image should adhere to the prompt; higher
    values make the image more aligned with the prompt
    """

    height: int
    """The height of the generated image in pixels"""

    image: Iterable[float]
    """For use with img2img tasks.

    An array of integers that represent the image data constrained to 8-bit unsigned
    integer values
    """

    image_b64: str
    """For use with img2img tasks. A base64-encoded string of the input image"""

    mask: Iterable[float]
    """
    An array representing An array of integers that represent mask image data for
    inpainting constrained to 8-bit unsigned integer values
    """

    negative_prompt: str
    """Text describing elements to avoid in the generated image"""

    num_steps: int
    """
    The number of diffusion steps; higher values can improve quality but take longer
    """

    seed: int
    """Random seed for reproducibility of the image generation"""

    strength: float
    """
    A value between 0 and 1 indicating how strongly to apply the transformation
    during img2img tasks; lower values make the output closer to the input image
    """

    width: int
    """The width of the generated image in pixels"""


class TextToSpeech(TypedDict, total=False):
    account_id: Required[str]

    prompt: Required[str]
    """A text description of the image you want to generate"""

    lang: str
    """The speech language (e.g., 'en' for English, 'fr' for French).

    Defaults to 'en' if not specified
    """


class TextEmbeddings(TypedDict, total=False):
    account_id: Required[str]

    text: Required[Union[str, List[str]]]
    """The text to embed"""


class AutomaticSpeechRecognition(TypedDict, total=False):
    account_id: Required[str]

    audio: Required[Iterable[float]]
    """
    An array of integers that represent the audio data constrained to 8-bit unsigned
    integer values
    """

    source_lang: str
    """The language of the recorded audio"""

    target_lang: str
    """The language to translate the transcription into.

    Currently only English is supported.
    """


class ImageClassification(TypedDict, total=False):
    account_id: Required[str]

    image: Required[Iterable[float]]
    """
    An array of integers that represent the image data constrained to 8-bit unsigned
    integer values
    """


class ObjectDetection(TypedDict, total=False):
    account_id: Required[str]

    image: Iterable[float]
    """
    An array of integers that represent the image data constrained to 8-bit unsigned
    integer values
    """


class Prompt(TypedDict, total=False):
    account_id: Required[str]

    prompt: Required[str]
    """The input text prompt for the model to generate a response."""

    frequency_penalty: float
    """Decreases the likelihood of the model repeating the same lines verbatim."""

    lora: str
    """Name of the LoRA (Low-Rank Adaptation) model to fine-tune the base model."""

    max_tokens: int
    """The maximum number of tokens to generate in the response."""

    presence_penalty: float
    """Increases the likelihood of the model introducing new topics."""

    raw: bool
    """
    If true, a chat template is not applied and you must adhere to the specific
    model's expected formatting.
    """

    repetition_penalty: float
    """Penalty for repeated tokens; higher values discourage repetition."""

    response_format: PromptResponseFormat

    seed: int
    """Random seed for reproducibility of the generation."""

    stream: bool
    """
    If true, the response will be streamed back incrementally using SSE, Server Sent
    Events.
    """

    temperature: float
    """
    Controls the randomness of the output; higher values produce more random
    results.
    """

    top_k: int
    """Limits the AI to choose from the top 'k' most probable words.

    Lower values make responses more focused; higher values introduce more variety
    and potential surprises.
    """

    top_p: float
    """
    Adjusts the creativity of the AI's responses by controlling how many possible
    words it considers. Lower values make outputs more predictable; higher values
    allow for more varied and creative responses.
    """


class PromptResponseFormat(TypedDict, total=False):
    json_schema: object

    type: Literal["json_object", "json_schema"]


class Messages(TypedDict, total=False):
    account_id: Required[str]

    messages: Required[Iterable[MessagesMessage]]
    """An array of message objects representing the conversation history."""

    frequency_penalty: float
    """Decreases the likelihood of the model repeating the same lines verbatim."""

    functions: Iterable[MessagesFunction]

    max_tokens: int
    """The maximum number of tokens to generate in the response."""

    presence_penalty: float
    """Increases the likelihood of the model introducing new topics."""

    repetition_penalty: float
    """Penalty for repeated tokens; higher values discourage repetition."""

    response_format: MessagesResponseFormat

    seed: int
    """Random seed for reproducibility of the generation."""

    stream: bool
    """If true, the response will be streamed back incrementally."""

    temperature: float
    """
    Controls the randomness of the output; higher values produce more random
    results.
    """

    tools: Iterable[MessagesTool]
    """A list of tools available for the assistant to use."""

    top_k: int
    """Limits the AI to choose from the top 'k' most probable words.

    Lower values make responses more focused; higher values introduce more variety
    and potential surprises.
    """

    top_p: float
    """
    Controls the creativity of the AI's responses by adjusting how many possible
    words it considers. Lower values make outputs more predictable; higher values
    allow for more varied and creative responses.
    """


class MessagesMessage(TypedDict, total=False):
    content: Required[str]
    """The content of the message as a string."""

    role: Required[str]
    """The role of the message sender (e.g., 'user', 'assistant', 'system', 'tool')."""


class MessagesFunction(TypedDict, total=False):
    code: Required[str]

    name: Required[str]


class MessagesResponseFormat(TypedDict, total=False):
    json_schema: object

    type: Literal["json_object", "json_schema"]


class MessagesToolUnionMember0ParametersProperties(TypedDict, total=False):
    description: Required[str]
    """A description of the expected parameter."""

    type: Required[str]
    """The data type of the parameter."""


class MessagesToolUnionMember0Parameters(TypedDict, total=False):
    properties: Required[Dict[str, MessagesToolUnionMember0ParametersProperties]]
    """Definitions of each parameter."""

    type: Required[str]
    """The type of the parameters object (usually 'object')."""

    required: List[str]
    """List of required parameter names."""


class MessagesToolUnionMember0(TypedDict, total=False):
    description: Required[str]
    """A brief description of what the tool does."""

    name: Required[str]
    """The name of the tool. More descriptive the better."""

    parameters: Required[MessagesToolUnionMember0Parameters]
    """Schema defining the parameters accepted by the tool."""


class MessagesToolUnionMember1FunctionParametersProperties(TypedDict, total=False):
    description: Required[str]
    """A description of the expected parameter."""

    type: Required[str]
    """The data type of the parameter."""


class MessagesToolUnionMember1FunctionParameters(TypedDict, total=False):
    properties: Required[Dict[str, MessagesToolUnionMember1FunctionParametersProperties]]
    """Definitions of each parameter."""

    type: Required[str]
    """The type of the parameters object (usually 'object')."""

    required: List[str]
    """List of required parameter names."""


class MessagesToolUnionMember1Function(TypedDict, total=False):
    description: Required[str]
    """A brief description of what the function does."""

    name: Required[str]
    """The name of the function."""

    parameters: Required[MessagesToolUnionMember1FunctionParameters]
    """Schema defining the parameters accepted by the function."""


class MessagesToolUnionMember1(TypedDict, total=False):
    function: Required[MessagesToolUnionMember1Function]
    """Details of the function tool."""

    type: Required[str]
    """Specifies the type of tool (e.g., 'function')."""


MessagesTool: TypeAlias = Union[MessagesToolUnionMember0, MessagesToolUnionMember1]


class Translation(TypedDict, total=False):
    account_id: Required[str]

    target_lang: Required[str]
    """The language code to translate the text into (e.g., 'es' for Spanish)"""

    text: Required[str]
    """The text to be translated"""

    source_lang: str
    """The language code of the source text (e.g., 'en' for English).

    Defaults to 'en' if not specified
    """


class Summarization(TypedDict, total=False):
    account_id: Required[str]

    input_text: Required[str]
    """The text that you want the model to summarize"""

    max_length: int
    """The maximum length of the generated summary in tokens"""


class ImageToText(TypedDict, total=False):
    account_id: Required[str]

    image: Required[Iterable[float]]
    """
    An array of integers that represent the image data constrained to 8-bit unsigned
    integer values
    """

    frequency_penalty: float
    """Decreases the likelihood of the model repeating the same lines verbatim."""

    max_tokens: int
    """The maximum number of tokens to generate in the response."""

    presence_penalty: float
    """Increases the likelihood of the model introducing new topics."""

    prompt: str
    """The input text prompt for the model to generate a response."""

    raw: bool
    """
    If true, a chat template is not applied and you must adhere to the specific
    model's expected formatting.
    """

    repetition_penalty: float
    """Penalty for repeated tokens; higher values discourage repetition."""

    seed: float
    """Random seed for reproducibility of the generation."""

    temperature: float
    """
    Controls the randomness of the output; higher values produce more random
    results.
    """

    top_k: float
    """Limits the AI to choose from the top 'k' most probable words.

    Lower values make responses more focused; higher values introduce more variety
    and potential surprises.
    """

    top_p: float
    """
    Controls the creativity of the AI's responses by adjusting how many possible
    words it considers. Lower values make outputs more predictable; higher values
    allow for more varied and creative responses.
    """


AIRunParams: TypeAlias = Union[
    TextClassification,
    TextToImage,
    TextToSpeech,
    TextEmbeddings,
    AutomaticSpeechRecognition,
    ImageClassification,
    ObjectDetection,
    Prompt,
    Messages,
    Translation,
    Summarization,
    ImageToText,
]
