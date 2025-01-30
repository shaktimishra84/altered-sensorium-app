import streamlit as st

class AlteredSensoriumAssistant:
    def __init__(self):
        self.recommendations = []

    def assess_oxygenation(self, spo2, gcs, secretions):
        if spo2 < 94:
            self.recommendations.append("Administer oxygen (SpO2 < 94%).")
        if gcs < 8 or secretions:
            self.recommendations.append("Intubate and secure the airway (GCS < 8 or pooling of secretions).")

    def assess_circulation(self, sbp, map_):
        if sbp < 100 or map_ < 65:
            self.recommendations.append("Maintain circulation: Administer IV fluids or vasopressors.")

    def assess_glucose(self, glucose):
        if glucose < 70:
            self.recommendations.append("Administer dextrose to correct hypoglycemia (glucose < 70 mg/dL).")

    def check_seizures(self, seizures):
        if seizures:
            self.recommendations.append("Refer to Algorithm 2 for seizure management.")

    def perform_physical_exam(self, trauma, fever, meningitis_signs, skin_rashes, visible_clues):
        if trauma:
            self.recommendations.append("Evaluate for trauma: Inspect for injuries, bruises, or head trauma.")
        if fever or meningitis_signs:
            self.recommendations.append("Suspect infection: Perform lumbar puncture and order cultures.")
        if skin_rashes:
            self.recommendations.append("Evaluate skin rashes for systemic infection.")
        if visible_clues:
            self.recommendations.append("Investigate visible clues: Needle marks, breath odor, jaundice, etc.")

    def order_diagnostics(self):
        self.recommendations.append("Order non-contrast CT brain.")
        self.recommendations.append("Perform laboratory tests (refer to Table 3).")
        self.recommendations.append("Measure optic nerve sheath diameter.")

    def classify_cause(self, infection, metabolic, cerebral_injury, psychogenic):
        if infection:
            self.recommendations.append("Likely cause: Infection. Investigate fever, neck stiffness, and elevated WBC.")
        elif metabolic:
            self.recommendations.append("Likely cause: Metabolic. Check for organ failure, abnormal labs, and systemic diseases.")
        elif cerebral_injury:
            self.recommendations.append("Likely cause: Cerebral injury. Assess for focal deficits, trauma, or abnormal CT/MRI.")
        elif psychogenic:
            self.recommendations.append("Likely cause: Psychogenic. Consider psychiatric history and absence of other abnormalities.")
        else:
            self.recommendations.append("Cause unclear. Continue monitoring and further testing.")

    def run(self, patient_data):
        self.assess_oxygenation(patient_data['spo2'], patient_data['gcs'], patient_data['secretions'])
        self.assess_circulation(patient_data['sbp'], patient_data['map'])
        self.assess_glucose(patient_data['glucose'])
        self.check_seizures(patient_data['seizures'])
        self.perform_physical_exam(patient_data['trauma'], patient_data['fever'], 
                                   patient_data['meningitis_signs'], patient_data['skin_rashes'], 
                                   patient_data['visible_clues'])
        self.order_diagnostics()
        self.classify_cause(patient_data['infection'], patient_data['metabolic'], 
                            patient_data['cerebral_injury'], patient_data['psychogenic'])
        return self.recommendations

# Streamlit App
st.title("Altered Sensorium Assistant")

# Input fields
spo2 = st.number_input("SpO2 (%)", min_value=0, max_value=100, value=90)
gcs = st.number_input("GCS Score", min_value=0, max_value=15, value=7)
secretions = st.checkbox("Pooling of Secretions?")
sbp = st.number_input("Systolic Blood Pressure (mmHg)", min_value=0, value=90)
map_ = st.number_input("MAP (mmHg)", min_value=0, value=60)
glucose = st.number_input("Glucose (mg/dL)", min_value=0, value=65)
seizures = st.checkbox("Seizures?")
trauma = st.checkbox("Signs of Trauma?")
fever = st.checkbox("Fever?")
meningitis_signs = st.checkbox("Signs of Meningitis?")
skin_rashes = st.checkbox("Skin Rashes?")
visible_clues = st.checkbox("Visible Clues (needle marks, jaundice)?")
infection = st.checkbox("Suspected Infection?")
metabolic = st.checkbox("Suspected Metabolic Cause?")
cerebral_injury = st.checkbox("Suspected Cerebral Injury?")
psychogenic = st.checkbox("Suspected Psychogenic Cause?")

# Run the assistant
if st.button("Get Recommendations"):
    assistant = AlteredSensoriumAssistant()
    data = {
        'spo2': spo2,
        'gcs': gcs,
        'secretions': secretions,
        'sbp': sbp,
        'map': map_,
        'glucose': glucose,
        'seizures': seizures,
        'trauma': trauma,
        'fever': fever,
        'meningitis_signs': meningitis_signs,
        'skin_rashes': skin_rashes,
        'visible_clues': visible_clues,
        'infection': infection,
        'metabolic': metabolic,
        'cerebral_injury': cerebral_injury,
        'psychogenic': psychogenic,
    }
    recommendations = assistant.run(data)
    st.subheader("Recommendations:")
    for rec in recommendations:
        st.write(f"- {rec}")
y
