import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer

def preprocess_data(df):
    # Handling missing values
    imputer = SimpleImputer(strategy='mean')  # or use 'median', 'most_frequent', etc.
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numerical_cols] = imputer.fit_transform(df[numerical_cols])

    # Encoding categorical features
    categorical_cols = df.select_dtypes(include=['object']).columns
    encoder = OneHotEncoder(sparse=False, drop='first')
    encoded_features = encoder.fit_transform(df[categorical_cols])
    encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(categorical_cols))
    df = df.drop(categorical_cols, axis=1)
    df = pd.concat([df, encoded_df], axis=1)

    # Scaling numerical data
    scaler = StandardScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    return df
