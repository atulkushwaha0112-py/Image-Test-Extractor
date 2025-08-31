<!--🧠 Highlight.js and Font Awesome already included in your Blogger theme-->
<!--🧠 Highlight.js for Code Highlighting-->
<link href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/default.min.css" rel="stylesheet"></link>
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" rel="stylesheet"></link>



  <!-- WhatsApp Channel Promo (Theme-Compatible) -->
<ul style="list-style: none; padding-left: 0; margin-top: 10px; margin-bottom: 20px; font-family: Arial, sans-serif;">
  <li style="margin: 8px 0; font-size: 18px;">
    <i class="fab fa-whatsapp" style="margin-right: 10px;"></i>
    <a href="https://whatsapp.com/channel/0029Vb5oq3gBA1f23Latsb3a" target="_blank" style="text-decoration: none;">
      📢 Stay updated with tutorials, projects & coding hacks — <strong>Join our WhatsApp Channel</strong>
    </a>
  </li>
</ul>


<p>This project shows how to extract text from any image using Python and <strong>Tesseract OCR</strong>. In just a few steps, you can convert images into editable text!</p>

<h3>📂 Project Requirements</h3>
<ul>
  <li><code>pytesseract</code> – Python wrapper for Tesseract</li>
  <li><code>Pillow</code> – For image processing</li>
  <li><strong>Tesseract-OCR</strong> – The OCR engine (must be installed separately)</li>
</ul>

<h3>🔗 Download Tesseract-OCR</h3>
<p>👉 Download the latest stable version from this direct link:</p>
<p><a href="https://github.com/tesseract-ocr/tesseract/releases/download/5.5.0/tesseract-ocr-w64-setup-5.5.0.20241111.exe" target="_blank">
🔗 Download Tesseract-OCR for Windows
</a></p>

<p>After downloading:</p>
<ul>
  <li>Run the setup file to install Tesseract-OCR</li>
  <li>By default, it's installed at:<br />
  <code>C:\Program Files\Tesseract-OCR\tesseract.exe</code></li>
  <li>If you want to change the path, make sure to set it during installation</li>
</ul>

<h3>🔍 How to Find the Path to <code>tesseract.exe</code></h3>
<p>If you're unsure where Tesseract was installed, here’s how to find the path:</p>
<ol>
  <li>Open the folder: <code>C:\Program Files\Tesseract-OCR</code></li>
  <li>Look for the file: <code>tesseract.exe</code></li>
  <li>Copy the full path from the address bar</li>
</ol>

<p>Example path to use in your Python script:</p>
<pre><code class="language-python">pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'</code></pre>

<h3>📦 Install Required Python Libraries</h3>
<pre><code>pip install pytesseract
pip install pillow</code></pre>

<h3>📌 Python Code to Extract Text from Image</h3>
<p>Make sure the image (e.g. <code>quote1.png</code>) is in the same folder as your script.</p>

<pre><code class="language-python">import pytesseract
from PIL import Image

# ✅ Set the full path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load and process image
image = Image.open("quote1.png")
text = pytesseract.image_to_string(image)

# Display the extracted text
print(text)</code></pre>

<h3>⚡ Pro Tips &amp; Hacks</h3>
<ul>
  <li>🔍 Use high-quality images with clear text for best results</li>
  <li>🧽 Preprocess image: grayscale, resize, sharpen etc. for better OCR accuracy</li>
  <li>🌐 For different languages, use <code>lang='your_lang_code'</code> in <code>image_to_string</code></li>
  <li>📁 Automate multiple images by using a loop with a folder</li>
</ul>

<h3>✅ Example Output</h3>
<p>The script will print the extracted text directly to the terminal. You can also save it to a file if needed.</p>

<pre><code class="language-python">with open("output.txt", "w", encoding="utf-8") as file:
    file.write(text)</code></pre>

<hr />
