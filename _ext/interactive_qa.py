import html
import uuid
import json

class QuestionBlock:
    """
    Renders a self-contained block of interactive questions.
    Each block manages its own state and saving logic.
    """
    def __init__(self):
        self.questions = []
        self._rendered = False

    def add_question(self, question_id: str, question_text: str):
        """Adds a question to this specific block."""
        if self._rendered:
            print("Warning: Cannot add questions after the block has been rendered.")
            return
        if not question_id or not question_text:
            raise ValueError("question_id and question_text cannot be empty.")
        self.questions.append({'id': question_id, 'text': question_text})

    def render(self) -> str:
        """Generates the HTML for just the questions and a self-contained script."""
        if self._rendered:
            return ""
        if not self.questions:
            return "<p><em>No questions were added to this block.</em></p>"
        self._rendered = True
        
        widget_id = f"qa-block-{uuid.uuid4().hex}"
        
        html_parts = []
        for q in self.questions:
            safe_id = html.escape(q['id'])
            # We escape the text for the data attribute to ensure it doesn't break the HTML structure
            attr_safe_text = html.escape(q['text'])
            # For the visible label, we allow HTML tags (like <b> or <i>) to render formatting
            display_text = q['text']
            
            html_parts.append(f"""
            <div class="question-container mb-8" data-question-id="{safe_id}" data-raw-text="{attr_safe_text}">
                <label for="{safe_id}" class="block text-lg font-semibold text-gray-700 mb-2">{display_text}</label>
                <textarea id="{safe_id}" rows="5" class="answer-textarea w-full p-3 border border-gray-300 rounded-lg" placeholder="Type your answer here..."></textarea>
                <div class="save-status text-xs text-gray-500 mt-1 h-4"></div>
            </div>
            """)
        
        all_questions_html = "\n".join(html_parts)

        return f"""
        <div id="{widget_id}" class="qa-block-container" style="clear: both; width: 100%;">
            {all_questions_html}
            <script>
            (function() {{
                const container = document.getElementById('{widget_id}');
                if (!container || container.dataset.initialized) return;
                container.dataset.initialized = 'true';

                const storageKey = 'jupyterBookAnswers';
                const textareas = container.querySelectorAll('.answer-textarea');

                const loadAnswers = () => {{
                    const savedAnswers = JSON.parse(localStorage.getItem(storageKey)) || {{}};
                    textareas.forEach(t => {{ if (savedAnswers[t.id]) t.value = savedAnswers[t.id]; }});
                }};

                const saveAnswer = (id, answer) => {{
                    const saved = JSON.parse(localStorage.getItem(storageKey)) || {{}};
                    saved[id] = answer;
                    localStorage.setItem(storageKey, JSON.stringify(saved));
                    const statusEl = container.querySelector(`[data-question-id="${{id}}"] .save-status`);
                    if(statusEl) {{ statusEl.textContent = 'Saved!'; setTimeout(() => {{ statusEl.textContent = ''; }}, 2000); }}
                }};
                
                const debouncedSave = (func => {{
                    let timeout;
                    return (...args) => {{ clearTimeout(timeout); timeout = setTimeout(() => func(...args), 500); }};
                }})(saveAnswer);

                textareas.forEach(textarea => {{
                    textarea.addEventListener('input', () => {{
                        const statusEl = container.querySelector(`[data-question-id="${{textarea.id}}"] .save-status`);
                        if(statusEl) statusEl.textContent = 'Saving...';
                        debouncedSave(textarea.id, textarea.value);
                    }});
                }});

                loadAnswers();
            }})();
            </script>
        </div>
        """

class QAManager:
    """
    Renders the master control panel with 'Print All' and 'Clear All' buttons.
    Supports LaTeX rendering, custom macros, and refined print aesthetics.
    """
    def __init__(self, page_title: str = "My Answers", macros: dict = None):
        """
        Args:
            page_title (str): Title for the printed page.
            macros (dict): Custom LaTeX macros (e.g., {"bftext": ["\\\\mathbf{#1}", 1]})
        """
        self.page_title = html.escape(page_title)
        self.macros_json = json.dumps(macros or {})
        self._rendered = False

    def render(self) -> str:
        if self._rendered: return ""
        self._rendered = True
        
        widget_id = f"qa-manager-{uuid.uuid4().hex}"

        return f"""
        <div id="{widget_id}" class="qa-manager-container my-12 p-6 bg-gray-100 rounded-xl border-2 border-dashed" style="clear: both; display: block; width: 100%; position: relative; z-index: 50;">
            <style>
                .qa-custom-button {{
                    color: white; font-weight: bold; padding: 0.75rem 1.5rem; border-radius: 0.5rem;
                    transition: filter 0.2s ease-in-out;
                    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
                    cursor: pointer;
                    border: none;
                }}
                .qa-custom-button:hover {{ filter: brightness(1.1); }}
            </style>
            <h3 class="text-2xl font-bold text-gray-800 mb-4">My Answer Summary</h3>
            <p class="text-gray-600 mb-6">Use the buttons below to manage all the answers you've written on this page.</p>
            <div class="flex flex-wrap gap-4 items-center">
                <button class="print-all-button qa-custom-button" style="background-color: #2244b0;">Print All Answers</button>
                <div class="flex items-center">
                    <button class="clear-all-button qa-custom-button" style="background-color: #2244b0;">Clear All Answers</button>
                    <button class="confirm-clear-button qa-custom-button" style="background-color: #c8a00c; display: none;">Are you sure? Click to Confirm</button>
                    <span class="cleared-message ml-4 text-green-700 font-semibold" style="display: none;">Answers Cleared!</span>
                </div>
            </div>
        </div>

        <script>
        (function() {{
            const container = document.getElementById('{widget_id}');
            if (!container || container.dataset.initialized) return;
            container.dataset.initialized = 'true';

            const storageKey = 'jupyterBookAnswers';

            // Helper to decode HTML entities (like &amp; or &quot;) from dataset strings
            const decodeEntities = (text) => {{
                const textArea = document.createElement('textarea');
                textArea.innerHTML = text;
                return textArea.value;
            }};

            const printButton = container.querySelector('.print-all-button');
            const clearButton = container.querySelector('.clear-all-button');
            const confirmClearButton = container.querySelector('.confirm-clear-button');
            const clearedMessage = container.querySelector('.cleared-message');

            if (printButton) {{
                printButton.addEventListener('click', () => {{
                    const pageTitle = "{self.page_title}";
                    const macros = {self.macros_json};
                    let printContents = `<h1>${{pageTitle}}</h1>`;
                    const savedAnswers = JSON.parse(localStorage.getItem(storageKey)) || {{}};
                    
                    document.querySelectorAll('.question-container').forEach(q => {{
                        const qId = q.dataset.questionId;
                        // Use raw text to ensure delimiters ($ and \\) are clean for the printer
                        const rawText = q.dataset.rawText || "Question";
                        const qText = decodeEntities(rawText);
                        const answer = savedAnswers[qId] || 'No answer saved.';
                        
                        printContents += `<div class="qa-item">
                            <h2 class="question-header tex2jax_process">${{qText}}</h2>
                            <p class="answer-text tex2jax_ignore">${{answer}}</p>
                        </div>`;
                    }});

                    const iframe = document.createElement('iframe');
                    iframe.style.display = 'none';
                    document.body.appendChild(iframe);
                    const doc = iframe.contentWindow.document;
                    
                    const html = `
                        <!DOCTYPE html>
                        <html>
                        <head>
                            <title>${{pageTitle}}</title>
                            <script>
                                window.MathJax = {{
                                    tex: {{ 
                                        inlineMath: [['$', '$']],
                                        displayMath: [['$$', '$$']],
                                        processEscapes: true,
                                        macros: ${{JSON.stringify(macros)}}
                                    }},
                                    options: {{
                                        ignoreHtmlClass: 'tex2jax_ignore',
                                        processHtmlClass: 'tex2jax_process'
                                    }},
                                    svg: {{ fontCache: 'global' }}
                                }};
                            <\\/script>
                            <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"><\\/script>
                            <style>
                                body {{ 
                                    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; 
                                    padding: 20px 40px; 
                                    line-height: 1.4; 
                                    color: #333;
                                }}
                                h1 {{ 
                                    font-size: 18pt; 
                                    border-bottom: 2px solid #2244b0; 
                                    padding-bottom: 8px; 
                                    margin-bottom: 24px; 
                                    color: #2244b0;
                                }}
                                .qa-item {{ 
                                    break-inside: avoid; 
                                    margin-bottom: 1.5rem; 
                                }}
                                .question-header {{ 
                                    font-size: 11pt; 
                                    font-weight: 600; 
                                    margin-bottom: 0.25rem; 
                                    color: #444;
                                }}
                                .answer-text {{ 
                                    white-space: pre-wrap; 
                                    font-size: 11pt; 
                                    margin-top: 0;
                                    color: #000;
                                    padding-left: 10px;
                                    border-left: 2px solid #eee;
                                }}
                                @media print {{ 
                                    body {{ padding: 0; }}
                                    h1 {{ font-size: 16pt; }}
                                }}
                            </style>
                        </head>
                        <body class="tex2jax_ignore">
                            ${{printContents}}
                        </body>
                        </html>
                    `;

                    doc.open();
                    doc.write(html);
                    doc.close();
                    
                    setTimeout(() => {{
                        iframe.contentWindow.focus();
                        iframe.contentWindow.print();
                        document.body.removeChild(iframe);
                    }}, 2000);
                }});
            }}

            if (clearButton && confirmClearButton) {{
                let confirmTimeout;
                clearButton.addEventListener('click', () => {{
                    clearButton.style.display = 'none';
                    confirmClearButton.style.display = 'inline-block';
                    confirmTimeout = setTimeout(() => {{
                        confirmClearButton.style.display = 'none';
                        clearButton.style.display = 'inline-block';
                    }}, 5000);
                }});
                confirmClearButton.addEventListener('click', () => {{
                    clearTimeout(confirmTimeout);
                    localStorage.removeItem(storageKey);
                    document.querySelectorAll('.answer-textarea').forEach(t => {{ t.value = ''; }});
                    confirmClearButton.style.display = 'none';
                    clearButton.style.display = 'inline-block';
                    clearedMessage.style.display = 'inline';
                    setTimeout(() => {{ clearedMessage.style.display = 'none'; }}, 3000);
                }});
            }}
        }})();
        </script>
        """
#```

### How to Check the Output
#After you rebuild the book and open the chapter page:

#1.  **Open the Developer Console** in your browser. (You can usually do this by right-clicking on the page and selecting "Inspect" or "Inspect Element", then clicking on the "Console" tab).
#2.  You should see several messages that start with `[Q&A Widget]`.

#Please let me know what those messages say. They will tell us if the script is running, if it's finding the button, and if any errors are happening. This will give us the final clue we ne
