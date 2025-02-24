from flask import Flask, request, render_template, jsonify
import pickle
import os
from flask_cors import CORS  # Import Flask-CORS
from counloop import count_loops
from cyclomatic import calculate_cyclomatic_complexity
from funlen import calculate_function_length
from modularity import calculate_modularity_score
from coment_quality import calculate_comment_quality
from naming_quality import calculate_naming_quality
from get_fun_name import get_function_names

app = Flask(__name__)

# Apply CORS to all routes globally
CORS(app)

base_dir = os.path.dirname(__file__)

# Define paths for the model and scaler files
model_path = os.path.join(base_dir, "Model", "Model.pkl")
scaler_path = os.path.join(base_dir, "Model", "scaler.pkl")


with open(model_path, 'rb') as f:
    model = pickle.load(f)

with open(scaler_path, 'rb') as f:
    scaler = pickle.load(f)

# Function to perform all code analysis
def analyze_code(code):
    try:
        function_names=get_function_names(code)
        name=function_names[0]

        cyclomatic_complexity = calculate_cyclomatic_complexity(code)
        loop_count = count_loops(code)
        comment_quality = calculate_comment_quality(code, name)
        naming_quality = calculate_naming_quality(name)
        function_length = calculate_function_length(code)
        modularity = calculate_modularity_score(code)

        analysis_result = {
            'Cyclomatic_Complexity': cyclomatic_complexity,
            'Number_of_Loops': loop_count,
            'Function_Length': function_length,
            'Modularity': modularity,
            'Comment_Quality': comment_quality,
            'Naming_Quality': naming_quality
        }
        return analysis_result  # Directly return the dictionary

    except Exception as e:
        # For testing, simply return the error message instead of Flask response
        return {'status': 'error', 'message': str(e)}



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit_code', methods=['POST'])
def submit_code():
    try:
        data = request.json
        code = data.get('code')

        if not code:
            return jsonify({'error': 'No code provided'}), 400

        # Analyze the code using predefined functions
        analysis_result = analyze_code(code)

        # Log the analysis result
        print("Analysis Result:", analysis_result)

        # Extract analysis results
        cyclomatic_complexity = analysis_result['Cyclomatic_Complexity']
        function_length = analysis_result['Function_Length']
        number_of_loops = analysis_result['Number_of_Loops']
        modularity = analysis_result['Modularity']
        comment_quality = analysis_result['Comment_Quality']
        naming_quality = analysis_result['Naming_Quality']

        # Create a feature vector for the model
        features = [cyclomatic_complexity, function_length, number_of_loops, modularity, comment_quality, naming_quality]

        # Scale the features and predict score
        if scaler and model:
            features_scaled = scaler.transform([features])
            score = model.predict(features_scaled)[0]
            score= round(score, 2)

            # Generate suggestions based on analysis metrics
            suggestions = []

            # Score-based suggestions
            if score < 3:
                suggestions.append("The code is not readable. Consider simplifying it and improving clarity.")
            elif 3 <= score <= 7:
                suggestions.append("The code is moderately readable.")
            else:
                suggestions.append("Good job! Your code is well-structured and readable.")

            # Specific improvement suggestions
            if comment_quality == 0:
                suggestions.append("Add comments to improve code readability.")
            elif comment_quality < 5:
                suggestions.append("Make comments more relevant and meaningful.")

            if naming_quality < 5:
                suggestions.append("Use meaningful function names that clearly describe their purpose.")

            if (cyclomatic_complexity > 3 or function_length > 15 or number_of_loops > 2) and modularity < 2:
                suggestions.append("Improve modularity by breaking down functions into smaller, reusable units.")

            return jsonify({'score': score, 'suggestions': suggestions})

        else:
            return jsonify({'error': 'Scaler or model not loaded correctly'}), 500

    except Exception as e:
        # Log the exception for debugging
        print(f"Exception occurred: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
