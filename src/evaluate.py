import dvc.api
import os
from helper import load_data
from sklearn.metrics import accuracy_score
from dvclive import Live
from mlem.api import load
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score,
                            )
import mlflow
import mlflow.sklearn



MLFLOW_TRACKING_URI=os.getenv('MLFLOW_TRACKING_URI')

def load_model(path: str):
    """Load model from path"""
    return load(path)


def evaluate() -> None:
    """Evaluate model and log metrics"""
    params = dvc.api.params_show()
    with mlflow.start_run(): 
        with Live(save_dvc_exp=True, resume=True) as live:
            X_test = load_data(f"{params['data']['intermediate']}/X_test.pkl")
            y_test = load_data(f"{params['data']['intermediate']}/y_test.pkl")
            model = load_model(params["model"])
            y_pred = model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            precision = precision_score(y_test, y_pred, average='micro')
            recall = recall_score(y_test, y_pred, average='micro')
            f1 = f1_score(y_test, y_pred,average='micro')
            print(f"The model's accuracy is {accuracy}")
            print(f"The model's  precision is {precision}")
            print(f"The model's recall is {recall}")
            print(f"The model's  f1 is { f1}")
            live.log_metric("accuracy", accuracy)
            live.log_metric("precision", precision)
            live.log_metric("recall", recall)
            live.log_metric("f1", f1)
            
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("precision", precision)
        mlflow.log_metric("recall", recall)
        mlflow.log_metric("f1", f1)



if __name__ == "__main__":
    evaluate()
    
