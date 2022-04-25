import streamlit as st


st.header("========== WineMakers Dilemna ==========")
st.caption("Created By: Lokeshwar Jha")


def main():

    botrytis_chance = st.slider("Pick a likelihood for development of botrytis mold", min_value=0, max_value=100, value=10, step=5)
    no_sugar = st.slider("Pick a likelihood for chance of no sugar", min_value=0, max_value=100, value=60, step=5)
    typical_sugar = st.slider("Pick a likelihood for chance of typical sugar", min_value=0, max_value=100, value=30, step=5)
    high_sugar = st.slider("Pick a likelihood for chance of high sugar", min_value=0, max_value=100, value=10, step=5)

    total_sugar_likelihood = no_sugar + typical_sugar + high_sugar

    if total_sugar_likelihood > 100:
        st.write("Sum of sugar likelihoods should not exceed 100, please select values accordingly")
    elif total_sugar_likelihood < 100:
        st.write("Sum of sugar likelihoods should not be less than 100, please select values accordingly")
    else:
        e_val_btn = st.button("Calculate e-value")
        if e_val_btn:
            with st.spinner('Calculating e-value....'):
                st.success('Calculation done.')
                e_val, recommendation = -120, 'Will recommend using the model'

                if e_val > 0:
                    st.success('E-value: ' + str(e_val) + '$')
                    st.write(recommendation)
                else:
                    st.error('E-value: ' + str(e_val) + '$')
                    st.write(recommendation)

        
if __name__ == "__main__":
    main()
