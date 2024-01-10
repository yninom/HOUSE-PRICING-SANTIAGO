
import streamlit as st
from model import predict_price

def main():
    st.title("Linear Regression Price Predictor")
    
    # User input for variables
    habitaciones = st.number_input("Número de habitaciones", min_value=1, max_value=5, value=3)
    piso = st.number_input("Número de piso", min_value=1, max_value=20, value=5)
    barrio = st.number_input("Número del barrio", min_value=1, max_value=50, value=1)
    
    # Add a button to generate the prediction
    if st.button("Generar predicción"):
        # Predict price using the model
        predicted_price = predict_price(habitaciones, piso, barrio)
        
        # Display the predicted price
        st.subheader("Precio predicho:")
        st.write(predicted_price)



if __name__ == "__main__":
    main()

