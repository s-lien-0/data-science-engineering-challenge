import argparse
from pipeline.data_loaders import load_json_file
from pipeline.flatteners import flatten_orders
from pipeline.cleaners import clean_order_df
from pipeline.enrichers import enrich_with_history
from pipeline.reporting import generate_summary, plot_top_products
import pandas as pd
import logging
logging.basicConfig(level=logging.INFO)

def main():
    parser = argparse.ArgumentParser(description="Run data pipeline on nested order JSON.")
    parser.add_argument('--filepath', type=str, required=True, help='Path to the input JSON file')
    parser.add_argument('--history', type=str, required=True, help='Path to the product history CSV')
    args = parser.parse_args()
    

    data = load_json_file(args.filepath)
    if data is None:
        logging.info("❌ Failed to load data.")
        return

    df = flatten_orders(data)
    
    logging.info("✅ Flattened data:")
    logging.info(df.head())

    cleaned_df = clean_order_df(df)
    logging.info("✅ Cleaned data:")
    logging.info(cleaned_df.head())

    history_df = pd.read_csv(args.history)
    enriched_df = enrich_with_history(cleaned_df, history_df)

    logging.info("✅ Enriched data:")
    logging.info(enriched_df.head())

    generate_summary(enriched_df)
    plot_top_products(enriched_df)

    # Export to reports
    enriched_df.to_csv("reports/enriched_orders.csv", index=False)
    logging.info("✅ Saved report to reports/enriched_orders.csv")


if __name__ == "__main__":
    main()
