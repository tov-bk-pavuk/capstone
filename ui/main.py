import gradio as gr


def estimate_probability(
        age, birth_country, citizenship, education, gender, legal_status, NOC, language_proficiency, skill_level
        ):
    # Placeholder function for estimation logic
    probability = "50%"  # Example probability rate
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
            age = gr.Number(label="Age")
            birth_country = gr.Textbox(label="Birth Country")
            citizenship = gr.Textbox(label="Citizenship")
            education = gr.Dropdown(label="Education", choices=["None", "Primary", "Secondary", "Tertiary"])
            gender = gr.Radio(label="Gender", choices=["Male", "Female", "Other"])
            legal_status = gr.Textbox(label="Legal Status")
            NOC = gr.Textbox(label="NOC")
            language_proficiency = gr.Slider(label="Language Proficiency", minimum=0, maximum=100, step=1)
            skill_level = gr.Slider(label="Skill Level", minimum=0, maximum=100, step=1)
            estimate_button = gr.Button("Estimate")

        with gr.Column():
            result = gr.Textbox(label="Probability rate estimation field", interactive=False)

    estimate_button.click(
        estimate_probability,
        inputs=[age, birth_country, citizenship, education, gender, legal_status, NOC, language_proficiency,
            skill_level],
        outputs=result
        )

    gr.HTML(footer_html)


if __name__ == '__main__':
    demo.launch()
