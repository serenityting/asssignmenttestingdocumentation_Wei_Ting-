# test_steps.py
import pytest
from pipeline_steps import (
    collect_samples,
    extract_genetic_data,
    sequence_data,
    clean_and_trim_data,
    align_reads,
    call_variants,
    export_vcf,
    annotate_variants,
    filter_variants,
    match_variants,
    compile_results,
    review_and_interpret,
)

@pytest.mark.parametrize("sample_id, expected", [
    ("sample1", True),
    ("sample2", True),
])
def test_collect_samples(sample_id, expected):
    result = collect_samples(sample_id)
    assert result == expected

@pytest.mark.parametrize("raw_data, expected", [
    ("raw_data_1", True),
    ("raw_data_2", True),
])
def test_extract_genetic_data(raw_data, expected):
    result = extract_genetic_data(raw_data)
    assert result == expected

def test_sequence_data():
    data = "raw_sequencing_data"
    result = sequence_data(data)
    assert result is True

@pytest.mark.parametrize("raw_data, expected_output", [
    ("raw_data_1", "cleaned_data_1"),
    ("raw_data_2", "cleaned_data_2"),
])
def test_clean_and_trim_data(raw_data, expected_output):
    result = clean_and_trim_data(raw_data)
    assert result == expected_output

@pytest.mark.parametrize("cleaned_data, expected", [
    ("cleaned_data_1", True),
    ("cleaned_data_2", True),
])
def test_align_reads(cleaned_data, expected):
    result = align_reads(cleaned_data)
    assert result == expected

@pytest.mark.parametrize("aligned_data, expected", [
    ("aligned_data_1", True),
    ("aligned_data_2", True),
])
def test_call_variants(aligned_data):
    result = call_variants(aligned_data)
    assert result is True

def test_export_vcf():
    result = export_vcf()
    assert result == "VCF exported"

@pytest.mark.parametrize("variants, expected", [
    ("variants_1", "annotated_variants_1"),
    ("variants_2", "annotated_variants_2"),
])
def test_annotate_variants(variants, expected):
    result = annotate_variants(variants)
    assert result == expected

@pytest.mark.parametrize("annotated_variants, expected", [
    ("annotated_variants_1", "filtered_variants_1"),
    ("annotated_variants_2", "filtered_variants_2"),
])
def test_filter_variants(annotated_variants, expected):
    result = filter_variants(annotated_variants)
    assert result == expected

@pytest.mark.parametrize("filtered_variants, database, expected", [
    ("filtered_variants_1", "database_1", True),
    ("filtered_variants_2", "database_2", True),
])
def test_match_variants(filtered_variants, database, expected):
    result = match_variants(filtered_variants, database)
    assert result == expected

def test_compile_results():
    result = compile_results()
    assert result == "Results compiled"

def test_review_and_interpret():
    results = "Sample Results"
    interpretation = review_and_interpret(results)
    assert isinstance(interpretation, dict)
