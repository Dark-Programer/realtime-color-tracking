<h1>Real-Time Color Detection with OpenCV</h1>

  <p>This Python script utilizes OpenCV to access your system's camera and extract red, green, and blue objects in real-time.</p>

<h2>Requirements</h2>

  <ul>
    <li>Python 3.x</li>
    <li>OpenCV (<code>pip install opencv-python</code>)</li>
  </ul>

<h2>Usage</h2>

  <ol>
    <li>Ensure your system's camera is accessible and the shutter is open.</li>
    <li>Install the required Python modules mentioned above.</li>
    <li>Run the Python script.</li>
    <li>The script will open the camera feed and display three windows showing the original frame along with the extracted green, red, and blue objects.</li>
    <li>Press the 'Esc' key to exit the program.</li>
  </ol>

<h2>How It Works</h2>

  <ol>
    <li>The script accesses the camera using OpenCV's <code>VideoCapture()</code> function.</li>
    <li>It continuously reads frames from the camera feed inside a while loop.</li>
    <li>Each frame is converted from BGR to HSV color space using <code>cv.cvtColor()</code> function.</li>
    <li>Thresholding is applied to the HSV image to extract green, red, and blue colors using <code>cv.inRange()</code> function.</li>
    <li>Bitwise AND operation is performed between the mask and the original frame to extract the colored objects using <code>cv.bitwise_and()</code> function.</li>
    <li>The original frame and the extracted colored objects are displayed using <code>cv.imshow()</code> function.</li>
    <li>The program exits when the 'Esc' key is pressed.</li>
  </ol>

<h2>Note</h2>

  <ul>
    <li>Ensure your system allows access to the camera.</li>
    <li>Adjust the color range values (<code>lower_green</code>, <code>upper_green</code>, <code>lower_red</code>, <code>upper_red</code>, <code>lower_blue</code>, <code>upper_blue</code>) as per your requirement to detect different shades of colors accurately.</li>
  </ul>

  <p><strong>Disclaimer:</strong> Please use this script responsibly and ensure compliance with all relevant laws and regulations regarding the use of camera and image processing.</p>
