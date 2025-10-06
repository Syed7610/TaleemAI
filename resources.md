# 📚 Resources & Tools Used — TaleemAI

> *Developed by **Syed Mushahid Ali Kazmi** | Supported by Muhammad Abdullah.  
> *(All resources are open-source or publicly available for educational use.)*

---

## 🧩 1. Core Utility Tools (Base Level)

| Tool         | Purpose                                           | Source                  |
|:-------------|:--------------------------------------------------|:-------------------------|
| **Pathlib**  | Creating and managing project directories.        | Python Standard Library |
| **OS & Shutil** | File and folder operations (copying, moving, cleanup). | Python Standard Library |
| **Subprocess** | Automating Git commands such as commit and push. | Python Standard Library |

---

## 🧪 2. Data Handling & Processing Libraries

| Library         | Functionality                                       | License |
|:---------------|:----------------------------------------------------|:--------|
| **NumPy**      | Fast numerical operations and array handling.       | BSD     |
| **Pandas**     | Data manipulation, loading, and cleaning CSV files. | BSD     |
| **Scikit-learn** | ML model training, evaluation, and preprocessing.   | BSD     |
| **Matplotlib** | Static plots and visualizations.                    | PSF     |
| **Seaborn**    | Advanced statistical plots and enhanced visuals.    | BSD     |

---

## 🔠 3. NLP & Language Tools

| Library                | Functionality                                         | Use Case                |
|:------------------------|:------------------------------------------------------|:-------------------------|
| **TextBlob**           | Simple NLP processing for sentiment and translation.  | Translation module      |
| **Googletrans (v4)**   | Language translation API.                             | Translation notebook    |
| **NLTK (Optional)**    | Tokenization, stopword removal, text preprocessing.   | NLP module support      |

---

## 🧰 4. Supporting & Automation Libraries

| Library        | Functionality                                    | Description                            |
|:---------------|:-------------------------------------------------|:-----------------------------------------|
| **ReportLab**  | PDF generation with styled text and graphs.     | Creates auto-generated reports.        |
| **Joblib**     | Model serialization and saving trained models.  | Used in `/models/`.                    |
| **tqdm**       | Progress bar for long-running loops.           | Used in notebooks.                     |
| **Datetime**   | Timestamping outputs, logs, and screenshots.   | Used across the project.              |

---

## 💻 5. Integrated Development Environments

| Platform           | Purpose                                      | Use Case                    |
|:--------------------|:---------------------------------------------|:-----------------------------|
| **Google Colab**   | Cloud-based Jupyter environment with GPU.   | Primary training environment |
| **Jupyter Notebook** | Local notebook interface.                   | Testing and experimentation |
| **VS Code (Optional)** | IDE for editing, debugging, and structuring code. | Local project development   |

---

## 📊 6. Dataset Source

| Dataset                          | Description                                                                                                 | Source                                                                                                         |
|:----------------------------------|:-------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------|
| **Students Performance in Exams** | Dataset with student demographics, parental education, test prep info, and exam scores for ML training. | [Kaggle: spscientist/students-performance-in-exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams) |

**Usage Note:**  
Dataset is used exclusively for **educational and research purposes**, in accordance with Kaggle’s open data policy.

---

## ☁️ 7. Cloud & Automation Platforms

| Platform                  | Functionality                                     | Description                                       |
|:---------------------------|:--------------------------------------------------|:--------------------------------------------------|
| **GitHub**               | Source code hosting and version control.          | Main project repository and CI/CD workflows.     |
| **GitHub Actions**       | Workflow automation for retraining and reporting. | Enables automated runs on each push.            |
| **Google Drive (Colab)** | Temporary file storage and syncing.               | Optional dataset mounting and backups.          |
| **Kaggle API**           | Automated dataset download and access.           | Uses `kaggle.json` for authentication.         |

---

## 🧠 8. Machine Learning Models Used

| Model                   | Purpose                               | Type         |
|:-------------------------|:---------------------------------------|:-------------|
| **Logistic Regression** | Student performance classification.   | Supervised   |
| **Random Forest**      | Accuracy optimization.                | Ensemble ML |
| **Linear Regression**  | Forecasting future performance.       | Predictive   |
| **Naive Bayes (Optional)** | NLP classification tasks.             | Probabilistic |

---

## 📈 9. Visualization & Reporting

| Tool                    | Purpose                                                     | Output Format         |
|:-------------------------|:------------------------------------------------------------|:-----------------------|
| **Matplotlib & Seaborn** | Generating class distribution charts, accuracy plots, and confusion matrices. | `.png`, `.pdf`        |
| **ReportLab**          | Automatic generation of full project reports.              | `/reports/summary.pdf` |
| **Pandas Profiling (Optional)** | Automated EDA reports for dataset exploration.           | `/reports/data_overview.html` |

---

## 🧾 10. Documentation & Project Files

| File                 | Description                                                                |
|:----------------------|:---------------------------------------------------------------------------|
| **README.md**       | Complete project overview, setup, and workflow.                           |
| **resources.md**     | This file — lists all tools, libraries, and datasets.                     |
| **project_report.md** | Summarizes results, evaluations, and methodology.                         |
| **requirements.txt** | Python dependencies for quick environment setup.                         |

---

## 🌐 11. Hosting & Version Control

| Platform | Function                                                                 |
|:---------|:--------------------------------------------------------------------------|
| **GitHub Repository:** [TaleemAI](https://github.com/Syed7610/TaleemAI) | Central hub for code, models, workflows, and reports. |
| **GitHub Pages (Optional)** | Can be configured to publish documentation or static pages. |

---

## 🪄 12. Automation Flow Summary

```mermaid
flowchart TD
    A[📥 Data from Kaggle] --> B[🤖 Model Training in Colab]
    B --> C[📊 Evaluation Metrics & Visualizations]
    C --> D[📝 Auto PDF Report Generation]
    D --> E[⬆️ GitHub Commit & Push]
    E --> F[⚙️ GitHub Actions Workflow]
    F --> G[🔁 Automated Retraining + Reporting]
