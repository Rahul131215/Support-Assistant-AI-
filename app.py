import gradio as gr

def greet(name):
    return f"Hello, {name}! 👋"

demo = gr.Interface(
    fn=greet,
    inputs="text",
    outputs="text",
    title="Simple Greeting App"
)

if __name__ == "__main__":
    demo.launch()
