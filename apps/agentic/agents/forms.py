from __future__ import annotations

from typing import Literal
from pydantic import BaseModel, Field


class LoadResearchDocumentForm(BaseModel):
    """Form data for loading a research document into the research library."""

    type: Literal["load_research_document"] = "load_research_document"

    filename: str = Field(
        ...,
        description="Filename of the document to load.",
    )
    title: str = Field(
        ...,
        description="Document title.",
    )
    authors: str = Field(
        ...,
        description="Document authors.",
    )
    document_date: str = Field(
        ...,
        description="Publication or document date.",
    )
    topic: str = Field(
        ...,
        description="Topic or subject area.",
    )
    shelf: str = Field(
        ...,
        description="Library shelf to assign the document to.",
    )


class LoadGitHubRepoForm(BaseModel):
    """Form data for loading a GitHub repository into the code store."""

    type: Literal["load_github_repo"] = "load_github_repo"

    account: str = Field(
        ...,
        description="GitHub account or organization name (required).",
    )
    repo: str = Field(
        ...,
        description="Repository name (required).",
    )


class LoadPDFDocumentForm(BaseModel):
    """Form data for loading a PDF document into the document library."""

    type: Literal["load_pdf_document"] = "load_pdf_document"

    filename: str = Field(
        ...,
        description="Filename of the PDF document to load.",
    )
    title: str = Field(
        ...,
        description="Document title.",
    )
    authors: str = Field(
        ...,
        description="Document authors.",
    )
    published_date: str = Field(
        ...,
        description="Publication date.",
    )
    topic: str = Field(
        ...,
        description="Topic or subject area.",
    )
    shelf: str = Field(
        ...,
        description="Library shelf to assign the document to.",
    )


# Maps the form type discriminator to its model class.
# Used by HumanInputNode to validate resumed form data.
FORM_REGISTRY: dict[str, type[BaseModel]] = {
    "load_research_document": LoadResearchDocumentForm,
    "load_github_repo": LoadGitHubRepoForm,
    "load_pdf_document": LoadPDFDocumentForm,
}


def validate_form(form_data: dict) -> BaseModel:
    """
    Validate raw form submission data against the appropriate form model.

    Parameters
    ----------
    form_data : dict
        Must include a ``type`` key matching a registered form type.

    Returns
    -------
    BaseModel
        Validated form instance.

    Raises
    ------
    ValueError
        If ``type`` is missing or not in the registry.
    ValidationError
        If the data fails Pydantic validation.
    """
    
    form_type = form_data.get("type")
    if not form_type:
        raise ValueError("form_data must include a 'type' field")
    model_cls = FORM_REGISTRY.get(form_type)
    if model_cls is None:
        raise ValueError(
            f"Unknown form type '{form_type}'. "
            f"Available: {list(FORM_REGISTRY.keys())}"
        )
    return model_cls(**form_data)
