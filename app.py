from flask import Flask, render_template, request

app = Flask(__name__)

def relu(x):
    """
    ReLU (Rectified Linear Unit) activation function.
    
    Args:
    x (float or array): The input value(s) for which ReLU will be applied.
    
    Returns:
    float or array: The result after applying ReLU.
    """
    if isinstance(x, (list, tuple)):
        return [max(0, xi) for xi in x]
    return max(0, x)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apply_relu', methods=['POST'])
def apply_relu():
    try:
        # Parse the input data (assumed to be a comma-separated list of numbers)
        data = request.form['numbers']
        
        # Convert input to a list of floats
        input_values = [float(x.strip()) for x in data.split(',')]
        
        # Apply ReLU
        output_values = relu(input_values)
        
        # Zip input and output values together and pass to the result template
        result = zip(input_values, output_values)
        
        # Render result.html and pass the zipped data
        return render_template('result.html', result=result)
    
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
