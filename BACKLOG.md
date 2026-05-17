# YADA Backlog

## Report Agent

- **Report creation fails when series are not cached.**
  If the user provides cache IDs that don't exist in `time_series_cache`, creation is aborted
  with a `ValueError`. The user must manually fetch each series via `DataFetcherAgent` first,
  collect the returned `native_id`s, then re-submit the report form.

- **Auto-download uncached series at report creation time.**
  Change the form to accept FRED external IDs (e.g. `UNRATE, GDP`) instead of native_id UUIDs.
  Add an async `fetch_and_create_report` module-level function in `time_series_report_agent.py`
  (same pattern as `plot_time_series_report`) that checks the cache for each ID, fetches any
  misses via `DataFetcherAgent`, collects the resulting `native_id`s, then calls
  `create_time_series_report`. Register it as a tool in `TimeSeriesReportAgent`. No changes
  needed to `create_time_series_report`, `SeriesCache`, `ReportCache`, or `CachingFredTool`.
