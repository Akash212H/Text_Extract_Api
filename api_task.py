from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
import base64
import io

app = Flask(__name__)

@app.route('/api_extract_text', methods=['POST'])

def api_extract_text():
    try:
        data = request.json
        base64_image = data.get("image")
        if not base64_image:
            return jsonify({"Error": "Data not provided, try again please"}), 400

       


        image_data = base64.b64decode(base64_image)
        image = Image.open(io.BytesIO(image_data))

       
        api_extract_text = pytesseract.image_to_string(image)

    
        result = {
            "CI Seria": None,
            "CNP": None,
            "Nume Familie": None,
            "Prenume": None,
            "Sex": None,
            "Loc nastere": None,
            "Domiciliu": None,
            "Emis de": None,
            "Valabilitate": None
           
        }

        
        for key in result.keys():
            if key in api_extract_text:
                result[key] = api_extract_text.split(key)[-1].split("\n")[0].strip()

        # Return the result
        return jsonify(result), 200

    except Exception as ak:
        return jsonify({"error": str(ak)}), 500

if __name__ == "__main__":
    app.run(debug=True)
