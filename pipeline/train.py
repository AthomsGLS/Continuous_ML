from src import data_preprocessing, train_test_split, model_train, model_evaluation
import argparse
import os

parser = argparse.ArgumentParser(description="Train a model on the wine quality dataset")
parser.add_argument("--seed", type=int, default=42, help="Random seed")
parser.add_argument("--data_path", type=str, default="data/wine_quality.csv", help="Path to the dataset")
parser.add_argument("--output_path", type=str, default="results", help="Path to the output directory")
parser.add_argument("--test_size", type=float, default=0.2, help="Size of the test set")
parser.add_argument("--target_name", type=str, default="quality", help="Name of the target variable")
args = parser.parse_args()

# if output path does not exist, create it
if not os.path.exists(args.output_path):
    os.makedirs(args.output_path)

# run pipeline
df = data_preprocessing.data_processing(args.data_path)
X_train, X_test, y_train, y_test = train_test_split.data_split(df, args.target_name, args.test_size, args.seed)
model = model_train.model_train(X_train, y_train, args.seed)
model_evaluation.model_evaluation(model, X_train, y_train, X_test, y_test, args.output_path)