import os
import pandas as pd
from pipeline.core import run_pipeline

def test_run_pipeline_outputs(tmp_path):
    output_dir = tmp_path / "test_output"
    df = run_pipeline(save_csv=True, generate_plot=False, output_dir=output_dir)

    csv_path = output_dir / "summary.csv"
    assert csv_path.exists(), "CSV output was not created."

    df_loaded = pd.read_csv(csv_path)
    assert df_loaded.shape == df.shape, "Loaded CSV shape does not match original DataFrame."

def test_run_pipeline_plot(tmp_path):
    output_dir = tmp_path / "plot_output"
    run_pipeline(save_csv=False, generate_plot=True, output_dir=output_dir)

    plot_path = output_dir / "plot.png"
    assert plot_path.exists(), "Plot output was not created."
