import gradio as gr

from modeling.probability_estimation import probabilities
from modeling.probability_estimation import estimate_probability


def get_probability(
        age,
        education,
        gender,
        legal_status,
        marital_status,
        preferred_language,
        province
        ):
    user_input = {
        "age": age,
        "education": education,
        "gender": gender,
        "legal_status": legal_status,
        "marital_status": marital_status,
        "preferred_language": preferred_language,
        "province": province,
        }
    # Placeholder function for estimation logic
    # probability = "50%"  # Example probability rate
    probability = estimate_probability(user_input)
    return f"Probability rate estimation: {probability}"


header_html = """
<div style='background-image: url("header.jpg"); height: 100px; background-size: cover;'></div>
"""

footer_html = """
<div style='background-image: url("footer.jpg"); height: 100px; background-size: cover;'></div>
"""

with gr.Blocks() as demo:
    gr.HTML(header_html)

    with gr.Row():
        with gr.Column():
            # age = gr.Dropdown(label="Age", choices=["None", "Primary", "Secondary", "Tertiary"])
            age = gr.Dropdown(label="Age", choices=probabilities["age"].keys())
            education = gr.Dropdown(label="Education", choices=probabilities["education"].keys())
            gender = gr.Radio(label="Gender", choices=probabilities["gender"].keys())
            legal_status = gr.Dropdown(label="Legal status", choices=probabilities["legal_status"].keys())
            marital_status = gr.Dropdown(label="Marital status", choices=probabilities["marital_status"].keys())
            preferred_language = gr.Radio(
                label="Preferred language", choices=probabilities["preferred_language"].keys()
                )
            province = gr.Dropdown(label="Province", choices=probabilities["province"].keys())
            # NOC = gr.Textbox(label="NOC")
            # language_proficiency = gr.Slider(label="Language Proficiency", minimum=0, maximum=100, step=1)
            # skill_level = gr.Slider(label="Skill Level", minimum=0, maximum=100, step=1)
            estimate_button = gr.Button("Estimate")

        with gr.Column():
            result = gr.Textbox(label="Probability rate estimation field", interactive=False)

    estimate_button.click(
        get_probability,
        inputs=[
            age,
            education,
            gender,
            legal_status,
            marital_status,
            preferred_language,
            province
            ],
        outputs=result
        )

    gr.HTML(footer_html)

if __name__ == '__main__':
    demo.launch()
