# -*- coding: utf-8 -*-


import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('C:/Users/adity/Downloads/FraudDetection-master/Credit_Card_default_pickle_RF_final', 'rb'))


# creating a function for Prediction

def Fraud_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'Transaction is not Fraud'
    elif (prediction[0] == 1):
      return 'It is a Fraud Transaction.'
  
    
  
def main():
    
    
    # giving a title
    st.title('credit card fraud Prediction Web App')
    
    
    # getting the input data from the user
    
    
    LIMIT_BAL = st.text_input('Limit bal')
    SEX  = st.text_input('sex')
    EDUCATION = st.text_input('education')
    MARRIAGE = st.text_input('marriage')
    AGE = st.text_input('age')
    September_Repayment_Status = st.text_input('september repay')
    July_Repayment_Status = st.text_input('july repay')
    August_Repayment_Status = st.text_input('august repay')
    June_Repayment_Status = st.text_input('june repay')
    May_Repayment_Status = st.text_input('May repay')
    April_Repayment_Status = st.text_input('April repay')
    September_bill_statement =st.text_input('sept bell statement')
    August_bill_statement = st.text_input('August bill statement')
    July_bill_statement = st.text_input('july bill statement')
    June_bill_statement = st.text_input('june bill statement')
    May_bill_statement = st.text_input('may bill statement')
    April_bill_statement = st.text_input('april bill statement')
    September_previous_Payment = st.text_input('sept prev statement')
    August_previous_Payment = st.text_input('august prev payment')
    July_previous_Payment = st.text_input('july prev payment')
    June_previous_payment = st.text_input('June prev payment')
    May_previous_payment = st.text_input('May prev payment')
    April_previous_payment = st.text_input('April prev payment')
    
    
    # code for Prediction
    is_fraud = ''
    
    # creating a button for Prediction
    
    if st.button('Fraud prediction'):
        is_fraud = Fraud_prediction([LIMIT_BAL, SEX, EDUCATION, MARRIAGE, AGE, September_Repayment_Status, July_Repayment_Status,
        August_Repayment_Status,June_Repayment_Status,May_Repayment_Status,April_Repayment_Status, September_bill_statement,
        August_bill_statement,July_bill_statement, June_bill_statement, May_bill_statement, April_bill_statement,
        September_previous_Payment,August_previous_Payment, July_previous_Payment, June_previous_payment,
        May_previous_payment, April_previous_payment])
        
        
    st.success(is_fraud)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
  
    
  