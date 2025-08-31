def boxplot_stats(col):
    q1 = col.quantile(0.25)
    q3 = col.quantile(0.75)
    iqr = q3 - q1

    lower_whisker = q1 - 1.5 * iqr
    upper_whisker = q3 + 1.5 * iqr

    mild_outliers_range = (q1 - 3 * iqr, q1 - 1.5 * iqr)
    severe_outliers_range = (q3 + 1.5 * iqr, q3 + 3 * iqr)

    return {
        "Q1": q1,
        "Q3": q3,
        "IQR": iqr,
        "Lower whisker": lower_whisker,
        "Upper whisker": upper_whisker,
        "Mild outliers range": mild_outliers_range,
        "Severe outliers range": severe_outliers_range,
        "Max value": col.max(),
        "Min value": col.min()
    }
