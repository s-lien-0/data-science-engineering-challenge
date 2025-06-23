import os
import tempfile
from pipeline.core import run_pipeline

def test_run_pipeline_outputs():
    with tempfile.TemporaryDirectory() as tmpdir:
        run_pipeline(save_csv=True, generate_plot=False, output_dir=tmpdir)
        output_path = os.path.join(tmpdir, "hospital_visits.csv")
        assert os.path.exists(output_path), "CSV output was not created."


def test_run_pipeline_plot():
    with tempfile.TemporaryDirectory() as tmpdir:
        run_pipeline(save_csv=False, generate_plot=True, output_dir=tmpdir)
        output_path = os.path.join(tmpdir, "cost_by_department.png")
        assert os.path.exists(output_path), "Plot output was not created."
