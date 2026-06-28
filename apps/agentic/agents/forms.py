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
    path: str = Field(
        ...,
        description="Relative file path to the document with respect to application root directory.",
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


class CreateTimeSeriesReportForm(BaseModel):
    """Form data for creating a time series report."""

    type: Literal["create_time_series_report"] = "create_time_series_report"

    report_title: str = Field(
        ...,
        description="Title of the report.",
    )
    report_description: str = Field(
        ...,
        description="Description of the report.",
    )
    time_series_ids: str = Field(
        ...,
        description="Comma-separated list of time series cache IDs to include in the report.",
    )
    tags: str = Field(
        "",
        description="Comma-separated list of tags to categorize the report (e.g. gdp,labor,quarterly).",
    )
    time_range_from: str = Field(
        ...,
        description="Start date of the report time range in ISO format YYYY-MM-DD.",
    )
    time_range_to: str | None = Field(
        None,
        description="End date of the report time range in ISO format YYYY-MM-DD. Leave blank for latest available data.",
    )


class SelectTimeSeriesReportForm(BaseModel):
    """Form data for selecting an existing time series report to plot."""

    type: Literal["select_time_series_report"] = "select_time_series_report"

    report_id: str = Field(
        ...,
        description="UUID of the selected time series report.",
    )


# Maps the form type discriminator to its model class.
# Used by HumanInputNode to validate resumed form data.
FORM_REGISTRY: dict[str, type[BaseModel]] = {
    "load_research_document": LoadResearchDocumentForm,
    "load_github_repo": LoadGitHubRepoForm,
    "create_time_series_report": CreateTimeSeriesReportForm,
    "select_time_series_report": SelectTimeSeriesReportForm,
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
