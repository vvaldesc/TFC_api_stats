from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

def RMT_testing(model, X_test, y_test):
    # Hacer predicciones en el conjunto de prueba
    y_pred = model.predict(X_test)

    # Calcular métricas
    
    
#   Error cuadrático medio (MSE, Mean Squared Error): Es el promedio de los cuadrados de los errores. Cuanto más pequeño es el MSE, mejor es el modelo.
#   Raíz del error cuadrático medio (RMSE, Root Mean Squared Error): Es la raíz cuadrada del MSE. Tiene la ventaja de estar en las mismas unidades que la variable objetivo.
#   Error absoluto medio (MAE, Mean Absolute Error): Es el promedio de los valores absolutos de los errores. Es menos sensible a los outliers que el MSE.
#   Coeficiente de determinación (R^2): Mide cuánta de la variabilidad en la variable objetivo puede ser explicada por el modelo. Un valor de 1 indica que el modelo explica toda la variabilidad, mientras que un valor de 0 indica que el modelo no explica nada de la variabilidad.
    
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"MSE: {mse}")
    print(f"RMSE: {rmse}")
    print(f"MAE: {mae}")
    print(f"R^2: {r2}")

    # Devolver las métricas
    return mse, rmse, mae, r2