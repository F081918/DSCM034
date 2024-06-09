
# ML Model Deployment with FastAPI

This repository contains a machine learning model deployment system using FastAPI, Docker, and Kubernetes.

## Requirements

- Python 3.9
- Docker
- Kubernetes

## Project Structure

```
.
├── src
│   ├── main.py
│   └── iris_model.joblib
├── training
│   └── train_model.py
├── tests
│   └── test_app.py
├── ml-deployment.yaml
├── ml-service.yaml
├── Dockerfile
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Train the Model

First, you need to train the model and save it as `iris_model.joblib`.

```bash
python training/train_model.py
```

### 2. Build the Docker Image

Create a Docker image for the FastAPI application.

```bash
docker build -t ml-app:1.0 .
```

### 3. Load the Docker Image into Kubernetes

Since Docker Desktop uses Docker as its container runtime, images built with Docker are automatically available to Kubernetes.

### 4. Deploy to Kubernetes

Use the provided Kubernetes configuration files to deploy the application.

1. Apply the deployment:

```bash
kubectl apply -f ml-deployment.yaml
```

2. Apply the service:

```bash
kubectl apply -f ml-service.yaml
```

### 5. Accessing the FastAPI Documentation

Once the pods are running, you can access the FastAPI documentation.

Navigate to:

```bash
http://localhost/docs
```

## API Usage

The FastAPI application provides an endpoint to predict the class of an iris flower.

### Endpoint

```
POST /predict/
```

### Request Body

```json
{
  "sepal_length": float,
  "sepal_width": float,
  "petal_length": float,
  "petal_width": float
}
```

### Response

```json
{
  "prediction": int
}
```

### Sample Request Body for Iris-virginica (prediction: 2)

```json
{
  "sepal_length": 7.0,
  "sepal_width": 3.2,
  "petal_length": 6.0,
  "petal_width": 2.5
}
```

### Expected Response

```json
{
  "prediction": 2
}
```

## Error Handling

The application provides appropriate error messages for invalid inputs or prediction errors.

## Running Tests

You can run tests using pytest to ensure the application works correctly.

```bash
pytest tests/
```
