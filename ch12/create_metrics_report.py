import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from sklearn.metrics import precision_score, recall_score


def get_precision_recall(data):
    y_true = data["churn"]
    y_pred = data["model_pred"]

    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)

    return precision, recall

def plot_precision_recall(precision_values, recall_values):

    days = range(1, len(precision_values) + 1)

    plt.figure(figsize=(8, 4))

    plt.plot(days,
        precision_values,
        label="Precision",
        marker="o")

    plt.plot(days,
        recall_values,
        label="Recall",
        marker="o")

    plt.xlabel("Days")
    plt.ylabel("Value")
    plt.title("Precision and Recall Over Last 7 Days")

    plt.legend()
    plt.grid(True)

    plt.savefig("precision_recall_plot.png")
    plt.close()

def plot_feature_distribution(data, features):
    for feature in features:
        plt.figure(figsize=(8, 4))
        plt.hist(data[feature],
            bins=20,
            edgecolor = "black")

        plt.xlabel(feature)
        plt.title(f"Distribution of {feature}")
        plt.grid(True)

        plt.savefig(f"{feature}_distribution.png")
        plt.close()

def create_metrics_report(filepath, output_file):

    customer_data = pd.read_csv(filepath)

    features = [col for col in
        customer_data.columns if col not in
        ("model_pred", "churn", "model_pred")]

    precision_values = []
    recall_values = []

    for day in customer_data.pred_date.unique():
        daily_data = customer_data[customer_data.pred_date == day]
        precision, recall = get_precision_recall(daily_data)
        precision_values.append(precision)
        recall_values.append(recall)

    plot_precision_recall(precision_values,
        recall_values)

    plot_feature_distribution(customer_data,
        features)

    doc = SimpleDocTemplate(output_file,
        pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    title = Paragraph("Metrics Report", styles['h1'])
    story.append(title)

    story.append(Spacer(1, 12))
    story.append(
        Paragraph("Precision and Recall Over Last 7 Days",
        styles['h2']))
    story.append(Spacer(1, 12))

    img_path = "precision_recall_plot.png"
    story.append(Image(img_path,
        width=500,
        height=250))

    story.append(Spacer(1, 12))
    story.append(Paragraph("Feature Distribution",
        styles['h2']))
    story.append(Spacer(1, 12))

    for feature in features:
        img_path = f"{feature}_distribution.png"
        story.append(
            Paragraph(f"Distribution of {feature}",
            styles['h3']))
        story.append(Image(img_path, width=500, height=250))
        story.append(Spacer(1, 12))

    doc.build(story)

if __name__ == "__main__":
    create_metrics_report("data/customer_metrics_data.csv",
                          "metrics_report.pdf")