import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import scikitplot as skplt

def prediksi():
    st.title("🔍 Prediksi Churn Pelanggan dengan XGBoost")

    def load_model():
        return joblib.load("xgb_model.joblib")

    def load_data():
        X_test = pd.read_csv("X_test.csv")
        y_test = pd.read_csv("y_test.csv")
        return X_test, y_test

    xgb_model = load_model()
    X_test, y_test = load_data()

    st.markdown("#### Pilih pelanggan yang ingin diprediksi")
    with st.form("form_prediksi"):
        idx = st.number_input("Index data pelanggan (0 - {}):".format(len(X_test)-1), min_value=0, max_value=len(X_test)-1, value=0)
        submit = st.form_submit_button("Lakukan Prediksi")

        if submit:
            st.markdown("### 🧾 Data Pelanggan")
            st.dataframe(X_test.iloc[[idx]])

            pred = xgb_model.predict(X_test.iloc[[idx]])
            prob = xgb_model.predict_proba(X_test.iloc[[idx]])

            pred_label = "Churn" if pred[0] == 1 else "Tidak Churn"
            st.success(f"Hasil Prediksi: **{pred_label}**")
            st.write(f"Probabilitas Churn: **{round(prob[0][1]*100, 2)}%**")

            st.markdown("---")
            st.markdown("### 📊 Profil Fitur Pelanggan")

            sample_data = X_test.iloc[idx]
            sample_data = sample_data.copy().astype(float)

            df_fitur = pd.DataFrame(sample_data).T
            df_fitur = df_fitur.T.reset_index()
            df_fitur.columns = ['Fitur', 'Nilai']

            chart_data = df_fitur.set_index('Fitur')
            st.line_chart(chart_data)

            st.markdown("---")
            st.markdown("### 📈 Evaluasi Model - ROC Curve")
            prob_all = xgb_model.predict_proba(X_test)
            skplt.metrics.plot_roc_curve(y_test, prob_all)
            st.pyplot(plt.gcf())

            st.markdown("### 🧮 Confusion Matrix")
            y_pred_all = xgb_model.predict(X_test)
            skplt.metrics.plot_confusion_matrix(y_test, y_pred_all)
            st.pyplot(plt.gcf())
