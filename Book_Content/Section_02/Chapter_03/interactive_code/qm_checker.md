:::{code-cell} python
:tags: ["remove-input"]
:label: quantum_number_validator
from IPython.display import HTML, display
import uuid

def create_validator_widget():
    uid = "val_" + uuid.uuid4().hex[:8]
    
    html_template = r"""
    <div id="ID_container" style="font-family: sans-serif; max-width: 600px; margin: 10px auto; padding: 20px; border: 1px solid #ddd; border-radius: 10px; background-color: #f9f9f9; text-align: center;">
        <h4 style="margin-top: 0;">Quantum Number Validator</h4>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-bottom: 20px;">
            <div>
                <label style="display:block; font-size: 0.8em; font-weight: bold;">n</label>
                <input id="ID_n" type="number" value="1" min="1" style="width: 100%; text-align: center; padding: 5px;">
            </div>
            <div>
                <label style="display:block; font-size: 0.8em; font-weight: bold;">l</label>
                <input id="ID_l" type="number" value="0" min="0" style="width: 100%; text-align: center; padding: 5px;">
            </div>
            <div>
                <label style="display:block; font-size: 0.8em; font-weight: bold;">m<sub>l</sub></label>
                <input id="ID_ml" type="number" value="0" style="width: 100%; text-align: center; padding: 5px;">
            </div>
            <div>
                <label style="display:block; font-size: 0.8em; font-weight: bold;">m<sub>s</sub></label>
                <select id="ID_ms" style="width: 100%; text-align: center; padding: 5px;">
                    <option value="0.5">1/2</option>
                    <option value="-0.5">-1/2</option>
                </select>
            </div>
        </div>
        
        <div id="ID_result_box" style="padding: 15px; border-radius: 8px; border: 2px solid #ccc; background-color: #fff; min-height: 50px;">
            <div id="ID_status" style="font-weight: bold; font-size: 1.1em; margin-bottom: 5px;">ALLOWED</div>
            <div id="ID_details" style="font-size: 0.9em; color: #555;">This represents a <strong>1s</strong> orbital.</div>
        </div>
        
        <script>
            (function() {
                const nIn = document.getElementById('ID_n');
                const lIn = document.getElementById('ID_l');
                const mlIn = document.getElementById('ID_ml');
                const msIn = document.getElementById('ID_ms');
                const status = document.getElementById('ID_status');
                const details = document.getElementById('ID_details');
                const resBox = document.getElementById('ID_result_box');
                
                const lLabels = ['s', 'p', 'd', 'f', 'g', 'h'];

                function validate() {
                    const n = parseInt(nIn.value);
                    const l = parseInt(lIn.value);
                    const ml = parseInt(mlIn.value);
                    const ms = parseFloat(msIn.value);
                    
                    let error = "";
                    
                    if (isNaN(n) || n < 1) error = "n must be a positive integer (1, 2, ...).";
                    else if (l < 0 || l >= n) error = "l must be an integer between 0 and (n-1).";
                    else if (Math.abs(ml) > l) error = "ml must be between -l and +l.";
                    
                    if (error) {
                        status.innerText = "FORBIDDEN";
                        status.style.color = "#d9534f";
                        resBox.style.borderColor = "#d9534f";
                        details.innerText = error;
                    } else {
                        status.innerText = "ALLOWED";
                        status.style.color = "#5cb85c";
                        resBox.style.borderColor = "#5cb85c";
                        const label = lLabels[l] || `(l=${l})`;
                        details.innerHTML = `This represents an electron in a <strong>${n}${label}</strong> orbital.`;
                    }
                }

                [nIn, lIn, mlIn, msIn].forEach(el => el.addEventListener('input', validate));
                validate();
            })();
        </script>
    </div>
    """
    return HTML(html_template.replace("ID_", uid + "_"))

display(create_validator_widget())
:::