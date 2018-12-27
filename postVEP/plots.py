def plot_feature_counts(obj):
    return obj.data['Uploaded_variation'].value_counts().plot.bar()
