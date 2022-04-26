import streamlit as st


st.header("========== WineMakers Dilemna ==========")
st.caption("Created By: Lokeshwar Jha")

def estimate_value(prob_storm, sensitivity, specificity, p_harvest, p_no_harvest_storm, p_no_harvest_no_storm):
    
    p_dns = specificity*(1-prob_storm) + (1-sensitivity)*(1-prob_storm)
    p_ns_dns = (specificity*prob_storm)/p_dns
    
    val_nh_ns = p_ns_dns*p_no_harvest_no_storm
    val_nh_s = (1-p_ns_dns)*p_no_harvest_storm
    val_nh = val_nh_ns + val_nh_s
    
    val_h = p_harvest*(1-p_dns)
    
    total_estimated_value = (val_nh_ns + val_nh_s)*p_dns + val_h
    
    return total_estimated_value

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
                p_no_harvest_no_storm = (no_sugar*960 + typical_sugar*1410 + high_sugar*1500)/100
                p_no_harvest_storm = (botrytis_chance*3300 + (100-botrytis_chance)*420)/100
                p_harvest = 960
                eval = estimate_value(prob_storm = 0.5, sensitivity = 0.17, specificity = 0.86,
                                     p_harvest = p_harvest, p_no_harvest_storm = p_no_harvest_storm,
                                     p_no_harvest_no_storm = p_no_harvest_no_storm)
                st.success('Calculation done.')
                
                if eval > p_harvest:
                    st.success('E-value: ' + str(eval) + 'k$')
                    st.write('Will recommend to buy clairvoyance')
                else:
                    st.error('E-value: ' + str(eval) + 'k$')
                    st.write('Will not recommend to buy clairvoyance')

        
if __name__ == "__main__":
    main()
