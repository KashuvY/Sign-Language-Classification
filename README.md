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
* ["best_model_resnet.h5"](https://uflorida-my.sharepoint.com/:u:/g/personal/rashighosh_ufl_edu/EcLUUC2puhNCnz1ib9AOJ2gBgjWzHbVlFdiHi-voO0lMCw?e=9rtgQi)

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

If the project is going to be ran outside HiPerGator, follow the instructions below to create the appropriate environment.

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

To use this model, follow these steps:

1. **Open the Notebook**: Navigate and open the `execution.ipynb` file in this repository with the `tensorflow-2.7.0` kernel on HiPerGator.

2. **Place the best_model_resnet.h5 in the root directory.** It is important to keep this file in the root directory (same directory level as where the `execution.ipynb` is located).

3.  **Update File Paths**: It is essential to replace the default file paths in the notebook with the paths to your specific test data and test labels. Ensure these paths correctly point to your files.

    Example:
    ```python
    data_test_file_path = "path/to/your/test_data.npy"
    labels_test_file_path = "path/to/your/test_labels.npy"
    ```

4. **Run the Cell**: Execute the cell in the notebook to run the test file. This cells encompass the necessary code for model execution and result visualization.

5. **Review and Analyze**: Use the `accuracy`, and `predicted_labels` variables to evaluate the model against the test set.


<!-- Authors -->
## Authors

* Jorge Moros
* Rashi Ghosh
* Youval Kashuv
