 
from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np
model = load_model('airline')






def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions

def run():
    from PIL import Image
    image = Image.open('airline pic2')
    image_office = Image.open('airline pic')
    st.image(image,use_column_width=True)
    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?",
    ("Online", "Batch"))
    st.sidebar.info('This app is created to predict the satisfaction of passenger')
    st.sidebar.success('https://www.pycaret.org')
    st.sidebar.image(image_office)
    st.title("Predicting satisfaction of passenger")
    if add_selectbox == 'Online':
        Gender= st.selectbox('Gender',['Female','Male'])
        customer_type= st.selectbox('customer_type',['Loyal Customer','disloyal Customer'])
        age=st.number_input('age' , min_value=7.0, max_value=90.0, value=7.0)
        type_of_travel= st.selectbox('type_of_travel',['Business travel','Personal Travel'])
        customer_class= st.selectbox('customer_class',['Business','Eco','Eco Plus'])
        flight_distance=st.number_input('flight_distance',min_value=31.0, max_value=5000.0, value=31.0)
        inflight_wifi_service=st.number_input('inflight_wifi_service',min_value=0.0, max_value=5.0, value=0.0)
        departure_arrival_time_convenient=st.number_input('departure_arrival_time_convenient',min_value=0.0, max_value=5.0, value=0.0)
        ease_of_online_booking=st.number_input('ease_of_online_booking',min_value=0.0, max_value=5.0, value=0.0)
        gate_location=st.number_input('gate_location',min_value=0.0, max_value=5.0, value=0.0)
        food_and_drink=st.number_input('food_and_drink',min_value=0.0, max_value=5.0, value=0.0)
        online_boarding=st.number_input('online_boarding',min_value=0.0, max_value=5.0, value=0.0)
        seat_comfort=st.number_input('seat_comfort',min_value=0.0, max_value=5.0, value=0.0)
        inflight_entertainment=st.number_input('inflight_entertainment',min_value=0.0, max_value=5.0, value=0.0)
        onboard_service=st.number_input('onboard_service',min_value=0.0, max_value=5.0, value=0.0)
        leg_room_service=st.number_input('leg_room_service',min_value=0.0, max_value=5.0, value=0.0)
        baggage_handling=st.number_input('baggage_handling',min_value=0.0, max_value=5.0, value=0.0)
        checkin_service=st.number_input('checkin_service',min_value=0.0, max_value=5.0, value=0.0)
        inflight_service=st.number_input('inflight_service',min_value=0.0, max_value=5.0, value=0.0)
        cleanliness=st.number_input('cleanliness',min_value=0.0, max_value=5.0, value=0.0)
        departure_delay_in_minutes=st.number_input('departure_delay_in_minutes',min_value=0.0, max_value=1600.0, value=0.0)
        arrival_delay_in_minutes=st.number_input('arrival_delay_in_minutes',min_value=0.0, max_value=1600.0, value=0.0)
        output=""
        input_dict={'Gender':Gender,'customer_type':customer_type,'age':age,'type_of_travel':type_of_travel,'customer_class':customer_class,'flight_distance':flight_distance,'inflight_wifi_service' : inflight_wifi_service,'departure_arrival_time_convenient':departure_arrival_time_convenient,'ease_of_online_booking':ease_of_online_booking,'gate_location':gate_location,'food_and_drink':food_and_drink,'online_boarding':online_boarding,'seat_comfort':seat_comfort,'inflight_entertainment':inflight_entertainment,'onboard_service':onboard_service,'leg_room_service':leg_room_service,'baggage_handling':baggage_handling,'checkin_service':checkin_service,'inflight_service':inflight_service,'cleanliness':cleanliness,'departure_delay_in_minutes':departure_delay_in_minutes,'arrival_delay_in_minutes':arrival_delay_in_minutes}
        input_df = pd.DataFrame([input_dict])
        if st.button(" predict satisfaction"):
            output = predict(model=model, input_df=input_df)
            output = str(output)
            if output == '0' :
              output="satisfied the travel"
            else:
              output="neutral or dissatisfied the travel"
        st.success('The Prediction   --  {}'.format(output))
    if add_selectbox == 'Batch':
        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])
        if file_upload is not None:
            data = pd.read_csv(file_upload)            
            predictions = predict_model(estimator=model,data=data)
            st.write(predictions)
def main():
    run()

if __name__ == "__main__":
  main()
