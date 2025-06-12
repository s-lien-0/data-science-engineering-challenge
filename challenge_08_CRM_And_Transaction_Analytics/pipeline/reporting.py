import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_summary(df: pd.DataFrame) -> None:
    print("📦 Top Products by Margin:")
    print(df.groupby("product_name")["margin"].sum().sort_values(ascending=False).head(3), "\n")

    print("👥 Top Customers by Spend:")
    print(df.groupby("customer_id")["order_value"].sum().sort_values(ascending=False).head(3), "\n")

    repeat_rev = df[df["is_repeat_customer"]]["order_value"].sum()
    total_rev = df["order_value"].sum()
    pct = (repeat_rev / total_rev) * 100
    print(f"🔁 Repeat Customer Revenue: €{repeat_rev:.2f} ({pct:.1f}%)\n")

def plot_top_products(df: pd.DataFrame, output_path="reports/top_products_margin.png", n=5):
    top = df.groupby("product_name")["margin"].sum().sort_values(ascending=False).head(n)
    plt.figure(figsize=(8, 5))
    sns.barplot(x=top.values, y=top.index)
    plt.title("Top Products by Margin")
    plt.xlabel("Total Margin (€)")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()