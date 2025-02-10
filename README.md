
# Service Time Estimation API

Welcome to the Service Time Estimation API! This API uses a regression model based on a Regression Tree to predict the estimated service time in a hairdressing and aesthetics academy. This project was created as part of my TFC.

This API is designed to deliver complex statistics for my TFC, offering significantly improved scalability and is ready for immediate use.

![License](https://img.shields.io/github/license/vvaldesc/TFC_gestor_academia)
![Stars](https://img.shields.io/github/stars/vvaldesc/TFC_gestor_academia)
![Issues](https://img.shields.io/github/issues/vvaldesc/TFC_gestor_academia)

## Table of Contents

- [Requirements](#requirements)
- [Usage](#usage)
- [Running](#running)
- [Data](#data)
- [Model](#model)
- [Training](#training)
- [Developing](#developing)
- [Environment](#environment)
- [Testing](#testing)

## Requirements

This API is developed with 3.12 Python
To install the required packages, run the following command:

```sh
pip install -r requirements.txt
```

## Usage

The API offers several endpoints:

- **`/api/estimatedtime`**: Accepts a POST request with the service details and returns the estimated service time using a previously trained model.
- **`/api/estimatedtime/noTrain`**: Similar to the above, but trains the model with each request instead of using a previously trained model.
- **`/api/estimatedtime/train`**: Trains the model with the data provided in the POST request and returns the ROC curve of the model, which is a measure of its reliability.
- **`/`**: Returns the message "Hello world" to check that the API is working correctly.

## Running

To run the API, execute the following command:

```sh
python main.py
```

If this fails, use a custom environment by running `.\flask_start.ps1` with PowerShell and installig dependencies to this envoirment.

This will start the API on port 5000 by default.

## Data

An example of the data used to train the model is provided in `sampleData.json` file
Previous file is used by default to provide data to the client

The data used to train the model should be provided in the body of the POST request in JSON format. The required fields are:

- `price`: The price of the service.
- `employee_salary`: The salary of the employee providing the service.
- `rating`: The rating of the service.
- `service_id`: The ID of the service.
- `client_id`: The ID of the client.
- `teacher_id`: The ID of the teacher.
- `weather`: The weather during the service.

An example POST body:
```json

            {
                "id": 1,
                "client_id": 1,
                "teacher_id": 2,
                "student_id": null,
                "delay": null,
                "service_id": 1,
                "created_at": "2022-07-16T22:00:00.000Z",
                "updated_at": null,
                "reserved_at": "2024-05-28T17:10:09.133Z",
                "rating": null,
                "price": 5,
                "weather": "Snowy",
                "client_name": "John Doe",
                "teacher_name": "Emily Johnson",
                "student_name": null,
                "client_surname": "Doe",
                "teacher_surname": "Johnson",
                "student_surname": null,
                "client_address": "123 Main St",
                "teacher_address": "321 Pine St",
                "student_address": null,
                "client_phone_number": "123456789",
                "teacher_phone_number": "222222222",
                "student_phone_number": null,
                "client_email": "example@example.com",
                "teacher_email": "example@example.com",
                "student_email": null,
                "employee_salary": 400
            }

```

## Model

The regression model used is a Regression Tree from the `sklearn` package. It is trained with the provided data and then used to make predictions about the service time.
The model provided in the repository is not trained with real data, in fact it is trained with more than 2000 fake registers with certain sense, it would only be valid if it is trained with real data.

## Training

Through an http request, the model expects a JSON array with a certain structure, the structure that the model expects can be edited in the code.
The expected structure in the array is similar to the previously mentioned.

When training, the new model name will end in 'test', so you have to rename it to 'model' if you really want to use it

## Developing

To correctly develop this app, would suggest to turn Flask debug mode on.

## Environment

It's important to watch out this variables.

- `FLASK_APP`: main.py.
- `FLASK_ENV`: (development/False) development to develop.
- `PORT`: (X.X.X.X).
- `USE_SAMPLE_DATA`: (True/False) switch that decides if the API uses the example dataset or an external API HTTP request.

## Testing

Tests can be performed using the `regression_model_test.py` script, which calculates various performance metrics of the model, such as:

- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)
- Coefficient of Determination (R²)

This are the default testing results:

- `mse`: 27.058695750000002,
- `rmse`: 5.201797357644759,
- `mae`: 3.995375,
- `r2`: 0.2489379443577333

## Contact

Deploy with pythonAnyWhere

For any inquiries, please reach out to me via [email](mailto:vvaldescobos@gmail.com).

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/vvaldesc">vvaldesc</a>
</p>
