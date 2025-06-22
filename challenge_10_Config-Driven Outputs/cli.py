import argparse
import json
from pipeline.core import run_pipeline

def load_config(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Config file not found: {path}")
        exit(1)
    except json.JSONDecodeError:
        print(f"❌ Invalid JSON in config file: {path}")
        exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run pipeline with config.")
    parser.add_argument("--config", type=str, default="config/default_config.json", help="Path to config file.")
    parser.add_argument("--save", dest="save_csv", action="store_true", help="Override: Save CSV output.")
    parser.add_argument("--no-save", dest="save_csv", action="store_false", help="Override: Do NOT save CSV.")
    parser.set_defaults(save_csv=None)

    parser.add_argument("--plot", dest="generate_plot", action="store_true", help="Override: Generate plot.")
    parser.add_argument("--no-plot", dest="generate_plot", action="store_false", help="Override: Do NOT generate plot.")
    parser.set_defaults(generate_plot=None)

    args = parser.parse_args()
    config = load_config(args.config)

    save_csv = args.save_csv if args.save_csv is not None else config.get("save_csv", True)
    generate_plot = args.generate_plot if args.generate_plot is not None else config.get("generate_plot", False)
    output_dir = config.get("output_dir", "output")

    print(f"⚙️ Using config: save_csv={save_csv}, generate_plot={generate_plot}, output_dir={output_dir}")
    run_pipeline(save_csv=save_csv, generate_plot=generate_plot, output_dir=output_dir)
