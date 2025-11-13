# conda activate streamlit_env
import streamlit as st
from PIL import Image
import base64 

# ------------------ CONFIG ------------------
st.set_page_config(page_title="Xinyi Zhang | Portfolio", page_icon="📊", layout="wide")

# ------------------ NAVIGATION MENU ------------------
menu = st.sidebar.radio(
    "Navigation",
    ["Home", "Projects", "Contact"]
)

# =====================================================
# ------------------ HOME PAGE ------------------------
# =====================================================
if menu == "Home":
    st.title("👋 Hi, I'm Xinyi Zhang")
    st.subheader("MSc Biostatistics & Data Science | BSc Biological Sciences | Healthcare Data Analytics | Computational Biology")

    st.markdown("""
    Welcome to my personal website!  
    I'm passionate about bridging data science and healthcare — using analytics to improve clinical research, genomics, and healthcare delivery.
    """)

    # ====== Image 2 centered before Education ======
    image2 = Image.open("profile2.jpeg")
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image2, width=700)
    st.markdown("</div>", unsafe_allow_html=True)

    st.divider()

    # ------------------ EDUCATION ------------------
    st.header("Education")

    # create two columns for education section: text (2/3 width) + image (1/3 width)
    col_text, col_img = st.columns([2, 1])
    with col_text:
        st.write("""
        **Weill Cornell Medicine**  
        *Master of Science in Biostatistics and Data Science*  
        GPA: 4.206 / 4.3  
        **Courses:** Hierarchical Data Analysis; Big Data in Medicine; Categorical & Censored Data Analysis; Statistical Programming (SAS); Data Science

        **Imperial College London**  
        *BSc Biological Sciences*  
        GPA: 3.79 / 4.0  
        **Courses:** Computational Omics; Stem Cell, Ageing, and Regeneration; Genetics
        """)
    with col_img:
        image3 = Image.open("profile3.jpg")
        st.image(image3, width=400)

    st.divider()

    # ------------------ SKILLS ------------------
    st.header("Technical Skills")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        - **Programming:** Python, R, MySQL, SAS  
        - **Softwares or Tools:** SPSS, Prism, Tableau, Shiny  
        - **Packages:** Pandas, Numpy, scikit-learn, TensorFlow, tidyverse, ggplot2, matplotlib, seaborn, Bioconductor  
        """)
    with col2:
        st.markdown("""
        - **Statistical Methods:** Regression, Survival, Longitudinal, Categorical Data  
        - **Applications:** Clinical trials, Transcriptomics, Genomics pipelines  
        - **Tools:** Git, Conda, HPC clusters, Linux  
        """)
    with col3:
        st.markdown("""
        - **Programming Certifications:** SAS Certified Professional (Base) & SAS Certified Specialist (Advanced)  
        - **Clinical Trials related:** Good Clinical Practice  
        """)

    st.divider()

    # ------------------ INTERESTS ------------------
    st.header("Interests")

    # create two columns again: image on right, text on left
    col_text, col_img = st.columns([2, 1])
    with col_text:
        st.markdown("""
        Professionally, I’m interested in:
        - Integrating **data science and biology** to improve clinical decision-making in clinical trials and observational studies.  
        - Building **visual, interactive tools** for scientists and clinicians.  
        - Using **machine learning** to uncover patterns in genomics and patient data.
        """)
        st.markdown("""
        In my spare time, I’m interested in:
        - **French musicals.** I adore Le Rouge et Le Noir!
        - **Cooking**, yummm... I can cook nearly all kinds of dishes around the world!
        - **Learning languages**, on day 500+ on Duolingo for Japanese course currently. Do your lesson!
        - **Observe the geese.* I used to live by a river back in London and I just love to observe them!
        - **Travelling.** This is a picture of me in front of Sagrada Familia! 👉
        """)
        st.markdown("""
        Fun fact about me: I have a wide range of collection of everything about penguin!
        """)
    with col_img:
        image1 = Image.open("profile.jpg")
        st.image(image1, width=400)
        image4 = Image.open("penguin.jpg")
        st.image(image4, width=400, caption = "A portion of my penguin collections")


# =====================================================
# ------------------ PROJECTS PAGE --------------------
# =====================================================
elif menu == "Projects":
    st.title("💡 Featured Projects")

    sub_menu = st.radio(
        "Select a category:",
        ["Biostatistics Projects", "Computational Biology Projects", "Machine Learning Projects", "Biology Projects", "Other Projects"]
    )

    # =====================================================
    # --- BIOSTATISTICS PROJECTS ---
    # =====================================================
    if sub_menu == "Biostatistics Projects":
        st.header("Biostatistics Projects")

        # --- helper function ---
        def show_file(title, file_path, description, file_type="pdf"):
            st.subheader(title)
            st.markdown(description)
            try:
                with open(file_path, "rb") as f:
                    if file_type == "pdf":
                        base64_data = base64.b64encode(f.read()).decode("utf-8")
                        display = f'<iframe src="data:application/pdf;base64,{base64_data}" width="800" height="500" type="application/pdf"></iframe>'
                        st.markdown(display, unsafe_allow_html=True)
                    elif file_type == "pptx":
                        st.info("This project is a PowerPoint presentation. Click below to download or view it locally.")
                    # Download button
                    with open(file_path, "rb") as f2:
                        st.download_button(f"📄 Download {title}", f2, file_name=file_path.split("/")[-1])
            except FileNotFoundError:
                st.warning(f"⚠️ File not found: {file_path}")

        # ---- 1. Natera Internship ----
        show_file(
            "Natera Internship - ShinyApp",
            "projects/Natera_Internship.pptx",
            """
            My internship experience included close collaboration with **Translational Medicine**, **Clinical Operations**, **Data Management**, and **Medical Affairs** teams to on Organ Health
            and Women Health projects. I've worked on projects including:
            - Building time-varying time-to-event analyses models
            - Calculating carrier frequency based on 1M patient records
            - Initiating Statistical Analysis Plan (SAP). 
            
            But the most impactful project I've done is this ShinyApp project which help the team to build a tool to visualize the longitudinal patient data from a RCT interactively, allowing 
            users to explore detailed data behind one single event within just one single click. 
            """,
            file_type="pptx"
        )

        st.divider()


        # ---- 2. Methylmalonic Acid and Lung Cancer ----
        show_file(
            "Association Between Methylmalonic Acid (MMA) and Lung Cancer",
            "projects/MMA and lung cancer.pdf",
            """
            Analyzed **NHANES 2001–2014** data to investigate the relationship between serum **Methylmalonic Acid (MMA)** levels
            and lung cancer history. Used multivariable **linear regression** and **Box–Cox transformations** to test interactions
            between MMA, age, and creatinine. We found that MMA levels were associated with general cancer history but **not**
            with recency of diagnosis or lung cancer type. Suggested that MMA is not a suitable biomarker for lung cancer
            detection.
            """
        )

        st.divider()

        # ---- 3. FDA NSCLC Safety Analysis ----
        show_file(
            "FDA FAERS Q4 2024 NSCLC Outcome Analysis - SAS Project",
            "projects/FDA 2024 Q4 AE Event in NSCLC Outcome Analysis.pdf",
            """
            Conducted a **real-world safety and survival study** using the FDA Adverse Event Reporting System (FAERS) to evaluate platinum-based chemotherapies in **Non-Small Cell Lung Cancer** (Carboplatin vs. Cisplatin).  
            Applied **Kaplan–Meier survival analysis** in SAS 9.4 to model time-to-event data for death, hospitalization,  
            and life-threatening outcomes. Results indicated favorable safety and survival, with hospitalization as the most
            common serious event.
            Applied advanced SAS materials including SAS SQL and SAS Macros.
            """
        )

        st.divider()

        # ---- 4. SAS TFL Final-term Project ----
        show_file(
            "Placebo and Treatment Comparison - SAS Project",
            "projects/Placebo_Treatment SAS project.pdf",
            """
            Designed a **Table–Figure–Listing (TFL)** report in **SAS 9.4** to summarize a clinical dataset comparing Placebo and Drug B treatment groups. Performed descriptive statistics and inferential tests:
            - Student’s *t*-test for BMI  
            - Chi-square for weight category  
            - Wilcoxon rank-sum for cost comparison  
            - Included correlation analysis by applying macros and visualization of BMI vs. demographic factors.  
            - Produced publication-ready tables and Q–Q plots following clinical programming standards.
            """
        )

    # =====================================================
    # --- COMPUTATIONAL PROJECTS ---
    # =====================================================
    elif sub_menu == "Computational Biology Projects":
        st.header("Computational Biology Projects")

        # --- helper function ---
        def show_pdf(title, file_path, description):
            st.subheader(title)
            st.markdown(description)
            try:
                with open(file_path, "rb") as f:
                    base64_pdf = base64.b64encode(f.read()).decode("utf-8")
                pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="500" type="application/pdf"></iframe>'
                st.markdown(pdf_display, unsafe_allow_html=True)
                with open(file_path, "rb") as f:
                    st.download_button(f"📄 Download {title}", f, file_name=file_path.split("/")[-1])
            except FileNotFoundError:
                st.warning(f"⚠️ File not found: {file_path}")

        # ---- 1. Tilgner Lab ----
        show_pdf(
            "Lab projects at Tilgner Lab",
            "projects/tilgnerlab.pdf",
            """
            1. Trained logistic regression models to predict exon inclusion/exclusion patterns, revealing how
            microenvironmental context influences alternative splicing across cell types.
            2. Built an R–Python hybrid **Shiny dashboard** to visualize spatial isoform expression from ONT VisiumHD datasets.  
            Integrated the lab’s `splIsoFind` Python package for PSI mapping and interactive barplots.  
            """
        )

        st.divider()

        # ---- 2. 16S rRNA Sequencing ----
        show_pdf(
            "16S rRNA Sequencing Project",
            "projects/16s rRNA sequencing_Xinyi Zhang.pdf",
            """
            Conducted **microbiome profiling using 16S rRNA sequencing**, analyzing operational taxonomic units (OTUs)
            to identify microbial diversity and abundance across different samples.  
            Performed sequence quality control, clustering, and alpha/beta diversity analysis to explore relationships
            between bacterial community composition and environmental variation.
            """
        )

        st.divider()

        # ---- 4. RNA-Seq Analysis ----
        show_pdf(
            "RNA-Seq Data Analysis",
            "projects/RNA Seq analysis.pdf",
            """
            Designed and executed a complete **RNA-Seq pipeline**: normalization, DEG identification, PCA, and pathway analysis.  
            Identified upregulation of **Pdcd-1** in thymus datasets, suggesting a potential role in T-cell negative selection
            and immune regulation. Visualized results with volcano plots, clustering heatmaps, and GSEA.
            """
        )

        st.divider()

        # ---- 5. Variant Calling ----
        show_pdf(
            "TP53 Variant Calling and Protein Structure Prediction",
            "projects/Variant calling_Xinyi Zhang.pdf",
            """
            Performed **variant calling on chromosome 17 (TP53 gene)** using GATK, SAMtools, and BCFtools pipelines.  
            Identified pathogenic SNPs (e.g., rs587782596 and rs786201057) associated with **Li-Fraumeni syndrome** and cancers.  
            Predicted mutant p53 protein structures using Missense3D and PhyreRisk, analyzing structural and functional consequences
            of amino acid substitutions.
            """
        )

        # =====================================================
        # --- MACHINE LEARNING PROJECTS ---
        # =====================================================
    elif sub_menu == "Machine Learning Projects":
        st.header("Machine Learning Projects")

    # helper function reused
        def show_pdf(title, file_path, description):
            st.subheader(title)
            st.markdown(description)
            try:
                with open(file_path, "rb") as f:
                    base64_pdf = base64.b64encode(f.read()).decode("utf-8")
                pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="500" type="application/pdf"></iframe>'
                st.markdown(pdf_display, unsafe_allow_html=True)
                with open(file_path, "rb") as f:
                    st.download_button(f"📄 Download {title}", f, file_name=file_path.split("/")[-1])
            except FileNotFoundError:
                st.warning(f"⚠️ File not found: {file_path}")

    # -----------------------------
    # 1. Customer Feedback Sentiment Analysis
    # -----------------------------
        show_pdf(
            "Customer Feedback Sentiment Analysis",
            "projects/customer_feedback_sentiment_analysis.pdf",
            """
            Fine-tuned pre-trained BERT model for binary sentiment classification using Hugging Face Transformers library with PyTorch.
            Designed Keras-based LSTM model with word embeddings to classify customer sentiment from text input.
            Applied confusion matrices, classification reports, and accuracy comparisons to evaluate BERT and LSTM model performance.
            """
        )

        st.divider()

    # -----------------------------
    # 2. TensorFlow2 Deep Learning Project (SVHN Image Classifier)
    # -----------------------------
        show_pdf(
            "TensorFlow2 CNN & MLP Image Classifier (SVHN Dataset)",
            "projects/Python Tensorflow2 Capstone.pdf",
            """
            Developed both **MLP and CNN architectures** to classify real-world street digit images from the **SVHN dataset**.  
            Implemented preprocessing, grayscale conversion, model callbacks, early stopping, and achieved >80% validation accuracy with a compact CNN design.
            """
        )

        st.divider()

    # -----------------------------
    # 3. Pumpkin Seed Classification (Random Forest & XGBoost)
    # -----------------------------
        show_pdf(
            "Pumpkin Seed Classification with Random Forest & XGBoost",
            "projects/pumpkin_random_forest_xgboost.pdf",
            """
            Built **Random Forest** and **XGBoost** models to classify pumpkin seed varieties using geometric and morphological features.  
            Tuned hyperparameters through grid-style experiments, evaluated performance with confusion matrices, and analyzed feature importance to identify key predictive traits.
            """
        )




    # =====================================================
    # --- BIOLOGY PROJECTS ---
    # =====================================================
    elif sub_menu == "Biology Projects":
        st.header("Biology Projects")

        # --- helper function ---
        def show_file(title, file_path, description, file_type="pdf"):
            st.subheader(title)
            st.markdown(description)
            try:
                with open(file_path, "rb") as f:
                    if file_type == "pdf":
                        base64_data = base64.b64encode(f.read()).decode("utf-8")
                        display = f'<iframe src="data:application/pdf;base64,{base64_data}" width="800" height="500" type="application/pdf"></iframe>'
                        st.markdown(display, unsafe_allow_html=True)
                    elif file_type == "pptx":
                        st.info("This project is a PowerPoint presentation. Click below to download or view it locally.")
                    # Download button
                    with open(file_path, "rb") as f2:
                        st.download_button(f"📄 Download {title}", f2, file_name=file_path.split("/")[-1])
            except FileNotFoundError:
                st.warning(f"⚠️ File not found: {file_path}")


    # =====================================================
    # --- 1. FINAL YEAR DISSERTATION ----------------------
    # =====================================================
        show_file(
            "Undergraduate Final Year Dissertation",
            "projects/390.pdf",
            """
            **Investigating the Impact of CHD3 Deficiency on the Pluripotency of Induced Pluripotent Stem Cells (iPSCs)**  
            A full experimental research project exploring how CHD3 knockout influences pluripotency at the RNA and protein levels.  
            Applied **RT-qPCR**, **bulk RNA-seq**, **immunofluorescence**, and **flow cytometry** to validate pluripotency and construct a CRISPR-based disease model for **Snijders Blok-Campeau Syndrome (SNIBCPS)**.
            """
        )

        st.divider()


    # =====================================================
    # --- 2. Influenza Pandemic Essay ---------------------
    # =====================================================
        show_file(
            "Will Influenza Become the Next Pandemic?",
            "projects/Will Influenza become the next pandemic and are we ready for it.pdf",
            """
            A scientific essay analyzing whether Influenza, particularly emerging H5N1 strains, could drive the next global pandemic.  
            Discusses **viral evolution**, **gene reassortment**, **global surveillance gaps**, and pandemic preparedness challenges.  
            Synthesizes findings from WHO, CDC, and recent genomic studies to evaluate global readiness.
            """
        )



    # =====================================================
    # --- Other PROJECTS ---
    # =====================================================
    elif sub_menu == "Other Projects":
        st.header("Other Projects")

        # --- helper function ---
        def show_pdf(title, file_path, description):
            st.subheader(title)
            st.markdown(description)
            try:
                with open(file_path, "rb") as f:
                    base64_pdf = base64.b64encode(f.read()).decode("utf-8")
                pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="500" type="application/pdf"></iframe>'
                st.markdown(pdf_display, unsafe_allow_html=True)
                with open(file_path, "rb") as f:
                    st.download_button(f"📄 Download {title}", f, file_name=file_path.split("/")[-1])
            except FileNotFoundError:
                st.warning(f"⚠️ File not found: {file_path}")

        # ---- 1. Health Equity Hackathon (MSD & Eli Lilly) ----
        show_pdf(
            "Health Equity Hackathon (MSD & Eli Lilly)",
            "projects/Health equity hackathon poster.pdf",
            """
            Led a team to improve Afro-Caribbean women’s participation in breast cancer trials.  
            Proposed an educational workshop series with occasional holiday themes to improve inclusiviness in the community strategies.
            """
        )

        st.divider()

# =====================================================
# ------------------ CONTACT PAGE ---------------------
# =====================================================
elif menu == "Contact":
    st.title("Contact")
    st.markdown("""
        If you have any thoughts, comments, or just want to say hi, you can find me here:
    """)

    st.markdown("""
    📧 Personal: [zceci1125@gmail.com](mailto:zceci1125@gmail.com) 

    📧 University: [xiz4024@med.cornell.edu](mailto:xiz4024@med.cornell.edu)

    💼 [LinkedIn](https://www.linkedin.com/in/xinyi-zhang-194863204/) 

    💻 [GitHub](https://github.com/XinyiCeci)
    """)

    st.divider()

    st.write("© 2025 Xinyi Zhang | Built with Streamlit")

