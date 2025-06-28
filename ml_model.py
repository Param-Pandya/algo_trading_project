from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from indicators import calculate_indicators

def prepare_ml_data(df):
    df = calculate_indicators(df)
    df['MACD'] = df['Close'].ewm(span=12).mean() - df['Close'].ewm(span=26).mean()
    df['Target'] = (df['Close'].shift(-1) > df['Close']).astype(int)
    df.dropna(inplace=True)
    features = df[['RSI', 'MACD', 'Volume']]
    target = df['Target']
    return train_test_split(features, target, test_size=0.2, random_state=42)

def train_model(df):
    X_train, X_test, y_train, y_test = prepare_ml_data(df)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    return accuracy_score(y_test, predictions)
