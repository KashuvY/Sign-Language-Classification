<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">EEL5840 Final Project</h3>
  <p align="center">
    Jorge Moros, Rashi Ghosh, and Youval Kashuv
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#project-dependencies">Project Dependencies</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#authors">Authors</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

A full report of this project can be found in the file report.pdf.

<!-- GETTING STARTED -->
## Getting Started

To utilize this model, in addition to the files in this repository you will need the following files:
* ["data_train.npy"](https://ufl.instructure.com/files/81900020/download?download_frd=1)
* ["labels_train.npy"](https://ufl.instructure.com/files/81900021/download?download_frd=1)

# Project Dependencies

Below is a list of libraries, packages, and other dependencies required to run this project. Ensure that you install these specific versions to maintain compatibility with the project's code.

* numpy
  ```sh
     pip install numpy
  ```
* tensorflow
  ```sh
    pip install tensorflow
  ```
* scikit-learn
  ```sh
    pip install scikit-learn
  ```
  
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/UF-FundMachineLearning-Fall23/final-project-code-report-team-jyr.git
   ```
2. Create your environment
   ```sh
   python -m venv team_jyr
   ```
3. Activate your environment
    * For Mac/Linux:
      ```sh
        source team_jyr/bin/activate
      ```
    * For Windows:
      ```sh
          team_jyr\Scripts\activate
      ```
   

<!-- USAGE EXAMPLES -->
## Usage

<!-- USAGE EXAMPLES -->
## Usage

To use this model, follow these steps:

1. **Open the Notebook**: Navigate and open the `execution.ipynb` file in this repository.

2. **Run the Cells**: Execute the cells in the notebook in order. These cells encompass the necessary code for model execution and result visualization.

3. **Update File Paths**: It is essential to replace the default file paths in the notebook with the paths to your specific test data and test labels. Ensure these paths correctly point to your files.

    Example:
    ```python
    data_test_file_path = "path/to/your/test_data.npy"
    labels_test_file_path = "path/to/your/test_labels.npy"
    ```

4. **Review and Analyze**: Use the `accuracy`, and `predicted_labels` variables to evaluate the model against the test set.


<!-- Authors -->
## Authors

Jorge Moros
Rashi Ghosh
Youval Kashuv
