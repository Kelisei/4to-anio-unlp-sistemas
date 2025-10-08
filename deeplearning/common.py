def boxplot_stats(col):
    """
    Calculate boxplot statistics for a given pandas Series.

    Parameters:
        col (pandas.Series): The input data column for which to compute boxplot statistics.

    Returns:
        dict: A dictionary containing the following keys:
            - "Q1": First quartile (25th percentile).
            - "Q3": Third quartile (75th percentile).
            - "Q2": Median (50th percentile).
            - "IQR": Interquartile range (Q3 - Q1).
            - "Lower whisker": The minimum value within 1.5*IQR below Q1.
            - "Upper whisker": The maximum value within 1.5*IQR above Q3.
            - "Mild outliers range (left)": Tuple indicating the range for mild outliers on the left (between 3*IQR and 1.5*IQR below Q1).
            - "Mild outliers range (right)": Tuple indicating the range for severe outliers on the right (between 1.5*IQR and 3*IQR above Q3).
            - "Max value": Maximum value in the column.
            - "Min value": Minimum value in the column.

    Note:
        The function assumes the input is a pandas Series containing numerical data.
    """
    q1 = float(col.quantile(0.25))
    q3 = float(col.quantile(0.75))
    q2 = float(col.median())
    iqr = float(q3 - q1)

    lower_whisker = float(q1 - 1.5 * iqr)
    upper_whisker = float(q3 + 1.5 * iqr)

    lower_whisker= col[col >= lower_whisker].min()
    upper_whisker = col[col <= upper_whisker].max()

    mild_outliers_range = (float(q1 - 3 * iqr), float(q1 - 1.5 * iqr))
    severe_outliers_range = (float(q3 + 1.5 * iqr), float(q3 + 3 * iqr))

    return {
        "Q1": q1,
        "Q3": q3,
        "Q2": q2,
        "IQR": iqr,
        "Lower whisker": lower_whisker,
        "Upper whisker": upper_whisker,
        "Mild outliers range (left)": mild_outliers_range,
        "Mild outliers range (right)": severe_outliers_range,
        "Max value": col.max(),
        "Min value": col.min(),
        "Extremes": col[(col < mild_outliers_range[0]) | (col > severe_outliers_range[1])].tolist(),
        "Mild outliers": col[(col >= mild_outliers_range[0]) & (col <= mild_outliers_range[1]) | (col >= severe_outliers_range[0]) & (col <= severe_outliers_range[1])].tolist(),
        "Num extremes": len(col[(col < mild_outliers_range[0]) | (col > severe_outliers_range[1])]),
        "Num mild outliers": len(col[(col >= mild_outliers_range[0]) & (col <= mild_outliers_range[1]) | (col >= severe_outliers_range[0]) & (col <= severe_outliers_range[1])]),
    }

def print_boxplot_stats(series):
    stats = boxplot_stats(series)
    for key, value in stats.items():
        print(key, value)


def corr_type(num:float):
    match abs(num):
        case x if x < 0.5:
            note = "No correlación"
        case x if x >= 0.8:
            note = "Fuerte correlación"
        case _:
            note = "Débil correlación"
    return note


from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

def visualizar_en_2d(X_scaled, y):
    tsne = TSNE(n_components=2, random_state=42)
    X_tsne = tsne.fit_transform(X_scaled)
    y_cat = y.astype("category")

    plt.scatter(X_tsne[:,0], X_tsne[:,1], c=y_cat.cat.codes, cmap='viridis')
    plt.title("Distribución de las clases en 2D usando t-SNE")
    plt.xlabel("Dim 1")
    plt.ylabel("Dim 2")
    plt.show()