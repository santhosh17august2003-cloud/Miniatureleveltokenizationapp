from dataclasses import dataclass
from functools import cached_property

import torch
from transformers import AutoModel


class EmbeddingServiceError(Exception):
    """Raised when embeddings cannot be generated."""


@dataclass(frozen=True)
class TokenEmbedding:
    token: str
    token_id: int
    dimension: int
    vector: list[float]

    @property
    def preview(self) -> str:
        shown = ", ".join(f"{value:.4f}" for value in self.vector[:8])
        suffix = ", ..." if len(self.vector) > 8 else ""
        return f"[{shown}{suffix}]"


class EmbeddingService:
    def __init__(self, model_name: str) -> None:
        self.model_name = model_name

    @cached_property
    def model(self):
        try:
            model = AutoModel.from_pretrained(self.model_name)
            model.eval()
            return model
        except Exception as exc:
            raise EmbeddingServiceError(
                f"Could not load embedding model '{self.model_name}'."
            ) from exc

    def embed_tokens(self, token_items) -> list[TokenEmbedding]:
        if not token_items:
            return []

        input_ids = torch.tensor([[item.token_id for item in token_items]], dtype=torch.long)

        try:
            with torch.no_grad():
                output = self.model(input_ids=input_ids)
                vectors = output.last_hidden_state.squeeze(0).cpu().tolist()
        except EmbeddingServiceError:
            raise
        except Exception as exc:
            raise EmbeddingServiceError("Embedding generation failed for these tokens.") from exc

        return [
            TokenEmbedding(
                token=item.token,
                token_id=item.token_id,
                dimension=len(vector),
                vector=[float(value) for value in vector],
            )
            for item, vector in zip(token_items, vectors)
        ]
